#!/usr/bin/env python3
"""
v3_extract.py — Extract hyper-entity candidates from source markdown files using Claude API.

Processes ~111 source files across 4 categories (podcast, world-gallery, ai-pathways, x-hope)
with category-specific prompts. Outputs results/v3/raw_candidates.json.
"""

import argparse
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from anthropic import Anthropic, RateLimitError, APIStatusError

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CONFIG = {
    "model": "claude-sonnet-4-6",
    "max_tokens": 4096,
    "temperature": 0,
    "sources_dir": Path("sources"),
    "output_dir": Path("results/v3"),
    "source_urls_file": Path("sources/source_urls.json"),
    "batch_delay": 0.5,
    "max_retries": 3,
}

SOURCES_DIR = CONFIG["sources_dir"]
OUTPUT_DIR = CONFIG["output_dir"]

# Pricing: Sonnet 4.5
INPUT_COST_PER_M = 3.0
OUTPUT_COST_PER_M = 15.0

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

ENTITY_SCHEMA_INSTRUCTION = """
Return a JSON array of extracted entities. Each entity must have these fields:
{
  "name": "string - use the speaker's name for it if given, or the most specific name from the text",
  "source_quote": "string - VERBATIM quote from the source (1-3 sentences)",
  "source_quote_context": "string - brief note on where in the doc the quote appears, e.g. 'Discussion of nuclear energy around timestamp 15:23' or 'Section on governance mechanisms'",
  "speaker": "string or null - who proposed/discussed this",
  "one_liner": "string - one sentence explaining what this is",
  "mechanism": "string - 2-4 sentences on how it works",
  "exists_today": "string - what partial implementations exist already"
}

If nothing qualifies, return an empty JSON array: []
"""

SHORT_PROMPT = """This is a brief speculative world sketch. Extract 0-2 SPECIFIC technologies, institutions, or systems described that someone could actually build or fund. If nothing is concrete enough to have a mechanism of action, return an empty list. Do NOT extract vague concepts or genre labels.

""" + ENTITY_SCHEMA_INSTRUCTION

PODCAST_PROMPT = """Extract SPECIFIC proposals, systems, architectures, or technologies discussed by the speaker that are:
1. NAMED or CONCRETE enough that someone could write a spec for it
2. NOT YET BUILT at scale (may have prototypes or research)
3. DISCUSSED SERIOUSLY with some mechanism explained (not throwaway mentions)

ANTI-PATTERNS (do NOT extract these):
- Generic field descriptions ('AI-enhanced governance')
- Vague compound nouns you invented
- Already widely deployed technology
- Abstract values or principles

Most transcripts yield 0-3 candidates. If nothing qualifies, return an empty list.

""" + ENTITY_SCHEMA_INSTRUCTION

REPORT_PROMPT_TEMPLATE = """This is a section from a research report titled '{section_heading}'. Extract only proposals that are NOVEL and have SPECIFIC implementation mechanisms described in this section.

Strict criteria — an entity must have ALL of:
1. A specific NAME or label given by the authors
2. A concrete MECHANISM (how it works, not just what it aims to do)
3. NOVELTY — it is NOT a well-known existing technology or framework

ANTI-PATTERNS (do NOT extract these):
- Well-known existing technologies (blockchain, federated learning, differential privacy, smart contracts, etc.)
- References to other people's published work or existing projects
- Vague policy recommendations ("we should create better governance")
- Generic categories of technology ("AI-enhanced monitoring systems")
- Abstract principles, values, or goals
- Restatements of problems without a proposed solution

Most sections yield 0-2 entities. Many sections yield 0. Return an empty array [] if nothing in this section is novel AND specific enough.

""" + ENTITY_SCHEMA_INSTRUCTION

# ---------------------------------------------------------------------------
# Text utilities
# ---------------------------------------------------------------------------

def smart_chunk_text(text, chunk_size, overlap):
    """Split text into overlapping chunks at paragraph boundaries."""
    if len(text) <= chunk_size:
        return [text]
    paragraphs = re.split(r'\n\n+', text)
    chunks = []
    current_chunk = []
    current_size = 0
    for para in paragraphs:
        para_size = len(para)
        if para_size > chunk_size:
            sentences = re.split(r'(?<=[.!?])\s+', para)
            for sentence in sentences:
                if current_size + len(sentence) > chunk_size and current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                    overlap_text = '\n\n'.join(current_chunk[-2:]) if len(current_chunk) >= 2 else current_chunk[-1] if current_chunk else ''
                    current_chunk = [overlap_text, sentence] if overlap_text else [sentence]
                    current_size = len(overlap_text) + len(sentence)
                else:
                    current_chunk.append(sentence)
                    current_size += len(sentence)
        else:
            if current_size + para_size > chunk_size and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                overlap_paras = current_chunk[-2:] if len(current_chunk) >= 2 else current_chunk[-1:] if current_chunk else []
                current_chunk = overlap_paras + [para]
                current_size = sum(len(p) for p in current_chunk)
            else:
                current_chunk.append(para)
                current_size += para_size
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    return chunks


def split_by_sections(content, level=2):
    """Split content by headings into (heading, text) tuples.

    Tries markdown headings first (## ), then falls back to numbered headings
    (e.g. '1 Title', '2.1 Subtitle') for plain-text reports.
    If no headings found, chunks by size (~30K chars).
    """
    lines = content.split('\n')
    md_prefix = '#' * level + ' '

    # Try markdown headings first
    heading_lines = [(i, line.lstrip('#').strip())
                     for i, line in enumerate(lines) if line.startswith(md_prefix)]

    # Fallback: numbered section headings like "1 Title" or "2.1 Subtitle"
    if not heading_lines:
        heading_pat = re.compile(r'^(\d+(?:\.\d+)*)\s+([A-Z][\w\s,\-:&/]+)$')
        heading_lines = []
        for i, line in enumerate(lines):
            m = heading_pat.match(line.strip())
            if m and len(m.group(2)) > 3:
                heading_lines.append((i, f"{m.group(1)} {m.group(2).strip()}"))

    # If still nothing found, chunk by size
    if not heading_lines:
        chunk_size = 15000
        if len(content) <= chunk_size:
            return [("Full document", content)]
        return [
            (f"Part {i+1}", content[i:i+chunk_size])
            for i in range(0, len(content), chunk_size)
        ]

    sections = []
    for idx, (line_num, heading) in enumerate(heading_lines):
        next_line = heading_lines[idx + 1][0] if idx + 1 < len(heading_lines) else len(lines)
        section_text = '\n'.join(lines[line_num:next_line])
        if len(section_text.strip()) > 100:  # skip tiny sections
            sections.append((heading, section_text))

    # Include content before first heading if substantial
    if heading_lines and heading_lines[0][0] > 5:
        preamble = '\n'.join(lines[:heading_lines[0][0]])
        if len(preamble.strip()) > 200:
            sections.insert(0, ("Preamble", preamble))

    return sections


def extract_json(text):
    """Extract JSON array or object from LLM response text."""
    text = text.strip()
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            if part.startswith("{") or part.startswith("["):
                text = part
                break
    for start_char, end_char in [("[", "]"), ("{", "}")]:
        start = text.find(start_char)
        if start != -1:
            depth = 0
            for i, char in enumerate(text[start:], start):
                if char == start_char:
                    depth += 1
                elif char == end_char:
                    depth -= 1
                    if depth == 0:
                        return json.loads(text[start:i + 1])
    raise ValueError("No JSON found in response")


# ---------------------------------------------------------------------------
# Source routing
# ---------------------------------------------------------------------------

def get_processing_strategy(source_file, content):
    """Determine prompt type and chunks based on source category."""
    rel = source_file.relative_to(SOURCES_DIR)
    category = rel.parts[0]  # "podcast", "world-gallery", "ai-pathways", "x-hope"
    if category == "world-gallery":
        return "short", [content], category
    elif category in ("ai-pathways", "x-hope"):
        return "report", split_by_sections(content), category
    else:  # podcast
        if len(content) > 50000:
            return "podcast", smart_chunk_text(content, 50000, 2000), category
        return "podcast", [content], category


def build_prompt(strategy, chunk, section_heading=None):
    """Build the system+user prompt pair for a given strategy."""
    system = "You are an expert at identifying concrete, specific technological or institutional proposals in text. You return valid JSON only."
    if strategy == "short":
        user = SHORT_PROMPT + "\n\n---\n\n" + chunk
    elif strategy == "report":
        prompt = REPORT_PROMPT_TEMPLATE.replace(
            "{section_heading}", section_heading or "Unknown"
        )
        user = prompt + "\n\n---\n\n" + chunk
    else:  # podcast
        user = PODCAST_PROMPT + "\n\n---\n\n" + chunk
    return system, user


# ---------------------------------------------------------------------------
# API calling
# ---------------------------------------------------------------------------

def call_api(client, system, user):
    """Call Claude API with retry logic. Returns (entities_list, input_tokens, output_tokens)."""
    for attempt in range(CONFIG["max_retries"]):
        try:
            response = client.messages.create(
                model=CONFIG["model"],
                max_tokens=CONFIG["max_tokens"],
                temperature=CONFIG["temperature"],
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            text = response.content[0].text
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            entities = extract_json(text)
            if isinstance(entities, dict):
                entities = [entities]
            return entities, input_tokens, output_tokens
        except RateLimitError as e:
            wait = (2 ** attempt) * 2
            print(f"    Rate limited, waiting {wait}s (attempt {attempt + 1}/{CONFIG['max_retries']})")
            time.sleep(wait)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"    JSON parse error: {e}")
            if attempt < CONFIG["max_retries"] - 1:
                wait = (2 ** attempt)
                print(f"    Retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"    Failed after {CONFIG['max_retries']} attempts, skipping chunk")
                return [], 0, 0
        except APIStatusError as e:
            wait = (2 ** attempt) * 2
            print(f"    API error ({e.status_code}): {e.message}, retrying in {wait}s")
            time.sleep(wait)
        except Exception as e:
            print(f"    Unexpected error: {e}")
            return [], 0, 0
    print(f"    All {CONFIG['max_retries']} retries exhausted, skipping chunk")
    return [], 0, 0


# ---------------------------------------------------------------------------
# Source loading
# ---------------------------------------------------------------------------

def load_source_urls():
    """Load source URL mapping."""
    urls_file = CONFIG["source_urls_file"]
    if urls_file.exists():
        with open(urls_file) as f:
            return json.load(f)
    return {}


def get_all_sources():
    """Find all markdown source files."""
    sources = sorted(SOURCES_DIR.rglob("*.md"))
    # Exclude non-content files
    sources = [s for s in sources if s.name != "source_urls.json" and not s.name.startswith(".")]
    return sources


def select_dry_run_sources(sources, n):
    """Select N sources, sampling from each category if possible."""
    by_category = {}
    for s in sources:
        rel = s.relative_to(SOURCES_DIR)
        cat = rel.parts[0]
        by_category.setdefault(cat, []).append(s)

    selected = []
    categories = sorted(by_category.keys())
    # Round-robin across categories
    idx = 0
    while len(selected) < n and idx < max(len(v) for v in by_category.values()):
        for cat in categories:
            if len(selected) >= n:
                break
            if idx < len(by_category[cat]):
                selected.append(by_category[cat][idx])
        idx += 1
    return selected


# ---------------------------------------------------------------------------
# Progress saving
# ---------------------------------------------------------------------------

def save_progress(candidates, metadata, filepath):
    """Save current progress to disk."""
    output = {
        "metadata": metadata,
        "candidates": candidates,
    }
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(output, f, indent=2)


def load_progress(filepath):
    """Load existing progress if available."""
    if filepath.exists():
        with open(filepath) as f:
            data = json.load(f)
        return data.get("candidates", []), data.get("metadata", {})
    return [], {}


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process_source(client, source_file, source_urls):
    """Process a single source file. Returns (entities, input_tokens, output_tokens)."""
    content = source_file.read_text(encoding="utf-8")
    strategy, chunks, category = get_processing_strategy(source_file, content)

    rel_path = str(source_file.relative_to(SOURCES_DIR))
    url_entry = source_urls.get(rel_path, {})
    source_url = url_entry.get("url") if isinstance(url_entry, dict) else url_entry

    all_entities = []
    total_in = 0
    total_out = 0

    skip_headings = re.compile(
        r'(reference|bibliography|appendix|master reference|table of contents|acknowledgement|about the author)',
        re.I,
    )

    if strategy == "report":
        # chunks is list of (heading, text) tuples
        print(f"    Strategy: report, {len(chunks)} sections")
        for i, (heading, text) in enumerate(chunks):
            if len(text.strip()) < 50:
                continue
            if skip_headings.search(heading):
                print(f"      Section '{heading[:50]}': SKIPPED (reference/appendix)")
                continue
            system, user = build_prompt(strategy, text, section_heading=heading)
            entities, in_tok, out_tok = call_api(client, system, user)
            total_in += in_tok
            total_out += out_tok
            for e in entities:
                e["source_file"] = rel_path
                e["source_category"] = category
                e["source_url"] = source_url
                e["source_section"] = heading
            all_entities.extend(entities)
            print(f"      Section '{heading[:50]}': {len(entities)} entities")
            if i < len(chunks) - 1:
                time.sleep(CONFIG["batch_delay"])
    else:
        # chunks is list of text strings
        print(f"    Strategy: {strategy}, {len(chunks)} chunk(s)")
        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) < 50:
                continue
            system, user = build_prompt(strategy, chunk)
            entities, in_tok, out_tok = call_api(client, system, user)
            total_in += in_tok
            total_out += out_tok
            for e in entities:
                e["source_file"] = rel_path
                e["source_category"] = category
                e["source_url"] = source_url
                if len(chunks) > 1:
                    e["source_chunk"] = i + 1
            all_entities.extend(entities)
            if len(chunks) > 1:
                print(f"      Chunk {i + 1}/{len(chunks)}: {len(entities)} entities")
            if i < len(chunks) - 1:
                time.sleep(CONFIG["batch_delay"])

    return all_entities, total_in, total_out


def main():
    parser = argparse.ArgumentParser(description="Extract hyper-entity candidates from source files")
    parser.add_argument("--dry-run", type=int, metavar="N",
                        help="Process only N files (sampled across categories)")
    parser.add_argument("--resume", action="store_true",
                        help="Skip already-processed sources from progress file")
    args = parser.parse_args()

    # API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        return
    client = Anthropic(api_key=api_key)

    # Load source URLs
    source_urls = load_source_urls()

    # Find sources
    all_sources = get_all_sources()
    print(f"Found {len(all_sources)} source files")

    if args.dry_run:
        all_sources = select_dry_run_sources(all_sources, args.dry_run)
        print(f"Dry run: processing {len(all_sources)} files")

    # Resume support
    progress_file = OUTPUT_DIR / "raw_candidates_progress.json"
    output_file = OUTPUT_DIR / "raw_candidates.json"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = []
    processed_files = set()

    if args.resume:
        candidates, _ = load_progress(progress_file)
        processed_files = {c["source_file"] for c in candidates}
        print(f"Resuming: {len(processed_files)} sources already processed, {len(candidates)} candidates loaded")

    # Track stats
    total_input_tokens = 0
    total_output_tokens = 0
    by_category = {}

    # Count already-loaded candidates into by_category
    for c in candidates:
        cat = c.get("source_category", "unknown")
        if cat not in by_category:
            by_category[cat] = {"sources": set(), "candidates": 0}
        by_category[cat]["sources"].add(c["source_file"])
        by_category[cat]["candidates"] += 1

    # Process
    sources_to_process = [
        s for s in all_sources
        if str(s.relative_to(SOURCES_DIR)) not in processed_files
    ]
    print(f"Processing {len(sources_to_process)} sources...")
    print()

    for idx, source_file in enumerate(sources_to_process):
        rel_path = str(source_file.relative_to(SOURCES_DIR))
        rel = source_file.relative_to(SOURCES_DIR)
        category = rel.parts[0]

        print(f"[{idx + 1}/{len(sources_to_process)}] {rel_path}")

        try:
            entities, in_tok, out_tok = process_source(client, source_file, source_urls)
        except Exception as e:
            print(f"    ERROR processing {rel_path}: {e}")
            entities, in_tok, out_tok = [], 0, 0

        total_input_tokens += in_tok
        total_output_tokens += out_tok

        if category not in by_category:
            by_category[category] = {"sources": set(), "candidates": 0}
        by_category[category]["sources"].add(rel_path)
        by_category[category]["candidates"] += len(entities)

        candidates.extend(entities)
        print(f"    -> {len(entities)} entities (tokens: {in_tok:,} in / {out_tok:,} out)")

        # Save incremental progress
        progress_metadata = {
            "model": CONFIG["model"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "sources_processed": len(processed_files) + idx + 1,
            "total_candidates": len(candidates),
        }
        save_progress(candidates, progress_metadata, progress_file)

        # Rate limiting delay
        if idx < len(sources_to_process) - 1:
            time.sleep(CONFIG["batch_delay"])

    # Build final metadata
    cost_in = (total_input_tokens / 1_000_000) * INPUT_COST_PER_M
    cost_out = (total_output_tokens / 1_000_000) * OUTPUT_COST_PER_M

    # Serialize by_category (convert sets to counts)
    by_category_out = {}
    for cat, info in sorted(by_category.items()):
        by_category_out[cat] = {
            "sources": len(info["sources"]),
            "candidates": info["candidates"],
        }

    total_sources = sum(v["sources"] for v in by_category_out.values())

    metadata = {
        "model": CONFIG["model"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_sources": total_sources,
        "total_candidates": len(candidates),
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "estimated_cost_usd": round(cost_in + cost_out, 2),
        "by_category": by_category_out,
    }

    # Save final output
    save_progress(candidates, metadata, output_file)
    print()
    print("=" * 60)
    print(f"DONE — {len(candidates)} candidates from {total_sources} sources")
    print(f"Tokens: {total_input_tokens:,} input / {total_output_tokens:,} output")
    print(f"Estimated cost: ${cost_in + cost_out:.2f} (${cost_in:.2f} in + ${cost_out:.2f} out)")
    print(f"By category:")
    for cat, info in by_category_out.items():
        print(f"  {cat}: {info['sources']} sources -> {info['candidates']} candidates")
    print(f"Output: {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()

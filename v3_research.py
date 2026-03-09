#!/usr/bin/env python3
"""
v3_research.py — Web research for deduplicated hyper-entity candidates.

Uses Claude Haiku 4.5 with built-in web search tool to ground each entity with
real-world evidence (organizations, funding, TRL, publications, state of the art).

Reads results/v3/deduplicated.json (189 candidates), outputs results/v3/researched.json.
"""

import argparse
import asyncio
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import anthropic
from anthropic import RateLimitError, APIStatusError

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CONFIG = {
    "model": "claude-haiku-4-5-20251001",
    "max_tokens": 2048,
    "temperature": 0,
    "input_file": Path("results/v3/deduplicated.json"),
    "output_dir": Path("results/v3"),
    "output_file": Path("results/v3/researched.json"),
    "progress_file": Path("results/v3/researched_progress.json"),
    "max_retries": 3,
    "semaphore_limit": 10,
    "save_every": 10,
    "max_web_searches": 5,
}

# Haiku 4.5 pricing
INPUT_COST_PER_M = 0.80
OUTPUT_COST_PER_M = 4.0
# Web search: $10 per 1000 searches (Anthropic pricing)
WEB_SEARCH_COST_EACH = 0.01

# ---------------------------------------------------------------------------
# JSON extraction (from v3_dedup.py)
# ---------------------------------------------------------------------------

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
    for start_char, end_char in [("{", "}"), ("[", "]")]:
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
# Research schema
# ---------------------------------------------------------------------------

RESEARCH_SCHEMA = """{
  "organizations": [
    {"name": "Org Name", "url": "https://...", "role": "Building X"}
  ],
  "funding": "Series A $10M from Y in 2024",
  "trl": 3,
  "trl_justification": "Lab prototypes demonstrated but no field testing",
  "key_publications": [
    {"title": "Paper Title", "date": "2024", "url": "https://..."}
  ],
  "state_of_the_art": "3-5 sentences on where things stand",
  "barriers": "2-3 sentences on what's blocking progress"
}"""

RESEARCH_PROMPT = """Research this proposed technology/system/institution:

Name: {name}
Description: {one_liner}
Mechanism: {mechanism}
Existing work: {exists_today}

Search the web to find:
1. ORGANIZATIONS (2-5) working on this or closely related tech — provide name, URL, and role
2. FUNDING — specific amounts, sources, and years if findable
3. TRL LEVEL (1-9) — Technology Readiness Level with justification
4. KEY PUBLICATIONS/DEMOS (1-3) — with titles, dates, and URLs
5. STATE OF THE ART — 3-5 sentences on where things actually stand today
6. BARRIERS — 2-3 sentences on what's blocking progress

Return your findings as a JSON object with this exact structure:
{schema}

If you cannot find information for a field, use "None found" for strings, [] for arrays, and 1 for TRL.
Return ONLY the JSON object, no other text."""


# ---------------------------------------------------------------------------
# API calling
# ---------------------------------------------------------------------------

def count_web_searches(response):
    """Count the number of web search tool uses in a response."""
    stu = getattr(response.usage, "server_tool_use", None)
    if stu:
        return getattr(stu, "web_search_requests", 0)
    return 0


def extract_text_from_response(response):
    """Extract all text blocks from response (skipping tool_use/tool_result blocks)."""
    texts = []
    for block in response.content:
        if getattr(block, "type", None) == "text":
            texts.append(block.text)
    return "\n".join(texts)


async def research_entity(client, sem, entity, idx, total):
    """Research a single entity via Haiku with web search. Returns (research_dict, in_tok, out_tok, search_count)."""
    name = entity.get("name", "Unknown")
    prompt = RESEARCH_PROMPT.format(
        name=name,
        one_liner=entity.get("one_liner", ""),
        mechanism=entity.get("mechanism", ""),
        exists_today=entity.get("exists_today", ""),
        schema=RESEARCH_SCHEMA,
    )

    for attempt in range(CONFIG["max_retries"]):
        async with sem:
            try:
                response = await client.messages.create(
                    model=CONFIG["model"],
                    max_tokens=CONFIG["max_tokens"],
                    temperature=CONFIG["temperature"],
                    system="You are a research analyst. Search the web to find real-world evidence about proposed technologies. Return valid JSON only.",
                    messages=[{"role": "user", "content": prompt}],
                    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": CONFIG["max_web_searches"]}],
                )
                text = extract_text_from_response(response)
                in_tok = response.usage.input_tokens
                out_tok = response.usage.output_tokens
                search_count = count_web_searches(response)

                research = extract_json(text)

                # Validate expected fields
                if not isinstance(research, dict):
                    raise ValueError(f"Expected dict, got {type(research)}")

                # Ensure required fields exist with defaults
                research.setdefault("organizations", [])
                research.setdefault("funding", "None found")
                research.setdefault("trl", 1)
                research.setdefault("trl_justification", "")
                research.setdefault("key_publications", [])
                research.setdefault("state_of_the_art", "None found")
                research.setdefault("barriers", "None found")

                print(f"  [{idx + 1}/{total}] {name[:50]} — TRL {research['trl']}, {len(research['organizations'])} orgs, {search_count} searches ({in_tok:,} in / {out_tok:,} out)")
                return research, in_tok, out_tok, search_count

            except RateLimitError:
                wait = (2 ** attempt) * 2
                print(f"  [{idx + 1}/{total}] {name[:40]} — rate limited, waiting {wait}s (attempt {attempt + 1})")
                await asyncio.sleep(wait)
            except (json.JSONDecodeError, ValueError) as e:
                if attempt < CONFIG["max_retries"] - 1:
                    wait = 2 ** attempt
                    print(f"  [{idx + 1}/{total}] {name[:40]} — JSON error: {e}, retrying in {wait}s")
                    await asyncio.sleep(wait)
                else:
                    print(f"  [{idx + 1}/{total}] {name[:40]} — FAILED after {CONFIG['max_retries']} attempts: {e}")
                    return None, 0, 0, 0
            except APIStatusError as e:
                wait = (2 ** attempt) * 2
                print(f"  [{idx + 1}/{total}] {name[:40]} — API error ({e.status_code}), retrying in {wait}s")
                await asyncio.sleep(wait)
            except Exception as e:
                print(f"  [{idx + 1}/{total}] {name[:40]} — unexpected error: {e}")
                return None, 0, 0, 0

    print(f"  [{idx + 1}/{total}] {name[:40]} — all retries exhausted")
    return None, 0, 0, 0


# ---------------------------------------------------------------------------
# Progress management
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
# Main
# ---------------------------------------------------------------------------

async def async_main(args):
    # Load input
    input_file = CONFIG["input_file"]
    if not input_file.exists():
        print(f"ERROR: {input_file} not found")
        return

    with open(input_file) as f:
        data = json.load(f)

    candidates = data["candidates"]
    print(f"Loaded {len(candidates)} candidates from {input_file}")

    # Resume support: load already-researched candidates
    progress_file = CONFIG["progress_file"]
    output_file = CONFIG["output_file"]
    CONFIG["output_dir"].mkdir(parents=True, exist_ok=True)

    researched = []
    already_done = set()

    if args.resume and progress_file.exists():
        researched, _ = load_progress(progress_file)
        already_done = {c.get("name") for c in researched if c.get("research")}
        print(f"Resuming: {len(already_done)} entities already researched")

    # Determine which entities to process
    to_process = []
    for c in candidates:
        if c.get("name") in already_done:
            continue
        to_process.append(c)

    if args.dry_run is not None:
        to_process = to_process[:args.dry_run]
        print(f"Dry run: processing {len(to_process)} entities")

    if not to_process:
        print("Nothing to process.")
        return

    # API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        return
    client = anthropic.AsyncAnthropic(api_key=api_key)

    # Build a name -> candidate map for quick lookup
    name_to_idx = {}
    for i, c in enumerate(candidates):
        name_to_idx[c.get("name")] = i

    # Copy all candidates for output (preserve order)
    if args.resume and researched:
        # Build from progress: keep already-researched versions
        output_candidates = list(researched)
        # Add any new candidates not in progress
        progress_names = {c.get("name") for c in researched}
        for c in candidates:
            if c.get("name") not in progress_names:
                output_candidates.append(c.copy())
    else:
        output_candidates = [c.copy() for c in candidates]

    # Create name -> output index for updating
    name_to_output_idx = {}
    for i, c in enumerate(output_candidates):
        name_to_output_idx[c.get("name")] = i

    print(f"\nProcessing {len(to_process)} entities with semaphore={CONFIG['semaphore_limit']}...\n")

    # Process entities with controlled concurrency
    sem = asyncio.Semaphore(CONFIG["semaphore_limit"])
    total = len(to_process)
    total_in_tok = 0
    total_out_tok = 0
    total_searches = 0
    succeeded = 0
    failed = 0

    # Process in batches for incremental saving
    batch_size = CONFIG["save_every"]
    for batch_start in range(0, total, batch_size):
        batch = to_process[batch_start:batch_start + batch_size]
        tasks = []
        for i, entity in enumerate(batch):
            global_idx = batch_start + i
            task = research_entity(client, sem, entity, global_idx, total)
            tasks.append((entity, task))

        # Run batch concurrently
        results = await asyncio.gather(*[t for _, t in tasks])

        for (entity, _), (research, in_tok, out_tok, search_count) in zip(tasks, results):
            total_in_tok += in_tok
            total_out_tok += out_tok
            total_searches += search_count

            name = entity.get("name")
            out_idx = name_to_output_idx.get(name)
            if out_idx is not None:
                if research is not None:
                    output_candidates[out_idx]["research"] = research
                    succeeded += 1
                else:
                    failed += 1

        # Incremental save
        progress_metadata = {
            "model": CONFIG["model"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "entities_researched": succeeded,
            "entities_failed": failed,
            "total_input_tokens": total_in_tok,
            "total_output_tokens": total_out_tok,
            "total_web_searches": total_searches,
        }
        save_progress(output_candidates, progress_metadata, progress_file)
        processed_so_far = batch_start + len(batch)
        print(f"  -- Saved progress: {processed_so_far}/{total} processed, {succeeded} ok, {failed} failed --\n")

    # Cost calculation
    cost_in = (total_in_tok / 1_000_000) * INPUT_COST_PER_M
    cost_out = (total_out_tok / 1_000_000) * OUTPUT_COST_PER_M
    cost_search = total_searches * WEB_SEARCH_COST_EACH
    total_cost = round(cost_in + cost_out + cost_search, 2)

    # Build final metadata
    metadata = {
        "model": CONFIG["model"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_candidates": len(output_candidates),
        "entities_researched": succeeded,
        "entities_failed": failed,
        "total_input_tokens": total_in_tok,
        "total_output_tokens": total_out_tok,
        "total_web_searches": total_searches,
        "estimated_cost_usd": total_cost,
        "cost_breakdown": {
            "input": round(cost_in, 4),
            "output": round(cost_out, 4),
            "web_search": round(cost_search, 4),
        },
    }

    # Save final output
    save_progress(output_candidates, metadata, output_file)

    # TRL distribution
    trl_dist = {}
    for c in output_candidates:
        r = c.get("research")
        if r:
            trl = r.get("trl", 0)
            trl_dist[trl] = trl_dist.get(trl, 0) + 1

    print(f"\n{'=' * 60}")
    print(f"DONE — {succeeded} researched, {failed} failed (of {total} processed)")
    print(f"Tokens: {total_in_tok:,} input / {total_out_tok:,} output")
    print(f"Web searches: {total_searches}")
    print(f"Estimated cost: ${total_cost} (${cost_in:.2f} in + ${cost_out:.2f} out + ${cost_search:.2f} search)")
    if trl_dist:
        print(f"TRL distribution: {dict(sorted(trl_dist.items()))}")
    print(f"Output: {output_file}")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Web research for hyper-entity candidates")
    parser.add_argument("--dry-run", type=int, metavar="N",
                        help="Process only N entities")
    parser.add_argument("--resume", action="store_true",
                        help="Skip already-researched entities from progress file")
    args = parser.parse_args()

    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()

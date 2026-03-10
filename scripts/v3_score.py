#!/usr/bin/env python3
"""
v3_score.py — Score hyper-entity candidates on d/acc values, actionability, and
transformative potential using Claude Haiku 4.5.

Reads results/v3/researched.json (189 candidates), outputs results/v3/scored.json.
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
    "input_file": Path("results/v3/researched.json"),
    "output_dir": Path("results/v3"),
    "output_file": Path("results/v3/scored.json"),
    "progress_file": Path("results/v3/scored_progress.json"),
    "max_retries": 3,
    "semaphore_limit": 15,
    "save_every": 10,
}

# Haiku 4.5 pricing
INPUT_COST_PER_M = 0.80
OUTPUT_COST_PER_M = 4.0

# ---------------------------------------------------------------------------
# JSON extraction (from v3_extract.py)
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
# Scoring prompt
# ---------------------------------------------------------------------------

SCORE_SCHEMA = """{
  "dacc": {
    "democratic": <0-5>,
    "democratic_evidence": "...",
    "decentralized": <0-5>,
    "decentralized_evidence": "...",
    "defensive": <0-5>,
    "defensive_evidence": "...",
    "differential": <0-5>,
    "differential_evidence": "..."
  },
  "actionability": {
    "readiness_bottleneck": "Physics|Engineering|Funding|Regulation|Coordination|Social Acceptance",
    "what_to_do_now": "Fund|Build|Research|Advocate|Convene|Nothing Yet",
    "foresight_connection": <0-3>
  },
  "transformative": {
    "score": <0-5>,
    "evidence": "..."
  }
}"""

SCORE_PROMPT = """Score this hyper-entity candidate on three dimensions. Use ONLY evidence from the provided description and research data. No evidence = score 0.

## Entity
Name: {name}
One-liner: {one_liner}
Mechanism: {mechanism}
Exists today: {exists_today}
Source quote: {source_quote}

## Research data
Organizations: {organizations}
Funding: {funding}
TRL: {trl} — {trl_justification}
Publications: {publications}
State of the art: {state_of_art}
Barriers: {barriers}

## Scoring dimensions

### A. d/acc Values (each 0-5)
- **Democratic**: Does this distribute decision-making power? (0=concentrates power, 5=radically democratizes)
- **Decentralized**: Does this reduce single points of failure/control? (0=highly centralized, 5=fully distributed)
- **Defensive**: Does this protect rather than attack? Is it defense-dominant? (0=offensive, 5=purely defensive)
- **Differential**: Does this accelerate defensive tech faster than offensive tech? (0=accelerates offense, 5=strongly differential)

### B. Actionability
- **readiness_bottleneck**: What is the SINGLE biggest barrier? One of: Physics, Engineering, Funding, Regulation, Coordination, Social Acceptance
- **what_to_do_now**: What should someone do TODAY? One of: Fund, Build, Research, Advocate, Convene, Nothing Yet
- **foresight_connection**: How prominently discussed in source material? (0=barely mentioned, 1=mentioned in passing, 2=substantively discussed, 3=central focus)

### C. Transformative potential (0-5)
- 0=incremental improvement, 1=notable advance, 2=transforms a niche, 3=transforms a field, 4=transforms multiple fields, 5=civilizational new action space

Return ONLY a JSON object with this structure:
{schema}"""


def build_entity_prompt(entity):
    """Build scoring prompt for a single entity."""
    research = entity.get("research", {})

    # Format organizations
    orgs = research.get("organizations", [])
    if orgs:
        org_str = "; ".join(
            f"{o.get('name', '?')} ({o.get('role', '')})" for o in orgs
        )
    else:
        org_str = "None found"

    # Format publications
    pubs = research.get("key_publications", [])
    if pubs:
        pub_str = "; ".join(
            f"{p.get('title', '?')} ({p.get('date', '?')})" for p in pubs
        )
    else:
        pub_str = "None found"

    # Format source quote (may be list from merging)
    source_quote = entity.get("source_quote", "")
    if isinstance(source_quote, list):
        source_quote = " | ".join(source_quote)

    return SCORE_PROMPT.format(
        name=entity.get("name", "Unknown"),
        one_liner=entity.get("one_liner", ""),
        mechanism=entity.get("mechanism", ""),
        exists_today=entity.get("exists_today", ""),
        source_quote=source_quote,
        organizations=org_str,
        funding=research.get("funding", "None found"),
        trl=research.get("trl", "?"),
        trl_justification=research.get("trl_justification", ""),
        publications=pub_str,
        state_of_art=research.get("state_of_the_art", "None found"),
        barriers=research.get("barriers", "None found"),
        schema=SCORE_SCHEMA,
    )


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

VALID_BOTTLENECKS = {"Physics", "Engineering", "Funding", "Regulation", "Coordination", "Social Acceptance"}
VALID_ACTIONS = {"Fund", "Build", "Research", "Advocate", "Convene", "Nothing Yet"}


def validate_scores(scores):
    """Validate and clamp score values. Returns cleaned scores dict."""
    dacc = scores.get("dacc", {})
    for dim in ("democratic", "decentralized", "defensive", "differential"):
        val = dacc.get(dim, 0)
        if not isinstance(val, (int, float)):
            val = 0
        dacc[dim] = max(0, min(5, int(round(val))))
        # Ensure evidence field exists
        ev_key = f"{dim}_evidence"
        if ev_key not in dacc:
            dacc[ev_key] = ""
    dacc["total"] = dacc["democratic"] + dacc["decentralized"] + dacc["defensive"] + dacc["differential"]

    act = scores.get("actionability", {})
    if act.get("readiness_bottleneck") not in VALID_BOTTLENECKS:
        act["readiness_bottleneck"] = "Engineering"  # safe default
    if act.get("what_to_do_now") not in VALID_ACTIONS:
        act["what_to_do_now"] = "Research"  # safe default
    fc = act.get("foresight_connection", 0)
    if not isinstance(fc, (int, float)):
        fc = 0
    act["foresight_connection"] = max(0, min(3, int(round(fc))))

    trans = scores.get("transformative", {})
    ts = trans.get("score", 0)
    if not isinstance(ts, (int, float)):
        ts = 0
    trans["score"] = max(0, min(5, int(round(ts))))
    if "evidence" not in trans:
        trans["evidence"] = ""

    # Composite = dacc.total + transformative.score
    composite = dacc["total"] + trans["score"]

    return {
        "dacc": dacc,
        "actionability": act,
        "transformative": trans,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# API calling
# ---------------------------------------------------------------------------

async def score_entity(client, sem, entity, idx, total):
    """Score a single entity. Returns (scores_dict, in_tok, out_tok)."""
    name = entity.get("name", "Unknown")
    prompt = build_entity_prompt(entity)

    for attempt in range(CONFIG["max_retries"]):
        async with sem:
            try:
                response = await client.messages.create(
                    model=CONFIG["model"],
                    max_tokens=CONFIG["max_tokens"],
                    temperature=CONFIG["temperature"],
                    system="You are an expert technology assessor. Score entities precisely using the provided rubrics. Return valid JSON only.",
                    messages=[{"role": "user", "content": prompt}],
                )
                text = response.content[0].text
                in_tok = response.usage.input_tokens
                out_tok = response.usage.output_tokens

                raw_scores = extract_json(text)
                if not isinstance(raw_scores, dict):
                    raise ValueError(f"Expected dict, got {type(raw_scores)}")

                scores = validate_scores(raw_scores)

                print(f"  [{idx + 1}/{total}] {name[:50]} — d/acc={scores['dacc']['total']}, trans={scores['transformative']['score']}, composite={scores['composite']} ({in_tok:,} in / {out_tok:,} out)")
                return scores, in_tok, out_tok

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
                    return None, 0, 0
            except APIStatusError as e:
                wait = (2 ** attempt) * 2
                print(f"  [{idx + 1}/{total}] {name[:40]} — API error ({e.status_code}), retrying in {wait}s")
                await asyncio.sleep(wait)
            except Exception as e:
                print(f"  [{idx + 1}/{total}] {name[:40]} — unexpected error: {e}")
                return None, 0, 0

    print(f"  [{idx + 1}/{total}] {name[:40]} — all retries exhausted")
    return None, 0, 0


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
# Summary statistics
# ---------------------------------------------------------------------------

def print_summary(candidates):
    """Print score distribution histograms."""
    scored = [c for c in candidates if c.get("scores")]

    if not scored:
        print("  No scored entities to summarize.")
        return

    # d/acc total distribution
    dacc_totals = [c["scores"]["dacc"]["total"] for c in scored]
    print(f"\n  d/acc total (0-20): min={min(dacc_totals)}, max={max(dacc_totals)}, mean={sum(dacc_totals)/len(dacc_totals):.1f}")
    dacc_hist = {}
    for v in dacc_totals:
        bucket = (v // 5) * 5
        label = f"{bucket}-{bucket+4}"
        dacc_hist[label] = dacc_hist.get(label, 0) + 1
    for bucket in sorted(dacc_hist.keys()):
        bar = "#" * dacc_hist[bucket]
        print(f"    {bucket:>5}: {bar} ({dacc_hist[bucket]})")

    # Per d/acc dimension
    for dim in ("democratic", "decentralized", "defensive", "differential"):
        vals = [c["scores"]["dacc"][dim] for c in scored]
        print(f"  {dim}: mean={sum(vals)/len(vals):.1f}, dist={dict(sorted({v: vals.count(v) for v in set(vals)}.items()))}")

    # Transformative distribution
    trans_scores = [c["scores"]["transformative"]["score"] for c in scored]
    print(f"\n  Transformative (0-5): min={min(trans_scores)}, max={max(trans_scores)}, mean={sum(trans_scores)/len(trans_scores):.1f}")
    for s in range(6):
        count = trans_scores.count(s)
        bar = "#" * count
        print(f"    {s}: {bar} ({count})")

    # Composite distribution
    composites = [c["scores"]["composite"] for c in scored]
    print(f"\n  Composite (0-25): min={min(composites)}, max={max(composites)}, mean={sum(composites)/len(composites):.1f}")

    # Actionability summaries
    bottlenecks = {}
    actions = {}
    for c in scored:
        act = c["scores"]["actionability"]
        b = act.get("readiness_bottleneck", "?")
        bottlenecks[b] = bottlenecks.get(b, 0) + 1
        a = act.get("what_to_do_now", "?")
        actions[a] = actions.get(a, 0) + 1

    print(f"\n  Readiness bottleneck: {dict(sorted(bottlenecks.items(), key=lambda x: -x[1]))}")
    print(f"  What to do now: {dict(sorted(actions.items(), key=lambda x: -x[1]))}")

    # Top 10 by composite
    top = sorted(scored, key=lambda c: -c["scores"]["composite"])[:10]
    print(f"\n  Top 10 by composite score:")
    for c in top:
        s = c["scores"]
        print(f"    {s['composite']:>2} (d/acc={s['dacc']['total']}, trans={s['transformative']['score']}) {c['name']}")


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

    # Resume support
    progress_file = CONFIG["progress_file"]
    output_file = CONFIG["output_file"]
    CONFIG["output_dir"].mkdir(parents=True, exist_ok=True)

    scored_candidates = []
    already_done = set()

    if args.resume and progress_file.exists():
        scored_candidates, _ = load_progress(progress_file)
        already_done = {c.get("name") for c in scored_candidates if c.get("scores")}
        print(f"Resuming: {len(already_done)} entities already scored")

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

    # Build output candidates list (preserve order)
    if args.resume and scored_candidates:
        output_candidates = list(scored_candidates)
        progress_names = {c.get("name") for c in scored_candidates}
        for c in candidates:
            if c.get("name") not in progress_names:
                output_candidates.append(c.copy())
    else:
        output_candidates = [c.copy() for c in candidates]

    # Name -> output index mapping
    name_to_output_idx = {}
    for i, c in enumerate(output_candidates):
        name_to_output_idx[c.get("name")] = i

    print(f"\nScoring {len(to_process)} entities with semaphore={CONFIG['semaphore_limit']}...\n")

    # Process in batches for incremental saving
    sem = asyncio.Semaphore(CONFIG["semaphore_limit"])
    total = len(to_process)
    total_in_tok = 0
    total_out_tok = 0
    succeeded = 0
    failed = 0

    batch_size = CONFIG["save_every"]
    for batch_start in range(0, total, batch_size):
        batch = to_process[batch_start:batch_start + batch_size]
        tasks = []
        for i, entity in enumerate(batch):
            global_idx = batch_start + i
            task = score_entity(client, sem, entity, global_idx, total)
            tasks.append((entity, task))

        results = await asyncio.gather(*[t for _, t in tasks])

        for (entity, _), (scores, in_tok, out_tok) in zip(tasks, results):
            total_in_tok += in_tok
            total_out_tok += out_tok

            name = entity.get("name")
            out_idx = name_to_output_idx.get(name)
            if out_idx is not None:
                if scores is not None:
                    output_candidates[out_idx]["scores"] = scores
                    succeeded += 1
                else:
                    failed += 1

        # Incremental save
        progress_metadata = {
            "model": CONFIG["model"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "entities_scored": succeeded,
            "entities_failed": failed,
            "total_input_tokens": total_in_tok,
            "total_output_tokens": total_out_tok,
        }
        save_progress(output_candidates, progress_metadata, progress_file)
        processed_so_far = batch_start + len(batch)
        print(f"  -- Saved progress: {processed_so_far}/{total} processed, {succeeded} ok, {failed} failed --\n")

    # Cost calculation
    cost_in = (total_in_tok / 1_000_000) * INPUT_COST_PER_M
    cost_out = (total_out_tok / 1_000_000) * OUTPUT_COST_PER_M
    total_cost = round(cost_in + cost_out, 2)

    # Build final metadata
    metadata = {
        "model": CONFIG["model"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_candidates": len(output_candidates),
        "entities_scored": succeeded,
        "entities_failed": failed,
        "total_input_tokens": total_in_tok,
        "total_output_tokens": total_out_tok,
        "estimated_cost_usd": total_cost,
        "cost_breakdown": {
            "input": round(cost_in, 4),
            "output": round(cost_out, 4),
        },
    }

    # Save final output
    save_progress(output_candidates, metadata, output_file)

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"DONE — {succeeded} scored, {failed} failed (of {total} processed)")
    print(f"Tokens: {total_in_tok:,} input / {total_out_tok:,} output")
    print(f"Estimated cost: ${total_cost} (${cost_in:.2f} in + ${cost_out:.2f} out)")

    print_summary(output_candidates)

    print(f"\nOutput: {output_file}")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Score hyper-entity candidates on d/acc, actionability, transformative potential")
    parser.add_argument("--dry-run", type=int, metavar="N",
                        help="Process only N entities")
    parser.add_argument("--resume", action="store_true",
                        help="Skip already-scored entities from progress file")
    args = parser.parse_args()

    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()

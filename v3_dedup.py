#!/usr/bin/env python3
"""
v3_dedup.py — Semantic deduplication of hyper-entity candidates.

Reads results/v3/raw_candidates.json (193 candidates), finds near-duplicates via
TF-IDF cosine similarity, confirms with Haiku LLM pairwise comparison, merges
confirmed duplicates, and assigns thematic groups.

Outputs results/v3/deduplicated.json.
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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CONFIG = {
    "model": "claude-haiku-4-5-20251001",
    "max_tokens": 1024,
    "temperature": 0,
    "input_file": Path("results/v3/raw_candidates.json"),
    "output_dir": Path("results/v3"),
    "pairs_file": Path("results/v3/dedup_pairs.json"),
    "output_file": Path("results/v3/deduplicated.json"),
    "max_retries": 3,
    "semaphore_limit": 20,
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
# TF-IDF pre-filtering
# ---------------------------------------------------------------------------

def build_candidate_text(c):
    """Combine name + one_liner + mechanism into a single text for TF-IDF."""
    parts = [
        c.get("name", ""),
        c.get("one_liner", ""),
        c.get("mechanism", ""),
    ]
    return " ".join(p for p in parts if p)


def find_similar_pairs(candidates, threshold):
    """Return list of (i, j, score) pairs with cosine similarity > threshold."""
    texts = [build_candidate_text(c) for c in candidates]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(texts)
    sim_matrix = cosine_similarity(tfidf_matrix)

    pairs = []
    n = len(candidates)
    for i in range(n):
        for j in range(i + 1, n):
            score = sim_matrix[i, j]
            if score > threshold:
                pairs.append((i, j, float(round(score, 4))))

    pairs.sort(key=lambda x: -x[2])
    return pairs


# ---------------------------------------------------------------------------
# LLM pairwise comparison
# ---------------------------------------------------------------------------

PAIRWISE_PROMPT = """You are comparing two hyper-entity candidates to determine if they describe the same concept.

Entity A:
- Name: {name_a}
- One-liner: {oneliner_a}
- Mechanism: {mechanism_a}

Entity B:
- Name: {name_b}
- One-liner: {oneliner_b}
- Mechanism: {mechanism_b}

Classify the relationship as exactly one of:
- SAME: These describe the same entity/concept/system (even if named differently). They should be merged.
- OVERLAPPING: Related concepts in the same domain, but distinct enough to keep separate.
- DISTINCT: Unrelated or only superficially similar.

Return a JSON object: {{"verdict": "SAME"|"OVERLAPPING"|"DISTINCT", "reason": "one sentence explanation"}}"""


async def compare_pair(client, sem, candidates, i, j, score):
    """Compare a single pair via Haiku. Returns (i, j, verdict, reason, in_tok, out_tok)."""
    a = candidates[i]
    b = candidates[j]

    prompt = PAIRWISE_PROMPT.format(
        name_a=a.get("name", ""),
        oneliner_a=a.get("one_liner", ""),
        mechanism_a=a.get("mechanism", ""),
        name_b=b.get("name", ""),
        oneliner_b=b.get("one_liner", ""),
        mechanism_b=b.get("mechanism", ""),
    )

    for attempt in range(CONFIG["max_retries"]):
        async with sem:
            try:
                response = await client.messages.create(
                    model=CONFIG["model"],
                    max_tokens=CONFIG["max_tokens"],
                    temperature=CONFIG["temperature"],
                    system="You compare entity descriptions and return JSON only.",
                    messages=[{"role": "user", "content": prompt}],
                )
                text = response.content[0].text
                in_tok = response.usage.input_tokens
                out_tok = response.usage.output_tokens
                result = extract_json(text)
                verdict = result.get("verdict", "DISTINCT").upper()
                reason = result.get("reason", "")
                if verdict not in ("SAME", "OVERLAPPING", "DISTINCT"):
                    verdict = "DISTINCT"
                return (i, j, verdict, reason, in_tok, out_tok)
            except RateLimitError:
                wait = (2 ** attempt) * 2
                await asyncio.sleep(wait)
            except (json.JSONDecodeError, ValueError):
                if attempt < CONFIG["max_retries"] - 1:
                    await asyncio.sleep(2 ** attempt)
                else:
                    return (i, j, "DISTINCT", "JSON parse error", 0, 0)
            except APIStatusError as e:
                wait = (2 ** attempt) * 2
                await asyncio.sleep(wait)
            except Exception as e:
                return (i, j, "DISTINCT", f"Error: {e}", 0, 0)

    return (i, j, "DISTINCT", "Retries exhausted", 0, 0)


async def compare_all_pairs(client, candidates, pairs, cached_results):
    """Compare all pairs, skipping cached ones. Returns list of result dicts."""
    sem = asyncio.Semaphore(CONFIG["semaphore_limit"])
    results = list(cached_results)  # start with cached
    cached_keys = {(r["i"], r["j"]) for r in cached_results}

    to_compare = [(i, j, s) for i, j, s in pairs if (i, j) not in cached_keys]

    if not to_compare:
        print(f"All {len(pairs)} pairs already cached, skipping API calls.")
        return results

    print(f"Comparing {len(to_compare)} pairs via Haiku (skipping {len(cached_keys)} cached)...")

    tasks = [compare_pair(client, sem, candidates, i, j, s) for i, j, s in to_compare]
    total = len(tasks)
    completed = 0
    total_in = 0
    total_out = 0

    for coro in asyncio.as_completed(tasks):
        i, j, verdict, reason, in_tok, out_tok = await coro
        completed += 1
        total_in += in_tok
        total_out += out_tok
        results.append({
            "i": i, "j": j,
            "name_a": candidates[i].get("name", ""),
            "name_b": candidates[j].get("name", ""),
            "cosine": next((s for ii, jj, s in pairs if ii == i and jj == j), 0),
            "verdict": verdict,
            "reason": reason,
        })
        if completed % 20 == 0 or completed == total:
            print(f"  [{completed}/{total}] Last: {candidates[i]['name'][:30]} vs {candidates[j]['name'][:30]} -> {verdict}")

    return results, total_in, total_out


# ---------------------------------------------------------------------------
# Union-Find for merging
# ---------------------------------------------------------------------------

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


def merge_clusters(candidates, same_pairs):
    """Merge candidates that are SAME. Returns list of merged candidates + merge log."""
    n = len(candidates)
    uf = UnionFind(n)

    for pair in same_pairs:
        uf.union(pair["i"], pair["j"])

    # Group by root
    groups = {}
    for idx in range(n):
        root = uf.find(idx)
        groups.setdefault(root, []).append(idx)

    merged = []
    merge_log = []

    for root, members in sorted(groups.items()):
        cluster_candidates = [candidates[m] for m in members]

        if len(members) == 1:
            merged.append(cluster_candidates[0].copy())
            continue

        # Pick the best name: longest/most specific
        best = max(cluster_candidates, key=lambda c: len(c.get("name", "")))
        result = best.copy()

        # Merge source_quotes
        all_quotes = []
        all_files = []
        all_names = []
        for c in cluster_candidates:
            q = c.get("source_quote", "")
            if q and q not in all_quotes:
                all_quotes.append(q)
            f = c.get("source_file", "")
            if f and f not in all_files:
                all_files.append(f)
            all_names.append(c.get("name", ""))

        if len(all_quotes) > 1:
            result["source_quote"] = all_quotes
        if len(all_files) > 1:
            result["source_file"] = all_files

        result["merged_from"] = all_names

        merge_log.append({
            "kept": best.get("name", ""),
            "merged": [c.get("name", "") for c in cluster_candidates if c is not best],
            "member_indices": members,
        })

        merged.append(result)

    return merged, merge_log


# ---------------------------------------------------------------------------
# Thematic grouping
# ---------------------------------------------------------------------------

GROUPING_PROMPT = """Below is a list of {n} hyper-entity candidates (future technologies, systems, and institutions). Assign each one to exactly ONE thematic group. Create 8-12 groups with descriptive names.

Return a JSON object mapping each entity name (exactly as given) to its group name.
Example: {{"Entity Name": "Decentralized Governance", "Another Entity": "Biotech & Health"}}

Entities:
{entity_list}"""


async def assign_groups(client, candidates):
    """Send candidates to Haiku for thematic grouping. Returns (name->group dict, in_tok, out_tok)."""
    entity_list = "\n".join(
        f"- {c.get('name', 'Unknown')}: {c.get('one_liner', '')}"
        for c in candidates
    )

    prompt = GROUPING_PROMPT.format(n=len(candidates), entity_list=entity_list)

    for attempt in range(CONFIG["max_retries"]):
        try:
            response = await client.messages.create(
                model=CONFIG["model"],
                max_tokens=4096,
                temperature=CONFIG["temperature"],
                system="You categorize entities into thematic groups and return JSON only.",
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text
            in_tok = response.usage.input_tokens
            out_tok = response.usage.output_tokens
            mapping = extract_json(text)
            if isinstance(mapping, dict):
                return mapping, in_tok, out_tok
            raise ValueError("Expected JSON object for grouping")
        except RateLimitError:
            wait = (2 ** attempt) * 2
            print(f"  Rate limited during grouping, waiting {wait}s")
            await asyncio.sleep(wait)
        except Exception as e:
            if attempt < CONFIG["max_retries"] - 1:
                print(f"  Grouping error: {e}, retrying...")
                await asyncio.sleep(2 ** attempt)
            else:
                print(f"  Grouping failed after retries: {e}")
                return {}, 0, 0

    return {}, 0, 0


# ---------------------------------------------------------------------------
# Caching
# ---------------------------------------------------------------------------

def load_cached_pairs(filepath):
    """Load previously saved pair comparisons."""
    if filepath.exists():
        with open(filepath) as f:
            data = json.load(f)
        return data.get("results", [])
    return []


def save_pairs(filepath, pairs_data, results):
    """Save pair comparison results for incremental reruns."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "tfidf_pairs": [{"i": i, "j": j, "cosine": s} for i, j, s in pairs_data],
            "results": results,
        }, f, indent=2)


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

    # Step 1: TF-IDF pre-filter
    threshold = args.threshold
    print(f"\nStep 1: TF-IDF cosine similarity (threshold={threshold})...")
    pairs = find_similar_pairs(candidates, threshold)
    print(f"  Found {len(pairs)} pairs above threshold (out of {len(candidates) * (len(candidates) - 1) // 2} total)")

    if pairs:
        print(f"  Top 10 most similar:")
        for i, j, score in pairs[:10]:
            print(f"    {score:.3f}  {candidates[i]['name'][:40]}  <->  {candidates[j]['name'][:40]}")

    if args.dry_run:
        print(f"\n[DRY RUN] Would compare {len(pairs)} pairs via Haiku. Exiting.")
        print(f"\nAll pairs above threshold:")
        for i, j, score in pairs:
            print(f"  {score:.3f}  {candidates[i]['name']}  <->  {candidates[j]['name']}")
        return

    # API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        return
    client = anthropic.AsyncAnthropic(api_key=api_key)

    # Step 2: LLM pairwise comparison
    print(f"\nStep 2: LLM pairwise comparison ({len(pairs)} pairs)...")
    cached_results = load_cached_pairs(CONFIG["pairs_file"])
    if cached_results:
        print(f"  Loaded {len(cached_results)} cached pair results")

    result = await compare_all_pairs(client, candidates, pairs, cached_results)
    if isinstance(result, tuple):
        pair_results, pair_in_tok, pair_out_tok = result
    else:
        pair_results = result
        pair_in_tok, pair_out_tok = 0, 0

    # Save pairs for incremental reuse
    save_pairs(CONFIG["pairs_file"], pairs, pair_results)

    # Summarize verdicts
    verdicts = {}
    for r in pair_results:
        v = r["verdict"]
        verdicts[v] = verdicts.get(v, 0) + 1
    print(f"\n  Verdicts: {verdicts}")

    same_pairs = [r for r in pair_results if r["verdict"] == "SAME"]
    if same_pairs:
        print(f"\n  SAME pairs ({len(same_pairs)}):")
        for r in same_pairs:
            print(f"    {r['name_a']}  <->  {r['name_b']}  ({r['reason']})")

    # Step 3: Merge SAME entities
    print(f"\nStep 3: Merging SAME entities...")
    merged_candidates, merge_log = merge_clusters(candidates, same_pairs)
    print(f"  {len(candidates)} -> {len(merged_candidates)} candidates ({len(candidates) - len(merged_candidates)} merged)")
    for m in merge_log:
        print(f"    Kept '{m['kept']}', merged: {m['merged']}")

    # Step 4: Thematic grouping
    print(f"\nStep 4: Thematic grouping...")
    group_mapping, group_in_tok, group_out_tok = await assign_groups(client, merged_candidates)

    # Apply groups
    groups_used = set()
    unmatched = 0
    for c in merged_candidates:
        name = c.get("name", "")
        group = group_mapping.get(name, "Uncategorized")
        c["group"] = group
        groups_used.add(group)
        if group == "Uncategorized":
            unmatched += 1

    groups_sorted = sorted(groups_used)
    print(f"  Assigned {len(groups_sorted)} groups ({unmatched} uncategorized)")
    for g in groups_sorted:
        count = sum(1 for c in merged_candidates if c.get("group") == g)
        print(f"    {g}: {count}")

    # Cost calculation
    total_in = pair_in_tok + group_in_tok
    total_out = pair_out_tok + group_out_tok
    cost_in = (total_in / 1_000_000) * INPUT_COST_PER_M
    cost_out = (total_out / 1_000_000) * OUTPUT_COST_PER_M
    total_cost = round(cost_in + cost_out, 4)

    # Build output
    metadata = {
        "model": CONFIG["model"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input_candidates": len(candidates),
        "output_candidates": len(merged_candidates),
        "merges": merge_log,
        "pairs_compared": len(pair_results),
        "groups": groups_sorted,
        "total_input_tokens": total_in,
        "total_output_tokens": total_out,
        "estimated_cost_usd": total_cost,
    }

    output = {
        "metadata": metadata,
        "candidates": merged_candidates,
    }

    output_file = CONFIG["output_file"]
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"DONE — {len(merged_candidates)} deduplicated candidates ({len(candidates) - len(merged_candidates)} merged)")
    print(f"Pairs compared: {len(pair_results)} | Verdicts: {verdicts}")
    print(f"Groups: {len(groups_sorted)}")
    print(f"Tokens: {total_in:,} input / {total_out:,} output")
    print(f"Estimated cost: ${total_cost}")
    print(f"Output: {output_file}")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Deduplicate hyper-entity candidates")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run TF-IDF filtering only, print pairs, skip API calls")
    parser.add_argument("--threshold", type=float, default=0.3,
                        help="Cosine similarity threshold (default: 0.3)")
    args = parser.parse_args()

    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()

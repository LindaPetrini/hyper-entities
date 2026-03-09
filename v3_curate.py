#!/usr/bin/env python3
"""
v3_curate.py — Curate scored hyper-entity candidates into tiers.

Pure Python (no API calls). Two steps:
1. Match v3 entities to v2 consensus list via TF-IDF cosine similarity.
2. Apply tiering rules to produce Tier 1 (Spotlight) and Tier 2 (Watch list).

Reads:  results/v3/scored.json, results/consensus_entities.json
Writes: results/v3/curated.json, results/v3/scatter_data.json
"""

import json
from datetime import datetime, timezone
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SCORED_FILE = Path("results/v3/scored.json")
CONSENSUS_FILE = Path("results/consensus_entities.json")
OUTPUT_DIR = Path("results/v3")
CURATED_FILE = OUTPUT_DIR / "curated.json"
SCATTER_FILE = OUTPUT_DIR / "scatter_data.json"

MATCH_THRESHOLD = 0.4

# ---------------------------------------------------------------------------
# Step 1: Match v3 entities to v2 consensus
# ---------------------------------------------------------------------------

def match_v2_consensus(candidates, consensus_entities):
    """Match v3 candidates to v2 consensus entities using TF-IDF cosine similarity."""
    v3_names = [c["name"] for c in candidates]
    v2_names = [e["name"] for e in consensus_entities]

    if not v2_names:
        print("  No v2 consensus entities found.")
        return candidates

    # Build TF-IDF matrix over all names together
    all_names = v3_names + v2_names
    vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4), lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(all_names)

    v3_vectors = tfidf_matrix[: len(v3_names)]
    v2_vectors = tfidf_matrix[len(v3_names) :]

    # Compute pairwise similarity
    sim_matrix = cosine_similarity(v3_vectors, v2_vectors)

    matches = 0
    for i, candidate in enumerate(candidates):
        best_j = sim_matrix[i].argmax()
        best_score = sim_matrix[i][best_j]

        if best_score >= MATCH_THRESHOLD:
            v2_entity = consensus_entities[best_j]
            candidate["v2_consensus"] = True
            candidate["v2_voted_by"] = v2_entity.get("voted_by", [])
            candidate["v2_matched_name"] = v2_entity["name"]
            matches += 1
            print(f"  MATCH ({best_score:.2f}): {candidate['name'][:50]}  <->  {v2_entity['name'][:50]}")
        else:
            candidate["v2_consensus"] = False

    print(f"\n  Total matches: {matches} / {len(candidates)}")
    return candidates


# ---------------------------------------------------------------------------
# Step 2: Tiering
# ---------------------------------------------------------------------------

def apply_tiers(candidates):
    """Apply tiering rules. Returns (tier1, tier2) lists."""
    tier1 = []
    tier2 = []

    for c in candidates:
        scores = c.get("scores", {})
        dacc_total = scores.get("dacc", {}).get("total", 0)
        trans_score = scores.get("transformative", {}).get("score", 0)
        foresight = scores.get("actionability", {}).get("foresight_connection", 0)
        trl = c.get("research", {}).get("trl", 0)
        if not isinstance(trl, (int, float)):
            trl = 0

        is_v2 = c.get("v2_consensus", False)

        # Tier 1 thresholds
        if is_v2:
            dacc_threshold = 10
        else:
            dacc_threshold = 12

        if (dacc_total >= dacc_threshold
                and trans_score >= 3
                and foresight >= 2
                and trl >= 2):
            c["tier"] = 1
            tier1.append(c)
        else:
            c["tier"] = 2
            tier2.append(c)

    # Sort by composite score descending
    tier1.sort(key=lambda c: -c.get("scores", {}).get("composite", 0))
    tier2.sort(key=lambda c: -c.get("scores", {}).get("composite", 0))

    return tier1, tier2


# ---------------------------------------------------------------------------
# Scatter data
# ---------------------------------------------------------------------------

def build_scatter_data(candidates):
    """Build scatter_data.json for visualization."""
    scatter = []
    for c in candidates:
        scores = c.get("scores", {})
        scatter.append({
            "name": c.get("name", ""),
            "dacc_total": scores.get("dacc", {}).get("total", 0),
            "transformative": scores.get("transformative", {}).get("score", 0),
            "group": c.get("group", ""),
            "tier": c.get("tier", 2),
            "bottleneck": scores.get("actionability", {}).get("readiness_bottleneck", ""),
            "action": scores.get("actionability", {}).get("what_to_do_now", ""),
        })
    return scatter


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Load inputs
    if not SCORED_FILE.exists():
        print(f"ERROR: {SCORED_FILE} not found")
        return
    if not CONSENSUS_FILE.exists():
        print(f"ERROR: {CONSENSUS_FILE} not found")
        return

    with open(SCORED_FILE) as f:
        scored_data = json.load(f)
    candidates = scored_data["candidates"]

    with open(CONSENSUS_FILE) as f:
        consensus_data = json.load(f)
    consensus_entities = consensus_data.get("entities", [])

    print(f"Loaded {len(candidates)} scored candidates")
    print(f"Loaded {len(consensus_entities)} v2 consensus entities\n")

    # Step 1: Match to v2 consensus
    print("Step 1: Matching v3 entities to v2 consensus...\n")
    candidates = match_v2_consensus(candidates, consensus_entities)

    # Step 2: Apply tiers
    print("\nStep 2: Applying tiering rules...\n")
    tier1, tier2 = apply_tiers(candidates)

    v2_match_count = sum(1 for c in candidates if c.get("v2_consensus"))

    # Build metadata
    metadata = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_candidates": len(candidates),
        "tier1_count": len(tier1),
        "tier2_count": len(tier2),
        "v2_matches": v2_match_count,
    }

    # Write curated.json
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    curated_output = {
        "metadata": metadata,
        "tier1": tier1,
        "tier2": tier2,
    }
    with open(CURATED_FILE, "w") as f:
        json.dump(curated_output, f, indent=2)

    # Write scatter_data.json
    scatter = build_scatter_data(candidates)
    with open(SCATTER_FILE, "w") as f:
        json.dump(scatter, f, indent=2)

    # Summary
    print(f"  Tier 1 (Spotlight): {len(tier1)} entities")
    print(f"  Tier 2 (Watch list): {len(tier2)} entities")
    print(f"  v2 consensus matches: {v2_match_count}")

    # Print Tier 1 entities
    if tier1:
        print(f"\n  Tier 1 entities:")
        for c in tier1:
            s = c.get("scores", {})
            v2_tag = " [v2]" if c.get("v2_consensus") else ""
            print(f"    {s.get('composite', 0):>2} (d/acc={s.get('dacc', {}).get('total', 0)}, "
                  f"trans={s.get('transformative', {}).get('score', 0)}, "
                  f"fc={s.get('actionability', {}).get('foresight_connection', 0)}, "
                  f"trl={c.get('research', {}).get('trl', '?')}) "
                  f"{c['name'][:60]}{v2_tag}")

    print(f"\nOutput: {CURATED_FILE}")
    print(f"Scatter: {SCATTER_FILE}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Export hyper-entities data to CSV for multi-column sorting.
"""

import json
import pandas as pd
from pathlib import Path

CONFIG = {
    "input_json": "results/stage3_concrete/entities.json",
    "output_csv": "results/entities_full.csv",
}


def main():
    print("Loading data...")
    with open(CONFIG["input_json"]) as f:
        data = json.load(f)

    entities = data["entities"]
    print(f"Loaded {len(entities)} entities")

    # Flatten into rows
    rows = []
    for e in entities:
        row = {
            "id": e.get("id"),
            "name": e.get("name"),
            "category": e.get("category"),
            "description": e.get("description", "")[:200],  # Truncate for readability
            "cluster_id": e.get("cluster_id"),
            "cluster_name": e.get("cluster_name"),

            # Stage 1 consolidated
            "s1_total": e.get("stage1_consolidated", {}).get("total", 0),
            "s1_reality_gap": e.get("stage1_consolidated", {}).get("reality_gap", 0),
            "s1_transformative_potential": e.get("stage1_consolidated", {}).get("transformative_potential", 0),
            "s1_current_momentum": e.get("stage1_consolidated", {}).get("current_momentum", 0),

            # Stage 2 consolidated
            "s2_total": e.get("stage2_consolidated", {}).get("total", 0),
            "s2_transformative_power": e.get("stage2_consolidated", {}).get("transformative_power", 0),
            "s2_systemic_risk": e.get("stage2_consolidated", {}).get("systemic_risk", 0),
            "s2_lockin_effects": e.get("stage2_consolidated", {}).get("lockin_effects", 0),

            # d/acc scores
            "dacc_total": e.get("stage3_dacc", {}).get("total", 0),
            "dacc_democratic": e.get("stage3_dacc", {}).get("democratic", 0),
            "dacc_decentralized": e.get("stage3_dacc", {}).get("decentralized", 0),
            "dacc_defensive": e.get("stage3_dacc", {}).get("defensive", 0),
            "dacc_differential": e.get("stage3_dacc", {}).get("differential", 0),

            # Concreteness
            "concrete_score": e.get("concreteness", {}).get("score", 0),
            "concrete_verdict": e.get("concreteness", {}).get("verdict", ""),
            "core_technologies": ", ".join(e.get("concreteness", {}).get("core_technologies", [])),
            "concrete_version": e.get("concreteness", {}).get("concrete_version", "")[:300],
            "concrete_reasoning": e.get("concreteness", {}).get("reasoning", ""),

            # Additional info
            "problems_solved": e.get("problems_solved", "")[:200],
            "why_new_different": e.get("why_new_different", "")[:200],
        }
        rows.append(row)

    # Create DataFrame
    df = pd.DataFrame(rows)

    # Sort by concreteness then d/acc as default
    df = df.sort_values(["concrete_score", "dacc_total"], ascending=[False, False])

    # Save to CSV
    output_path = Path(CONFIG["output_csv"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"\nSaved to: {output_path}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nTop 10 by concreteness + d/acc:")
    print(df[["name", "concrete_score", "dacc_total", "concrete_verdict"]].head(10).to_string())

    # Also save a Parquet for faster pandas loading
    parquet_path = output_path.with_suffix(".parquet")
    df.to_parquet(parquet_path, index=False)
    print(f"\nAlso saved Parquet: {parquet_path}")

    return df


if __name__ == "__main__":
    df = main()

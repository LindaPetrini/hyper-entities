#!/usr/bin/env python3
"""
Apply Stage 2 assessment scoring (14-dimension impact table) to qualified entities.
Uses Claude API to score each entity on the 14 dimensions (0-5 each).
"""

import os
import json
from pathlib import Path
from anthropic import Anthropic
import time

# Configuration
CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-3-5-haiku-20241022",
    "input_json": "results/hyperentities_v3.json",
    "output_json": "results/hyperentities_v3_with_stage2.json",
    "max_tokens": 2000,
    "temperature": 0.3,
    "batch_size": 10,  # Process in batches to show progress
}

STAGE2_PROMPT = """You are assessing a hyper-entity using Stage 2: Impact Assessment.

STAGE 2: IMPACT ASSESSMENT (14 dimensions, 0-5 per dimension)

Score this entity on each dimension below. Provide ONLY the numeric scores.

| Dimension | What you're scoring | 0 | 5 |
|-----------|---------------------|---|---|
| Capability Discontinuity | New powers unlocked | Incremental | Phase change |
| Cross-Domain Reach | How many sectors it touches | Single domain | Many domains |
| Scalability | Speed + cheapness of global spread | Local / slow | Global / fast |
| Autonomy | Operates without ongoing human control | Fully manual | Largely autonomous |
| Composability | Can be embedded everywhere | Standalone | Universal substrate |
| Feedback Intensity | Strength of self-reinforcing loops | Weak | Explosive |
| Irreversibility | Difficulty of rollback once deployed | Easy | Practically impossible |
| Power Concentration | Centralizes leverage | Dispersed | Highly concentrated |
| Externality Magnitude | Size of spillovers (±) | Contained | Civilizational |
| Misuse Asymmetry | Harm vs benefit ratio | Symmetric | Offense-dominant |
| Governance Lag | Gap vs institutions | Aligned | Wildly outpaced |
| Narrative Lock-In | Inevitable story it enforces | Optional | Totalizing |
| Path Dependency | Futures foreclosed | Minimal | Many locked |
| Human Agency Impact | Effect on human choice | Expands | Compresses |

ENTITY TO ASSESS:
Name: {name}
Description: {description}
Category: {category}
Stage 1 Score: {stage1_score}/27

OUTPUT FORMAT (provide only these 14 numbers, one per line):
Capability Discontinuity: [0-5]
Cross-Domain Reach: [0-5]
Scalability: [0-5]
Autonomy: [0-5]
Composability: [0-5]
Feedback Intensity: [0-5]
Irreversibility: [0-5]
Power Concentration: [0-5]
Externality Magnitude: [0-5]
Misuse Asymmetry: [0-5]
Governance Lag: [0-5]
Narrative Lock-In: [0-5]
Path Dependency: [0-5]
Human Agency Impact: [0-5]
"""


def load_entities():
    """Load entities from JSON."""
    with open(CONFIG["input_json"]) as f:
        return json.load(f)


def assess_entity(client, entity):
    """Assess a single entity with Stage 2 scoring."""
    prompt = STAGE2_PROMPT.format(
        name=entity['name'],
        description=entity.get('description', 'No description'),
        category=entity.get('category', 'Unknown'),
        stage1_score=entity.get('total_score', 0)
    )

    try:
        message = client.messages.create(
            model=CONFIG["model"],
            max_tokens=CONFIG["max_tokens"],
            temperature=CONFIG["temperature"],
            messages=[{"role": "user", "content": prompt}]
        )

        result = message.content[0].text

        # Parse scores
        stage2_scores = {}
        lines = result.strip().split('\n')

        for line in lines:
            if ':' in line:
                parts = line.split(':')
                dimension = parts[0].strip()
                try:
                    score = int(parts[1].strip().split()[0])
                    stage2_scores[dimension] = max(0, min(5, score))  # Clamp 0-5
                except:
                    continue

        # Calculate total
        total = sum(stage2_scores.values())

        return {
            "status": "success",
            "stage2_scores": stage2_scores,
            "stage2_total": total,
            "tokens": {
                "input": message.usage.input_tokens,
                "output": message.usage.output_tokens
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "stage2_scores": {},
            "stage2_total": 0
        }


def main():
    """Main execution."""
    print("=" * 80)
    print("Stage 2 Assessment: Impact Scoring")
    print("=" * 80)
    print()

    # Load API key
    api_key = os.environ.get(CONFIG["api_key_env"])
    if not api_key:
        # Try loading from .env
        env_file = Path(".env")
        if env_file.exists():
            for line in env_file.read_text().split('\n'):
                if line.startswith('ANTHROPIC_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    break

    if not api_key:
        print(f"ERROR: {CONFIG['api_key_env']} not found")
        return

    print("✓ API key found")

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Load entities
    print("✓ Loading entities...")
    data = load_entities()
    entities = data['entities']

    # Filter to qualified entities only (Stage 1 score ≥18)
    qualified = [e for e in entities if e.get('qualified', False) and e.get('total_score', 0) >= 18]

    print(f"✓ Found {len(qualified)} qualified entities (≥18/27) to assess")
    print(f"  (Skipping {len(entities) - len(qualified)} entities below threshold)")
    print()

    # Process entities
    print("Assessing entities...")
    print("-" * 80)

    total_input = 0
    total_output = 0
    assessed = 0

    for i, entity in enumerate(qualified, 1):
        print(f"[{i}/{len(qualified)}] {entity['name'][:60]}...", end=" ", flush=True)

        result = assess_entity(client, entity)

        if result["status"] == "success":
            entity["stage2_scores"] = result["stage2_scores"]
            entity["stage2_total"] = result["stage2_total"]
            total_input += result["tokens"]["input"]
            total_output += result["tokens"]["output"]
            assessed += 1
            print(f"✓ ({result['stage2_total']}/70)")
        else:
            print(f"✗ {result.get('error', 'Unknown')}")

        # Small delay to avoid rate limits
        if i % 5 == 0:
            time.sleep(1)

    # Update metadata
    data['metadata']['stage2_assessed'] = assessed
    data['metadata']['stage2_statistics'] = {
        "assessed_entities": assessed,
        "avg_stage2_score": round(sum(e.get('stage2_total', 0) for e in qualified) / assessed, 2) if assessed > 0 else 0,
        "max_stage2_score": max((e.get('stage2_total', 0) for e in qualified), default=0),
    }

    # Save updated JSON
    print()
    print("-" * 80)
    print()
    print("Saving results...")
    with open(CONFIG["output_json"], 'w') as f:
        json.dump(data, f, indent=2)

    print()
    print("=" * 80)
    print("ASSESSMENT COMPLETE!")
    print("=" * 80)
    print(f"Entities assessed: {assessed}/{len(qualified)}")
    print(f"Total tokens: {total_input:,} in / {total_output:,} out")

    cost = (total_input / 1_000_000) * 0.8 + (total_output / 1_000_000) * 4
    print(f"Cost: ${cost:.2f}")

    if assessed > 0:
        avg_score = sum(e.get('stage2_total', 0) for e in qualified) / assessed
        print(f"Average Stage 2 score: {avg_score:.1f}/70")

    print()
    print(f"✓ Saved to: {CONFIG['output_json']}")
    print()


if __name__ == "__main__":
    main()

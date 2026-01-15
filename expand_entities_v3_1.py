#!/usr/bin/env python3
"""
Expand entities for v3.1 with:
1. Consolidated 3+3 scoring
2. Concrete details (problems solved, why new, why not exists)
3. Cluster organization
"""

import os
import json
import time
from pathlib import Path
from anthropic import Anthropic

CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-3-5-haiku-20241022",
    "input_json": "results/cluster_analysis_v3.json",
    "output_json": "results/v3.1_organized_expanded/entities.json",
    "max_tokens": 1500,
    "temperature": 0.3,
    "batch_delay": 1,  # seconds between requests
}

EXPANSION_PROMPT = """You are expanding a hyper-entity description with concrete, specific details.

ENTITY: {name}
CATEGORY: {category}
CURRENT DESCRIPTION: {description}

Add the following details in a concise, specific manner:

1. **PROBLEMS SOLVED** (2-3 sentences):
   - What specific challenges or gaps does this address?
   - What pain points does it solve?

2. **WHY NEW/DIFFERENT** (2-3 sentences):
   - What makes this distinct from existing approaches?
   - What novel capabilities or architecture does it introduce?

3. **WHY NOT EXISTS YET** (2-3 sentences):
   - What are the key barriers preventing deployment today?
   - What needs to change or be built first?

OUTPUT FORMAT (provide only these 3 sections, be specific and concrete):

**Problems Solved:**
[2-3 specific sentences]

**Why New/Different:**
[2-3 specific sentences]

**Why Not Exists Yet:**
[2-3 specific sentences]
"""


def consolidate_stage1_scores(entity):
    """Consolidate 9 Stage 1 axes into 3 scores."""
    scoring = entity.get('scoring', {})

    # Reality Gap (0-9): How far from existing
    reality_gap = sum([
        scoring.get('Non-existence', 0),
        scoring.get('Plausibility', 0),
        scoring.get('Design specificity', 0),
    ])

    # Transformative Potential (0-6): How much it changes things
    transformative_potential = sum([
        scoring.get('New action space', 0),
        scoring.get('Roadmap clarity', 0),
    ])

    # Current Momentum (0-12): Pre-real effects now
    current_momentum = sum([
        scoring.get('Coordination gravity', 0),
        scoring.get('Resource pull', 0),
        scoring.get('Narrative centrality', 0),
        scoring.get('Pre-real effects', 0),
    ])

    return {
        "reality_gap": reality_gap,
        "transformative_potential": transformative_potential,
        "current_momentum": current_momentum,
        "total": reality_gap + transformative_potential + current_momentum
    }


def consolidate_stage2_scores(entity):
    """Consolidate 14 Stage 2 dimensions into 3 scores."""
    stage2 = entity.get('stage2_scores', {})

    # Transformative Power (0-25): Capability & scale
    transformative_power = sum([
        stage2.get('Capability Discontinuity', 0),
        stage2.get('Cross-Domain Reach', 0),
        stage2.get('Scalability', 0),
        stage2.get('Autonomy', 0),
        stage2.get('Composability', 0),
    ])

    # Systemic Risk (0-25): Dangers & governance gaps
    systemic_risk = sum([
        stage2.get('Irreversibility', 0),
        stage2.get('Power Concentration', 0),
        stage2.get('Externality Magnitude', 0),
        stage2.get('Misuse Asymmetry', 0),
        stage2.get('Governance Lag', 0),
    ])

    # Lock-in Effects (0-20): Path dependency & agency
    lockin_effects = sum([
        stage2.get('Feedback Intensity', 0),
        stage2.get('Narrative Lock-In', 0),
        stage2.get('Path Dependency', 0),
        stage2.get('Human Agency Impact', 0),
    ])

    return {
        "transformative_power": transformative_power,
        "systemic_risk": systemic_risk,
        "lockin_effects": lockin_effects,
        "total": transformative_power + systemic_risk + lockin_effects
    }


def expand_entity(client, entity):
    """Expand a single entity with concrete details using Claude."""
    prompt = EXPANSION_PROMPT.format(
        name=entity['name'],
        category=entity.get('category', 'Unknown'),
        description=entity.get('description', 'No description')
    )

    try:
        message = client.messages.create(
            model=CONFIG["model"],
            max_tokens=CONFIG["max_tokens"],
            temperature=CONFIG["temperature"],
            messages=[{"role": "user", "content": prompt}]
        )

        result = message.content[0].text

        # Parse the three sections
        expanded = {}

        if "**Problems Solved:**" in result:
            parts = result.split("**Problems Solved:**")[1]
            if "**Why New/Different:**" in parts:
                expanded['problems_solved'] = parts.split("**Why New/Different:**")[0].strip()
                parts = parts.split("**Why New/Different:**")[1]
                if "**Why Not Exists Yet:**" in parts:
                    expanded['why_new_different'] = parts.split("**Why Not Exists Yet:**")[0].strip()
                    expanded['why_not_exists'] = parts.split("**Why Not Exists Yet:**")[1].strip()

        return {
            "status": "success",
            "expanded": expanded,
            "tokens": {
                "input": message.usage.input_tokens,
                "output": message.usage.output_tokens
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "expanded": {}
        }


def main():
    """Main execution."""
    print("=" * 80)
    print("Expanding Entities for v3.1")
    print("=" * 80)
    print()

    # Load API key
    api_key = os.environ.get(CONFIG["api_key_env"])
    if not api_key:
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

    # Load clustered entities
    print("✓ Loading clustered entities...")
    with open(CONFIG['input_json']) as f:
        data = json.load(f)

    entities = data['entities_with_clusters']
    print(f"✓ Loaded {len(entities)} entities")
    print()

    # First pass: Consolidate scores (fast, no API calls)
    print("Consolidating scores to 3+3 system...")
    for entity in entities:
        entity['stage1_consolidated'] = consolidate_stage1_scores(entity)
        entity['stage2_consolidated'] = consolidate_stage2_scores(entity)

    print(f"✓ Consolidated scores for {len(entities)} entities")
    print()

    # Second pass: Expand with concrete details (API calls - slow)
    print("Expanding entities with concrete details...")
    print("This will take ~30-45 minutes for 345 entities...")
    print("-" * 80)

    total_input = 0
    total_output = 0
    expanded_count = 0

    for i, entity in enumerate(entities, 1):
        print(f"[{i}/{len(entities)}] {entity['name'][:60]}...", end=" ", flush=True)

        result = expand_entity(client, entity)

        if result["status"] == "success":
            entity.update(result["expanded"])
            total_input += result["tokens"]["input"]
            total_output += result["tokens"]["output"]
            expanded_count += 1
            print(f"✓")
        else:
            print(f"✗ {result.get('error', 'Unknown')[:50]}")

        # Rate limiting
        if i % 5 == 0:
            time.sleep(CONFIG["batch_delay"])

    print()
    print("-" * 80)
    print()

    # Prepare output
    output = {
        "metadata": {
            "version": "3.1",
            "description": "Organized & Expanded with consolidated scoring",
            "total_entities": len(entities),
            "expanded_entities": expanded_count,
            "n_clusters": data['metadata']['n_clusters'],
            "thematic_groups": len(data['related_groups']),
            "expansion_date": "2026-01-14",
            "scoring_system": {
                "stage1_consolidated": {
                    "reality_gap": "0-9 (Non-existence, Plausibility, Design specificity)",
                    "transformative_potential": "0-6 (New action space, Roadmap clarity)",
                    "current_momentum": "0-12 (Coordination gravity, Resource pull, Narrative centrality, Pre-real effects)",
                    "total": "0-27"
                },
                "stage2_consolidated": {
                    "transformative_power": "0-25 (Capability Discontinuity, Cross-Domain Reach, Scalability, Autonomy, Composability)",
                    "systemic_risk": "0-25 (Irreversibility, Power Concentration, Externality Magnitude, Misuse Asymmetry, Governance Lag)",
                    "lockin_effects": "0-20 (Feedback Intensity, Narrative Lock-In, Path Dependency, Human Agency Impact)",
                    "total": "0-70"
                }
            }
        },
        "clusters": data['clusters'],
        "related_groups": data['related_groups'],
        "entities": entities
    }

    # Save
    output_path = Path(CONFIG["output_json"])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

    print("=" * 80)
    print("EXPANSION COMPLETE")
    print("=" * 80)
    print(f"Entities processed: {len(entities)}")
    print(f"Successfully expanded: {expanded_count}")
    print(f"Total tokens: {total_input:,} in / {total_output:,} out")

    cost = (total_input / 1_000_000) * 0.8 + (total_output / 1_000_000) * 4
    print(f"Cost: ${cost:.2f}")
    print()
    print(f"✓ Saved to: {output_path}")
    print()


if __name__ == "__main__":
    main()

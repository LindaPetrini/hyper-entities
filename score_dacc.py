#!/usr/bin/env python3
"""
Score entities on d/acc dimensions (Stage 3: Values Alignment Assessment)
Based on Vitalik Buterin's d/acc framework: Democratic, Decentralized, Defensive, Differential
"""

import os
import json
import time
from pathlib import Path
from anthropic import Anthropic

CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-3-5-haiku-20241022",
    "input_json": "results/stage2_assessment/entities.json",
    "output_json": "results/stage2_assessment/entities.json",
    "max_tokens": 800,
    "temperature": 0.2,
    "batch_delay": 0.5,  # seconds between requests
}

DACC_SCORING_PROMPT = """You are scoring a hyper-entity on the d/acc framework (Democratic, Decentralized, Defensive, Differential).

ENTITY: {name}
CATEGORY: {category}
DESCRIPTION: {description}
PROBLEMS SOLVED: {problems_solved}
WHY NEW/DIFFERENT: {why_new_different}

Score this entity on 4 dimensions (0-5 each). Be specific and calibrated.

## Scoring Criteria

**DEMOCRATIC (0-5)**: Does this enable collective decision-making vs elite control?
- 0: Concentrates decisions in elites/experts; excludes participation
- 5: Deeply enables community choice; surfaces diverse perspectives; resists capture
- Consider: Can communities shape how it's used? Does it require expert gatekeepers?

**DECENTRALIZED (0-5)**: Does this distribute power vs concentrate it?
- 0: Creates new single points of control/failure; centralizes leverage
- 5: Distributes power across many actors; no single chokepoint; resistant to authoritarian capture
- Consider: Can it function without central authorities? Does it create dependencies?

**DEFENSIVE (0-5)**: Does this favor protection/resilience vs harm/offense?
- 0: Primarily useful for causing harm; offense-dominant capabilities
- 5: Primarily helps people protect themselves; makes attack harder than defense
- Consider: Does it help people/communities protect themselves from harm?

**DIFFERENTIAL (0-5)**: Should this technology be accelerated vs restrained?
- 0: High dual-use risk; advances capabilities that threaten coordination
- 5: Creates positive asymmetries; accelerating this improves defense/freedom relative to offense/control
- Consider: Does faster development of this improve the defense/freedom side of the ledger?

OUTPUT FORMAT (JSON only, no other text):
{{"democratic": X, "decentralized": X, "defensive": X, "differential": X, "reasoning": "1-2 sentence justification"}}
"""


def extract_json(text):
    """Extract JSON object from text, handling various formats."""
    text = text.strip()

    # Remove markdown code blocks
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            if part.startswith("{"):
                text = part
                break

    # Find JSON object boundaries
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found")

    # Find matching closing brace
    depth = 0
    end = start
    for i, char in enumerate(text[start:], start):
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    json_str = text[start:end]
    return json.loads(json_str)


def score_entity_dacc(client, entity):
    """Score a single entity on d/acc dimensions."""
    prompt = DACC_SCORING_PROMPT.format(
        name=entity['name'],
        category=entity.get('category', 'Unknown'),
        description=entity.get('description', 'No description'),
        problems_solved=entity.get('problems_solved', 'Unknown'),
        why_new_different=entity.get('why_new_different', 'Unknown')
    )

    try:
        message = client.messages.create(
            model=CONFIG["model"],
            max_tokens=CONFIG["max_tokens"],
            temperature=CONFIG["temperature"],
            messages=[{"role": "user", "content": prompt}]
        )

        result = message.content[0].text.strip()
        scores = extract_json(result)

        return {
            "status": "success",
            "scores": {
                "democratic": scores.get("democratic", 0),
                "decentralized": scores.get("decentralized", 0),
                "defensive": scores.get("defensive", 0),
                "differential": scores.get("differential", 0),
            },
            "reasoning": scores.get("reasoning", ""),
            "tokens": {
                "input": message.usage.input_tokens,
                "output": message.usage.output_tokens
            }
        }

    except json.JSONDecodeError as e:
        return {
            "status": "error",
            "error": f"JSON parse error: {str(e)[:50]}",
            "scores": {"democratic": 0, "decentralized": 0, "defensive": 0, "differential": 0},
            "reasoning": ""
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)[:50],
            "scores": {"democratic": 0, "decentralized": 0, "defensive": 0, "differential": 0},
            "reasoning": ""
        }


def main():
    """Main execution."""
    print("=" * 80)
    print("d/acc Scoring (Stage 3: Values Alignment Assessment)")
    print("=" * 80)
    print()
    print("Dimensions: Democratic, Decentralized, Defensive, Differential")
    print("Scale: 0-5 per dimension, max total: 20")
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

    print("API key found")

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Load entities
    print("Loading entities...")
    with open(CONFIG['input_json']) as f:
        data = json.load(f)

    entities = data['entities']
    print(f"Loaded {len(entities)} entities")
    print()

    # Score entities
    print("Scoring entities on d/acc dimensions...")
    print("-" * 80)

    total_input = 0
    total_output = 0
    success_count = 0
    error_count = 0

    for i, entity in enumerate(entities, 1):
        print(f"[{i}/{len(entities)}] {entity['name'][:55]}...", end=" ", flush=True)

        result = score_entity_dacc(client, entity)

        if result["status"] == "success":
            entity['stage3_dacc'] = result["scores"]
            entity['stage3_dacc']['total'] = sum(result["scores"].values())
            entity['stage3_dacc']['reasoning'] = result["reasoning"]
            total_input += result["tokens"]["input"]
            total_output += result["tokens"]["output"]
            success_count += 1
            total = entity['stage3_dacc']['total']
            print(f"d/acc={total}/20")
        else:
            entity['stage3_dacc'] = result["scores"]
            entity['stage3_dacc']['total'] = 0
            entity['stage3_dacc']['reasoning'] = f"Error: {result.get('error', 'Unknown')}"
            error_count += 1
            print(f"ERROR: {result.get('error', 'Unknown')[:30]}")

        # Rate limiting
        time.sleep(CONFIG["batch_delay"])

    print()
    print("-" * 80)
    print()

    # Update metadata
    data['metadata']['stage3_dacc'] = {
        "democratic": "0-5 (enables collective decision-making vs elite control)",
        "decentralized": "0-5 (distributes power vs concentrates it)",
        "defensive": "0-5 (favors protection/resilience vs harm/offense)",
        "differential": "0-5 (should be accelerated vs restrained)",
        "total": "0-20"
    }
    data['metadata']['dacc_scoring_date'] = "2026-01-22"

    # Save
    output_path = Path(CONFIG["output_json"])
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print("=" * 80)
    print("d/acc SCORING COMPLETE")
    print("=" * 80)
    print(f"Entities processed: {len(entities)}")
    print(f"Successfully scored: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Total tokens: {total_input:,} in / {total_output:,} out")

    cost = (total_input / 1_000_000) * 0.8 + (total_output / 1_000_000) * 4
    print(f"Estimated cost: ${cost:.2f}")
    print()
    print(f"Saved to: {output_path}")
    print()

    # Show sample scores
    print("Sample d/acc scores:")
    print("-" * 40)
    for entity in entities[:5]:
        dacc = entity.get('stage3_dacc', {})
        print(f"  {entity['name'][:40]}: {dacc.get('total', 0)}/20")
        print(f"    D:{dacc.get('democratic',0)} De:{dacc.get('decentralized',0)} Df:{dacc.get('defensive',0)} Di:{dacc.get('differential',0)}")
    print()


if __name__ == "__main__":
    main()

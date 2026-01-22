#!/usr/bin/env python3
"""
Extract concrete technologies from hyper-entities.
Filters out vague/abstract concepts, keeps actual buildable technologies,
and attempts to distill concrete mechanisms from abstract descriptions.
"""

import os
import json
import time
from pathlib import Path
from anthropic import Anthropic

CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-3-5-haiku-20241022",  # Much cheaper than Sonnet
    "input_json": "results/stage2_assessment/entities.json",
    "output_json": "results/stage3_concrete/entities.json",
    "max_tokens": 800,  # Reduced - we don't need long outputs
    "temperature": 0.2,
    "batch_delay": 0.3,
}

EXTRACTION_PROMPT = """You are evaluating a "hyper-entity" (a future technology concept) for CONCRETENESS.

ENTITY: {name}
DESCRIPTION: {description}
PROBLEMS SOLVED: {problems_solved}
WHY NEW/DIFFERENT: {why_new_different}

Your task: Determine if this describes an ACTUAL TECHNOLOGY that could be built, or just abstract vibes.

CONCRETE examples (keep these):
- "Prediction markets for policy decisions" - specific mechanism
- "Zero-knowledge proofs for identity verification" - actual cryptographic technique
- "Quadratic voting for resource allocation" - specific voting mechanism
- "Federated learning across hospital networks" - real ML architecture
- "CRISPR-based gene drives for malaria eradication" - specific biotech

VAGUE examples (reject or transform):
- "A system where humans and AI flourish together" - no mechanism specified
- "Coordination infrastructure for collective intelligence" - what does this actually DO?
- "Symbiotic socio-technological system for abundance" - meaningless buzzwords
- "Platform for value alignment across stakeholders" - how, specifically?

EVALUATION CRITERIA:
1. Does it specify a concrete MECHANISM (how it works)?
2. Could an engineer start building this with the description?
3. Is there a specific technology, protocol, or technique named?
4. Or is it just "good thing happens through coordination"?

OUTPUT FORMAT (JSON only):
{{
  "concreteness_score": 0-5,  // 0=pure vibes, 5=could write a spec
  "verdict": "keep" | "transform" | "reject",
  "core_technologies": ["list", "of", "specific", "technologies"],  // empty if none
  "concrete_version": "If vague, what SPECIFIC technology could this become? Be specific about mechanisms. If already concrete, just improve clarity. If unfixable vibes, leave empty.",
  "reasoning": "1-2 sentences explaining your verdict"
}}

Be HARSH. Most of these are too vague. Only "keep" if there's a real technology. "Transform" if you can salvage something concrete. "Reject" if it's pure philosophy/vibes."""


def extract_json(text):
    """Extract JSON object from text, handling control characters."""
    import re

    text = text.strip()
    if "```" in text:
        parts = text.split("```")
        for part in parts:
            part = part.strip()
            if part.startswith("json"):
                part = part[4:].strip()
            if part.startswith("{"):
                text = part
                break

    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found")

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

    # Fix control characters inside JSON strings
    # Replace literal newlines/tabs inside strings with escaped versions
    def fix_string_content(match):
        content = match.group(1)
        content = content.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
        return f'"{content}"'

    # Match JSON string values and fix control chars
    json_str = re.sub(r'"((?:[^"\\]|\\.)*?)"', fix_string_content, json_str, flags=re.DOTALL)

    return json.loads(json_str)


def process_entity(client, entity):
    """Process a single entity for concreteness."""
    prompt = EXTRACTION_PROMPT.format(
        name=entity['name'],
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

        result = extract_json(message.content[0].text)
        return {
            "status": "success",
            "concreteness_score": result.get("concreteness_score", 0),
            "verdict": result.get("verdict", "reject"),
            "core_technologies": result.get("core_technologies", []),
            "concrete_version": result.get("concrete_version", ""),
            "reasoning": result.get("reasoning", ""),
            "tokens": {
                "input": message.usage.input_tokens,
                "output": message.usage.output_tokens
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)[:100],
            "concreteness_score": 0,
            "verdict": "reject",
            "core_technologies": [],
            "concrete_version": "",
            "reasoning": f"Error: {str(e)[:50]}"
        }


def save_progress(output_path, data, results):
    """Save current progress to disk."""
    output_data = {
        "metadata": {
            **data.get('metadata', {}),
            "concreteness_extraction": {
                "date": "2026-01-22",
                "model": CONFIG["model"],
                "in_progress": True
            }
        },
        "entities": results
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)


def main():
    print("=" * 80)
    print("Concrete Technology Extraction")
    print("=" * 80)
    print()
    print("Filtering hyper-entities for actual buildable technologies...")
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
    client = Anthropic(api_key=api_key)

    output_path = Path(CONFIG["output_json"])

    # Check for existing progress
    processed_names = set()
    results = []
    if output_path.exists():
        print("Found existing progress file, resuming...")
        with open(output_path) as f:
            existing = json.load(f)
        results = existing.get('entities', [])
        processed_names = {e['name'] for e in results if 'concreteness' in e}
        print(f"  Already processed: {len(processed_names)} entities")
        print()

    # Load entities
    print("Loading entities...")
    with open(CONFIG['input_json']) as f:
        data = json.load(f)

    entities = data['entities']
    print(f"Loaded {len(entities)} entities")

    # Filter to only unprocessed
    to_process = [e for e in entities if e['name'] not in processed_names]
    print(f"Remaining to process: {len(to_process)} entities")
    print()

    # Process entities
    print("Processing entities for concreteness...")
    print("-" * 80)

    total_input = 0
    total_output = 0
    keep_count = len([e for e in results if e.get('concreteness', {}).get('verdict') == 'keep'])
    transform_count = len([e for e in results if e.get('concreteness', {}).get('verdict') == 'transform'])
    reject_count = len([e for e in results if e.get('concreteness', {}).get('verdict') == 'reject'])
    error_count = len([e for e in results if e.get('concreteness', {}).get('verdict') == 'error'])

    for i, entity in enumerate(to_process, 1):
        total_processed = len(processed_names) + i
        print(f"[{total_processed}/{len(entities)}] {entity['name'][:50]}...", end=" ", flush=True)

        result = process_entity(client, entity)

        if result["status"] == "success":
            total_input += result["tokens"]["input"]
            total_output += result["tokens"]["output"]

            # Store result in entity
            entity['concreteness'] = {
                'score': result['concreteness_score'],
                'verdict': result['verdict'],
                'core_technologies': result['core_technologies'],
                'concrete_version': result['concrete_version'],
                'reasoning': result['reasoning']
            }

            verdict = result['verdict']
            score = result['concreteness_score']

            if verdict == 'keep':
                keep_count += 1
                print(f"KEEP (score={score})")
            elif verdict == 'transform':
                transform_count += 1
                print(f"TRANSFORM (score={score})")
            else:
                reject_count += 1
                print(f"REJECT (score={score})")

            results.append(entity)
        else:
            error_count += 1
            entity['concreteness'] = {
                'score': 0,
                'verdict': 'error',
                'reasoning': result.get('error', 'Unknown error')
            }
            results.append(entity)
            print(f"ERROR: {result.get('error', 'Unknown')[:30]}")

        # Save progress after each entity
        save_progress(output_path, data, results)

        time.sleep(CONFIG["batch_delay"])

    print()
    print("-" * 80)
    print()

    # Create final output (mark as complete)
    output_data = {
        "metadata": {
            **data.get('metadata', {}),
            "concreteness_extraction": {
                "date": "2026-01-22",
                "model": CONFIG["model"],
                "total_entities": len(entities),
                "keep": keep_count,
                "transform": transform_count,
                "reject": reject_count,
                "errors": error_count,
                "complete": True
            }
        },
        "entities": results
    }

    # Save full results
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)

    # Create filtered version (keep + transform only)
    filtered_entities = [e for e in results if e.get('concreteness', {}).get('verdict') in ['keep', 'transform']]
    filtered_data = {
        "metadata": output_data["metadata"],
        "entities": filtered_entities
    }
    filtered_path = output_path.parent / "entities_filtered.json"
    with open(filtered_path, 'w') as f:
        json.dump(filtered_data, f, indent=2)

    print("=" * 80)
    print("EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"Total entities: {len(entities)}")
    print(f"  KEEP:      {keep_count} ({keep_count/len(entities)*100:.1f}%)")
    print(f"  TRANSFORM: {transform_count} ({transform_count/len(entities)*100:.1f}%)")
    print(f"  REJECT:    {reject_count} ({reject_count/len(entities)*100:.1f}%)")
    print(f"  ERRORS:    {error_count}")
    print()
    print(f"Total tokens: {total_input:,} in / {total_output:,} out")
    cost = (total_input / 1_000_000) * 0.8 + (total_output / 1_000_000) * 4  # Haiku pricing
    print(f"Estimated cost: ${cost:.2f}")
    print()
    print(f"Full results: {output_path}")
    print(f"Filtered (keep+transform): {filtered_path} ({len(filtered_entities)} entities)")
    print()

    # Show examples
    print("Sample KEEP entities:")
    for e in [x for x in results if x.get('concreteness', {}).get('verdict') == 'keep'][:3]:
        print(f"  - {e['name']}: {e['concreteness'].get('core_technologies', [])}")

    print()
    print("Sample TRANSFORM entities:")
    for e in [x for x in results if x.get('concreteness', {}).get('verdict') == 'transform'][:3]:
        print(f"  - {e['name']}")
        print(f"    → {e['concreteness'].get('concrete_version', '')[:100]}...")

    print()
    print("Sample REJECT entities:")
    for e in [x for x in results if x.get('concreteness', {}).get('verdict') == 'reject'][:3]:
        print(f"  - {e['name']}: {e['concreteness'].get('reasoning', '')[:80]}")


if __name__ == "__main__":
    main()

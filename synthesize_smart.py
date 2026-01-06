#!/usr/bin/env python3
"""
Smart synthesis: Parse extractions first, then synthesize only key data.
Two-stage approach:
1. Extract structured data from each source
2. Synthesize the structured data
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from anthropic import Anthropic

# Configuration
CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 16384,
    "temperature": 0.3,
    "input_file": "results/hyperentities_extracted.md",
    "output_dir": "results/synthesis",
}


def load_extracted_entities():
    """Load all extracted hyper-entities from the results file."""
    input_path = Path(CONFIG["input_file"])
    if not input_path.exists():
        raise FileNotFoundError(f"Extraction results not found: {input_path}")

    content = input_path.read_text(encoding="utf-8")

    # Split by source files
    sources = re.split(r'^## Source: ', content, flags=re.MULTILINE)

    entities_by_source = {}
    for source_section in sources[1:]:  # Skip the header
        lines = source_section.split('\n', 1)
        if len(lines) < 2:
            continue

        source_file = lines[0].strip()
        extraction = lines[1] if len(lines) > 1 else ""

        # Only add if extraction is not empty and not an error
        if extraction and "ERROR" not in extraction[:100]:
            entities_by_source[source_file] = extraction

    return entities_by_source


def parse_entities_from_text(text):
    """Extract entity names and categories from extraction text."""
    entities = []

    # Pattern to match entity blocks
    # Looking for lines like: **Entity Name:** Something
    entity_pattern = r'\*\*Entity Name:\*\*\s*(.+?)(?:\n|$)'
    category_pattern = r'\*\*Category:\*\*\s*(.+?)(?:\n|$)'

    # Find all entity names
    entity_matches = re.finditer(entity_pattern, text, re.IGNORECASE)

    for match in entity_matches:
        entity_name = match.group(1).strip()

        # Try to find category after this entity
        category = "Unknown"
        text_after = text[match.end():match.end()+200]
        cat_match = re.search(category_pattern, text_after, re.IGNORECASE)
        if cat_match:
            category = cat_match.group(1).strip()

        if entity_name:
            entities.append({
                "name": entity_name,
                "category": category
            })

    return entities


def generate_statistics(entities_by_source):
    """Generate statistics about all entities."""
    all_entities = []
    category_counts = {}
    source_directory_counts = {}

    for source_file, extraction in entities_by_source.items():
        entities = parse_entities_from_text(extraction)

        # Count by directory
        if "/" in source_file:
            directory = source_file.split("/")[1] if source_file.startswith("sources/") else "other"
        else:
            directory = "root"

        source_directory_counts[directory] = source_directory_counts.get(directory, 0) + 1

        # Count entities
        for entity in entities:
            all_entities.append({
                "name": entity["name"],
                "category": entity["category"],
                "source": source_file,
            })

            category = entity["category"]
            category_counts[category] = category_counts.get(category, 0) + 1

    return {
        "total_sources": len(entities_by_source),
        "total_entities": len(all_entities),
        "entities_per_source": len(all_entities) / len(entities_by_source) if entities_by_source else 0,
        "category_counts": category_counts,
        "source_directory_counts": source_directory_counts,
        "all_entities": all_entities,
    }


def create_condensed_dataset(all_entities, max_entities=500):
    """Create a condensed representation of all entities for synthesis."""
    # Group by name (case-insensitive) to find duplicates
    entity_groups = {}

    for entity in all_entities:
        name_lower = entity["name"].lower()
        if name_lower not in entity_groups:
            entity_groups[name_lower] = {
                "name": entity["name"],
                "category": entity["category"],
                "sources": [entity["source"]],
                "count": 1,
            }
        else:
            entity_groups[name_lower]["sources"].append(entity["source"])
            entity_groups[name_lower]["count"] += 1

    # Convert to list and sort by frequency
    entities_list = list(entity_groups.values())
    entities_list.sort(key=lambda x: x["count"], reverse=True)

    # Take top N
    if len(entities_list) > max_entities:
        entities_list = entities_list[:max_entities]

    return entities_list


def synthesize_entities(client, condensed_entities, stats):
    """Use Claude to synthesize the condensed entity list."""
    print("\nSynthesizing hyper-entities...")

    # Create compact representation
    entity_text = ""
    for entity in condensed_entities:
        entity_text += f"- {entity['name']} ({entity['category']}) [mentioned {entity['count']}x"
        if entity['count'] > 1:
            entity_text += f" across: {', '.join(entity['sources'][:3])}"
            if len(entity['sources']) > 3:
                entity_text += f" + {len(entity['sources'])-3} more"
        entity_text += "]\n"

    print(f"  Condensed to {len(condensed_entities)} unique entities")
    print(f"  Input size: {len(entity_text):,} characters")

    prompt = f"""You are analyzing {stats['total_entities']} hyper-entities extracted from {stats['total_sources']} documents about future technologies, institutions, and visions.

Below is a condensed list of the most frequently mentioned entities. Entities mentioned multiple times across different sources show stronger consensus.

TASK: Create a comprehensive synthesis report with the following sections:

## 1. OVERVIEW STATISTICS
- Total unique entities identified
- Distribution by category
- Most frequently mentioned entities (showing consensus)

## 2. TOP 30 HYPER-ENTITIES
Rank the top 30 most significant hyper-entities based on:
- Frequency of mentions (shows consensus)
- Category importance
- Innovation potential

For each, provide:
- **Name** and **Category**
- **Why Promising** (1-2 sentences)
- **Mention Count** (how many sources)

## 3. THEMATIC CLUSTERS
Group related entities into major themes:
- AI & Computation
- Biotechnology & Longevity
- Institutional Innovation
- Environmental & Sustainability
- Social & Cultural Transformation
- Space & Frontier Technologies
- Other emerging themes

For each theme, list 5-10 key entities.

## 4. KEY INSIGHTS
- Which entities show strongest consensus (mentioned most)?
- What unique/novel entities stand out?
- What patterns emerge across categories?
- Any gaps or missing perspectives?

## 5. RECOMMENDED FOCUS AREAS
Based on frequency and promise, which 10 hyper-entities should Foresight Institute prioritize?

---

CONDENSED ENTITY LIST:

{entity_text}

---

Please provide a well-structured markdown report."""

    print("\nCalling Claude API for synthesis...")
    message = client.messages.create(
        model=CONFIG["model"],
        max_tokens=CONFIG["max_tokens"],
        temperature=CONFIG["temperature"],
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    synthesis = message.content[0].text
    tokens_used = {
        "input": message.usage.input_tokens,
        "output": message.usage.output_tokens,
    }

    print(f"✓ Synthesis complete!")
    print(f"  Tokens: {tokens_used['input']:,} in / {tokens_used['output']:,} out")

    cost = (tokens_used['input'] / 1_000_000) * 3 + (tokens_used['output'] / 1_000_000) * 15
    print(f"  Cost: ${cost:.2f}")

    return synthesis, tokens_used


def main():
    """Main execution."""
    print("=" * 80)
    print("SMART HYPER-ENTITIES SYNTHESIS")
    print("=" * 80)
    print()

    # Check for API key
    api_key = os.environ.get(CONFIG["api_key_env"])
    if not api_key:
        print(f"ERROR: {CONFIG['api_key_env']} environment variable not set.")
        return

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Load extraction results
    print("Loading extracted hyper-entities...")
    entities_by_source = load_extracted_entities()
    print(f"✓ Loaded {len(entities_by_source)} source files")

    # Parse and analyze
    print("\nParsing entities from extractions...")
    stats = generate_statistics(entities_by_source)

    print(f"\nExtracted Statistics:")
    print(f"  Total sources: {stats['total_sources']}")
    print(f"  Total entities found: {stats['total_entities']}")
    print(f"  Average per source: {stats['entities_per_source']:.1f}")
    print(f"\n  Entities by category:")
    for category, count in sorted(stats["category_counts"].items(), key=lambda x: x[1], reverse=True):
        print(f"    - {category}: {count}")

    print(f"\n  Sources by directory:")
    for directory, count in sorted(stats["source_directory_counts"].items()):
        print(f"    - {directory}: {count}")

    # Create condensed dataset
    print("\nCreating condensed dataset...")
    condensed = create_condensed_dataset(stats["all_entities"], max_entities=500)
    print(f"✓ Condensed to {len(condensed)} unique entities (top by frequency)")

    # Show top 10
    print("\nTop 10 most frequently mentioned:")
    for i, entity in enumerate(condensed[:10], 1):
        print(f"  {i}. {entity['name']} ({entity['category']}) - {entity['count']}x")

    # Synthesize
    synthesis, tokens_used = synthesize_entities(client, condensed, stats)

    # Save results
    output_dir = Path(CONFIG["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save synthesis report
    synthesis_file = output_dir / "synthesis_report.md"
    with synthesis_file.open("w") as f:
        f.write("# Hyper-Entities Synthesis Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Sources analyzed:** {stats['total_sources']}\n")
        f.write(f"**Total entities extracted:** {stats['total_entities']}\n")
        f.write(f"**Unique entities:** {len(condensed)}\n\n")
        f.write(f"**Analysis tokens:** {tokens_used['input']:,} in / {tokens_used['output']:,} out\n\n")
        f.write("---\n\n")
        f.write(synthesis)

    print(f"\n✓ Synthesis saved to: {synthesis_file}")

    # Save structured data
    data_file = output_dir / "entities_data.json"
    with data_file.open("w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "statistics": {
                "total_sources": stats["total_sources"],
                "total_entities": stats["total_entities"],
                "unique_entities": len(condensed),
                "category_counts": stats["category_counts"],
                "source_directory_counts": stats["source_directory_counts"],
            },
            "condensed_entities": condensed[:100],  # Save top 100
        }, f, indent=2)

    print(f"✓ Entity data saved to: {data_file}")

    print("\n" + "=" * 80)
    print("SYNTHESIS COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Convert v3 extraction results (MD with scoring) to structured JSON.
"""

import json
import re
from pathlib import Path
from datetime import datetime


def parse_extraction_md(md_file):
    """Parse the v3 extraction markdown into structured JSON."""
    content = Path(md_file).read_text()

    # Split by source files
    sources = re.split(r'\n## Source: ', content)

    entities = []
    entity_id = 1

    for source_block in sources[1:]:  # Skip header
        lines = source_block.split('\n')
        source_file = lines[0].strip()

        # Extract all entities from this source
        entity_blocks = re.split(r'\n---\n\n\*\*ENTITY NAME:\*\*', source_block)

        for entity_block in entity_blocks[1:]:  # Skip first split (before first entity)
            entity = parse_entity(entity_block, source_file, entity_id)
            if entity:
                entities.append(entity)
                entity_id += 1

    return entities


def parse_entity(text, source_file, entity_id):
    """Parse a single entity block."""
    try:
        entity = {
            "id": entity_id,
            "source_file": source_file,
        }

        # Extract name
        name_match = re.search(r'^(.+?)(?:\n|$)', text)
        if name_match:
            entity["name"] = name_match.group(1).strip()

        # Extract definition check
        def_check = {}
        if match := re.search(r'\*\*DEFINITION CHECK:\*\*(.+?)\*\*QUALIFICATION SCORING:\*\*', text, re.DOTALL):
            def_text = match.group(1)

            if non_ex := re.search(r'Non-existent\?\s*(.+?)(?:\n|$)', def_text):
                def_check["non_existent"] = non_ex.group(1).strip()
            if new_act := re.search(r'New action space\?\s*(.+?)(?:\n|$)', def_text):
                def_check["new_action_space"] = new_act.group(1).strip()
            if pre_real := re.search(r'Pre-real effects\?\s*(.+?)(?:\n|$)', def_text):
                def_check["pre_real_effects"] = pre_real.group(1).strip()

        entity["definition_check"] = def_check

        # Extract scoring table
        scoring = {}
        score_pattern = r'\|\s*([^|]+?)\s*\|\s*(\d)\s*\|'
        for match in re.finditer(score_pattern, text):
            axis = match.group(1).strip()
            score = int(match.group(2))
            scoring[axis] = score

        entity["scoring"] = scoring

        # Extract total score
        if match := re.search(r'\*\*TOTAL SCORE:\*\*\s*(\d+)/27', text):
            entity["total_score"] = int(match.group(1))

        # Extract qualification status
        if match := re.search(r'\*\*QUALIFICATION:\*\*\s*(.+?)(?:\n|$)', text):
            status = match.group(1).strip()
            entity["qualification"] = status
            entity["qualified"] = "✓ QUALIFIED" in status

        # Extract description
        if match := re.search(r'\*\*DESCRIPTION:\*\*\s*(.+?)(?:\n\n|\*\*EVIDENCE)', text, re.DOTALL):
            entity["description"] = match.group(1).strip()

        # Extract evidence
        if match := re.search(r'\*\*EVIDENCE FROM TEXT:\*\*\s*(.+?)(?:\n\n|\*\*CATEGORY)', text, re.DOTALL):
            entity["evidence"] = match.group(1).strip()

        # Extract category
        if match := re.search(r'\*\*CATEGORY:\*\*\s*(.+?)(?:\n|$)', text):
            entity["category"] = match.group(1).strip()

        return entity

    except Exception as e:
        print(f"Error parsing entity: {e}")
        return None


def main():
    """Main execution."""
    print("=" * 80)
    print("Converting v3 Extraction Results to JSON")
    print("=" * 80)
    print()

    md_file = "results/hyperentities_extracted_v3.md"
    json_file = "results/hyperentities_v3.json"

    print(f"Reading: {md_file}")
    entities = parse_extraction_md(md_file)

    print(f"✓ Parsed {len(entities)} entities")

    # Create output structure
    output = {
        "metadata": {
            "extraction_date": datetime.now().isoformat(),
            "methodology": "See METHODOLOGY.md for scoring framework",
            "qualification_threshold": "≥18/27 on Stage 1 scoring",
            "total_entities": len(entities),
            "total_sources": len(set(e["source_file"] for e in entities)),
        },
        "entities": entities
    }

    # Calculate statistics
    qualified = [e for e in entities if e.get("qualified", False)]
    scores = [e.get("total_score", 0) for e in entities if "total_score" in e]

    if scores:
        output["metadata"]["statistics"] = {
            "qualified_entities": len(qualified),
            "average_score": round(sum(scores) / len(scores), 2),
            "max_score": max(scores),
            "min_score": min(scores),
        }

    # Category breakdown
    categories = {}
    for entity in entities:
        cat = entity.get("category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1

    output["metadata"]["category_breakdown"] = categories

    # Save JSON
    print(f"Writing: {json_file}")
    with open(json_file, 'w') as f:
        json.dump(output, f, indent=2)

    print()
    print("=" * 80)
    print("CONVERSION COMPLETE!")
    print("=" * 80)
    print(f"Total entities: {len(entities)}")
    print(f"Qualified (≥18): {len(qualified)}")
    if scores:
        print(f"Average score: {output['metadata']['statistics']['average_score']}/27")
        print(f"Score range: {min(scores)}-{max(scores)}")

    print()
    print("Category breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1])[:10]:
        print(f"  {cat}: {count}")

    print()
    print(f"✓ JSON saved to: {json_file}")
    print()


if __name__ == "__main__":
    main()

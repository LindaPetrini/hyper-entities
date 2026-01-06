#!/usr/bin/env python3
"""
Generate synthesis report based on visualization clustering.
Uses the same clustering (15 clusters) as the interactive visualization.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from anthropic import Anthropic

# Import clustering functions from visualization
import sys
sys.path.insert(0, str(Path(__file__).parent))
from create_visualization_v2 import load_and_parse_entities, create_visualization_data

# Configuration
CONFIG = {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 16384,
    "temperature": 0.3,
    "output_dir": "results/synthesis",
}


def create_synthesis_prompt(entities_by_cluster, cluster_centers):
    """Create synthesis prompt organized by clusters."""

    prompt = """You are analyzing a comprehensive extraction of "hyper-entities" from Foresight Institute's content.

HYPER-ENTITIES are ideas, technologies, or institutional architectures that mobilize real-world attention and resources. They are concepts that have the potential to shape the future.

Below is a dataset of 1,077 hyper-entities organized into 15 thematic clusters based on semantic similarity. Each cluster has been labeled with its most distinctive keywords.

YOUR TASK: Create a comprehensive synthesis report with the following sections:

1. **Executive Summary** (2-3 paragraphs)
   - Overview of the 15 clusters and their themes
   - Key patterns and insights across all entities
   - Strategic implications for Foresight Institute

2. **Cluster Analysis** (for each of the 15 clusters)
   For each cluster, provide:
   - Cluster theme/focus (3-5 words)
   - Number of entities and key characteristics
   - 3-5 most promising entities from this cluster with brief explanations
   - How this cluster relates to Foresight Institute's mission

3. **Cross-Cutting Themes** (2-3 paragraphs)
   - Patterns that span multiple clusters
   - Emerging opportunities and risks
   - Gaps in current coverage

4. **Top 20 Priority Entities** (across all clusters)
   Ranked list with:
   - Entity name and cluster
   - Why it's strategically important for Foresight
   - Suggested next steps

5. **Strategic Recommendations** (5-7 recommendations)
   - Concrete actions for Foresight Institute
   - Focus on undervalued opportunities
   - Consider resource allocation and timeline

---

DATA BY CLUSTER:

"""

    # Add cluster data
    for cluster_id in sorted(entities_by_cluster.keys()):
        entities = entities_by_cluster[cluster_id]
        center = cluster_centers.get(cluster_id, {})
        keywords = center.get('keywords', [])

        prompt += f"\n## Cluster {cluster_id}: {', '.join(keywords[:3]).title()}\n"
        prompt += f"Keywords: {', '.join(keywords)}\n"
        prompt += f"Entity count: {len(entities)}\n\n"

        # Add sample of entities (up to 30 per cluster for token limits)
        for i, entity in enumerate(entities[:30]):
            prompt += f"**{entity['name']}** ({entity['category']})\n"
            # Truncate description to keep prompt manageable
            desc = entity['description'][:200] + '...' if len(entity['description']) > 200 else entity['description']
            prompt += f"{desc}\n\n"

        if len(entities) > 30:
            prompt += f"... and {len(entities) - 30} more entities in this cluster\n\n"

    prompt += "\n---\n\nGenerate the comprehensive synthesis report now."

    return prompt


def generate_synthesis(entities_by_cluster, cluster_centers):
    """Generate synthesis using Claude API."""
    api_key = os.environ.get(CONFIG["api_key_env"])
    if not api_key:
        raise ValueError(f"API key not found in environment variable: {CONFIG['api_key_env']}")

    client = Anthropic(api_key=api_key)

    print("\nGenerating synthesis with Claude API...")
    prompt = create_synthesis_prompt(entities_by_cluster, cluster_centers)

    print(f"  Prompt length: {len(prompt)} chars")

    message = client.messages.create(
        model=CONFIG["model"],
        max_tokens=CONFIG["max_tokens"],
        temperature=CONFIG["temperature"],
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    synthesis = message.content[0].text

    # Calculate cost
    input_tokens = message.usage.input_tokens
    output_tokens = message.usage.output_tokens
    cost = (input_tokens / 1_000_000 * 3) + (output_tokens / 1_000_000 * 15)

    print(f"  Tokens: {input_tokens} in / {output_tokens} out")
    print(f"  Cost: ${cost:.2f}")

    return synthesis, cost


def save_synthesis(synthesis, entities_by_cluster, cluster_centers, cost):
    """Save synthesis report to file."""
    output_dir = Path(CONFIG["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate report
    report = f"""# Hyper-Entities Synthesis Report
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Based on visualization clustering (15 clusters, 1,077 entities)*

---

{synthesis}

---

## Appendix: Cluster Statistics

"""

    # Add cluster stats
    for cluster_id in sorted(entities_by_cluster.keys()):
        entities = entities_by_cluster[cluster_id]
        center = cluster_centers.get(cluster_id, {})
        keywords = center.get('keywords', [])

        report += f"\n### Cluster {cluster_id}: {', '.join(keywords[:3]).title()}\n"
        report += f"- **Keywords**: {', '.join(keywords)}\n"
        report += f"- **Entity count**: {len(entities)}\n"

        # Category breakdown
        from collections import Counter
        categories = [e['category'].split('/')[0] for e in entities]
        top_cats = Counter(categories).most_common(3)
        report += f"- **Top categories**: {', '.join(f'{cat} ({count})' for cat, count in top_cats)}\n"

    report += f"\n---\n\n**Generation cost**: ${cost:.2f}\n"

    # Save
    report_path = output_dir / "synthesis_report_v2.md"
    report_path.write_text(report)

    print(f"\n✓ Synthesis saved to: {report_path}")

    return report_path


def main():
    """Main execution."""
    print("=" * 80)
    print("SYNTHESIS FROM VISUALIZATION CLUSTERING")
    print("=" * 80)

    # Load and cluster entities (same as visualization)
    print("\nLoading and clustering entities...")
    entities = load_and_parse_entities()
    print(f"✓ Loaded {len(entities)} entities")

    vis_data, cluster_centers = create_visualization_data(entities)
    print(f"✓ Created {len(cluster_centers)} clusters")

    # Organize entities by cluster
    entities_by_cluster = {}
    for item in vis_data:
        cluster_id = item['cluster']
        if cluster_id not in entities_by_cluster:
            entities_by_cluster[cluster_id] = []

        # Find the full entity data
        entity = next((e for e in entities if e['name'] == item['name']), None)
        if entity:
            entities_by_cluster[cluster_id].append(entity)

    print(f"\nCluster sizes:")
    for cluster_id in sorted(entities_by_cluster.keys()):
        keywords = cluster_centers[cluster_id]['keywords']
        count = len(entities_by_cluster[cluster_id])
        print(f"  Cluster {cluster_id} ({', '.join(keywords[:2])}): {count} entities")

    # Generate synthesis
    synthesis, cost = generate_synthesis(entities_by_cluster, cluster_centers)

    # Save report
    report_path = save_synthesis(synthesis, entities_by_cluster, cluster_centers, cost)

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()

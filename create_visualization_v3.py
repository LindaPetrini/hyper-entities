#!/usr/bin/env python3
"""
Create interactive visualization for v3 extraction results with scoring framework.
"""

import json
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from collections import Counter

# Configuration
CONFIG = {
    "input_json": "results/hyperentities_v3.json",
    "output_html": "results/hyperentities_visualization_v3.html",
    "n_clusters": 12,
}


def load_entities():
    """Load entities from JSON."""
    print("Loading entities from JSON...")
    with open(CONFIG["input_json"]) as f:
        data = json.load(f)
    print(f"✓ Loaded {len(data['entities'])} entities")
    return data


def create_embeddings(entities):
    """Create embeddings using TF-IDF."""
    print("Creating TF-IDF embeddings...")

    # Combine name and description for embedding
    texts = []
    for e in entities:
        text = f"{e['name']}. {e.get('description', '')}"
        texts.append(text)

    vectorizer = TfidfVectorizer(
        max_features=300,
        stop_words='english',
        ngram_range=(1, 2),
        min_df=2
    )

    embeddings = vectorizer.fit_transform(texts).toarray()
    print(f"✓ Created embeddings: {embeddings.shape}")
    return embeddings


def cluster_entities(embeddings, n_clusters):
    """Cluster entities using K-means."""
    print(f"Clustering into {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)
    print(f"✓ Clustered {len(labels)} entities")
    return labels


def reduce_dimensions(embeddings):
    """Reduce to 2D for visualization."""
    print("Reducing to 2D...")
    pca = PCA(n_components=2, random_state=42)
    coords_2d = pca.fit_transform(embeddings)
    print(f"✓ Reduced to 2D")
    return coords_2d


def name_clusters(entities, labels):
    """Generate cluster names based on entity names."""
    print("Generating cluster names...")
    clusters = {}

    for entity, label in zip(entities, labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(entity['name'])

    cluster_names = {}
    for label, names in clusters.items():
        # Extract key words from entity names
        words = []
        for name in names:
            words.extend(name.lower().split())

        # Count common words
        word_counts = Counter(words)
        # Filter out very common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'for', 'of', 'in', 'to', 'system', 'systems'}
        key_words = [w for w, c in word_counts.most_common(3) if w not in stop_words and len(w) > 3]

        if key_words:
            cluster_names[int(label)] = ' & '.join(key_words[:2]).title()
        else:
            cluster_names[int(label)] = f"Cluster {label + 1}"

    print(f"✓ Named {len(cluster_names)} clusters")
    return cluster_names


def create_html_visualization(data, coords_2d, labels, cluster_names):
    """Create interactive HTML visualization."""
    print("Creating HTML visualization...")

    entities = data['entities']
    metadata = data['metadata']

    # Prepare data for JavaScript
    js_entities = []
    for i, entity in enumerate(entities):
        js_entity = {
            'id': entity.get('id', i),
            'name': entity['name'],
            'x': float(coords_2d[i, 0]),
            'y': float(coords_2d[i, 1]),
            'cluster': int(labels[i]),
            'category': entity.get('category', 'Unknown'),
            'description': entity.get('description', 'No description'),
            'source': entity.get('source_file', 'Unknown'),
            'score': entity.get('total_score', 0),
            'qualified': entity.get('qualified', False),
            'scoring': entity.get('scoring', {}),
        }
        js_entities.append(js_entity)

    # Create cluster centers
    cluster_centers = {}
    for label in set(labels):
        cluster_points = coords_2d[labels == label]
        center_x = float(np.mean(cluster_points[:, 0]))
        center_y = float(np.mean(cluster_points[:, 1]))
        cluster_centers[int(label)] = {'x': center_x, 'y': center_y}

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hyper-Entities v3 - Interactive Visualization</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }}
        #header {{
            max-width: 1400px;
            margin: 0 auto 20px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            margin: 0 0 10px;
            color: #333;
        }}
        .stats {{
            display: flex;
            gap: 30px;
            margin-top: 15px;
            font-size: 14px;
            color: #666;
        }}
        .stat {{
            display: flex;
            flex-direction: column;
        }}
        .stat-value {{
            font-size: 24px;
            font-weight: bold;
            color: #2563eb;
        }}
        #container {{
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            gap: 20px;
        }}
        #viz {{
            flex: 1;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        #sidebar {{
            width: 350px;
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-height: 800px;
            overflow-y: auto;
        }}
        .tooltip {{
            position: absolute;
            padding: 12px;
            background: rgba(0, 0, 0, 0.9);
            color: white;
            border-radius: 6px;
            pointer-events: none;
            font-size: 13px;
            max-width: 300px;
            z-index: 100;
        }}
        .tooltip-name {{
            font-weight: bold;
            margin-bottom: 6px;
            font-size: 14px;
        }}
        .tooltip-score {{
            background: #2563eb;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            display: inline-block;
            margin-bottom: 6px;
        }}
        .cluster-label {{
            font-size: 14px;
            font-weight: bold;
            fill: #333;
            pointer-events: none;
            text-anchor: middle;
        }}
        circle {{
            cursor: pointer;
            transition: r 0.2s;
        }}
        circle:hover {{
            stroke: #000;
            stroke-width: 2px;
        }}
        .entity-details {{
            display: none;
        }}
        .entity-details.active {{
            display: block;
        }}
        .entity-details h3 {{
            margin: 0 0 10px;
            color: #2563eb;
        }}
        .detail-section {{
            margin-bottom: 15px;
        }}
        .detail-label {{
            font-weight: bold;
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
            margin-bottom: 5px;
        }}
        .detail-value {{
            color: #333;
            line-height: 1.5;
        }}
        .scoring-grid {{
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 8px;
            font-size: 13px;
        }}
        .score-bar {{
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
            position: relative;
        }}
        .score-fill {{
            height: 100%;
            background: #2563eb;
            border-radius: 4px;
        }}
        .close-btn {{
            float: right;
            cursor: pointer;
            font-size: 20px;
            color: #999;
        }}
        .close-btn:hover {{
            color: #333;
        }}
    </style>
</head>
<body>
    <div id="header">
        <h1>🔮 Hyper-Entities v3 Visualization</h1>
        <p>Rigorous scoring framework (≥18/27 qualification threshold)</p>
        <div class="stats">
            <div class="stat">
                <span class="stat-value">{metadata['total_entities']}</span>
                <span>Total Entities</span>
            </div>
            <div class="stat">
                <span class="stat-value">{metadata['statistics']['qualified_entities']}</span>
                <span>Qualified (≥18)</span>
            </div>
            <div class="stat">
                <span class="stat-value">{metadata['statistics']['average_score']}</span>
                <span>Average Score</span>
            </div>
            <div class="stat">
                <span class="stat-value">{CONFIG['n_clusters']}</span>
                <span>Thematic Clusters</span>
            </div>
        </div>
    </div>

    <div id="container">
        <div id="viz"></div>
        <div id="sidebar">
            <div id="default-view">
                <h3>Interactive Visualization</h3>
                <p>Click on any entity to see detailed scoring and information.</p>
                <p><strong>Color:</strong> Thematic cluster</p>
                <p><strong>Size:</strong> Qualification score (bigger = higher score)</p>
            </div>
            <div id="entity-details" class="entity-details"></div>
        </div>
    </div>

    <script>
        const entities = {json.dumps(js_entities, indent=2)};
        const clusterNames = {json.dumps(cluster_names)};
        const clusterCenters = {json.dumps(cluster_centers)};

        // Set up SVG
        const width = 900;
        const height = 800;
        const margin = {{top: 40, right: 40, bottom: 40, left: 40}};

        const svg = d3.select("#viz")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        // Color scale for clusters
        const colorScale = d3.scaleOrdinal(d3.schemeTableau10);

        // Calculate scales
        const xExtent = d3.extent(entities, d => d.x);
        const yExtent = d3.extent(entities, d => d.y);

        const xScale = d3.scaleLinear()
            .domain(xExtent)
            .range([margin.left, width - margin.right]);

        const yScale = d3.scaleLinear()
            .domain(yExtent)
            .range([height - margin.bottom, margin.top]);

        // Size scale based on score
        const sizeScale = d3.scaleLinear()
            .domain([11, 26])
            .range([4, 10]);

        // Create tooltip
        const tooltip = d3.select("body")
            .append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);

        // Draw cluster labels
        Object.entries(clusterCenters).forEach(([label, center]) => {{
            svg.append("text")
                .attr("class", "cluster-label")
                .attr("x", xScale(center.x))
                .attr("y", yScale(center.y))
                .text(clusterNames[label]);
        }});

        // Draw entities
        const circles = svg.selectAll("circle")
            .data(entities)
            .enter()
            .append("circle")
            .attr("cx", d => xScale(d.x))
            .attr("cy", d => yScale(d.y))
            .attr("r", d => sizeScale(d.score))
            .attr("fill", d => colorScale(d.cluster))
            .attr("opacity", 0.7)
            .on("mouseover", function(event, d) {{
                d3.select(this)
                    .attr("opacity", 1)
                    .attr("r", sizeScale(d.score) * 1.3);

                tooltip.transition()
                    .duration(200)
                    .style("opacity", 1);

                tooltip.html(`
                    <div class="tooltip-name">${{d.name}}</div>
                    <div class="tooltip-score">Score: ${{d.score}}/27</div>
                    <div style="margin-top:6px;">${{d.category}}</div>
                `)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY - 10) + "px");
            }})
            .on("mouseout", function(event, d) {{
                d3.select(this)
                    .attr("opacity", 0.7)
                    .attr("r", sizeScale(d.score));

                tooltip.transition()
                    .duration(200)
                    .style("opacity", 0);
            }})
            .on("click", function(event, d) {{
                showEntityDetails(d);
            }});

        function showEntityDetails(entity) {{
            const sidebar = document.getElementById("entity-details");
            document.getElementById("default-view").style.display = "none";
            sidebar.classList.add("active");

            // Build scoring HTML
            let scoringHTML = '';
            if (entity.scoring && Object.keys(entity.scoring).length > 0) {{
                scoringHTML = '<div class="detail-section"><div class="detail-label">9-Axis Scoring</div><div class="scoring-grid">';
                for (const [axis, score] of Object.entries(entity.scoring)) {{
                    const percentage = (score / 3) * 100;
                    scoringHTML += `
                        <div>${{axis}}</div>
                        <div>
                            <div class="score-bar">
                                <div class="score-fill" style="width: ${{percentage}}%"></div>
                            </div>
                        </div>
                        <div style="text-align: right;">${{score}}/3</div>
                        <div></div>
                    `;
                }}
                scoringHTML += '</div></div>';
            }}

            sidebar.innerHTML = `
                <span class="close-btn" onclick="closeDetails()">&times;</span>
                <h3>${{entity.name}}</h3>

                <div class="detail-section">
                    <div class="detail-label">Total Score</div>
                    <div class="detail-value">
                        <strong style="font-size: 24px; color: #2563eb;">${{entity.score}}/27</strong>
                        ${{entity.qualified ? '<span style="color: #10b981; margin-left: 10px;">✓ Qualified</span>' : ''}}
                    </div>
                </div>

                ${{scoringHTML}}

                <div class="detail-section">
                    <div class="detail-label">Category</div>
                    <div class="detail-value">${{entity.category}}</div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Description</div>
                    <div class="detail-value">${{entity.description}}</div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Source</div>
                    <div class="detail-value" style="font-size: 11px; color: #999;">${{entity.source}}</div>
                </div>
            `;
        }}

        function closeDetails() {{
            document.getElementById("entity-details").classList.remove("active");
            document.getElementById("default-view").style.display = "block";
        }}
    </script>
</body>
</html>"""

    # Save HTML
    output_path = Path(CONFIG["output_html"])
    output_path.write_text(html_content, encoding='utf-8')
    print(f"✓ Saved visualization to: {output_path}")


def main():
    """Main execution."""
    print("=" * 80)
    print("Creating Hyper-Entities v3 Visualization")
    print("=" * 80)
    print()

    # Load data
    data = load_entities()
    entities = data['entities']

    # Create embeddings
    embeddings = create_embeddings(entities)

    # Cluster
    labels = cluster_entities(embeddings, CONFIG['n_clusters'])

    # Reduce dimensions
    coords_2d = reduce_dimensions(embeddings)

    # Name clusters
    cluster_names = name_clusters(entities, labels)

    # Create visualization
    create_html_visualization(data, coords_2d, labels, cluster_names)

    print()
    print("=" * 80)
    print("VISUALIZATION COMPLETE!")
    print("=" * 80)
    print(f"✓ Interactive HTML: {CONFIG['output_html']}")
    print()
    print("Open the HTML file in a browser to explore:")
    print("  - Click entities to see detailed scoring")
    print("  - Hover for quick info")
    print("  - Entity size = qualification score")
    print("  - Entity color = thematic cluster")
    print()


if __name__ == "__main__":
    main()

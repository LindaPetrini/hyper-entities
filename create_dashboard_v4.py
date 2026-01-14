#!/usr/bin/env python3
"""
Create enhanced dashboard with list view, ranking, and Stage 2 scores.
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
    "input_json": "results/hyperentities_v3_with_stage2.json",  # Try Stage 2 first
    "fallback_json": "results/hyperentities_v3.json",  # Fallback if Stage 2 not ready
    "output_html": "results/hyperentities_dashboard_v4.html",
    "n_clusters": 12,
}


def load_entities():
    """Load entities from JSON (try Stage 2 first, fallback to v3)."""
    stage2_path = Path(CONFIG["input_json"])

    if stage2_path.exists():
        print(f"Loading entities with Stage 2 scores from: {stage2_path}")
        with open(stage2_path) as f:
            data = json.load(f)
        has_stage2 = True
    else:
        print(f"Stage 2 scores not ready, using: {CONFIG['fallback_json']}")
        with open(CONFIG["fallback_json"]) as f:
            data = json.load(f)
        has_stage2 = False

    print(f"✓ Loaded {len(data['entities'])} entities")
    return data, has_stage2


def create_embeddings(entities):
    """Create embeddings using TF-IDF."""
    print("Creating TF-IDF embeddings...")
    texts = [f"{e['name']}. {e.get('description', '')}" for e in entities]

    vectorizer = TfidfVectorizer(max_features=300, stop_words='english', ngram_range=(1, 2), min_df=2)
    embeddings = vectorizer.fit_transform(texts).toarray()
    print(f"✓ Created embeddings: {embeddings.shape}")
    return embeddings


def cluster_entities(embeddings, n_clusters):
    """Cluster entities using K-means."""
    print(f"Clustering into {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)
    return labels


def reduce_dimensions(embeddings):
    """Reduce to 2D for visualization."""
    print("Reducing to 2D...")
    pca = PCA(n_components=2, random_state=42)
    coords_2d = pca.fit_transform(embeddings)
    return coords_2d


def name_clusters(entities, labels):
    """Generate cluster names."""
    print("Generating cluster names...")
    clusters = {}
    for entity, label in zip(entities, labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(entity['name'])

    cluster_names = {}
    for label, names in clusters.items():
        words = []
        for name in names:
            words.extend(name.lower().split())

        word_counts = Counter(words)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'for', 'of', 'in', 'to', 'system', 'systems'}
        key_words = [w for w, c in word_counts.most_common(3) if w not in stop_words and len(w) > 3]

        if key_words:
            cluster_names[int(label)] = ' & '.join(key_words[:2]).title()
        else:
            cluster_names[int(label)] = f"Cluster {label + 1}"

    return cluster_names


def create_dashboard_html(data, coords_2d, labels, cluster_names, has_stage2):
    """Create enhanced dashboard HTML."""
    print("Creating dashboard HTML...")

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
            'stage1_score': entity.get('total_score', 0),
            'qualified': entity.get('qualified', False),
            'scoring': entity.get('scoring', {}),
        }

        if has_stage2:
            js_entity['stage2_scores'] = entity.get('stage2_scores', {})
            js_entity['stage2_total'] = entity.get('stage2_total', 0)

        js_entities.append(js_entity)

    # Cluster centers
    cluster_centers = {}
    for label in set(labels):
        cluster_points = coords_2d[labels == label]
        center_x = float(np.mean(cluster_points[:, 0]))
        center_y = float(np.mean(cluster_points[:, 1]))
        cluster_centers[int(label)] = {'x': center_x, 'y': center_y}

    stage2_js = "true" if has_stage2 else "false"

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hyper-Entities Dashboard v4</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 0;
            background: #f5f5f5;
            overflow: hidden;
        }}
        #app {{
            display: flex;
            flex-direction: column;
            height: 100vh;
        }}
        #header {{
            padding: 20px;
            background: white;
            border-bottom: 1px solid #e5e7eb;
            flex-shrink: 0;
        }}
        h1 {{
            margin: 0 0 10px;
            color: #333;
            font-size: 24px;
        }}
        .stats {{
            display: flex;
            gap: 30px;
            margin-top: 15px;
            font-size: 14px;
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
        #main {{
            flex: 1;
            display: flex;
            overflow: hidden;
        }}
        #list-panel {{
            width: 500px;
            background: white;
            border-right: 1px solid #e5e7eb;
            display: flex;
            flex-direction: column;
        }}
        #list-controls {{
            padding: 15px;
            border-bottom: 1px solid #e5e7eb;
            flex-shrink: 0;
        }}
        #search-box {{
            width: 100%;
            padding: 8px;
            border: 1px solid #d1d5db;
            border-radius: 4px;
            font-size: 14px;
            margin-bottom: 10px;
        }}
        #sort-controls {{
            display: flex;
            gap: 10px;
        }}
        select {{
            flex: 1;
            padding: 6px;
            border: 1px solid #d1d5db;
            border-radius: 4px;
            font-size: 13px;
        }}
        #entity-list {{
            flex: 1;
            overflow-y: auto;
        }}
        .entity-item {{
            padding: 12px 15px;
            border-bottom: 1px solid #f3f4f6;
            cursor: pointer;
            transition: background 0.1s;
        }}
        .entity-item:hover {{
            background: #f9fafb;
        }}
        .entity-item.selected {{
            background: #eff6ff;
            border-left: 3px solid #2563eb;
        }}
        .entity-name {{
            font-weight: 600;
            color: #111827;
            font-size: 14px;
            margin-bottom: 4px;
            line-height: 1.4;
        }}
        .entity-meta {{
            font-size: 12px;
            color: #6b7280;
            display: flex;
            gap: 10px;
        }}
        .score-badge {{
            background: #dbeafe;
            color: #1e40af;
            padding: 2px 6px;
            border-radius: 3px;
            font-weight: 600;
        }}
        .stage2-badge {{
            background: #dcfce7;
            color: #166534;
            padding: 2px 6px;
            border-radius: 3px;
            font-weight: 600;
        }}
        #viz-panel {{
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        #viz {{
            flex: 1;
            background: white;
        }}
        #detail-panel {{
            width: 450px;
            background: white;
            border-left: 1px solid #e5e7eb;
            padding: 20px;
            overflow-y: auto;
        }}
        .detail-section {{
            margin-bottom: 20px;
        }}
        .detail-label {{
            font-weight: bold;
            font-size: 12px;
            color: #6b7280;
            text-transform: uppercase;
            margin-bottom: 8px;
        }}
        .detail-value {{
            color: #374151;
            line-height: 1.6;
            font-size: 14px;
        }}
        .expand-btn {{
            background: #2563eb;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 13px;
            margin-bottom: 15px;
        }}
        .expand-btn:hover {{
            background: #1d4ed8;
        }}
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }}
        .modal.active {{
            display: flex;
        }}
        .modal-content {{
            background: white;
            border-radius: 8px;
            max-width: 900px;
            max-height: 90vh;
            overflow-y: auto;
            padding: 30px;
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3);
        }}
        .modal-close {{
            float: right;
            font-size: 28px;
            cursor: pointer;
            color: #999;
            line-height: 1;
        }}
        .modal-close:hover {{
            color: #333;
        }}
        .scoring-grid {{
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 8px;
            font-size: 13px;
        }}
        .score-bar {{
            height: 6px;
            background: #e5e7eb;
            border-radius: 3px;
            overflow: hidden;
        }}
        .score-fill {{
            height: 100%;
            background: #2563eb;
        }}
        .score-fill-stage2 {{
            background: #10b981;
        }}
        .tooltip {{
            position: absolute;
            padding: 10px;
            background: rgba(0, 0, 0, 0.9);
            color: white;
            border-radius: 4px;
            pointer-events: none;
            font-size: 12px;
            max-width: 250px;
            z-index: 100;
        }}
        .cluster-label {{
            font-size: 13px;
            font-weight: bold;
            fill: #6b7280;
            pointer-events: none;
            text-anchor: middle;
        }}
        circle {{
            cursor: pointer;
        }}
        circle:hover {{
            stroke: #000;
            stroke-width: 2px;
        }}
        circle.selected {{
            stroke: #2563eb;
            stroke-width: 3px;
        }}
    </style>
</head>
<body>
    <div id="app">
        <div id="header">
            <h1>🔮 Hyper-Entities Dashboard v4</h1>
            <div class="stats">
                <div class="stat">
                    <span class="stat-value">{metadata['total_entities']}</span>
                    <span>Total Entities</span>
                </div>
                <div class="stat">
                    <span class="stat-value">{metadata['statistics']['qualified_entities']}</span>
                    <span>Qualified (≥18/27)</span>
                </div>
                <div class="stat">
                    <span class="stat-value">{metadata['statistics']['average_score']}</span>
                    <span>Avg Stage 1</span>
                </div>
                {f'''<div class="stat">
                    <span class="stat-value">{data['metadata'].get('stage2_statistics', {}).get('avg_stage2_score', 'N/A')}</span>
                    <span>Avg Stage 2</span>
                </div>''' if has_stage2 else ''}
            </div>
        </div>

        <div id="main">
            <div id="list-panel">
                <div id="list-controls">
                    <input type="text" id="search-box" placeholder="Search entities...">
                    <div id="sort-controls">
                        <select id="sort-by">
                            <option value="stage1_score">Stage 1 Score</option>
                            {f'<option value="stage2_total">Stage 2 Score</option>' if has_stage2 else ''}
                            <option value="name">Name (A-Z)</option>
                            <option value="category">Category</option>
                        </select>
                        <select id="sort-order">
                            <option value="desc">High to Low</option>
                            <option value="asc">Low to High</option>
                        </select>
                    </div>
                </div>
                <div id="entity-list"></div>
            </div>

            <div id="viz-panel">
                <div id="viz"></div>
            </div>

            <div id="detail-panel" style="display:none;">
                <div id="detail-content"></div>
            </div>
        </div>

        <div id="modal" class="modal">
            <div class="modal-content">
                <span class="modal-close" onclick="closeModal()">&times;</span>
                <div id="modal-body"></div>
            </div>
        </div>
    </div>

    <script>
        const entities = {json.dumps(js_entities, indent=2)};
        const hasStage2 = {stage2_js};
        const clusterNames = {json.dumps(cluster_names)};
        const clusterCenters = {json.dumps(cluster_centers)};

        let filteredEntities = [...entities];
        let selectedEntity = null;

        // Set up visualization
        const vizContainer = document.getElementById('viz');
        const width = vizContainer.clientWidth;
        const height = vizContainer.clientHeight;
        const margin = {{top: 30, right: 30, bottom: 30, left: 30}};

        const svg = d3.select("#viz")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        const colorScale = d3.scaleOrdinal(d3.schemeTableau10);

        const xExtent = d3.extent(entities, d => d.x);
        const yExtent = d3.extent(entities, d => d.y);

        const xScale = d3.scaleLinear()
            .domain(xExtent)
            .range([margin.left, width - margin.right]);

        const yScale = d3.scaleLinear()
            .domain(yExtent)
            .range([height - margin.bottom, margin.top]);

        const sizeScale = d3.scaleLinear()
            .domain([11, 26])
            .range([4, 9]);

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
            .attr("r", d => sizeScale(d.stage1_score))
            .attr("fill", d => colorScale(d.cluster))
            .attr("opacity", 0.7)
            .attr("data-id", d => d.id)
            .on("mouseover", function(event, d) {{
                d3.select(this).attr("opacity", 1);
                tooltip.transition().duration(200).style("opacity", 1);
                tooltip.html(`
                    <div style="font-weight:bold;">${{d.name}}</div>
                    <div style="margin-top:4px;">Stage 1: ${{d.stage1_score}}/27</div>
                    ${{hasStage2 ? `<div>Stage 2: ${{d.stage2_total || 0}}/70</div>` : ''}}
                `)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY - 10) + "px");
            }})
            .on("mouseout", function() {{
                d3.select(this).attr("opacity", 0.7);
                tooltip.transition().duration(200).style("opacity", 0);
            }})
            .on("click", function(event, d) {{
                selectEntity(d);
            }});

        // List rendering
        function renderList() {{
            const listEl = document.getElementById('entity-list');
            listEl.innerHTML = '';

            filteredEntities.forEach(entity => {{
                const item = document.createElement('div');
                item.className = 'entity-item';
                if (selectedEntity && selectedEntity.id === entity.id) {{
                    item.className += ' selected';
                }}

                item.innerHTML = `
                    <div class="entity-name">${{entity.name}}</div>
                    <div class="entity-meta">
                        <span class="score-badge">S1: ${{entity.stage1_score}}</span>
                        ${{hasStage2 ? `<span class="stage2-badge">S2: ${{entity.stage2_total || 0}}</span>` : ''}}
                        <span>${{entity.category}}</span>
                    </div>
                `;

                item.onclick = () => selectEntity(entity);
                listEl.appendChild(item);
            }});
        }}

        // Sorting and filtering
        function updateList() {{
            const searchTerm = document.getElementById('search-box').value.toLowerCase();
            const sortBy = document.getElementById('sort-by').value;
            const sortOrder = document.getElementById('sort-order').value;

            // Filter
            filteredEntities = entities.filter(e =>
                e.name.toLowerCase().includes(searchTerm) ||
                e.description.toLowerCase().includes(searchTerm) ||
                e.category.toLowerCase().includes(searchTerm)
            );

            // Sort
            filteredEntities.sort((a, b) => {{
                let valA, valB;
                if (sortBy === 'name') {{
                    valA = a.name.toLowerCase();
                    valB = b.name.toLowerCase();
                    return sortOrder === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
                }} else if (sortBy === 'category') {{
                    valA = a.category.toLowerCase();
                    valB = b.category.toLowerCase();
                    return sortOrder === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
                }} else {{
                    valA = a[sortBy] || 0;
                    valB = b[sortBy] || 0;
                    return sortOrder === 'asc' ? valA - valB : valB - valA;
                }}
            }});

            renderList();
        }}

        // Entity selection
        function selectEntity(entity) {{
            selectedEntity = entity;

            // Update viz
            svg.selectAll("circle")
                .classed("selected", d => d.id === entity.id);

            // Update list
            renderList();

            // Show detail panel
            showDetails(entity);
        }}

        function showDetails(entity) {{
            const panel = document.getElementById('detail-panel');
            const content = document.getElementById('detail-content');
            panel.style.display = 'block';

            let stage1HTML = '<div class="scoring-grid">';
            for (const [axis, score] of Object.entries(entity.scoring)) {{
                const pct = (score / 3) * 100;
                stage1HTML += `
                    <div>${{axis}}</div>
                    <div style="display:flex;align-items:center;gap:8px;">
                        <div class="score-bar" style="flex:1;">
                            <div class="score-fill" style="width:${{pct}}%;"></div>
                        </div>
                        <span style="font-size:11px;color:#6b7280;">${{score}}/3</span>
                    </div>
                `;
            }}
            stage1HTML += '</div>';

            let stage2HTML = '';
            if (hasStage2 && entity.stage2_scores) {{
                stage2HTML = '<div class="detail-section"><div class="detail-label">Stage 2: Impact Assessment (0-5 per dimension)</div><div class="scoring-grid">';
                for (const [dim, score] of Object.entries(entity.stage2_scores)) {{
                    const pct = (score / 5) * 100;
                    stage2HTML += `
                        <div>${{dim}}</div>
                        <div style="display:flex;align-items:center;gap:8px;">
                            <div class="score-bar" style="flex:1;">
                                <div class="score-fill score-fill-stage2" style="width:${{pct}}%;"></div>
                            </div>
                            <span style="font-size:11px;color:#6b7280;">${{score}}/5</span>
                        </div>
                    `;
                }}
                stage2HTML += '</div></div>';
            }}

            content.innerHTML = `
                <button class="expand-btn" onclick="expandEntity()">📄 Open in Larger View</button>
                <h3 style="margin-top:0;color:#2563eb;">${{entity.name}}</h3>

                <div class="detail-section">
                    <div class="detail-label">Scores</div>
                    <div style="font-size:20px;">
                        <strong style="color:#2563eb;">Stage 1: ${{entity.stage1_score}}/27</strong>
                        ${{hasStage2 ? `<br><strong style="color:#10b981;">Stage 2: ${{entity.stage2_total || 0}}/70</strong>` : ''}}
                    </div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Category</div>
                    <div class="detail-value">${{entity.category}}</div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Description</div>
                    <div class="detail-value">${{entity.description}}</div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Stage 1: Qualification Scoring (0-3 per axis)</div>
                    ${{stage1HTML}}
                </div>

                ${{stage2HTML}}

                <div class="detail-section">
                    <div class="detail-label">Source</div>
                    <div class="detail-value" style="font-size:11px;color:#999;">${{entity.source}}</div>
                </div>
            `;
        }}

        // Event listeners
        document.getElementById('search-box').addEventListener('input', updateList);
        document.getElementById('sort-by').addEventListener('change', updateList);
        document.getElementById('sort-order').addEventListener('change', updateList);

        // Modal functions
        function expandEntity() {{
            if (!selectedEntity) return;

            const modal = document.getElementById('modal');
            const modalBody = document.getElementById('modal-body');

            // Build full entity display
            let stage1HTML = '<div class="scoring-grid">';
            for (const [axis, score] of Object.entries(selectedEntity.scoring)) {{
                const pct = (score / 3) * 100;
                stage1HTML += `
                    <div>${{axis}}</div>
                    <div style="display:flex;align-items:center;gap:8px;">
                        <div class="score-bar" style="flex:1;">
                            <div class="score-fill" style="width:${{pct}}%;"></div>
                        </div>
                        <span style="font-size:11px;color:#6b7280;">${{score}}/3</span>
                    </div>
                `;
            }}
            stage1HTML += '</div>';

            let stage2HTML = '';
            if (hasStage2 && selectedEntity.stage2_scores) {{
                stage2HTML = '<div class="detail-section"><div class="detail-label">Stage 2: Impact Assessment (0-5 per dimension)</div><div class="scoring-grid">';
                for (const [dim, score] of Object.entries(selectedEntity.stage2_scores)) {{
                    const pct = (score / 5) * 100;
                    stage2HTML += `
                        <div>${{dim}}</div>
                        <div style="display:flex;align-items:center;gap:8px;">
                            <div class="score-bar" style="flex:1;">
                                <div class="score-fill score-fill-stage2" style="width:${{pct}}%;"></div>
                            </div>
                            <span style="font-size:11px;color:#6b7280;">${{score}}/5</span>
                        </div>
                    `;
                }}
                stage2HTML += '</div></div>';
            }}

            modalBody.innerHTML = `
                <h2 style="margin-top:0;color:#2563eb;">${{selectedEntity.name}}</h2>

                <div class="detail-section">
                    <div class="detail-label">Scores</div>
                    <div style="font-size:24px;">
                        <strong style="color:#2563eb;">Stage 1: ${{selectedEntity.stage1_score}}/27</strong>
                        ${{hasStage2 ? `<br><strong style="color:#10b981;margin-top:8px;display:inline-block;">Stage 2: ${{selectedEntity.stage2_total || 0}}/70</strong>` : ''}}
                    </div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Category</div>
                    <div class="detail-value">${{selectedEntity.category}}</div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Description</div>
                    <div class="detail-value" style="font-size:15px;line-height:1.7;">${{selectedEntity.description}}</div>
                </div>

                <div class="detail-section">
                    <div class="detail-label">Stage 1: Qualification Scoring (0-3 per axis)</div>
                    ${{stage1HTML}}
                </div>

                ${{stage2HTML}}

                <div class="detail-section">
                    <div class="detail-label">Source</div>
                    <div class="detail-value" style="font-size:12px;color:#999;">${{selectedEntity.source}}</div>
                </div>
            `;

            modal.classList.add('active');
        }}

        function closeModal() {{
            document.getElementById('modal').classList.remove('active');
        }}

        // Close modal on escape key
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeModal();
        }});

        // Close modal on background click
        document.getElementById('modal').addEventListener('click', (e) => {{
            if (e.target.id === 'modal') closeModal();
        }});

        // Initial render
        updateList();
    </script>
</body>
</html>"""

    output_path = Path(CONFIG["output_html"])
    output_path.write_text(html, encoding='utf-8')
    print(f"✓ Saved dashboard to: {output_path}")


def main():
    """Main execution."""
    print("=" * 80)
    print("Creating Enhanced Dashboard v4")
    print("=" * 80)
    print()

    # Load data
    data, has_stage2 = load_entities()
    entities = data['entities']

    # Create embeddings
    embeddings = create_embeddings(entities)

    # Cluster
    labels = cluster_entities(embeddings, CONFIG['n_clusters'])

    # Reduce dimensions
    coords_2d = reduce_dimensions(embeddings)

    # Name clusters
    cluster_names = name_clusters(entities, labels)

    # Create dashboard
    create_dashboard_html(data, coords_2d, labels, cluster_names, has_stage2)

    print()
    print("=" * 80)
    print("DASHBOARD COMPLETE!")
    print("=" * 80)
    print(f"✓ Dashboard: {CONFIG['output_html']}")
    print()
    print("Features:")
    print("  - Scrollable entity list with search")
    print("  - Sort by Stage 1 score, Stage 2 score, name, or category")
    print("  - Click entities to see full scoring breakdown")
    print("  - Interactive visualization with cluster labels")
    if has_stage2:
        print("  - ✓ Stage 2 scores included!")
    else:
        print("  - ⏳ Stage 2 scores will appear once assessment completes")
    print()


if __name__ == "__main__":
    main()

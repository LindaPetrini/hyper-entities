#!/usr/bin/env python3
"""
Improved visualization with better clustering and visible cluster labels.
"""

import os
import json
import re
from pathlib import Path
from collections import Counter
import numpy as np

# Configuration
CONFIG = {
    "input_file": "results/hyperentities_extracted.md",
    "output_html": "results/hyperentities_visualization_v2.html",
    "n_clusters": 15,  # More clusters for better granularity
}


def load_and_parse_entities():
    """Load and parse all entities."""
    input_path = Path(CONFIG["input_file"])
    content = input_path.read_text(encoding="utf-8")
    sources = re.split(r'^## Source: ', content, flags=re.MULTILINE)

    all_entities = []
    for source_section in sources[1:]:
        lines = source_section.split('\n', 1)
        if len(lines) < 2:
            continue

        source_file = lines[0].strip()
        extraction = lines[1] if len(lines) > 1 else ""

        if "ERROR" in extraction[:100]:
            continue

        # Parse entities
        sections = re.split(r'\*\*Entity Name:\*\*', extraction)
        for section in sections[1:]:
            try:
                name_match = re.match(r'\s*(.+?)(?:\n|$)', section)
                if not name_match:
                    continue
                entity_name = name_match.group(1).strip()

                category_match = re.search(r'\*\*Category:\*\*\s*(.+?)(?:\n|$)', section)
                category = category_match.group(1).strip() if category_match else "Unknown"

                desc_match = re.search(r'\*\*Description:\*\*\s*(.+?)(?:\n\*\*|$)', section, re.DOTALL)
                description = desc_match.group(1).strip() if desc_match else ""

                promising_match = re.search(r'\*\*Why Promising:\*\*\s*(.+?)(?:\n\*\*|$)', section, re.DOTALL)
                why_promising = promising_match.group(1).strip() if promising_match else ""

                undervalued_match = re.search(r'\*\*Why Undervalued:\*\*\s*(.+?)(?:\n\*\*|$)', section, re.DOTALL)
                why_undervalued = undervalued_match.group(1).strip() if undervalued_match else ""

                # Combine all text for better embedding
                full_text = f"{entity_name}. {description} {why_promising} {why_undervalued}"

                if entity_name and len(entity_name) > 2:
                    all_entities.append({
                        "name": entity_name,
                        "category": category,
                        "description": description[:300] if description else "No description",
                        "why_promising": why_promising[:200] if why_promising else "",
                        "source": source_file,
                        "full_text": full_text,
                    })
            except Exception as e:
                continue

    return all_entities


def try_sentence_transformers(entities):
    """Try to use sentence-transformers for embeddings."""
    try:
        from sentence_transformers import SentenceTransformer
        print("  Using sentence-transformers for embeddings...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        texts = [e['full_text'][:512] for e in entities]  # Limit length
        embeddings = model.encode(texts, show_progress_bar=True)
        return embeddings
    except ImportError:
        return None


def create_improved_tfidf_embeddings(entities):
    """Create improved TF-IDF embeddings with better preprocessing."""
    print("  Using improved TF-IDF embeddings...")

    # Better text preprocessing
    def preprocess(text):
        # Lowercase
        text = text.lower()
        # Remove common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                      'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
                      'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                      'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that',
                      'these', 'those', 'it', 'its'}
        words = [w for w in re.findall(r'\b\w+\b', text) if w not in stop_words and len(w) > 2]
        return words

    # Process all texts
    entity_words = [preprocess(e['full_text']) for e in entities]
    all_words = [w for words in entity_words for w in words]

    # Get important vocabulary (more selective)
    word_counts = Counter(all_words)
    # Exclude very common words (>50% of docs) and very rare words (<2 docs)
    n_docs = len(entities)
    doc_freq = Counter()
    for words in entity_words:
        for word in set(words):
            doc_freq[word] += 1

    vocab = [word for word, count in word_counts.most_common(1000)
             if 2 <= doc_freq[word] <= n_docs * 0.5]
    word_to_idx = {word: idx for idx, word in enumerate(vocab)}

    # Create TF-IDF vectors
    import math
    embeddings = []

    for words in entity_words:
        vector = np.zeros(len(vocab))
        word_freq = Counter(words)

        for word in set(words):
            if word in word_to_idx:
                idx = word_to_idx[word]
                tf = word_freq[word] / len(words) if len(words) > 0 else 0
                idf = math.log(n_docs / (1 + doc_freq[word]))
                vector[idx] = tf * idf

        # Normalize
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm

        embeddings.append(vector)

    return np.array(embeddings)


def get_cluster_keywords(entities, clusters, n_clusters, top_n=5):
    """Extract top keywords for each cluster."""
    cluster_keywords = {}

    # Expanded list of generic/common words to exclude
    generic = {
        # Common verbs
        'system', 'systems', 'make', 'makes', 'made', 'making', 'allow', 'allows', 'allowed',
        'enable', 'enables', 'enabled', 'enabling', 'provide', 'provides', 'provided', 'providing',
        'create', 'creates', 'created', 'creating', 'help', 'helps', 'helped', 'helping',
        'support', 'supports', 'supported', 'supporting', 'develop', 'develops', 'developed',
        # Common adjectives/adverbs
        'more', 'most', 'many', 'much', 'very', 'other', 'such', 'some', 'different',
        'current', 'existing', 'potential', 'possible', 'better', 'greater', 'larger',
        # Connectives and comparatives
        'that', 'than', 'then', 'thus', 'also', 'just', 'only', 'even', 'both', 'either',
        'rather', 'whether', 'while', 'where', 'when', 'which', 'what', 'would', 'could',
        'should', 'might', 'must', 'need', 'needs', 'needed', 'from', 'into', 'onto', 'with',
        # Generic nouns
        'approach', 'approaches', 'framework', 'frameworks', 'model', 'models', 'method',
        'methods', 'technology', 'technologies', 'thing', 'things', 'way', 'ways', 'time',
        'times', 'example', 'examples', 'case', 'cases', 'part', 'parts', 'area', 'areas',
        # Generic descriptors
        'based', 'using', 'through', 'across', 'between', 'within', 'without', 'around',
        'future', 'human', 'humans', 'people', 'work', 'works', 'working', 'used', 'uses',
        'include', 'includes', 'including', 'allow', 'allows', 'allowing',
        # Temporal/modal
        'will', 'would', 'could', 'should', 'may', 'might', 'can', 'cannot',
        # Extra common
        'have', 'having', 'been', 'being', 'become', 'becomes', 'becoming',
    }

    for cluster_id in range(n_clusters):
        cluster_entities = [entities[i] for i in range(len(entities)) if clusters[i] == cluster_id]

        if not cluster_entities:
            cluster_keywords[cluster_id] = []
            continue

        # Collect entity names and key terms (prioritize entity names)
        entity_names = [entity['name'].lower() for entity in cluster_entities]

        # Extract meaningful terms from names first
        name_words = []
        for name in entity_names:
            words = re.findall(r'\b[a-z]{4,}\b', name)
            name_words.extend([w for w in words if w not in generic])

        # Get key terms from descriptions
        desc_words = []
        for entity in cluster_entities:
            # Focus on first 200 chars of description (usually most important)
            text = entity['description'][:200].lower()
            words = re.findall(r'\b[a-z]{4,}\b', text)
            desc_words.extend([w for w in words if w not in generic])

        # Prioritize name words (they're usually more distinctive)
        name_counts = Counter(name_words)
        desc_counts = Counter(desc_words)

        # Combine with name words weighted 3x
        combined_counts = Counter()
        for word, count in name_counts.items():
            combined_counts[word] = count * 3
        for word, count in desc_counts.items():
            combined_counts[word] += count

        # Filter out if appears in >50% of entities (too generic within cluster)
        n_entities = len(cluster_entities)
        distinctive_words = []
        for word, count in combined_counts.most_common(top_n * 3):
            # Check how many entities have this word
            entity_freq = sum(1 for e in cluster_entities if word in e['full_text'].lower())
            if entity_freq < n_entities * 0.5:  # Appears in less than 50%
                distinctive_words.append(word)
            if len(distinctive_words) >= top_n:
                break

        # If we don't have enough, add more common ones
        if len(distinctive_words) < top_n:
            for word, count in combined_counts.most_common(top_n * 2):
                if word not in distinctive_words:
                    distinctive_words.append(word)
                if len(distinctive_words) >= top_n:
                    break

        cluster_keywords[cluster_id] = distinctive_words[:top_n]

    return cluster_keywords


def create_visualization_data(entities):
    """Create embeddings, projection, and clustering."""
    print(f"\nCreating visualization for {len(entities)} entities...")

    # Try sentence-transformers first, fall back to TF-IDF
    embeddings = try_sentence_transformers(entities)
    if embeddings is None:
        embeddings = create_improved_tfidf_embeddings(entities)

    # Use UMAP if available, otherwise t-SNE
    print("  Applying dimensionality reduction...")
    try:
        from umap import UMAP
        print("    Using UMAP...")
        reducer = UMAP(n_components=2, random_state=42, n_neighbors=15, min_dist=0.1)
        coords_2d = reducer.fit_transform(embeddings)
    except ImportError:
        from sklearn.manifold import TSNE
        print("    Using t-SNE...")
        tsne = TSNE(n_components=2, random_state=42, perplexity=30)
        coords_2d = tsne.fit_transform(embeddings)

    # Clustering
    print("  Clustering entities...")
    from sklearn.cluster import KMeans
    n_clusters = min(CONFIG["n_clusters"], len(entities))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(embeddings)

    # Get cluster keywords
    print("  Extracting cluster keywords...")
    cluster_keywords = get_cluster_keywords(entities, clusters, n_clusters)

    # Calculate cluster centers in 2D space
    cluster_centers = {}
    for cluster_id in range(n_clusters):
        cluster_points = coords_2d[clusters == cluster_id]
        if len(cluster_points) > 0:
            center = cluster_points.mean(axis=0)
            cluster_centers[cluster_id] = {
                "x": float(center[0]),
                "y": float(center[1]),
                "keywords": cluster_keywords[cluster_id],
                "label": ", ".join(cluster_keywords[cluster_id][:3]).title()
            }

    # Combine data
    vis_data = []
    for i, entity in enumerate(entities):
        vis_data.append({
            "name": entity["name"],
            "category": entity["category"],
            "description": entity["description"],
            "why_promising": entity["why_promising"],
            "source": entity["source"],
            "x": float(coords_2d[i, 0]),
            "y": float(coords_2d[i, 1]),
            "cluster": int(clusters[i]),
        })

    return vis_data, cluster_centers


def create_html_visualization(vis_data, cluster_centers):
    """Create interactive HTML with cluster labels."""

    html_template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hyper-Entities Visualization v2</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        .info {
            color: #666;
            margin-bottom: 20px;
        }
        #plot {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stats {
            margin-top: 20px;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stats h3 {
            margin-top: 0;
        }
        /* Compact vertical hover tooltip with proper wrapping */
        .hoverlayer .hovertext {
            max-width: 280px !important;
            min-width: 200px !important;
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            overflow-wrap: break-word !important;
            line-height: 1.5 !important;
            padding: 10px 12px !important;
            max-height: 400px !important;
            overflow-y: auto !important;
        }
        .hoverlayer .hovertext path {
            shape-rendering: auto !important;
        }
        .hoverlayer .hovertext text {
            white-space: pre-wrap !important;
        }
    </style>
</head>
<body>
    <h1>Hyper-Entities Visualization v2</h1>
    <div class="info">
        Interactive clustering of {num_entities} hyper-entities across {num_clusters} clusters.
        <br>Hover over points to see details. Cluster labels show common themes.
    </div>

    <div id="plot"></div>

    <div class="stats">
        <h3>Cluster Themes</h3>
        <div id="cluster-stats"></div>
    </div>

    <script>
        const data = {data_json};
        const clusterCenters = {cluster_centers_json};

        // Prepare traces for each cluster
        const traces = [];
        const clusterIds = [...new Set(data.map(d => d.cluster))].sort((a, b) => a - b);

        // Vibrant color palette
        const colors = [
            '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00',
            '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5',
            '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f'
        ];

        clusterIds.forEach(clusterId => {
            const clusterData = data.filter(d => d.cluster === clusterId);

            // Compact hover text - shorter and more concise
            const hoverText = clusterData.map(d => {
                const shortDesc = d.description.length > 150
                    ? d.description.substring(0, 150) + '...'
                    : d.description;
                return `<b>${d.name}</b><br>` +
                    `<i>${d.category}</i><br><br>` +
                    `${shortDesc}`;
            });

            traces.push({
                x: clusterData.map(d => d.x),
                y: clusterData.map(d => d.y),
                mode: 'markers',
                type: 'scatter',
                name: `Cluster ${clusterId}`,
                text: hoverText,
                hovertemplate: '%{text}<extra></extra>',
                hoverlabel: {
                    bgcolor: 'white',
                    bordercolor: colors[clusterId % colors.length],
                    font: {
                        size: 12,
                        family: 'Arial, sans-serif'
                    },
                    align: 'left',
                    namelength: -1
                },
                marker: {
                    size: 6,
                    color: colors[clusterId % colors.length],
                    line: {
                        color: 'white',
                        width: 0.5
                    },
                    opacity: 0.7
                }
            });
        });

        // Add cluster labels as annotations
        const annotations = [];
        Object.keys(clusterCenters).forEach(clusterId => {
            const center = clusterCenters[clusterId];
            annotations.push({
                x: center.x,
                y: center.y,
                text: center.label,
                showarrow: false,
                font: {
                    size: 12,
                    color: '#333',
                    family: 'Arial Black, sans-serif'
                },
                bgcolor: 'rgba(255, 255, 255, 0.8)',
                borderpad: 4,
                bordercolor: colors[clusterId % colors.length],
                borderwidth: 2
            });
        });

        const layout = {
            hovermode: 'closest',
            showlegend: true,
            annotations: annotations,
            hoverlabel: {
                bgcolor: 'white',
                font: {
                    size: 12
                },
                align: 'left'
            },
            legend: {
                x: 1.02,
                y: 1,
                orientation: 'v',
                bgcolor: 'rgba(255, 255, 255, 0.8)',
                bordercolor: '#ddd',
                borderwidth: 1
            },
            xaxis: {
                title: '',
                showgrid: false,
                zeroline: false,
                showticklabels: false
            },
            yaxis: {
                title: '',
                showgrid: false,
                zeroline: false,
                showticklabels: false
            },
            height: 800,
            margin: {
                l: 50,
                r: 250,
                t: 50,
                b: 50
            },
            plot_bgcolor: '#fafafa'
        };

        const config = {
            responsive: true,
            displayModeBar: true,
            displaylogo: false,
            modeBarButtonsToRemove: ['lasso2d', 'select2d']
        };

        Plotly.newPlot('plot', traces, layout, config);

        // Generate cluster statistics
        let statsHTML = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px;">';
        clusterIds.forEach(id => {
            const clusterData = data.filter(d => d.cluster === id);
            const center = clusterCenters[id];
            const categories = [...new Set(clusterData.map(d => d.category.split('/')[0]))];
            const topCategory = categories.length > 0 ? categories[0] : 'Unknown';

            statsHTML += `
                <div style="padding: 10px; border-left: 3px solid ${colors[id % colors.length]};">
                    <strong>Cluster ${id}: ${center.label}</strong><br>
                    <small style="color: #666;">
                        ${clusterData.length} entities<br>
                        Keywords: ${center.keywords.join(', ')}
                    </small>
                </div>
            `;
        });
        statsHTML += '</div>';
        document.getElementById('cluster-stats').innerHTML = statsHTML;
    </script>
</body>
</html>"""

    html = html_template.replace('{data_json}', json.dumps(vis_data))
    html = html.replace('{cluster_centers_json}', json.dumps(cluster_centers))
    html = html.replace('{num_entities}', str(len(vis_data)))
    html = html.replace('{num_clusters}', str(len(cluster_centers)))

    return html


def main():
    """Main execution."""
    print("=" * 80)
    print("IMPROVED HYPER-ENTITIES VISUALIZATION")
    print("=" * 80)

    print("\nLoading and parsing entities...")
    entities = load_and_parse_entities()
    print(f"✓ Parsed {len(entities)} entities")

    vis_data, cluster_centers = create_visualization_data(entities)

    print("\nGenerating HTML visualization...")
    html = create_html_visualization(vis_data, cluster_centers)

    output_path = Path(CONFIG["output_html"])
    output_path.write_text(html)

    print(f"✓ Visualization saved to: {output_path}")
    print(f"\n{output_path.absolute()}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()

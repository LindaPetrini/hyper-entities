#!/usr/bin/env python3
"""
Analyze and cluster all 345 entities to identify similar themes and directions.
Creates detailed cluster analysis for v3.1 organization.
"""

import json
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from collections import Counter, defaultdict

CONFIG = {
    "input_json": "results/stage1_extraction/entities.json",
    "output_json": "results/cluster_analysis.json",
    "n_clusters": 20,  # More granular clustering for organization
}


def load_entities():
    """Load entities from v3.0."""
    with open(CONFIG["input_json"]) as f:
        data = json.load(f)
    print(f"✓ Loaded {len(data['entities'])} entities")
    return data


def create_embeddings(entities):
    """Create TF-IDF embeddings from entity descriptions."""
    print("Creating embeddings...")

    # Combine multiple fields for richer representation
    texts = []
    for e in entities:
        text = f"{e['name']} {e.get('description', '')} {e.get('category', '')}"
        texts.append(text)

    vectorizer = TfidfVectorizer(
        max_features=500,
        stop_words='english',
        ngram_range=(1, 3),
        min_df=2
    )

    embeddings = vectorizer.fit_transform(texts).toarray()
    print(f"✓ Created embeddings: {embeddings.shape}")
    return embeddings, vectorizer


def cluster_entities(embeddings, n_clusters):
    """Cluster entities using K-means."""
    print(f"Clustering into {n_clusters} groups...")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=20)
    labels = kmeans.fit_predict(embeddings)
    print(f"✓ Clustered entities")
    return labels, kmeans


def analyze_clusters(entities, labels, embeddings, vectorizer):
    """Analyze each cluster in detail."""
    print("Analyzing clusters...")

    n_clusters = len(set(labels))
    clusters = {}

    for cluster_id in range(n_clusters):
        cluster_entities = [e for i, e in enumerate(entities) if labels[i] == cluster_id]
        cluster_indices = [i for i, label in enumerate(labels) if label == cluster_id]

        # Extract key themes
        names = [e['name'] for e in cluster_entities]
        categories = [e.get('category', 'Unknown') for e in cluster_entities]

        # Get top keywords for this cluster
        cluster_embeddings = embeddings[cluster_indices]
        centroid = cluster_embeddings.mean(axis=0)

        # Get top features from centroid
        feature_names = vectorizer.get_feature_names_out()
        top_indices = centroid.argsort()[-10:][::-1]
        top_keywords = [feature_names[i] for i in top_indices]

        # Category distribution
        category_dist = Counter(categories)

        # Score statistics
        stage1_scores = [e.get('stage1_score', 0) for e in cluster_entities]
        stage2_scores = [e.get('stage2_total', 0) for e in cluster_entities]

        # Generate cluster name from common themes
        name_words = []
        for name in names:
            name_words.extend(name.lower().split())

        word_counts = Counter(name_words)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'for', 'of', 'in', 'to', 'system', 'systems', 'infrastructure'}

        key_words = []
        for word, count in word_counts.most_common(5):
            if word not in stop_words and len(word) > 3 and count > 1:
                key_words.append(word)

        cluster_name = ' & '.join(key_words[:2]).title() if key_words else f"Cluster {cluster_id + 1}"

        clusters[cluster_id] = {
            "id": cluster_id,
            "name": cluster_name,
            "size": len(cluster_entities),
            "entity_ids": [e['id'] for e in cluster_entities],
            "entity_names": names,
            "top_keywords": top_keywords,
            "category_distribution": dict(category_dist.most_common(5)),
            "avg_stage1_score": round(np.mean(stage1_scores), 2) if stage1_scores else 0,
            "avg_stage2_score": round(np.mean(stage2_scores), 2) if stage2_scores else 0,
            "score_range_s1": f"{min(stage1_scores)}-{max(stage1_scores)}" if stage1_scores else "N/A",
            "score_range_s2": f"{min(stage2_scores)}-{max(stage2_scores)}" if stage2_scores else "N/A",
        }

    print(f"✓ Analyzed {n_clusters} clusters")
    return clusters


def identify_related_groups(clusters, entities, labels):
    """Identify groups of entities going in similar directions."""
    print("Identifying related groups...")

    related_groups = {}

    # Group clusters by themes
    themes = defaultdict(list)

    for cluster_id, cluster in clusters.items():
        keywords = cluster['top_keywords'][:3]

        # Identify theme from keywords
        theme = None
        if any(k in ['ai', 'artificial', 'intelligence', 'learning'] for k in keywords):
            theme = "AI Systems"
        elif any(k in ['governance', 'coordination', 'institutional'] for k in keywords):
            theme = "Governance & Coordination"
        elif any(k in ['infrastructure', 'network', 'distributed'] for k in keywords):
            theme = "Infrastructure"
        elif any(k in ['research', 'science', 'scientific'] for k in keywords):
            theme = "Research & Science"
        elif any(k in ['health', 'medical', 'healthcare'] for k in keywords):
            theme = "Health & Medicine"
        elif any(k in ['education', 'learning', 'skill'] for k in keywords):
            theme = "Education & Skills"
        elif any(k in ['economic', 'financial', 'capital'] for k in keywords):
            theme = "Economic Systems"
        elif any(k in ['climate', 'environmental', 'ecological'] for k in keywords):
            theme = "Climate & Environment"
        else:
            theme = "Other"

        themes[theme].append(cluster_id)

    for theme, cluster_ids in themes.items():
        total_entities = sum(clusters[cid]['size'] for cid in cluster_ids)
        related_groups[theme] = {
            "theme": theme,
            "cluster_ids": cluster_ids,
            "total_entities": total_entities,
            "clusters": [clusters[cid]['name'] for cid in cluster_ids]
        }

    print(f"✓ Identified {len(related_groups)} thematic groups")
    return related_groups


def main():
    """Main execution."""
    print("=" * 80)
    print("Cluster Analysis for v3.1 Organization")
    print("=" * 80)
    print()

    # Load data
    data = load_entities()
    entities = data['entities']

    # Create embeddings
    embeddings, vectorizer = create_embeddings(entities)

    # Cluster
    labels, kmeans = cluster_entities(embeddings, CONFIG['n_clusters'])

    # Analyze clusters
    clusters = analyze_clusters(entities, labels, embeddings, vectorizer)

    # Identify related groups
    related_groups = identify_related_groups(clusters, entities, labels)

    # Add cluster assignments to entities
    for i, entity in enumerate(entities):
        entity['cluster_id'] = int(labels[i])
        entity['cluster_name'] = clusters[labels[i]]['name']

    # Save results
    output = {
        "metadata": {
            "total_entities": len(entities),
            "n_clusters": CONFIG['n_clusters'],
            "analysis_date": "2026-01-14",
        },
        "clusters": clusters,
        "related_groups": related_groups,
        "entities_with_clusters": entities,
    }

    with open(CONFIG['output_json'], 'w') as f:
        json.dump(output, f, indent=2)

    print()
    print("=" * 80)
    print("CLUSTER ANALYSIS COMPLETE")
    print("=" * 80)
    print()

    # Print summary
    print(f"Total entities: {len(entities)}")
    print(f"Clusters: {CONFIG['n_clusters']}")
    print()

    print("Top 10 Clusters by Size:")
    sorted_clusters = sorted(clusters.values(), key=lambda x: x['size'], reverse=True)
    for i, cluster in enumerate(sorted_clusters[:10], 1):
        print(f"  {i}. {cluster['name']} - {cluster['size']} entities (Avg S1: {cluster['avg_stage1_score']}, S2: {cluster['avg_stage2_score']})")

    print()
    print("Thematic Groups:")
    for theme, group in sorted(related_groups.items(), key=lambda x: x[1]['total_entities'], reverse=True):
        print(f"  {theme}: {group['total_entities']} entities across {len(group['cluster_ids'])} clusters")

    print()
    print(f"✓ Saved to: {CONFIG['output_json']}")
    print()


if __name__ == "__main__":
    main()

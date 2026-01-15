# Hyper-Entities Project

## Overview
Dashboard for exploring "hyper-entities" - future systems that don't exist yet but are already reorganizing coordination, investment, and narrative around their anticipated existence.

## Key Files
- `create_dashboard.py` - Generates the interactive dashboard
- `analyze_clusters.py` - Clusters entities into thematic groups
- `expand_entities.py` - Expands entities with Stage 2 assessment (requires API key)
- `METHODOLOGY.md` - Full scoring framework documentation

## Results Structure
- `results/dashboard.html` - Main dashboard (hosted on GitHub Pages)
- `results/cluster_analysis.json` - Clustering data
- `results/stage1_extraction/` - Initial hyper-entity extraction (9-axis scoring)
- `results/stage2_assessment/` - Technology impact assessment (14-dimension scoring)

## Scoring Framework
- **Stage 1 (Hyper-Entity Assessment)**: 9 axes, 0-3 each, max 27. Threshold ≥18 to qualify.
- **Stage 2 (Technology Assessment)**: 14 dimensions, 0-5 each, max 70. Assesses impact/risk.

## Dashboard Features
- Version switcher (v3.0/v3.1)
- Cluster visualization with zoom/pan
- Star entities + export starred list
- Sort by Hyper-Entity or Technology scores
- Methodology modal with full scoring tables

## GitHub Pages URL
https://lindapetrini.github.io/hyper-entities/results/dashboard.html

## Commands
```bash
python create_dashboard.py  # Regenerate dashboard
```

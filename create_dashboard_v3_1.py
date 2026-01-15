#!/usr/bin/env python3
"""
Create v3.1 dashboard with version dropdown to switch between v3.0 and v3.1.
"""

import json
from pathlib import Path

CONFIG = {
    "v3_0_json": "results/v3.0_rigorous_dual_scoring/entities.json",
    "v3_1_json": "results/v3.1_organized_expanded/entities.json",
    "output_html": "results/hyperentities_dashboard_v3_1.html",
}


def load_data():
    """Load both v3.0 and v3.1 data."""
    print("Loading v3.0 data...")
    with open(CONFIG["v3_0_json"]) as f:
        v3_0_data = json.load(f)
    print(f"✓ Loaded {len(v3_0_data['entities'])} v3.0 entities")

    print("Loading v3.1 data...")
    with open(CONFIG["v3_1_json"]) as f:
        v3_1_data = json.load(f)
    print(f"✓ Loaded {len(v3_1_data['entities'])} v3.1 entities")

    return v3_0_data, v3_1_data


def create_dashboard_html(v3_0_data, v3_1_data):
    """Create dashboard HTML with version switcher."""
    print("Creating v3.1 dashboard...")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hyper-Entities Dashboard v3</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0a0e27;
            color: #e0e6f0;
            overflow: hidden;
        }}

        .header {{
            background: linear-gradient(135deg, #1a1f3a 0%, #2a2f4a 100%);
            padding: 20px 30px;
            border-bottom: 2px solid #3a4f7a;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .header-left {{
            display: flex;
            align-items: center;
            gap: 30px;
        }}

        h1 {{
            font-size: 24px;
            font-weight: 600;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .version-selector {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .version-selector label {{
            font-size: 14px;
            color: #94a3b8;
        }}

        .version-selector select {{
            background: #1e293b;
            color: #e0e6f0;
            border: 1px solid #3a4f7a;
            border-radius: 6px;
            padding: 6px 12px;
            font-size: 14px;
            cursor: pointer;
        }}

        .version-selector select:hover {{
            border-color: #60a5fa;
        }}

        .stats {{
            display: flex;
            gap: 20px;
            font-size: 13px;
            color: #94a3b8;
        }}

        .stat {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}

        .stat strong {{
            color: #60a5fa;
        }}

        .container {{
            display: flex;
            height: calc(100vh - 84px);
        }}

        #list-panel {{
            width: 500px;
            background: #0f1629;
            border-right: 2px solid #1e293b;
            display: flex;
            flex-direction: column;
        }}

        .search-box {{
            padding: 15px;
            background: #1a1f3a;
            border-bottom: 1px solid #2a2f4a;
        }}

        #search {{
            width: 100%;
            padding: 10px;
            background: #0a0e27;
            border: 1px solid #3a4f7a;
            border-radius: 6px;
            color: #e0e6f0;
            font-size: 14px;
        }}

        #search:focus {{
            outline: none;
            border-color: #60a5fa;
        }}

        .sort-controls {{
            padding: 10px 15px;
            background: #1a1f3a;
            border-bottom: 1px solid #2a2f4a;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .sort-btn {{
            padding: 6px 12px;
            background: #1e293b;
            border: 1px solid #3a4f7a;
            border-radius: 4px;
            color: #94a3b8;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
        }}

        .sort-btn:hover {{
            background: #2a3f5a;
            color: #e0e6f0;
        }}

        .sort-btn.active {{
            background: #60a5fa;
            border-color: #60a5fa;
            color: #ffffff;
        }}

        .star-btn {{
            background: none;
            border: none;
            font-size: 16px;
            cursor: pointer;
            padding: 2px 5px;
            opacity: 0.4;
            transition: all 0.2s;
        }}

        .star-btn:hover {{
            opacity: 1;
            transform: scale(1.2);
        }}

        .star-btn.starred {{
            opacity: 1;
            color: #fbbf24;
        }}

        .filter-starred {{
            background: #1e293b;
            border: 1px solid #3a4f7a;
        }}

        .filter-starred.active {{
            background: #fbbf24;
            border-color: #fbbf24;
            color: #000;
        }}

        .export-btn {{
            padding: 6px 12px;
            background: #059669;
            border: 1px solid #059669;
            border-radius: 4px;
            color: #fff;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
        }}

        .export-btn:hover {{
            background: #047857;
        }}

        .export-btn:disabled {{
            background: #374151;
            border-color: #374151;
            cursor: not-allowed;
            opacity: 0.5;
        }}

        .starred-count {{
            font-size: 11px;
            color: #fbbf24;
            margin-left: 5px;
        }}

        .entity-list {{
            flex: 1;
            overflow-y: auto;
            padding: 10px;
        }}

        .entity-item {{
            padding: 12px;
            margin-bottom: 8px;
            background: #1a1f3a;
            border: 1px solid #2a2f4a;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .entity-item:hover {{
            background: #1e2a4a;
            border-color: #3a5f8a;
            transform: translateX(3px);
        }}

        .entity-item.selected {{
            background: #2a3f5a;
            border-color: #60a5fa;
        }}

        .entity-name {{
            font-size: 14px;
            font-weight: 500;
            color: #e0e6f0;
            margin-bottom: 4px;
        }}

        .entity-meta {{
            display: flex;
            gap: 10px;
            font-size: 11px;
            color: #64748b;
        }}

        .entity-score {{
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        .score-badge {{
            padding: 2px 6px;
            background: #1e293b;
            border-radius: 3px;
            font-weight: 500;
        }}

        .score-s1 {{
            color: #60a5fa;
        }}

        .score-s2 {{
            color: #a78bfa;
        }}

        #viz-container {{
            flex: 1;
            background: #0f1629;
            position: relative;
        }}

        .zoom-controls {{
            position: absolute;
            top: 10px;
            right: 10px;
            display: flex;
            flex-direction: column;
            gap: 5px;
            z-index: 100;
        }}

        .zoom-btn {{
            width: 32px;
            height: 32px;
            background: #1e293b;
            border: 1px solid #3a4f7a;
            border-radius: 4px;
            color: #e0e6f0;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }}

        .zoom-btn:hover {{
            background: #2a3f5a;
            border-color: #60a5fa;
        }}

        .zoom-hint {{
            position: absolute;
            bottom: 10px;
            left: 10px;
            font-size: 11px;
            color: #64748b;
            background: rgba(15, 22, 41, 0.8);
            padding: 5px 10px;
            border-radius: 4px;
        }}

        #detail-panel {{
            width: 450px;
            background: #0f1629;
            border-left: 2px solid #1e293b;
            overflow-y: auto;
            padding: 30px;
        }}

        .detail-header {{
            margin-bottom: 20px;
        }}

        .detail-title {{
            font-size: 22px;
            font-weight: 600;
            color: #e0e6f0;
            margin-bottom: 8px;
        }}

        .detail-category {{
            font-size: 13px;
            color: #64748b;
            margin-bottom: 15px;
        }}

        .detail-scores {{
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
        }}

        .score-box {{
            flex: 1;
            padding: 12px;
            background: #1a1f3a;
            border: 1px solid #2a2f4a;
            border-radius: 6px;
            text-align: center;
        }}

        .score-label {{
            font-size: 11px;
            color: #64748b;
            margin-bottom: 4px;
        }}

        .score-value {{
            font-size: 20px;
            font-weight: 600;
        }}

        .detail-section {{
            margin-bottom: 25px;
        }}

        .section-title {{
            font-size: 14px;
            font-weight: 600;
            color: #60a5fa;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .section-content {{
            font-size: 13px;
            line-height: 1.6;
            color: #cbd5e1;
        }}

        .scoring-grid {{
            display: grid;
            gap: 8px;
            margin-top: 10px;
        }}

        .score-row {{
            display: grid;
            grid-template-columns: 140px 1fr 40px;
            align-items: center;
            gap: 10px;
            padding: 6px 10px;
            background: #1a1f3a;
            border-radius: 4px;
            font-size: 12px;
        }}

        .score-name {{
            color: #94a3b8;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .score-bar-container {{
            height: 6px;
            background: #1e293b;
            border-radius: 3px;
            overflow: hidden;
        }}

        .score-bar {{
            height: 100%;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            border-radius: 3px;
            transition: width 0.3s;
        }}

        .score-num {{
            color: #e0e6f0;
            font-weight: 500;
            text-align: right;
        }}

        .open-modal-btn {{
            margin-top: 20px;
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            border: none;
            border-radius: 6px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            font-size: 14px;
        }}

        .open-modal-btn:hover {{
            opacity: 0.9;
        }}

        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            align-items: center;
            justify-content: center;
        }}

        .modal-content {{
            background: #0f1629;
            border: 2px solid #3a4f7a;
            border-radius: 12px;
            max-width: 900px;
            max-height: 90vh;
            overflow-y: auto;
            padding: 30px;
            position: relative;
        }}

        .modal-close {{
            position: absolute;
            top: 15px;
            right: 15px;
            font-size: 28px;
            color: #94a3b8;
            cursor: pointer;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
        }}

        .modal-close:hover {{
            background: #1a1f3a;
            color: #e0e6f0;
        }}

        .modal .detail-title {{
            font-size: 26px;
            margin-right: 40px;
        }}

        .modal .section-content {{
            font-size: 15px;
            line-height: 1.7;
        }}

        .node {{
            cursor: pointer;
            transition: all 0.2s;
        }}

        .node:hover {{
            stroke: #60a5fa;
            stroke-width: 2px;
        }}

        .node.selected {{
            stroke: #60a5fa;
            stroke-width: 3px;
        }}

        ::-webkit-scrollbar {{
            width: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: #0a0e27;
        }}

        ::-webkit-scrollbar-thumb {{
            background: #3a4f7a;
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: #4a5f8a;
        }}

        .empty-state {{
            text-align: center;
            padding: 60px 20px;
            color: #64748b;
        }}

        .empty-state-icon {{
            font-size: 48px;
            margin-bottom: 16px;
        }}

        .version-badge {{
            padding: 4px 8px;
            background: #1e293b;
            border: 1px solid #3a4f7a;
            border-radius: 4px;
            font-size: 12px;
            color: #94a3b8;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <h1>Hyper-Entities Dashboard</h1>
            <div class="version-selector">
                <label for="version-select">Version:</label>
                <select id="version-select">
                    <option value="v3.0">v3.0 - Rigorous Dual Scoring (9+14 axes)</option>
                    <option value="v3.1" selected>v3.1 - Organized & Expanded (3+3 scores)</option>
                </select>
            </div>
        </div>
        <div class="stats">
            <div class="stat">
                <span>Entities:</span>
                <strong id="entity-count">0</strong>
            </div>
            <div class="stat">
                <span>Clusters:</span>
                <strong id="cluster-count">0</strong>
            </div>
            <div class="stat">
                <span>Qualified:</span>
                <strong id="qualified-count">0</strong>
            </div>
            <button class="sort-btn" onclick="showMethodology()" style="margin-left: 15px;">
                View Methodology
            </button>
        </div>
    </div>

    <div class="container">
        <div id="list-panel">
            <div class="search-box">
                <input type="text" id="search" placeholder="Search entities...">
            </div>
            <div class="sort-controls">
                <button class="sort-btn active" data-sort="s1">Sort: Stage 1 ↓</button>
                <button class="sort-btn" data-sort="s2">Sort: Stage 2 ↓</button>
                <button class="sort-btn" data-sort="name">Sort: Name</button>
                <button class="sort-btn" data-sort="category">Sort: Category</button>
            </div>
            <div class="sort-controls">
                <button class="sort-btn filter-starred" id="filter-starred" onclick="toggleStarredFilter()">
                    ★ Starred<span class="starred-count" id="starred-count">(0)</span>
                </button>
                <button class="export-btn" id="export-starred" onclick="exportStarred()" disabled>
                    Export Starred
                </button>
            </div>
            <div class="entity-list" id="entity-list"></div>
        </div>

        <div id="viz-container">
            <div class="zoom-controls">
                <button class="zoom-btn" onclick="zoomIn()" title="Zoom In">+</button>
                <button class="zoom-btn" onclick="zoomOut()" title="Zoom Out">-</button>
                <button class="zoom-btn" onclick="zoomReset()" title="Reset View">&#8634;</button>
            </div>
            <div class="zoom-hint">Scroll to zoom, drag to pan</div>
        </div>

        <div id="detail-panel">
            <div class="empty-state">
                <div class="empty-state-icon">→</div>
                <p>Select an entity from the list to view details</p>
            </div>
        </div>
    </div>

    <div id="modal" class="modal">
        <div class="modal-content">
            <span class="modal-close">&times;</span>
            <div id="modal-body"></div>
        </div>
    </div>

    <div id="methodology-modal" class="modal">
        <div class="modal-content" style="max-width: 900px; max-height: 85vh; display: flex; flex-direction: column;">
            <span class="modal-close" onclick="closeMethodology()">&times;</span>
            <h2 style="margin-bottom: 20px; color: #60a5fa; flex-shrink: 0;">Extraction Methodology</h2>

            <div class="method-tabs" style="flex-shrink: 0;">
                <button class="method-tab active" onclick="showMethodTab('v30')">v3.0 Extraction</button>
                <button class="method-tab" onclick="showMethodTab('v31')">v3.1 Expansion</button>
            </div>

            <div style="flex: 1; overflow-y: auto; padding-right: 10px;">
                <div id="method-v30" class="method-content active">
                    <h3>Stage 1: Hyper-Entity Extraction Prompt</h3>
                    <p style="color: #94a3b8; margin-bottom: 15px;">Used to identify and score hyper-entities from source documents.</p>
                    <pre style="background: #0a0e27; padding: 15px; border-radius: 8px; overflow-x: auto; font-size: 12px; line-height: 1.5; white-space: pre-wrap;">You are analyzing futures-oriented content to identify HYPER-ENTITIES using a rigorous scoring framework.

DEFINITION: A hyper-entity is "A coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence."

KEY REQUIREMENTS (ALL must be true):
1. Does NOT exist yet (or only partially exists)
2. Creates a NEW stable action space (new things humans can do)
3. Has PRE-REAL EFFECTS (already reorganizing coordination/investment/narrative NOW)

SCORING FRAMEWORK: 9 axes (0-3 per axis). Maximum: 27 points. Threshold: ≥18 to qualify.

| Axis               | 0          | 1           | 2                | 3                       |
|--------------------|------------|-------------|------------------|-------------------------|
| Non-existence      | Deployed   | Prototype   | Partial demos    | No instantiation        |
| Plausibility       | Fantasy    | Hand-wavy   | Credible theory  | Active scientific path  |
| Design specificity | Vague      | Metaphor    | Coarse arch.     | Detailed system model   |
| New action space   | Incremental| Narrow new  | Broad new cap.   | Entirely new verb       |
| Roadmap clarity    | None       | Wishful     | Research agenda  | Multi-stage roadmap     |
| Coordination gravity| Solo      | Small niche | Multiple orgs    | Global coordination     |
| Resource pull      | Trivial    | Some grants | Serious capital  | Massive capital+talent  |
| Narrative centrality| Ignored   | Peripheral  | Often referenced | Justifies present acts  |
| Pre-real effects   | None       | Speculation | Market/policy    | Institutions reorganize |</pre>
                </div>

                <div id="method-v31" class="method-content" style="display: none;">
                <h3>Stage 2: Entity Expansion Prompt</h3>
                <p style="color: #94a3b8; margin-bottom: 15px;">Used to add concrete details and consolidated scoring to each entity.</p>
                <pre style="background: #0a0e27; padding: 15px; border-radius: 8px; overflow-x: auto; font-size: 12px; line-height: 1.5; white-space: pre-wrap;">You are expanding a hyper-entity description with concrete, specific details.

ENTITY: [Entity Name]
CATEGORY: [Category]
CURRENT DESCRIPTION: [Description]

Add the following details in a concise, specific manner:

1. **PROBLEMS SOLVED** (2-3 sentences):
   - What specific challenges or gaps does this address?
   - What pain points does it solve?

2. **WHY NEW/DIFFERENT** (2-3 sentences):
   - What makes this distinct from existing approaches?
   - What novel capabilities or architecture does it introduce?

3. **WHY NOT EXISTS YET** (2-3 sentences):
   - What are the key barriers preventing deployment today?
   - What needs to change or be built first?

CONSOLIDATED SCORING (v3.1):
Stage 1 scores are consolidated into 3 dimensions:
- Reality Gap (0-9): Non-existence + Plausibility + Design specificity
- Transformative Potential (0-6): New action space + Roadmap clarity
- Current Momentum (0-12): Coordination gravity + Resource pull + Narrative centrality + Pre-real effects

Stage 2 scores are consolidated into 3 dimensions:
- Transformative Power (0-25): Capability Discontinuity + Cross-Domain Reach + Scalability + Autonomy + Composability
- Systemic Risk (0-25): Irreversibility + Power Concentration + Externality Magnitude + Misuse Asymmetry + Governance Lag
- Lock-in Effects (0-20): Feedback Intensity + Narrative Lock-In + Path Dependency + Human Agency Impact</pre>
                </div>
            </div>
        </div>
    </div>

    <style>
        .method-tabs {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }}
        .method-tab {{
            padding: 10px 20px;
            background: #1e293b;
            border: 1px solid #3a4f7a;
            border-radius: 6px;
            color: #94a3b8;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
        }}
        .method-tab:hover {{
            background: #2a3f5a;
            color: #e0e6f0;
        }}
        .method-tab.active {{
            background: #60a5fa;
            border-color: #60a5fa;
            color: #fff;
        }}
        .method-content {{
            display: none;
        }}
        .method-content.active {{
            display: block;
        }}
        .method-content h3 {{
            color: #a78bfa;
            margin-bottom: 10px;
        }}
    </style>

    <script>
        // Data embedded in HTML
        const v3_0_data = __V3_0_DATA_PLACEHOLDER__;
        const v3_1_data = __V3_1_DATA_PLACEHOLDER__;

        let currentVersion = 'v3.1';
        let currentData = v3_1_data;
        let entities = currentData.entities;
        let filteredEntities = entities;
        let selectedEntity = null;
        let currentSort = 's1';
        let showOnlyStarred = false;

        // Starred entities management (persisted to localStorage)
        let starredEntities = new Set(JSON.parse(localStorage.getItem('starredEntities') || '[]'));

        function saveStarred() {{
            localStorage.setItem('starredEntities', JSON.stringify([...starredEntities]));
            updateStarredCount();
        }}

        function toggleStar(entityId, event) {{
            if (event) event.stopPropagation();
            if (starredEntities.has(entityId)) {{
                starredEntities.delete(entityId);
            }} else {{
                starredEntities.add(entityId);
            }}
            saveStarred();
            renderList();
            if (selectedEntity && selectedEntity.id === entityId) {{
                showDetail(selectedEntity);
            }}
        }}

        function isStarred(entityId) {{
            return starredEntities.has(entityId);
        }}

        function updateStarredCount() {{
            const count = starredEntities.size;
            document.getElementById('starred-count').textContent = `(${{count}})`;
            document.getElementById('export-starred').disabled = count === 0;
        }}

        function toggleStarredFilter() {{
            showOnlyStarred = !showOnlyStarred;
            document.getElementById('filter-starred').classList.toggle('active', showOnlyStarred);
            filterAndSort();
        }}

        function exportStarred() {{
            const starredList = entities.filter(e => starredEntities.has(e.id));
            if (starredList.length === 0) {{
                alert('No starred entities to export');
                return;
            }}

            const exportData = {{
                exported_at: new Date().toISOString(),
                version: currentVersion,
                count: starredList.length,
                entities: starredList.map(e => ({{
                    id: e.id,
                    name: e.name,
                    category: e.category,
                    description: e.description,
                    stage1_total: currentVersion === 'v3.0' ? e.stage1_score : e.stage1_consolidated?.total,
                    stage2_total: currentVersion === 'v3.0' ? e.stage2_total : e.stage2_consolidated?.total,
                    cluster: e.cluster_name || null,
                    source: e.source_file
                }}))
            }};

            const blob = new Blob([JSON.stringify(exportData, null, 2)], {{ type: 'application/json' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `starred_entities_${{currentVersion}}_${{new Date().toISOString().slice(0,10)}}.json`;
            a.click();
            URL.revokeObjectURL(url);
        }}

        // Initialize
        function init() {{
            updateStats();
            updateStarredCount();
            renderList();
            renderVisualization();
            setupEventListeners();
        }}

        // Setup event listeners
        function setupEventListeners() {{
            document.getElementById('version-select').addEventListener('change', handleVersionChange);
            document.getElementById('search').addEventListener('input', handleSearch);
            document.querySelectorAll('.sort-btn').forEach(btn => {{
                btn.addEventListener('click', handleSort);
            }});
            document.querySelector('.modal-close').addEventListener('click', closeModal);
            document.getElementById('modal').addEventListener('click', (e) => {{
                if (e.target.id === 'modal') closeModal();
            }});
        }}

        // Handle version change
        function handleVersionChange(e) {{
            currentVersion = e.target.value;
            currentData = currentVersion === 'v3.0' ? v3_0_data : v3_1_data;
            entities = currentData.entities;
            filteredEntities = entities;
            selectedEntity = null;

            updateStats();
            renderList();
            renderVisualization();

            // Clear detail panel
            document.getElementById('detail-panel').innerHTML = `
                <div class="empty-state">
                    <div class="empty-state-icon">→</div>
                    <p>Select an entity from the list to view details</p>
                </div>
            `;
        }}

        // Update stats
        function updateStats() {{
            document.getElementById('entity-count').textContent = entities.length;

            // Count clusters
            const clusters = currentVersion === 'v3.1' && currentData.clusters
                ? Object.keys(currentData.clusters).length
                : 0;
            document.getElementById('cluster-count').textContent = clusters;

            // Count qualified (≥18 for v3.0, or use reality_gap for v3.1)
            const qualified = entities.filter(e => {{
                if (currentVersion === 'v3.0') {{
                    return (e.stage1_score || 0) >= 18;
                }} else {{
                    return (e.stage1_consolidated?.total || 0) >= 18;
                }}
            }}).length;
            document.getElementById('qualified-count').textContent = qualified;
        }}

        // Filter and sort entities
        function filterAndSort() {{
            const query = (document.getElementById('search').value || '').toLowerCase();

            filteredEntities = entities.filter(entity => {{
                // Search filter
                const matchesSearch = entity.name.toLowerCase().includes(query) ||
                    (entity.description || '').toLowerCase().includes(query) ||
                    (entity.category || '').toLowerCase().includes(query);

                // Starred filter
                const matchesStarred = !showOnlyStarred || starredEntities.has(entity.id);

                return matchesSearch && matchesStarred;
            }});

            // Apply current sort
            if (currentSort === 's1') {{
                if (currentVersion === 'v3.0') {{
                    filteredEntities.sort((a, b) => (b.stage1_score || 0) - (a.stage1_score || 0));
                }} else {{
                    filteredEntities.sort((a, b) => (b.stage1_consolidated?.total || 0) - (a.stage1_consolidated?.total || 0));
                }}
            }} else if (currentSort === 's2') {{
                if (currentVersion === 'v3.0') {{
                    filteredEntities.sort((a, b) => (b.stage2_total || 0) - (a.stage2_total || 0));
                }} else {{
                    filteredEntities.sort((a, b) => (b.stage2_consolidated?.total || 0) - (a.stage2_consolidated?.total || 0));
                }}
            }} else if (currentSort === 'name') {{
                filteredEntities.sort((a, b) => a.name.localeCompare(b.name));
            }} else if (currentSort === 'category') {{
                filteredEntities.sort((a, b) => (a.category || '').localeCompare(b.category || ''));
            }}

            renderList();
        }}

        // Handle search
        function handleSearch(e) {{
            filterAndSort();
        }}

        // Handle sort
        function handleSort(e) {{
            const sortType = e.target.dataset.sort;
            if (!sortType) return; // Ignore clicks on non-sort buttons
            currentSort = sortType;

            document.querySelectorAll('.sort-btn[data-sort]').forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');

            filterAndSort();
        }}

        // Render entity list
        function renderList() {{
            const listEl = document.getElementById('entity-list');
            listEl.innerHTML = '';

            filteredEntities.forEach(entity => {{
                const div = document.createElement('div');
                div.className = 'entity-item';
                if (selectedEntity && selectedEntity.id === entity.id) {{
                    div.classList.add('selected');
                }}

                const s1Score = currentVersion === 'v3.0'
                    ? (entity.stage1_score || 0)
                    : (entity.stage1_consolidated?.total || 0);
                const s2Score = currentVersion === 'v3.0'
                    ? (entity.stage2_total || 0)
                    : (entity.stage2_consolidated?.total || 0);
                const starred = isStarred(entity.id);

                div.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div class="entity-name">${{entity.name}}</div>
                        <button class="star-btn ${{starred ? 'starred' : ''}}" onclick="toggleStar(${{entity.id}}, event)" title="${{starred ? 'Unstar' : 'Star'}}">
                            ${{starred ? '★' : '☆'}}
                        </button>
                    </div>
                    <div class="entity-meta">
                        <div class="entity-score">
                            <span class="score-badge score-s1">S1: ${{s1Score}}</span>
                        </div>
                        <div class="entity-score">
                            <span class="score-badge score-s2">S2: ${{s2Score}}</span>
                        </div>
                    </div>
                `;

                div.addEventListener('click', (e) => {{
                    if (!e.target.classList.contains('star-btn')) {{
                        selectEntity(entity);
                    }}
                }});
                listEl.appendChild(div);
            }});
        }}

        // Select entity
        function selectEntity(entity) {{
            selectedEntity = entity;
            renderList();
            renderDetail(entity);
            highlightNode(entity);
        }}

        // Render detail panel
        function renderDetail(entity) {{
            const detailPanel = document.getElementById('detail-panel');

            const s1Score = currentVersion === 'v3.0'
                ? (entity.stage1_score || 0)
                : (entity.stage1_consolidated?.total || 0);
            const s2Score = currentVersion === 'v3.0'
                ? (entity.stage2_total || 0)
                : (entity.stage2_consolidated?.total || 0);
            const starred = isStarred(entity.id);

            let html = `
                <div class="detail-header">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div class="detail-title">${{entity.name}}</div>
                        <button class="star-btn ${{starred ? 'starred' : ''}}" onclick="toggleStar(${{entity.id}})" title="${{starred ? 'Unstar' : 'Star'}}" style="font-size: 24px;">
                            ${{starred ? '★' : '☆'}}
                        </button>
                    </div>
                    <div class="detail-category">${{entity.category || 'Uncategorized'}}</div>
                    <div class="detail-scores">
                        <div class="score-box">
                            <div class="score-label">Stage 1</div>
                            <div class="score-value score-s1">${{s1Score}}</div>
                        </div>
                        <div class="score-box">
                            <div class="score-label">Stage 2</div>
                            <div class="score-value score-s2">${{s2Score}}</div>
                        </div>
                    </div>
                </div>

                <div class="detail-section">
                    <div class="section-title">Description</div>
                    <div class="section-content">${{entity.description || 'No description available'}}</div>
                </div>
            `;

            // Version-specific sections
            if (currentVersion === 'v3.1') {{
                // Show consolidated scores
                if (entity.stage1_consolidated) {{
                    const s1_rg = (entity.stage1_consolidated.reality_gap / 9 * 10).toFixed(1);
                    const s1_tp = (entity.stage1_consolidated.transformative_potential / 6 * 10).toFixed(1);
                    const s1_cm = (entity.stage1_consolidated.current_momentum / 12 * 10).toFixed(1);
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Stage 1 Consolidated</div>
                            <div class="scoring-grid">
                                <div class="score-row">
                                    <span class="score-name">Reality Gap</span>
                                    <div class="score-bar-container">
                                        <div class="score-bar" style="width: ${{(entity.stage1_consolidated.reality_gap / 9) * 100}}%"></div>
                                    </div>
                                    <span class="score-num">${{s1_rg}}</span>
                                </div>
                                <div class="score-row">
                                    <span class="score-name">Transformative Potential</span>
                                    <div class="score-bar-container">
                                        <div class="score-bar" style="width: ${{(entity.stage1_consolidated.transformative_potential / 6) * 100}}%"></div>
                                    </div>
                                    <span class="score-num">${{s1_tp}}</span>
                                </div>
                                <div class="score-row">
                                    <span class="score-name">Current Momentum</span>
                                    <div class="score-bar-container">
                                        <div class="score-bar" style="width: ${{(entity.stage1_consolidated.current_momentum / 12) * 100}}%"></div>
                                    </div>
                                    <span class="score-num">${{s1_cm}}</span>
                                </div>
                            </div>
                        </div>
                    `;
                }}

                if (entity.stage2_consolidated) {{
                    const s2_tp = (entity.stage2_consolidated.transformative_power / 25 * 10).toFixed(1);
                    const s2_sr = (entity.stage2_consolidated.systemic_risk / 25 * 10).toFixed(1);
                    const s2_le = (entity.stage2_consolidated.lockin_effects / 20 * 10).toFixed(1);
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Stage 2 Consolidated</div>
                            <div class="scoring-grid">
                                <div class="score-row">
                                    <span class="score-name">Transformative Power</span>
                                    <div class="score-bar-container">
                                        <div class="score-bar" style="width: ${{(entity.stage2_consolidated.transformative_power / 25) * 100}}%"></div>
                                    </div>
                                    <span class="score-num">${{s2_tp}}</span>
                                </div>
                                <div class="score-row">
                                    <span class="score-name">Systemic Risk</span>
                                    <div class="score-bar-container">
                                        <div class="score-bar" style="width: ${{(entity.stage2_consolidated.systemic_risk / 25) * 100}}%"></div>
                                    </div>
                                    <span class="score-num">${{s2_sr}}</span>
                                </div>
                                <div class="score-row">
                                    <span class="score-name">Lock-in Effects</span>
                                    <div class="score-bar-container">
                                        <div class="score-bar" style="width: ${{(entity.stage2_consolidated.lockin_effects / 20) * 100}}%"></div>
                                    </div>
                                    <span class="score-num">${{s2_le}}</span>
                                </div>
                            </div>
                        </div>
                    `;
                }}

                // Show expanded details
                if (entity.problems_solved) {{
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Problems Solved</div>
                            <div class="section-content">${{entity.problems_solved}}</div>
                        </div>
                    `;
                }}

                if (entity.why_new_different) {{
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Why New/Different</div>
                            <div class="section-content">${{entity.why_new_different}}</div>
                        </div>
                    `;
                }}

                if (entity.why_not_exists) {{
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Why Not Exists Yet</div>
                            <div class="section-content">${{entity.why_not_exists}}</div>
                        </div>
                    `;
                }}
            }} else {{
                // v3.0 - Show original 9+14 scores
                if (entity.scoring) {{
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Stage 1 Scoring (0-27)</div>
                            <div class="scoring-grid">
                    `;

                    const stage1Axes = [
                        'Non-existence', 'Plausibility', 'Design specificity',
                        'New action space', 'Roadmap clarity', 'Coordination gravity',
                        'Resource pull', 'Narrative centrality', 'Pre-real effects'
                    ];

                    stage1Axes.forEach(axis => {{
                        const score = entity.scoring[axis] || 0;
                        const normalized = (score / 3 * 10).toFixed(1);
                        html += `
                            <div class="score-row">
                                <span class="score-name">${{axis}}</span>
                                <div class="score-bar-container">
                                    <div class="score-bar" style="width: ${{(score / 3) * 100}}%"></div>
                                </div>
                                <span class="score-num">${{normalized}}</span>
                            </div>
                        `;
                    }});

                    html += `
                            </div>
                        </div>
                    `;
                }}

                if (entity.stage2_scores) {{
                    html += `
                        <div class="detail-section">
                            <div class="section-title">Stage 2 Impact Assessment (0-70)</div>
                            <div class="scoring-grid">
                    `;

                    const stage2Dims = [
                        'Capability Discontinuity', 'Cross-Domain Reach', 'Scalability',
                        'Autonomy', 'Composability', 'Feedback Intensity',
                        'Irreversibility', 'Power Concentration', 'Externality Magnitude',
                        'Misuse Asymmetry', 'Governance Lag', 'Narrative Lock-In',
                        'Path Dependency', 'Human Agency Impact'
                    ];

                    stage2Dims.forEach(dim => {{
                        const score = entity.stage2_scores[dim] || 0;
                        const normalized = (score / 5 * 10).toFixed(1);
                        html += `
                            <div class="score-row">
                                <span class="score-name">${{dim}}</span>
                                <div class="score-bar-container">
                                    <div class="score-bar" style="width: ${{(score / 5) * 100}}%"></div>
                                </div>
                                <span class="score-num">${{normalized}}</span>
                            </div>
                        `;
                    }});

                    html += `
                            </div>
                        </div>
                    `;
                }}
            }}

            // Source info
            if (entity.source_file) {{
                html += `
                    <div class="detail-section">
                        <div class="section-title">Source</div>
                        <div class="section-content">${{entity.source_file}}</div>
                    </div>
                `;
            }}

            html += `
                <button class="open-modal-btn" onclick="openModal()">Open in Larger View</button>
            `;

            detailPanel.innerHTML = html;
        }}

        // Open modal
        function openModal() {{
            const modal = document.getElementById('modal');
            const modalBody = document.getElementById('modal-body');
            modalBody.innerHTML = document.getElementById('detail-panel').innerHTML;
            modal.style.display = 'flex';
        }}

        // Close modal
        function closeModal() {{
            document.getElementById('modal').style.display = 'none';
        }}

        // Show methodology modal
        function showMethodology() {{
            document.getElementById('methodology-modal').style.display = 'flex';
        }}

        // Close methodology modal
        function closeMethodology() {{
            document.getElementById('methodology-modal').style.display = 'none';
        }}

        // Switch methodology tabs
        function showMethodTab(tab) {{
            document.querySelectorAll('.method-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.method-content').forEach(c => c.classList.remove('active'));

            if (tab === 'v30') {{
                document.querySelector('.method-tab:first-child').classList.add('active');
                document.getElementById('method-v30').classList.add('active');
            }} else {{
                document.querySelector('.method-tab:last-child').classList.add('active');
                document.getElementById('method-v31').classList.add('active');
            }}
        }}

        // Render visualization
        function renderVisualization() {{
            const container = document.getElementById('viz-container');
            container.innerHTML = '';

            const width = container.clientWidth;
            const height = container.clientHeight;
            const centerX = width / 2;
            const centerY = height / 2;

            // Use cluster data if available (v3.1)
            let vizData = [];
            let clusterIds = new Set();
            if (currentVersion === 'v3.1' && currentData.clusters) {{
                // Group entities by cluster
                entities.forEach(e => {{
                    if (e.cluster_id !== undefined) {{
                        clusterIds.add(e.cluster_id);
                        vizData.push({{
                            entity: e,
                            cluster: e.cluster_id,
                            clusterName: e.cluster_name || `Cluster ${{e.cluster_id}}`
                        }});
                    }}
                }});
            }} else {{
                // Simple layout for v3.0
                vizData = entities.map((e, i) => ({{
                    entity: e,
                    cluster: i % 12,
                    clusterName: 'Entity'
                }}));
                for (let i = 0; i < 12; i++) clusterIds.add(i);
            }}

            // Calculate cluster center positions in a circle
            const numClusters = clusterIds.size;
            const clusterCenters = {{}};
            const radius = Math.min(width, height) * 0.35;
            Array.from(clusterIds).sort((a, b) => a - b).forEach((cid, i) => {{
                const angle = (2 * Math.PI * i / numClusters) - Math.PI / 2;
                clusterCenters[cid] = {{
                    x: centerX + radius * Math.cos(angle),
                    y: centerY + radius * Math.sin(angle)
                }};
            }});

            const svg = d3.select(container)
                .append('svg')
                .attr('width', width)
                .attr('height', height);

            // Add zoom behavior
            const g = svg.append('g');

            const zoom = d3.zoom()
                .scaleExtent([0.2, 5])
                .on('zoom', (event) => {{
                    g.attr('transform', event.transform);
                }});

            svg.call(zoom);

            // Start zoomed out to see all clusters
            svg.call(zoom.transform, d3.zoomIdentity.translate(centerX, centerY).scale(0.7).translate(-centerX, -centerY));

            // Color scale with more distinct colors for 20 clusters
            const colorScale = d3.scaleOrdinal()
                .domain(Array.from(clusterIds))
                .range([
                    '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
                    '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe',
                    '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000',
                    '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080'
                ]);

            // Create simulation with cluster-based forces
            const simulation = d3.forceSimulation(vizData)
                .force('charge', d3.forceManyBody().strength(-30))
                .force('collision', d3.forceCollide().radius(10))
                .force('x', d3.forceX(d => clusterCenters[d.cluster]?.x || centerX).strength(0.3))
                .force('y', d3.forceY(d => clusterCenters[d.cluster]?.y || centerY).strength(0.3));

            // Draw nodes
            const nodes = g.selectAll('circle.node')
                .data(vizData)
                .enter()
                .append('circle')
                .attr('class', 'node')
                .attr('r', d => {{
                    const s2 = currentVersion === 'v3.0'
                        ? (d.entity.stage2_total || 0)
                        : (d.entity.stage2_consolidated?.total || 0);
                    return 4 + (s2 / 70) * 10;
                }})
                .attr('fill', d => colorScale(d.cluster))
                .attr('stroke', '#fff')
                .attr('stroke-width', 0.5)
                .attr('opacity', 0.85)
                .style('cursor', 'pointer')
                .on('click', (event, d) => selectEntity(d.entity));

            // Add tooltips
            nodes.append('title')
                .text(d => `${{d.entity.name}}\n${{d.clusterName}}`);

            // Draw cluster labels ON TOP of nodes (drawn after nodes so they appear above)
            const labelRadius = radius + 100;
            Array.from(clusterIds).sort((a, b) => a - b).forEach((cid, i) => {{
                const angle = (2 * Math.PI * i / numClusters) - Math.PI / 2;
                const labelX = centerX + labelRadius * Math.cos(angle);
                const labelY = centerY + labelRadius * Math.sin(angle);
                const clusterName = currentData.clusters?.[cid]?.name || `Cluster ${{cid}}`;

                let rotation = 0;
                const angleDeg = (angle * 180 / Math.PI + 360) % 360;
                if (angleDeg > 90 && angleDeg < 270) {{
                    rotation = angleDeg + 180;
                }} else {{
                    rotation = angleDeg;
                }}

                const labelGroup = g.append('g')
                    .attr('transform', `translate(${{labelX}}, ${{labelY}}) rotate(${{rotation}})`);

                const bgRect = labelGroup.append('rect')
                    .attr('fill', colorScale(cid))
                    .attr('rx', 4)
                    .attr('ry', 4)
                    .attr('opacity', 0.95);

                const text = labelGroup.append('text')
                    .attr('text-anchor', 'middle')
                    .attr('dominant-baseline', 'middle')
                    .attr('fill', '#ffffff')
                    .attr('font-size', '11px')
                    .attr('font-weight', '700')
                    .text(clusterName);

                const bbox = text.node().getBBox();
                bgRect
                    .attr('x', bbox.x - 6)
                    .attr('y', bbox.y - 3)
                    .attr('width', bbox.width + 12)
                    .attr('height', bbox.height + 6);
            }});

            // Update positions
            simulation.on('tick', () => {{
                nodes
                    .attr('cx', d => d.x)
                    .attr('cy', d => d.y);
            }});

            // Store for highlighting and zoom control
            window.vizNodes = nodes;
            window.vizZoom = zoom;
            window.vizSvg = svg;
            window.vizCenterX = centerX;
            window.vizCenterY = centerY;
        }}

        // Zoom control functions
        function zoomIn() {{
            if (window.vizSvg && window.vizZoom) {{
                window.vizSvg.transition().duration(300).call(window.vizZoom.scaleBy, 1.5);
            }}
        }}

        function zoomOut() {{
            if (window.vizSvg && window.vizZoom) {{
                window.vizSvg.transition().duration(300).call(window.vizZoom.scaleBy, 0.67);
            }}
        }}

        function zoomReset() {{
            if (window.vizSvg && window.vizZoom) {{
                const cx = window.vizCenterX;
                const cy = window.vizCenterY;
                window.vizSvg.transition().duration(500).call(
                    window.vizZoom.transform,
                    d3.zoomIdentity.translate(cx, cy).scale(0.7).translate(-cx, -cy)
                );
            }}
        }}

        // Highlight selected node
        function highlightNode(entity) {{
            if (window.vizNodes) {{
                window.vizNodes.classed('selected', d => d.entity.id === entity.id);
            }}
        }}

        // Initialize on load
        init();
    </script>
</body>
</html>
"""

    # Embed data in HTML
    html = html.replace("__V3_0_DATA_PLACEHOLDER__", json.dumps(v3_0_data))
    html = html.replace("__V3_1_DATA_PLACEHOLDER__", json.dumps(v3_1_data))

    return html


def main():
    """Main execution."""
    print("=" * 80)
    print("Creating v3.1 Dashboard with Version Switcher")
    print("=" * 80)
    print()

    # Load data
    v3_0_data, v3_1_data = load_data()

    # Create HTML
    html = create_dashboard_html(v3_0_data, v3_1_data)

    # Save
    output_path = Path(CONFIG["output_html"])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print()
    print("=" * 80)
    print("DASHBOARD CREATED")
    print("=" * 80)
    print(f"✓ Saved to: {output_path}")
    print()
    print("Features:")
    print("  • Version dropdown to switch between v3.0 and v3.1")
    print("  • v3.0: Original 9+14 scoring display")
    print("  • v3.1: Consolidated 3+3 scores + expanded details")
    print("  • Cluster visualization based on v3.1 analysis")
    print("  • Search, sort, and filter capabilities")
    print("  • Modal view for detailed reading")
    print()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate v3 interactive HTML dashboard for hyper-entities.
Pure Python, no API calls. Outputs self-contained HTML.

Input:
  - results/v3/curated.json (tier1 + tier2 entities with all data)
  - results/v3/scatter_data.json (pre-computed scatter plot data)

Output:
  - results/v3/dashboard.html
"""

import json
from pathlib import Path
from collections import Counter

CURATED_PATH = Path("results/v3/curated.json")
SCATTER_PATH = Path("results/v3/scatter_data.json")
OUTPUT_PATH = Path("results/v3/dashboard.html")

# Bottleneck colors
BOTTLENECK_COLORS = {
    "Physics": "#ef4444",
    "Engineering": "#f97316",
    "Funding": "#22c55e",
    "Regulation": "#3b82f6",
    "Coordination": "#a855f7",
    "Social Acceptance": "#ec4899",
}

# Action badge colors
ACTION_COLORS = {
    "Fund": "#22c55e",
    "Build": "#f97316",
    "Research": "#3b82f6",
    "Advocate": "#ec4899",
    "Convene": "#a855f7",
}

# Group colors (12 groups)
GROUP_COLORS = {
    "AI Safety, Alignment & Governance": "#ef4444",
    "AI-Mediated Deliberation & Collective Intelligence": "#f97316",
    "Biotech, Medicine & Life Extension": "#eab308",
    "Decentralized & Democratic Institutions": "#22c55e",
    "Ecological & Regenerative Systems": "#14b8a6",
    "Economic Systems & Resource Distribution": "#06b6d4",
    "Education, Development & Human Flourishing": "#3b82f6",
    "Energy, Environment & Planetary Systems": "#6366f1",
    "International Governance & Coordination": "#8b5cf6",
    "Nanotechnology & Advanced Manufacturing": "#a855f7",
    "Neurotechnology & Brain-Computer Interfaces": "#d946ef",
    "Scientific Research & Knowledge Infrastructure": "#ec4899",
}


def load_data():
    print("Loading curated.json...")
    with open(CURATED_PATH) as f:
        curated = json.load(f)
    tier1 = curated["tier1"]
    tier2 = curated["tier2"]
    all_entities = tier1 + tier2
    print(f"  {len(tier1)} tier1, {len(tier2)} tier2, {len(all_entities)} total")

    print("Loading scatter_data.json...")
    with open(SCATTER_PATH) as f:
        scatter = json.load(f)
    print(f"  {len(scatter)} scatter points")

    return curated, scatter, all_entities


def compute_stats(all_entities, scatter):
    tier1_count = sum(1 for e in all_entities if e.get("tier") == 1)
    tier2_count = sum(1 for e in all_entities if e.get("tier") == 2)
    total = len(all_entities)

    dacc_scores = [e.get("scores", {}).get("dacc", {}).get("total", 0) for e in all_entities]
    trans_scores = [e.get("scores", {}).get("transformative", {}).get("score", 0) for e in all_entities]
    avg_dacc = sum(dacc_scores) / len(dacc_scores) if dacc_scores else 0
    avg_trans = sum(trans_scores) / len(trans_scores) if trans_scores else 0

    bottlenecks = [s["bottleneck"] for s in scatter]
    actions = [s["action"] for s in scatter]
    most_common_bottleneck = Counter(bottlenecks).most_common(1)[0][0] if bottlenecks else "N/A"
    most_common_action = Counter(actions).most_common(1)[0][0] if actions else "N/A"

    return {
        "total": total,
        "tier1": tier1_count,
        "tier2": tier2_count,
        "avg_dacc": round(avg_dacc, 1),
        "avg_trans": round(avg_trans, 1),
        "most_common_bottleneck": most_common_bottleneck,
        "most_common_action": most_common_action,
    }


def escape_js(s):
    """Escape a string for safe embedding in JavaScript."""
    if not s:
        return ""
    return (
        s.replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("<", "\\x3c")
        .replace(">", "\\x3e")
    )


def generate_html(curated, scatter, all_entities, stats):
    # Prepare entity data for JS embedding
    entities_js = json.dumps(all_entities, ensure_ascii=False)
    scatter_js = json.dumps(scatter, ensure_ascii=False)
    bottleneck_colors_js = json.dumps(BOTTLENECK_COLORS)
    action_colors_js = json.dumps(ACTION_COLORS)
    group_colors_js = json.dumps(GROUP_COLORS)

    # Extract unique groups, bottlenecks, actions for filters
    groups = sorted(set(s["group"] for s in scatter))
    bottlenecks = sorted(set(s["bottleneck"] for s in scatter))
    actions = sorted(set(s["action"] for s in scatter))

    group_checkboxes = "\n".join(
        f'                        <label class="filter-checkbox"><input type="checkbox" value="{g}" checked onchange="applyFilters()"><span class="filter-label">{g}</span></label>'
        for g in groups
    )

    bottleneck_checkboxes = "\n".join(
        f'                        <label class="filter-checkbox"><input type="checkbox" data-filter="bottleneck" value="{b}" checked onchange="applyFilters()"><span class="filter-dot" style="background:{BOTTLENECK_COLORS.get(b, "#888")};"></span><span class="filter-label">{b}</span></label>'
        for b in bottlenecks
    )

    action_checkboxes = "\n".join(
        f'                        <label class="filter-checkbox"><input type="checkbox" data-filter="action" value="{a}" checked onchange="applyFilters()"><span class="filter-dot" style="background:{ACTION_COLORS.get(a, "#888")};"></span><span class="filter-label">{a}</span></label>'
        for a in actions
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hyper-Entities v3 Dashboard</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0a0e27;
            color: #e0e6f0;
            overflow: hidden;
        }}

        /* Header */
        .header {{
            background: linear-gradient(135deg, #1a1f3a 0%, #2a2f4a 100%);
            padding: 14px 24px;
            border-bottom: 2px solid #3a4f7a;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .header-left {{
            display: flex;
            align-items: center;
            gap: 24px;
        }}

        h1 {{
            font-size: 22px;
            font-weight: 600;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .view-toggle {{
            display: flex;
            gap: 4px;
            background: #1e293b;
            border-radius: 6px;
            padding: 3px;
        }}

        .view-toggle button {{
            padding: 6px 14px;
            background: none;
            border: none;
            border-radius: 4px;
            color: #94a3b8;
            cursor: pointer;
            font-size: 13px;
            transition: all 0.2s;
        }}

        .view-toggle button.active {{
            background: #60a5fa;
            color: #fff;
        }}

        .view-toggle button:hover:not(.active) {{
            color: #e0e6f0;
        }}

        .stats-bar {{
            display: flex;
            gap: 16px;
            font-size: 12px;
            color: #94a3b8;
        }}

        .stat {{ display: flex; align-items: center; gap: 4px; }}
        .stat strong {{ color: #60a5fa; }}

        /* Container */
        .container {{
            display: flex;
            height: calc(100vh - 56px);
        }}

        /* Left panel: filters */
        #filter-panel {{
            width: 260px;
            background: #0f1629;
            border-right: 2px solid #1e293b;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }}

        .filter-section {{
            padding: 12px 14px;
            border-bottom: 1px solid #1e293b;
        }}

        .filter-section-title {{
            font-size: 11px;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}

        .filter-checkbox {{
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 3px 0;
            font-size: 12px;
            color: #cbd5e1;
            cursor: pointer;
        }}

        .filter-checkbox input {{ cursor: pointer; accent-color: #60a5fa; }}

        .filter-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
        }}

        .filter-label {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

        .tier-buttons {{
            display: flex;
            gap: 4px;
        }}

        .tier-btn {{
            flex: 1;
            padding: 6px 8px;
            background: #1e293b;
            border: 1px solid #3a4f7a;
            border-radius: 4px;
            color: #94a3b8;
            cursor: pointer;
            font-size: 11px;
            text-align: center;
            transition: all 0.2s;
        }}

        .tier-btn:hover {{ background: #2a3f5a; color: #e0e6f0; }}
        .tier-btn.active {{ background: #60a5fa; border-color: #60a5fa; color: #fff; }}

        #search {{
            width: 100%;
            padding: 8px 10px;
            background: #0a0e27;
            border: 1px solid #3a4f7a;
            border-radius: 6px;
            color: #e0e6f0;
            font-size: 13px;
        }}
        #search:focus {{ outline: none; border-color: #60a5fa; }}

        .select-all-row {{
            display: flex;
            gap: 8px;
            margin-bottom: 6px;
        }}
        .select-all-btn {{
            font-size: 11px;
            color: #60a5fa;
            cursor: pointer;
            background: none;
            border: none;
            padding: 0;
        }}
        .select-all-btn:hover {{ text-decoration: underline; }}

        /* Main viz area */
        #main-area {{
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
        }}

        #viz-container {{
            flex: 1;
            background: #0f1629;
            position: relative;
        }}

        #action-view {{
            flex: 1;
            background: #0f1629;
            overflow-y: auto;
            padding: 20px;
            display: none;
        }}

        .action-group {{
            margin-bottom: 24px;
        }}

        .action-group-title {{
            font-size: 16px;
            font-weight: 600;
            padding: 10px 14px;
            border-radius: 8px 8px 0 0;
            margin-bottom: 2px;
        }}

        .action-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 10px;
        }}

        .action-card {{
            background: #1a1f3a;
            border: 1px solid #2a2f4a;
            border-radius: 6px;
            padding: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .action-card:hover {{
            background: #1e2a4a;
            border-color: #3a5f8a;
            transform: translateY(-2px);
        }}

        .action-card-name {{
            font-size: 13px;
            font-weight: 500;
            color: #e0e6f0;
            margin-bottom: 4px;
        }}

        .action-card-meta {{
            font-size: 11px;
            color: #64748b;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .action-card-desc {{
            font-size: 11px;
            color: #94a3b8;
            margin-top: 6px;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        /* Zoom controls */
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

        .zoom-btn:hover {{ background: #2a3f5a; border-color: #60a5fa; }}

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

        /* Legend */
        .legend {{
            position: absolute;
            bottom: 10px;
            right: 10px;
            background: rgba(15, 22, 41, 0.9);
            border: 1px solid #2a2f4a;
            border-radius: 6px;
            padding: 10px 12px;
            font-size: 11px;
            z-index: 50;
        }}

        .legend-title {{
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 6px;
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 2px 0;
            color: #cbd5e1;
        }}

        .legend-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            flex-shrink: 0;
        }}

        .legend-shape {{
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 2px 0;
            color: #cbd5e1;
            margin-top: 6px;
        }}

        /* Detail panel */
        #detail-panel {{
            width: 420px;
            background: #0f1629;
            border-left: 2px solid #1e293b;
            overflow-y: auto;
            padding: 24px;
            display: none;
        }}

        #detail-panel.open {{ display: block; }}

        .detail-close {{
            float: right;
            background: none;
            border: none;
            color: #64748b;
            font-size: 20px;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 4px;
        }}
        .detail-close:hover {{ background: #1a1f3a; color: #e0e6f0; }}

        .detail-header {{ margin-bottom: 16px; }}

        .detail-title {{
            font-size: 20px;
            font-weight: 600;
            color: #e0e6f0;
            margin-bottom: 6px;
        }}

        .detail-group {{
            font-size: 12px;
            color: #64748b;
            margin-bottom: 4px;
        }}

        .detail-badges {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }}

        .badge {{
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 500;
        }}

        .badge-tier1 {{ background: #60a5fa22; color: #60a5fa; border: 1px solid #60a5fa44; }}
        .badge-tier2 {{ background: #94a3b822; color: #94a3b8; border: 1px solid #94a3b844; }}

        .detail-scores {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 16px;
        }}

        .score-box {{
            padding: 10px;
            background: #1a1f3a;
            border: 1px solid #2a2f4a;
            border-radius: 6px;
            text-align: center;
        }}

        .score-label {{
            font-size: 10px;
            color: #64748b;
            margin-bottom: 2px;
            text-transform: uppercase;
        }}

        .score-value {{
            font-size: 18px;
            font-weight: 600;
        }}

        .detail-section {{
            margin-bottom: 18px;
        }}

        .section-title {{
            font-size: 12px;
            font-weight: 600;
            color: #60a5fa;
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .section-content {{
            font-size: 13px;
            line-height: 1.6;
            color: #cbd5e1;
        }}

        /* d/acc bar chart */
        .dacc-grid {{
            display: grid;
            gap: 6px;
        }}

        .dacc-row {{
            display: grid;
            grid-template-columns: 100px 1fr 30px;
            align-items: center;
            gap: 8px;
            padding: 5px 8px;
            background: #1a1f3a;
            border-radius: 4px;
            font-size: 12px;
        }}

        .dacc-name {{ color: #94a3b8; }}

        .dacc-bar-bg {{
            height: 6px;
            background: #1e293b;
            border-radius: 3px;
            overflow: hidden;
        }}

        .dacc-bar {{
            height: 100%;
            border-radius: 3px;
            transition: width 0.3s;
        }}

        .dacc-num {{ color: #e0e6f0; font-weight: 500; text-align: right; }}

        /* Orgs list */
        .org-item {{
            display: flex;
            gap: 8px;
            padding: 6px 0;
            border-bottom: 1px solid #1e293b;
            font-size: 12px;
        }}

        .org-item:last-child {{ border-bottom: none; }}

        .org-name {{
            color: #60a5fa;
            font-weight: 500;
        }}

        .org-name a {{ color: #60a5fa; text-decoration: none; }}
        .org-name a:hover {{ text-decoration: underline; }}

        .org-role {{ color: #94a3b8; }}

        /* Source quote */
        .source-quote {{
            background: #1a1f3a;
            border-left: 3px solid #60a5fa;
            padding: 10px 14px;
            border-radius: 0 6px 6px 0;
            font-size: 12px;
            line-height: 1.5;
            color: #94a3b8;
            font-style: italic;
        }}

        /* Action badge */
        .action-badge {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
        }}

        /* Methodology modal */
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

        .modal.open {{ display: flex; }}

        .modal-content {{
            background: #0f1629;
            border: 2px solid #3a4f7a;
            border-radius: 12px;
            max-width: 800px;
            max-height: 85vh;
            overflow-y: auto;
            padding: 30px;
            position: relative;
        }}

        .modal-close {{
            position: absolute;
            top: 12px;
            right: 12px;
            font-size: 24px;
            color: #94a3b8;
            cursor: pointer;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            background: none;
            border: none;
        }}

        .modal-close:hover {{ background: #1a1f3a; color: #e0e6f0; }}

        .modal h2 {{ font-size: 22px; color: #e0e6f0; margin-bottom: 16px; }}
        .modal h3 {{ font-size: 16px; color: #60a5fa; margin: 16px 0 8px; }}
        .modal p {{ font-size: 14px; line-height: 1.6; color: #cbd5e1; margin-bottom: 10px; }}
        .modal ul {{ margin-left: 20px; margin-bottom: 10px; }}
        .modal li {{ font-size: 13px; line-height: 1.6; color: #cbd5e1; margin-bottom: 4px; }}
        .modal table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        .modal th {{ background: #1a1f3a; padding: 8px 12px; text-align: left; font-size: 12px; color: #94a3b8; border: 1px solid #2a2f4a; }}
        .modal td {{ padding: 8px 12px; font-size: 12px; color: #cbd5e1; border: 1px solid #2a2f4a; }}

        /* Node styles */
        .node {{ cursor: pointer; transition: opacity 0.2s; }}
        .node:hover {{ stroke: #fff; stroke-width: 2px; }}
        .node.selected {{ stroke: #60a5fa; stroke-width: 3px; }}
        .node.dimmed {{ opacity: 0.15; }}

        /* Tooltip */
        .tooltip {{
            position: absolute;
            background: #1a1f3a;
            border: 1px solid #3a4f7a;
            border-radius: 8px;
            padding: 12px;
            font-size: 12px;
            pointer-events: none;
            z-index: 200;
            max-width: 320px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }}

        .tooltip-name {{ font-weight: 600; color: #e0e6f0; margin-bottom: 4px; font-size: 13px; }}
        .tooltip-group {{ color: #64748b; margin-bottom: 6px; }}
        .tooltip-scores {{ display: flex; gap: 10px; margin-bottom: 6px; }}
        .tooltip-score {{ display: flex; flex-direction: column; align-items: center; }}
        .tooltip-score-val {{ font-weight: 600; font-size: 14px; }}
        .tooltip-score-label {{ font-size: 10px; color: #64748b; }}
        .tooltip-action {{ margin-top: 4px; font-size: 11px; }}

        /* Scrollbar */
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: #0a0e27; }}
        ::-webkit-scrollbar-thumb {{ background: #3a4f7a; border-radius: 4px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #4a5f8a; }}

        .empty-detail {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: #64748b;
            font-size: 14px;
            text-align: center;
            padding: 40px;
        }}

        .info-btn {{
            padding: 6px 12px;
            background: #1e293b;
            border: 1px solid #3a4f7a;
            border-radius: 4px;
            color: #94a3b8;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
        }}
        .info-btn:hover {{ background: #2a3f5a; color: #e0e6f0; }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <h1>Hyper-Entities v3</h1>
            <div class="view-toggle">
                <button class="active" onclick="switchView('scatter')">Scatter Plot</button>
                <button onclick="switchView('action')">What Can I Do?</button>
            </div>
        </div>
        <div class="stats-bar">
            <div class="stat"><span>Total:</span> <strong>{stats['total']}</strong></div>
            <div class="stat"><span>Tier 1:</span> <strong>{stats['tier1']}</strong></div>
            <div class="stat"><span>Tier 2:</span> <strong>{stats['tier2']}</strong></div>
            <div class="stat"><span>Avg d/acc:</span> <strong>{stats['avg_dacc']}/20</strong></div>
            <div class="stat"><span>Avg Transform:</span> <strong>{stats['avg_trans']}/5</strong></div>
            <div class="stat"><span>Top Bottleneck:</span> <strong>{stats['most_common_bottleneck']}</strong></div>
            <div class="stat"><span>Top Action:</span> <strong>{stats['most_common_action']}</strong></div>
            <button class="info-btn" onclick="openMethodology()">Methodology</button>
        </div>
    </div>

    <div class="container">
        <!-- Filter panel -->
        <div id="filter-panel">
            <div class="filter-section">
                <div class="filter-section-title">Search</div>
                <input type="text" id="search" placeholder="Search entities..." oninput="applyFilters()">
            </div>

            <div class="filter-section">
                <div class="filter-section-title">Tier</div>
                <div class="tier-buttons">
                    <button class="tier-btn active" data-tier="all" onclick="setTier(this)">All</button>
                    <button class="tier-btn" data-tier="1" onclick="setTier(this)">Tier 1 ({stats['tier1']})</button>
                    <button class="tier-btn" data-tier="2" onclick="setTier(this)">Tier 2 ({stats['tier2']})</button>
                </div>
            </div>

            <div class="filter-section">
                <div class="filter-section-title">Bottleneck</div>
                <div class="select-all-row">
                    <button class="select-all-btn" onclick="toggleAllCheckboxes('bottleneck', true)">All</button>
                    <button class="select-all-btn" onclick="toggleAllCheckboxes('bottleneck', false)">None</button>
                </div>
{bottleneck_checkboxes}
            </div>

            <div class="filter-section">
                <div class="filter-section-title">Action</div>
                <div class="select-all-row">
                    <button class="select-all-btn" onclick="toggleAllCheckboxes('action', true)">All</button>
                    <button class="select-all-btn" onclick="toggleAllCheckboxes('action', false)">None</button>
                </div>
{action_checkboxes}
            </div>

            <div class="filter-section">
                <div class="filter-section-title">Group</div>
                <div class="select-all-row">
                    <button class="select-all-btn" onclick="toggleAllCheckboxes('group', true)">All</button>
                    <button class="select-all-btn" onclick="toggleAllCheckboxes('group', false)">None</button>
                </div>
{group_checkboxes}
            </div>
        </div>

        <!-- Main area -->
        <div id="main-area">
            <div id="viz-container">
                <div class="zoom-controls">
                    <button class="zoom-btn" onclick="zoomIn()">+</button>
                    <button class="zoom-btn" onclick="zoomOut()">-</button>
                    <button class="zoom-btn" onclick="zoomReset()" style="font-size:12px;">R</button>
                </div>
                <div class="zoom-hint">Scroll to zoom, drag to pan</div>
                <div class="legend">
                    <div class="legend-title">Bottleneck Color</div>
                    <div class="legend-item"><span class="legend-dot" style="background:#ef4444;"></span> Physics</div>
                    <div class="legend-item"><span class="legend-dot" style="background:#f97316;"></span> Engineering</div>
                    <div class="legend-item"><span class="legend-dot" style="background:#22c55e;"></span> Funding</div>
                    <div class="legend-item"><span class="legend-dot" style="background:#3b82f6;"></span> Regulation</div>
                    <div class="legend-item"><span class="legend-dot" style="background:#a855f7;"></span> Coordination</div>
                    <div class="legend-item"><span class="legend-dot" style="background:#ec4899;"></span> Social Acceptance</div>
                    <div style="margin-top:8px;">
                        <div class="legend-title">Tier</div>
                        <div class="legend-item"><svg width="14" height="14"><circle cx="7" cy="7" r="6" fill="#60a5fa" opacity="0.8"/></svg> Tier 1 (large)</div>
                        <div class="legend-item"><svg width="14" height="14"><circle cx="7" cy="7" r="4" fill="none" stroke="#94a3b8" stroke-width="1.5"/></svg> Tier 2 (hollow)</div>
                    </div>
                </div>
            </div>
            <div id="action-view"></div>
        </div>

        <!-- Detail panel -->
        <div id="detail-panel">
            <div class="empty-detail">Click an entity on the scatter plot to view details</div>
        </div>
    </div>

    <!-- Methodology Modal -->
    <div class="modal" id="methodology-modal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeMethodology()">&times;</button>
            <h2>v3 Scoring Methodology</h2>

            <h3>Pipeline Overview</h3>
            <p>The v3 pipeline extracts hyper-entities from 109 foresight sources (podcasts, world-gallery scenarios, reports), then scores them across multiple dimensions using Claude-based assessment.</p>

            <h3>d/acc Values Alignment (0-20)</h3>
            <p>Based on Vitalik Buterin's d/acc framework. Four dimensions, each scored 0-5:</p>
            <table>
                <tr><th>Dimension</th><th>What it measures</th></tr>
                <tr><td>Democratic (0-5)</td><td>Does the entity distribute decision-making power broadly?</td></tr>
                <tr><td>Decentralized (0-5)</td><td>Does the entity reduce single points of failure or control?</td></tr>
                <tr><td>Defensive (0-5)</td><td>Does the entity protect against misuse, attacks, or concentration of power?</td></tr>
                <tr><td>Differential (0-5)</td><td>Does the entity accelerate defense faster than offense?</td></tr>
            </table>

            <h3>Transformative Potential (0-5)</h3>
            <p>How fundamentally could this entity reshape its domain if fully realized? Score of 5 indicates civilizational-level transformation.</p>

            <h3>Readiness Bottleneck</h3>
            <p>The primary barrier to the entity becoming real:</p>
            <ul>
                <li><strong>Physics</strong> - Fundamental science not yet understood</li>
                <li><strong>Engineering</strong> - Science known, engineering challenges remain</li>
                <li><strong>Funding</strong> - Technically feasible, needs capital</li>
                <li><strong>Regulation</strong> - Technology exists, regulatory barriers</li>
                <li><strong>Coordination</strong> - Needs multi-stakeholder alignment</li>
                <li><strong>Social Acceptance</strong> - Public perception/adoption barrier</li>
            </ul>

            <h3>What To Do Now (Action)</h3>
            <p>The most impactful near-term action for advancing the entity:</p>
            <ul>
                <li><strong>Fund</strong> - Direct capital to existing efforts</li>
                <li><strong>Build</strong> - Start building prototypes/implementations</li>
                <li><strong>Research</strong> - Invest in foundational research</li>
                <li><strong>Advocate</strong> - Build public support and awareness</li>
                <li><strong>Convene</strong> - Bring stakeholders together</li>
            </ul>

            <h3>Tiering</h3>
            <p><strong>Tier 1</strong> ({stats['tier1']} entities): Composite score >= 18, representing the most promising and well-aligned hyper-entities.</p>
            <p><strong>Tier 2</strong> ({stats['tier2']} entities): All remaining entities that passed earlier filtering stages.</p>

            <h3>Data Sources</h3>
            <p>109 sources across podcast transcripts, Existential Hope world-gallery scenarios, AI pathways documents, and hope-themed Twitter/X threads.</p>
        </div>
    </div>

    <!-- Tooltip -->
    <div class="tooltip" id="tooltip" style="display:none;"></div>

    <script>
    // Data
    const allEntities = {entities_js};
    const scatterData = {scatter_js};
    const bottleneckColors = {bottleneck_colors_js};
    const actionColors = {action_colors_js};
    const groupColors = {group_colors_js};

    // Build lookup: name -> full entity
    const entityByName = {{}};
    allEntities.forEach(e => {{ entityByName[e.name] = e; }});

    // State
    let currentView = 'scatter';
    let selectedTier = 'all';
    let selectedEntity = null;
    let svg, g, xScale, yScale, zoom;

    // Initialize
    document.addEventListener('DOMContentLoaded', () => {{
        initScatter();
        applyFilters();
    }});

    // ---- View switching ----
    function switchView(view) {{
        currentView = view;
        document.querySelectorAll('.view-toggle button').forEach(b => b.classList.remove('active'));
        document.querySelector(`.view-toggle button[onclick="switchView('${{view}}')"]`).classList.add('active');

        document.getElementById('viz-container').style.display = view === 'scatter' ? 'block' : 'none';
        document.getElementById('action-view').style.display = view === 'action' ? 'block' : 'none';

        if (view === 'action') {{
            renderActionView();
        }}
    }}

    // ---- Filters ----
    function setTier(btn) {{
        document.querySelectorAll('.tier-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedTier = btn.dataset.tier;
        applyFilters();
    }}

    function toggleAllCheckboxes(filterType, checked) {{
        let selector;
        if (filterType === 'group') {{
            selector = '#filter-panel .filter-section:last-child input[type="checkbox"]';
        }} else {{
            selector = `input[data-filter="${{filterType}}"]`;
        }}
        document.querySelectorAll(selector).forEach(cb => {{ cb.checked = checked; }});
        applyFilters();
    }}

    function getActiveFilters() {{
        const search = (document.getElementById('search').value || '').toLowerCase();

        // Groups: checkboxes without data-filter
        const groupCheckboxes = document.querySelectorAll('#filter-panel .filter-section:last-child input[type="checkbox"]');
        const activeGroups = new Set();
        groupCheckboxes.forEach(cb => {{ if (cb.checked) activeGroups.add(cb.value); }});

        // Bottleneck
        const activeBottlenecks = new Set();
        document.querySelectorAll('input[data-filter="bottleneck"]').forEach(cb => {{
            if (cb.checked) activeBottlenecks.add(cb.value);
        }});

        // Action
        const activeActions = new Set();
        document.querySelectorAll('input[data-filter="action"]').forEach(cb => {{
            if (cb.checked) activeActions.add(cb.value);
        }});

        return {{ search, activeGroups, activeBottlenecks, activeActions }};
    }}

    function passesFilter(d, filters) {{
        // Search
        if (filters.search && !d.name.toLowerCase().includes(filters.search)) return false;
        // Tier
        if (selectedTier !== 'all' && d.tier !== parseInt(selectedTier)) return false;
        // Group
        if (!filters.activeGroups.has(d.group)) return false;
        // Bottleneck
        if (!filters.activeBottlenecks.has(d.bottleneck)) return false;
        // Action
        if (!filters.activeActions.has(d.action)) return false;
        return true;
    }}

    function applyFilters() {{
        const filters = getActiveFilters();
        const filtered = new Set();
        scatterData.forEach(d => {{
            if (passesFilter(d, filters)) filtered.add(d.name);
        }});

        // Update scatter dots
        if (svg) {{
            svg.selectAll('.node').classed('dimmed', d => !filtered.has(d.name));
        }}

        // Update action view if visible
        if (currentView === 'action') {{
            renderActionView();
        }}
    }}

    // ---- Scatter Plot ----
    function initScatter() {{
        const container = document.getElementById('viz-container');
        const width = container.clientWidth;
        const height = container.clientHeight;
        const margin = {{ top: 40, right: 40, bottom: 60, left: 60 }};
        const innerW = width - margin.left - margin.right;
        const innerH = height - margin.top - margin.bottom;

        xScale = d3.scaleLinear().domain([0, 20]).range([0, innerW]);
        yScale = d3.scaleLinear().domain([0, 5]).range([innerH, 0]);

        svg = d3.select('#viz-container').append('svg')
            .attr('width', width)
            .attr('height', height);

        // Zoom
        zoom = d3.zoom()
            .scaleExtent([0.5, 10])
            .on('zoom', (event) => {{ g.attr('transform', event.transform); }});
        svg.call(zoom);

        g = svg.append('g')
            .attr('transform', `translate(${{margin.left}},${{margin.top}})`);

        // Axes
        const xAxis = d3.axisBottom(xScale).ticks(10);
        const yAxis = d3.axisLeft(yScale).ticks(5);

        g.append('g')
            .attr('transform', `translate(0,${{innerH}})`)
            .call(xAxis)
            .attr('color', '#64748b')
            .selectAll('text').attr('fill', '#94a3b8');

        g.append('g')
            .call(yAxis)
            .attr('color', '#64748b')
            .selectAll('text').attr('fill', '#94a3b8');

        // Axis labels
        g.append('text')
            .attr('x', innerW / 2)
            .attr('y', innerH + 45)
            .attr('text-anchor', 'middle')
            .attr('fill', '#94a3b8')
            .attr('font-size', '13px')
            .text('d/acc Alignment Score (0-20)');

        g.append('text')
            .attr('transform', 'rotate(-90)')
            .attr('x', -innerH / 2)
            .attr('y', -45)
            .attr('text-anchor', 'middle')
            .attr('fill', '#94a3b8')
            .attr('font-size', '13px')
            .text('Transformative Potential (0-5)');

        // Grid lines
        g.append('g')
            .attr('class', 'grid')
            .selectAll('line')
            .data(d3.range(0, 21, 2))
            .join('line')
            .attr('x1', d => xScale(d)).attr('x2', d => xScale(d))
            .attr('y1', 0).attr('y2', innerH)
            .attr('stroke', '#1e293b').attr('stroke-dasharray', '2,4');

        g.append('g')
            .attr('class', 'grid')
            .selectAll('line')
            .data(d3.range(0, 6))
            .join('line')
            .attr('x1', 0).attr('x2', innerW)
            .attr('y1', d => yScale(d)).attr('y2', d => yScale(d))
            .attr('stroke', '#1e293b').attr('stroke-dasharray', '2,4');

        // Jitter to avoid overlapping dots
        const jitter = () => (Math.random() - 0.5) * 8;

        // Dots
        g.selectAll('.node')
            .data(scatterData)
            .join('circle')
            .attr('class', 'node')
            .attr('cx', d => xScale(d.dacc_total) + jitter())
            .attr('cy', d => yScale(d.transformative) + jitter())
            .attr('r', d => d.tier === 1 ? 8 : 4.5)
            .attr('fill', d => d.tier === 1 ? (bottleneckColors[d.bottleneck] || '#888') : 'none')
            .attr('stroke', d => bottleneckColors[d.bottleneck] || '#888')
            .attr('stroke-width', d => d.tier === 1 ? 0 : 1.5)
            .attr('opacity', d => d.tier === 1 ? 0.85 : 0.6)
            .on('mouseover', showTooltip)
            .on('mousemove', moveTooltip)
            .on('mouseout', hideTooltip)
            .on('click', (event, d) => {{
                selectEntity(d.name);
            }});
    }}

    // ---- Tooltip ----
    function showTooltip(event, d) {{
        const full = entityByName[d.name];
        const tooltip = document.getElementById('tooltip');
        const actionColor = actionColors[d.action] || '#888';
        tooltip.innerHTML = `
            <div class="tooltip-name">${{d.name}}</div>
            <div class="tooltip-group">${{d.group}}</div>
            <div class="tooltip-scores">
                <div class="tooltip-score">
                    <span class="tooltip-score-val" style="color:#34d399;">${{d.dacc_total}}</span>
                    <span class="tooltip-score-label">d/acc</span>
                </div>
                <div class="tooltip-score">
                    <span class="tooltip-score-val" style="color:#a78bfa;">${{d.transformative}}</span>
                    <span class="tooltip-score-label">Transform</span>
                </div>
            </div>
            <div class="tooltip-action">
                <span style="color:${{bottleneckColors[d.bottleneck] || '#888'}};">Bottleneck: ${{d.bottleneck}}</span>
                &nbsp;|&nbsp;
                <span style="color:${{actionColor}};">Action: ${{d.action}}</span>
            </div>
        `;
        tooltip.style.display = 'block';
        moveTooltip(event);
    }}

    function moveTooltip(event) {{
        const tooltip = document.getElementById('tooltip');
        const x = event.pageX + 12;
        const y = event.pageY - 10;
        tooltip.style.left = x + 'px';
        tooltip.style.top = y + 'px';
    }}

    function hideTooltip() {{
        document.getElementById('tooltip').style.display = 'none';
    }}

    // ---- Zoom ----
    function zoomIn() {{ svg.transition().duration(300).call(zoom.scaleBy, 1.5); }}
    function zoomOut() {{ svg.transition().duration(300).call(zoom.scaleBy, 0.67); }}
    function zoomReset() {{ svg.transition().duration(300).call(zoom.transform, d3.zoomIdentity); }}

    // ---- Entity Selection ----
    function selectEntity(name) {{
        selectedEntity = name;
        const entity = entityByName[name];
        if (!entity) return;

        // Highlight on scatter
        svg.selectAll('.node')
            .classed('selected', d => d.name === name);

        // Open detail panel
        const panel = document.getElementById('detail-panel');
        panel.classList.add('open');
        renderDetail(entity);
    }}

    function closeDetail() {{
        document.getElementById('detail-panel').classList.remove('open');
        selectedEntity = null;
        svg.selectAll('.node').classed('selected', false);
    }}

    function renderDetail(e) {{
        const panel = document.getElementById('detail-panel');
        const dacc = e.scores?.dacc || {{}};
        const act = e.scores?.actionability || {{}};
        const trans = e.scores?.transformative || {{}};
        const research = e.research || {{}};
        const tierBadge = e.tier === 1
            ? '<span class="badge badge-tier1">Tier 1</span>'
            : '<span class="badge badge-tier2">Tier 2</span>';
        const bottleneckColor = bottleneckColors[act.readiness_bottleneck] || '#888';
        const actionColor = actionColors[act.what_to_do_now] || '#888';

        // Organizations
        let orgsHtml = '';
        if (research.organizations && research.organizations.length > 0) {{
            orgsHtml = '<div class="detail-section"><div class="section-title">Organizations</div>';
            research.organizations.forEach(org => {{
                const link = org.url ? `<a href="${{org.url}}" target="_blank">${{org.name}}</a>` : org.name;
                orgsHtml += `<div class="org-item"><span class="org-name">${{link}}</span><span class="org-role">${{org.role || ''}}</span></div>`;
            }});
            orgsHtml += '</div>';
        }}

        // Source quote
        let quoteHtml = '';
        if (e.source_quote) {{
            quoteHtml = `
                <div class="detail-section">
                    <div class="section-title">Source Quote</div>
                    <div class="source-quote">${{e.source_quote}}</div>
                    ${{e.source_url ? `<div style="margin-top:6px;font-size:11px;"><a href="${{e.source_url}}" target="_blank" style="color:#60a5fa;">View source</a></div>` : ''}}
                </div>
            `;
        }}

        // Key publications
        let pubsHtml = '';
        if (research.key_publications && research.key_publications.length > 0) {{
            pubsHtml = '<div class="detail-section"><div class="section-title">Key Publications</div>';
            research.key_publications.forEach(pub => {{
                const link = pub.url ? `<a href="${{pub.url}}" target="_blank" style="color:#60a5fa;text-decoration:none;">${{pub.title}}</a>` : pub.title;
                pubsHtml += `<div style="font-size:12px;color:#cbd5e1;padding:4px 0;border-bottom:1px solid #1e293b;">${{link}} <span style="color:#64748b;">(${{pub.date || ''}})</span></div>`;
            }});
            pubsHtml += '</div>';
        }}

        panel.innerHTML = `
            <button class="detail-close" onclick="closeDetail()">&times;</button>
            <div class="detail-header">
                <div class="detail-title">${{e.name}}</div>
                <div class="detail-group">${{e.group || ''}}</div>
                <div class="detail-badges">
                    ${{tierBadge}}
                    <span class="badge" style="background:${{bottleneckColor}}22;color:${{bottleneckColor}};border:1px solid ${{bottleneckColor}}44;">${{act.readiness_bottleneck || '?'}}</span>
                    <span class="badge" style="background:${{actionColor}}22;color:${{actionColor}};border:1px solid ${{actionColor}}44;">${{act.what_to_do_now || '?'}}</span>
                    ${{e.v2_consensus ? '<span class="badge" style="background:#fbbf2422;color:#fbbf24;border:1px solid #fbbf2444;">v2 match</span>' : ''}}
                </div>
            </div>

            <div class="detail-scores">
                <div class="score-box"><div class="score-label">d/acc Total</div><div class="score-value" style="color:#34d399;">${{dacc.total || 0}}/20</div></div>
                <div class="score-box"><div class="score-label">Transformative</div><div class="score-value" style="color:#a78bfa;">${{trans.score || 0}}/5</div></div>
                <div class="score-box"><div class="score-label">TRL</div><div class="score-value" style="color:#f59e0b;">${{research.trl || '?'}}</div></div>
                <div class="score-box"><div class="score-label">Composite</div><div class="score-value" style="color:#60a5fa;">${{e.scores?.composite || 0}}</div></div>
            </div>

            <div class="detail-section">
                <div class="section-title">One-liner</div>
                <div class="section-content">${{e.one_liner || ''}}</div>
            </div>

            <div class="detail-section">
                <div class="section-title">Mechanism</div>
                <div class="section-content">${{e.mechanism || ''}}</div>
            </div>

            <div class="detail-section">
                <div class="section-title">d/acc Alignment</div>
                <div class="dacc-grid">
                    <div class="dacc-row">
                        <span class="dacc-name">Democratic</span>
                        <div class="dacc-bar-bg"><div class="dacc-bar" style="width:${{(dacc.democratic || 0) / 5 * 100}}%;background:#34d399;"></div></div>
                        <span class="dacc-num">${{dacc.democratic || 0}}/5</span>
                    </div>
                    <div class="dacc-row">
                        <span class="dacc-name">Decentralized</span>
                        <div class="dacc-bar-bg"><div class="dacc-bar" style="width:${{(dacc.decentralized || 0) / 5 * 100}}%;background:#22d3ee;"></div></div>
                        <span class="dacc-num">${{dacc.decentralized || 0}}/5</span>
                    </div>
                    <div class="dacc-row">
                        <span class="dacc-name">Defensive</span>
                        <div class="dacc-bar-bg"><div class="dacc-bar" style="width:${{(dacc.defensive || 0) / 5 * 100}}%;background:#60a5fa;"></div></div>
                        <span class="dacc-num">${{dacc.defensive || 0}}/5</span>
                    </div>
                    <div class="dacc-row">
                        <span class="dacc-name">Differential</span>
                        <div class="dacc-bar-bg"><div class="dacc-bar" style="width:${{(dacc.differential || 0) / 5 * 100}}%;background:#a78bfa;"></div></div>
                        <span class="dacc-num">${{dacc.differential || 0}}/5</span>
                    </div>
                </div>
            </div>

            <div class="detail-section">
                <div class="section-title">Action: ${{act.what_to_do_now || '?'}}</div>
                <div class="action-badge" style="background:${{actionColor}}22;color:${{actionColor}};">
                    ${{act.what_to_do_now || '?'}}
                </div>
                <div class="section-content" style="margin-top:8px;">${{act.what_to_do_now_evidence || ''}}</div>
            </div>

            ${{e.exists_today ? `<div class="detail-section"><div class="section-title">Exists Today?</div><div class="section-content">${{e.exists_today}}</div></div>` : ''}}

            ${{research.funding && research.funding !== 'None found' ? `<div class="detail-section"><div class="section-title">Funding</div><div class="section-content">${{research.funding}}</div></div>` : ''}}

            ${{orgsHtml}}
            ${{pubsHtml}}
            ${{quoteHtml}}

            ${{research.barriers ? `<div class="detail-section"><div class="section-title">Barriers</div><div class="section-content">${{research.barriers}}</div></div>` : ''}}
        `;
    }}

    // ---- Action View ----
    function renderActionView() {{
        const filters = getActiveFilters();
        const actionOrder = ['Fund', 'Build', 'Research', 'Advocate', 'Convene'];
        const grouped = {{}};
        actionOrder.forEach(a => {{ grouped[a] = []; }});

        scatterData.forEach(d => {{
            if (!passesFilter(d, filters)) return;
            const action = d.action;
            if (!grouped[action]) grouped[action] = [];
            grouped[action].push(d);
        }});

        const container = document.getElementById('action-view');
        let html = '';

        actionOrder.forEach(action => {{
            const items = grouped[action] || [];
            if (items.length === 0) return;
            const color = actionColors[action] || '#888';

            html += `<div class="action-group">`;
            html += `<div class="action-group-title" style="background:${{color}}22;color:${{color}};border-left:4px solid ${{color}};">${{action}} (${{items.length}})</div>`;
            html += `<div class="action-cards">`;

            items.sort((a, b) => b.dacc_total - a.dacc_total);
            items.forEach(d => {{
                const full = entityByName[d.name];
                const oneLiner = full?.one_liner || '';
                const tierLabel = d.tier === 1 ? 'T1' : 'T2';
                html += `
                    <div class="action-card" onclick="selectEntity('${{d.name.replace(/'/g, "\\\\'")}}')" >
                        <div class="action-card-name">${{d.name}}</div>
                        <div class="action-card-meta">
                            <span style="color:${{d.tier === 1 ? '#60a5fa' : '#64748b'}};">${{tierLabel}}</span>
                            <span style="color:#34d399;">d/acc: ${{d.dacc_total}}</span>
                            <span style="color:#a78bfa;">T: ${{d.transformative}}</span>
                            <span style="color:${{bottleneckColors[d.bottleneck] || '#888'}};">${{d.bottleneck}}</span>
                        </div>
                        <div class="action-card-desc">${{oneLiner}}</div>
                    </div>
                `;
            }});

            html += `</div></div>`;
        }});

        container.innerHTML = html || '<div style="text-align:center;color:#64748b;padding:60px;">No entities match current filters</div>';
    }}

    // ---- Methodology Modal ----
    function openMethodology() {{
        document.getElementById('methodology-modal').classList.add('open');
    }}

    function closeMethodology() {{
        document.getElementById('methodology-modal').classList.remove('open');
    }}

    // Close modal on background click
    document.addEventListener('click', (e) => {{
        if (e.target.id === 'methodology-modal') closeMethodology();
    }});

    // Escape key closes modal and detail
    document.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') {{
            closeMethodology();
            closeDetail();
        }}
    }});

    // Handle resize
    window.addEventListener('resize', () => {{
        // Remove old SVG and reinit
        d3.select('#viz-container svg').remove();
        initScatter();
        applyFilters();
    }});
    </script>
</body>
</html>"""

    return html


def main():
    curated, scatter, all_entities = load_data()
    stats = compute_stats(all_entities, scatter)
    print(f"Stats: {stats}")

    html = generate_html(curated, scatter, all_entities, stats)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(html)

    size_kb = OUTPUT_PATH.stat().st_size / 1024
    print(f"Dashboard written to {OUTPUT_PATH} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()

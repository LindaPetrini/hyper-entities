#!/usr/bin/env python3
"""
Create a standalone showcase page for top 15 hidden gem hyper-entities.
"""

import json
from pathlib import Path

CONFIG = {
    "input_json": "results/stage3_concrete/entities.json",
    "output_html": "results/showcase.html",
}


def calc_composite_scores(e):
    """Calculate composite scores for an entity."""
    concrete = (e.get('concreteness', {}).get('score', 0)) / 5
    dacc = (e.get('stage3_dacc', {}).get('total', 0)) / 20
    momentum = (e.get('stage1_consolidated', {}).get('current_momentum', 0)) / 12
    transform = (e.get('stage1_consolidated', {}).get('transformative_potential', 0)) / 6
    power = (e.get('stage2_consolidated', {}).get('transformative_power', 0)) / 25
    defensive = (e.get('stage3_dacc', {}).get('defensive', 0)) / 5
    decent = (e.get('stage3_dacc', {}).get('decentralized', 0)) / 5

    return {
        'hidden_gem': concrete * 0.35 + dacc * 0.35 + (1 - momentum) * 0.30,
        'buildable_good': concrete * 0.40 + dacc * 0.40 + power * 0.20,
        'defensive_tech': defensive * 0.40 + concrete * 0.30 + decent * 0.30,
        'underdog': (transform + concrete + dacc) / (momentum + 0.1)
    }


def get_diverse_top15(entities):
    """Get diverse top 15 across clusters."""
    # Calculate composite scores
    for e in entities:
        e['composites'] = calc_composite_scores(e)

    # Sort by hidden_gem
    sorted_entities = sorted(entities, key=lambda x: x['composites']['hidden_gem'], reverse=True)

    picks = []
    seen_clusters = {}

    for e in sorted_entities:
        if len(picks) >= 15:
            break
        cluster = e.get('cluster_name', 'Unknown')
        # Max 2 per cluster for diversity
        if seen_clusters.get(cluster, 0) < 2:
            picks.append(e)
            seen_clusters[cluster] = seen_clusters.get(cluster, 0) + 1

    return picks


def create_showcase_html(entities):
    """Create showcase HTML."""
    top15 = get_diverse_top15(entities)

    cards_html = ""
    for i, e in enumerate(top15, 1):
        score = e['composites']['hidden_gem']
        concrete = e.get('concreteness', {})
        dacc = e.get('stage3_dacc', {})
        techs = concrete.get('core_technologies', [])[:4]
        verdict = concrete.get('verdict', '')
        concrete_version = concrete.get('concrete_version', '')[:250]

        verdict_badge = ''
        if verdict == 'keep':
            verdict_badge = '<span class="badge badge-keep">Already Concrete</span>'
        elif verdict == 'transform':
            verdict_badge = '<span class="badge badge-transform">Made Concrete</span>'

        techs_html = ''.join([f'<span class="tech-tag">{t}</span>' for t in techs])

        cards_html += f"""
        <div class="card">
            <div class="card-header">
                <span class="rank">#{i}</span>
                <span class="score">Score: {score:.0%}</span>
            </div>
            <h3 class="card-title">{e['name']}</h3>
            <div class="card-badges">
                {verdict_badge}
                <span class="badge badge-dacc">d/acc: {dacc.get('total', 0)}/20</span>
                <span class="badge badge-concrete">Concrete: {concrete.get('score', 0)}/5</span>
            </div>
            <p class="card-desc">{e.get('description', '')[:200]}...</p>
            {f'<div class="concrete-version"><strong>What it could be:</strong> {concrete_version}...</div>' if concrete_version and verdict == 'transform' else ''}
            <div class="tech-tags">{techs_html}</div>
            <div class="card-footer">
                <span class="cluster">{e.get('cluster_name', 'Unknown')}</span>
                <div class="dacc-scores">
                    <span title="Democratic">D:{dacc.get('democratic', 0)}</span>
                    <span title="Decentralized">D:{dacc.get('decentralized', 0)}</span>
                    <span title="Defensive">D:{dacc.get('defensive', 0)}</span>
                    <span title="Differential">D:{dacc.get('differential', 0)}</span>
                </div>
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hidden Gems: 15 Under-Known Hyper-Entities Worth Building</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #e0e6f0;
            min-height: 100vh;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            margin-bottom: 50px;
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #f59e0b, #fbbf24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
        }}

        .subtitle {{
            font-size: 1.1rem;
            color: #94a3b8;
            max-width: 700px;
            margin: 0 auto 20px;
            line-height: 1.6;
        }}

        .scoring-info {{
            background: rgba(245, 158, 11, 0.1);
            border: 1px solid rgba(245, 158, 11, 0.3);
            border-radius: 8px;
            padding: 15px 25px;
            display: inline-block;
            font-size: 0.9rem;
            color: #fbbf24;
        }}

        .cards {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 25px;
        }}

        .card {{
            background: linear-gradient(145deg, #1a1f3a 0%, #0f1629 100%);
            border: 1px solid #2a3f5a;
            border-radius: 12px;
            padding: 25px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #f59e0b, #34d399);
        }}

        .card:hover {{
            border-color: #f59e0b;
            transform: translateY(-4px);
            box-shadow: 0 10px 40px rgba(245, 158, 11, 0.15);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}

        .rank {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #f59e0b;
        }}

        .score {{
            background: rgba(245, 158, 11, 0.2);
            color: #fbbf24;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }}

        .card-title {{
            font-size: 1.3rem;
            font-weight: 600;
            color: #fff;
            margin-bottom: 12px;
            line-height: 1.3;
        }}

        .card-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }}

        .badge {{
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 500;
        }}

        .badge-keep {{
            background: rgba(52, 211, 153, 0.2);
            color: #34d399;
        }}

        .badge-transform {{
            background: rgba(245, 158, 11, 0.2);
            color: #f59e0b;
        }}

        .badge-dacc {{
            background: rgba(52, 211, 153, 0.15);
            color: #34d399;
        }}

        .badge-concrete {{
            background: rgba(245, 158, 11, 0.15);
            color: #fbbf24;
        }}

        .card-desc {{
            color: #94a3b8;
            font-size: 0.9rem;
            line-height: 1.6;
            margin-bottom: 15px;
        }}

        .concrete-version {{
            background: rgba(245, 158, 11, 0.08);
            border-left: 3px solid #f59e0b;
            padding: 12px 15px;
            margin-bottom: 15px;
            font-size: 0.85rem;
            color: #cbd5e1;
            line-height: 1.5;
            border-radius: 0 6px 6px 0;
        }}

        .concrete-version strong {{
            color: #f59e0b;
        }}

        .tech-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 15px;
        }}

        .tech-tag {{
            background: #1e293b;
            color: #60a5fa;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
        }}

        .card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 15px;
            border-top: 1px solid #2a3f5a;
        }}

        .cluster {{
            color: #64748b;
            font-size: 0.8rem;
        }}

        .dacc-scores {{
            display: flex;
            gap: 8px;
            font-size: 0.75rem;
            color: #34d399;
        }}

        .dacc-scores span {{
            background: rgba(52, 211, 153, 0.1);
            padding: 2px 6px;
            border-radius: 3px;
        }}

        footer {{
            text-align: center;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 1px solid #2a3f5a;
        }}

        footer a {{
            color: #60a5fa;
            text-decoration: none;
        }}

        footer a:hover {{
            text-decoration: underline;
        }}

        .cta {{
            margin-top: 20px;
        }}

        .cta a {{
            display: inline-block;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            color: #fff;
            padding: 12px 30px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }}

        .cta a:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(96, 165, 250, 0.3);
        }}

        @media (max-width: 500px) {{
            .cards {{
                grid-template-columns: 1fr;
            }}
            h1 {{
                font-size: 1.8rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Hidden Gems</h1>
            <p class="subtitle">
                15 under-known hyper-entities that score high on <strong>concreteness</strong> (actually buildable)
                and <strong>d/acc alignment</strong> (beneficial direction) but low on <strong>current momentum</strong> (not yet mainstream).
            </p>
            <div class="scoring-info">
                Hidden Gem Score = 35% Concrete + 35% d/acc + 30% (1 - Momentum)
            </div>
        </header>

        <div class="cards">
            {cards_html}
        </div>

        <footer>
            <p>Data from <a href="dashboard.html">Hyper-Entities Dashboard v3.3</a></p>
            <p style="color: #64748b; margin-top: 10px;">
                Based on d/acc framework by Vitalik Buterin. Concreteness extraction via Claude.
            </p>
            <div class="cta">
                <a href="dashboard.html">Explore All 345 Entities</a>
            </div>
        </footer>
    </div>
</body>
</html>
"""

    return html


def main():
    print("Creating Hidden Gems Showcase...")

    # Load data
    with open(CONFIG["input_json"]) as f:
        data = json.load(f)

    entities = data["entities"]
    print(f"Loaded {len(entities)} entities")

    # Create HTML
    html = create_showcase_html(entities)

    # Save
    output_path = Path(CONFIG["output_html"])
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Saved to: {output_path}")

    # Show the top 15
    top15 = get_diverse_top15(entities)
    print("\nTop 15 Hidden Gems:")
    for i, e in enumerate(top15, 1):
        score = e['composites']['hidden_gem']
        print(f"  {i:2}. {e['name'][:50]} (score={score:.0%})")


if __name__ == "__main__":
    main()

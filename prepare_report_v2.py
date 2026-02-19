#!/usr/bin/env python3
"""
Prepare data for Report v2: tiering, maturity classification, scatter plot data.
Outputs JSON files consumed by generate_report_v2.py and create_dashboard.py.
"""

import json
from pathlib import Path

CONSENSUS_JSON = "results/consensus_entities.json"
SOURCE_LINKS_JSON = "results/source_links.json"
OUTPUT_DIR = Path("results/report_v2_data")

# ──────────────────────────────────────────────
# Maturity classification rules
# Non-existence=3 → entity mostly doesn't exist → Foundational or Early
# Non-existence=2 → partially exists → Scaling or Near Deployment
# We refine with manual overrides based on entity descriptions.
# ──────────────────────────────────────────────

MATURITY_LEVELS = {
    "Foundational Research": "theoretical work, no prototypes",
    "Early Demonstrations": "lab proofs-of-concept, small-scale experiments",
    "Scaling Challenges": "working implementations exist but face major barriers",
    "Near Deployment": "functioning systems approaching mainstream use",
}

# Manual maturity assignments for all 39 entities
# Based on Non-existence score + entity descriptions + domain knowledge
MATURITY_OVERRIDES = {
    # Energy & Infrastructure
    178: "Early Demonstrations",       # Deep Fision — no prototype yet, but SMR field active
    213: "Early Demonstrations",       # Climate Adaptation Jurisdictional Arbitrage — emerging concept
    173: "Scaling Challenges",         # Decentralized Adaptive Energy Network — VPPs exist, not integrated

    # Manufacturing & Matter
    202: "Scaling Challenges",         # End-User Programming — tools exist (Replit, Cursor), not universal
    51:  "Foundational Research",      # Atomically Precise Manufacturing — theoretical, Drexler vision
    151: "Early Demonstrations",       # Chemputing — Cronin lab demos, single lab
    68:  "Foundational Research",      # Universal Constructor — theoretical, von Neumann concept

    # Truth & Epistemic Infrastructure
    47:  "Early Demonstrations",       # Epistemic Stack — fragments exist (fact-checkers, C2PA), no stack
    141: "Early Demonstrations",       # AI-Assisted Epistemological Enhancement — early tools exist
    3:   "Scaling Challenges",         # Distributed ZK Security — ZK proofs deployed, not as security infra
    146: "Early Demonstrations",       # Epistemic Infra for Truth Verification — fragments exist

    # Governance & Collective Intelligence
    2:   "Early Demonstrations",       # Competitive Governance Protocol Stack — charter cities, Aragon
    265: "Foundational Research",      # LexCommons — concept stage, no unified effort
    35:  "Foundational Research",      # De-escalatory Self-Defense Mediation Tool — no one building this
    340: "Early Demonstrations",       # Global Deliberation Coordinator — Polis, but not GDaaS
    22:  "Early Demonstrations",       # Habermas Machines — DeepMind paper, early prototype
    112: "Early Demonstrations",       # Gevulot — testnet stage

    # Markets & Incentive Systems
    149: "Early Demonstrations",       # Reputational Markets — fragments (Gitcoin Passport)
    190: "Scaling Challenges",         # Prediction Markets — Polymarket, Kalshi exist, governance use limited
    71:  "Early Demonstrations",       # Futarchy — MetaDAO experiments

    # Ethics & Moral Expansion
    163: "Foundational Research",      # Expanded Moral Circle Technologies — philosophical concept
    101: "Foundational Research",      # Moral Trade Civilization — theoretical

    # AI & Human Agency
    142: "Early Demonstrations",       # EgoLets — Character.AI-like tools, not fiduciary
    43:  "Foundational Research",      # Fiduciary AI Assistance — concept, no true fiduciary AI
    286: "Early Demonstrations",       # Empathetic Neuro-AI — Hume AI, early stage
    259: "Early Demonstrations",       # Lifelong AI Guardians — personal AI assistants emerging

    # Interfaces & Augmentation
    137: "Foundational Research",      # Digital Mind Governance — no digital minds to govern yet
    262: "Near Deployment",            # Translation Language Models — DeepL, SeamlessM4T exist
    306: "Scaling Challenges",         # Digital Twin Ecosystem — Azure/Nvidia, but not unified
    115: "Early Demonstrations",       # Immune-Computer Interface — Dexcom, early biosensors
    212: "Early Demonstrations",       # Human Superintelligence via BCI — Neuralink implants, early
    144: "Foundational Research",      # Mind Uploading — theoretical
    107: "Foundational Research",      # Whole Brain Emulation — OpenWorm only

    # Science & Discovery
    39:  "Early Demonstrations",       # Automated Scientific Publishing — DeSci Labs, fragments
    309: "Early Demonstrations",       # Universal AI Learning UnCommons — open ed-tech exists, not unified
    171: "Foundational Research",      # Atheoretical Science AI — concept
    207: "Early Demonstrations",       # Origin of Life Experimental Platform — labs active
    65:  "Near Deployment",            # Protein Design — AlphaFold, RFdiffusion in use
    5:   "Scaling Challenges",         # Decentralized Scientific Collaboration — DeSci movement active
}

# ──────────────────────────────────────────────
# Tier 1 selection criteria
# ──────────────────────────────────────────────

# Entities to EXCLUDE from Tier 1 (well-known, overlapping, or not "undervalued"):
WELL_KNOWN_EXCLUDE = {
    212,  # Human Superintelligence via BCI — BCIs are well-funded/known
    65,   # Protein Design — AlphaFold massively funded
    144,  # Mind Uploading — well-known sci-fi concept
    107,  # Whole Brain Emulation — same
    190,  # Prediction Markets — Polymarket is mainstream now
    262,  # Translation Language Models — DeepL is mainstream, near deployment
    306,  # Digital Twin Ecosystem — well-known concept (Azure, NVIDIA)
    141,  # AI-Assisted Epistemological Enhancement — overlaps with Epistemic Stack
    146,  # Epistemic Infra for Truth Verification — overlaps with Epistemic Stack
    3,    # Distributed ZK Security — ZK already well-funded in crypto
}


def load_entities():
    with open(CONSENSUS_JSON) as f:
        data = json.load(f)
    return data["entities"]


def classify_tier(entity):
    """Assign Tier 1 or Tier 2 based on criteria."""
    eid = entity["id"]

    # Exclude well-known entities from Tier 1
    if eid in WELL_KNOWN_EXCLUDE:
        return 2

    voted_both = entity.get("voted_by") == "both"
    has_tech = entity.get("stage2_total") is not None and entity.get("stage2_total", 0) > 0
    has_dacc = entity.get("stage3_dacc") is not None
    dacc_score = entity.get("stage3_dacc", {}).get("total", 0) if has_dacc else 0

    # Strong Tier 1 candidates: voted by both + complete data + high d/acc
    if voted_both and has_tech and dacc_score >= 15:
        return 1

    # Also include high-d/acc entities that are genuinely novel even without tech scores
    if voted_both and dacc_score >= 16 and not has_tech:
        return 1

    # High d/acc individual picks representing underserved groups
    if eid == 163:  # Expanded Moral Circle — only Ethics representative with both-like quality
        return 1
    if eid == 173:  # Decentralized Adaptive Energy — high scores
        return 1

    return 2


def identify_undervalued(entities):
    """Identify the 5-7 most undervalued entities."""
    undervalued_ids = {
        151,  # Chemputing — single lab, d/acc: 13, Tech: 44
        35,   # De-escalatory Self-Defense Mediation Tool — no one building this
        47,   # Epistemic Stack — critical infra, fragmented
        265,  # LexCommons — high scores, no unified effort
        309,  # Universal AI Learning UnCommons — community ed-tech, no major funder
        39,   # Automated Scientific Publishing — high scores, no one building as system
        112,  # Gevulot — strong d/acc, under-resourced
    }
    return [e for e in entities if e["id"] in undervalued_ids]


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entities = load_entities()
    source_links = json.load(open(SOURCE_LINKS_JSON))

    # Assign maturity and tier to each entity
    enriched = []
    for e in entities:
        eid = e["id"]
        tier = classify_tier(e)
        maturity = MATURITY_OVERRIDES.get(eid, "Early Demonstrations")
        dacc = e.get("stage3_dacc", {})
        dacc_total = dacc.get("total") if dacc else None
        tech_total = e.get("stage2_total")
        if tech_total == 0:
            tech_total = None  # Treat 0 as N/A

        enriched.append({
            "id": eid,
            "name": e["name"],
            "tier": tier,
            "maturity": maturity,
            "voted_by": e.get("voted_by"),
            "cluster_name": e.get("cluster_name"),
            "cluster_id": e.get("cluster_id"),
            "dacc_total": dacc_total,
            "tech_total": tech_total,
            "stage1_total": e.get("stage1_consolidated", {}).get("total") or e.get("total_score"),
            "non_existence": e.get("scoring", {}).get("Non-existence"),
            "dacc_breakdown": {
                "democratic": dacc.get("democratic"),
                "decentralized": dacc.get("decentralized"),
                "defensive": dacc.get("defensive"),
                "differential": dacc.get("differential"),
            } if dacc else None,
            # Full entity data for report generation
            "description": e.get("description"),
            "problems_solved": e.get("problems_solved"),
            "why_new_different": e.get("why_new_different"),
            "why_not_exists": e.get("why_not_exists"),
            "evidence": e.get("evidence"),
            "concreteness": e.get("concreteness"),
            "dacc_reasoning": dacc.get("reasoning") if dacc else None,
        })

    # Sort by cluster, then tier, then d/acc score descending
    enriched.sort(key=lambda x: (
        x["cluster_id"] or 99,
        x["tier"],
        -(x["dacc_total"] or 0),
    ))

    tier1 = [e for e in enriched if e["tier"] == 1]
    tier2 = [e for e in enriched if e["tier"] == 2]
    undervalued = identify_undervalued(entities)

    # Summary stats
    print(f"\n{'='*60}")
    print(f"TIERING PROPOSAL")
    print(f"{'='*60}")
    print(f"Total entities: {len(enriched)}")
    print(f"Tier 1 (full write-up): {len(tier1)}")
    print(f"Tier 2 (summary table): {len(tier2)}")
    print()

    # Tier 1 by group
    print("TIER 1 ENTITIES:")
    print("-" * 60)
    current_group = None
    for e in tier1:
        if e["cluster_name"] != current_group:
            current_group = e["cluster_name"]
            print(f"\n  [{current_group}]")
        tech_str = f"Tech: {e['tech_total']}/70" if e['tech_total'] else "Tech: N/A"
        dacc_str = f"d/acc: {e['dacc_total']}/20" if e['dacc_total'] else "d/acc: N/A"
        print(f"    {e['name']}")
        print(f"      {dacc_str} | {tech_str} | {e['maturity']} | voted: {e['voted_by']}")

    print(f"\n\nTIER 2 ENTITIES:")
    print("-" * 60)
    current_group = None
    for e in tier2:
        if e["cluster_name"] != current_group:
            current_group = e["cluster_name"]
            print(f"\n  [{current_group}]")
        tech_str = f"Tech: {e['tech_total']}/70" if e['tech_total'] else "Tech: N/A"
        dacc_str = f"d/acc: {e['dacc_total']}/20" if e['dacc_total'] else "d/acc: N/A"
        print(f"    {e['name']}")
        print(f"      {dacc_str} | {tech_str} | {e['maturity']} | voted: {e['voted_by']}")

    # Maturity distribution
    print(f"\n\nMATURITY DISTRIBUTION:")
    print("-" * 60)
    for level in MATURITY_LEVELS:
        count = len([e for e in enriched if e["maturity"] == level])
        t1_count = len([e for e in tier1 if e["maturity"] == level])
        print(f"  {level}: {count} total ({t1_count} in Tier 1)")

    # Scatter plot readiness
    plottable = [e for e in enriched if e["dacc_total"] and e["tech_total"]]
    print(f"\n\nSCATTER PLOT:")
    print("-" * 60)
    print(f"  Entities with both d/acc + Tech scores: {len(plottable)}/39")
    print(f"  Entities excluded (N/A tech): {len(enriched) - len(plottable)}")

    # Undervalued shortlist
    print(f"\n\nMOST UNDERVALUED SHORTLIST ({len(undervalued)} entities):")
    print("-" * 60)
    for e in undervalued:
        dacc = e.get("stage3_dacc", {}).get("total", "N/A")
        tech = e.get("stage2_total") or "N/A"
        print(f"  {e['name']} — d/acc: {dacc}, Tech: {tech}")

    # Save enriched data
    output = {
        "generated_at": "2026-02-18",
        "tier1_count": len(tier1),
        "tier2_count": len(tier2),
        "entities": enriched,
        "undervalued_ids": [e["id"] for e in undervalued],
        "maturity_levels": MATURITY_LEVELS,
        "cluster_groups": sorted(set(e["cluster_name"] for e in enriched if e["cluster_name"])),
    }

    with open(OUTPUT_DIR / "enriched_entities.json", "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved enriched data to {OUTPUT_DIR / 'enriched_entities.json'}")

    # Save scatter plot data (only plottable entities)
    scatter_data = [{
        "id": e["id"],
        "name": e["name"],
        "dacc": e["dacc_total"],
        "tech": e["tech_total"],
        "cluster": e["cluster_name"],
        "cluster_id": e["cluster_id"],
        "maturity": e["maturity"],
        "tier": e["tier"],
        "description": e["description"],
    } for e in plottable]

    with open(OUTPUT_DIR / "scatter_data.json", "w") as f:
        json.dump(scatter_data, f, indent=2)
    print(f"Saved scatter plot data to {OUTPUT_DIR / 'scatter_data.json'}")


if __name__ == "__main__":
    main()

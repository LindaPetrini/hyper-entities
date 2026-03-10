#!/usr/bin/env python3
"""
v3_report.py — Generate a markdown report from curated v3 hyper-entities using Claude API.

Reads results/v3/curated.json (19 Tier 1 + 170 Tier 2 entities), generates a structured
markdown report with executive summary, methodology, spotlight write-ups, watch list table,
involvement matrix, and scoring appendix. Outputs results/v3/report_v3.md.
"""

import argparse
import asyncio
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import anthropic
from anthropic import RateLimitError, APIStatusError

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CONFIG = {
    "model": "claude-sonnet-4-6",
    "max_tokens": 4096,
    "temperature": 0.3,
    "input_file": Path("results/v3/curated.json"),
    "output_dir": Path("results/v3"),
    "output_file": Path("results/v3/report_v3.md"),
    "progress_file": Path("results/v3/report_v3_progress.json"),
    "max_retries": 3,
    "semaphore_limit": 5,
}

# Sonnet 4.6 pricing
INPUT_COST_PER_M = 3.0
OUTPUT_COST_PER_M = 15.0

# ---------------------------------------------------------------------------
# Progress management
# ---------------------------------------------------------------------------

def save_progress(sections, metadata, filepath):
    """Save current progress to disk."""
    output = {"metadata": metadata, "sections": sections}
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(output, f, indent=2)


def load_progress(filepath):
    """Load existing progress if available."""
    if filepath.exists():
        with open(filepath) as f:
            data = json.load(f)
        return data.get("sections", {}), data.get("metadata", {})
    return {}, {}


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def compute_stats(tier1, tier2):
    """Compute aggregate stats for prompts."""
    all_entities = tier1 + tier2
    groups = {}
    actions = {}
    bottlenecks = {}
    dacc_scores = []
    transformative_scores = []
    trls = []

    for e in all_entities:
        g = e.get("group", "Unknown")
        groups[g] = groups.get(g, 0) + 1

        scores = e.get("scores", {})
        act = scores.get("actionability", {})
        a = act.get("what_to_do_now", "Unknown")
        actions[a] = actions.get(a, 0) + 1
        b = act.get("readiness_bottleneck", "Unknown")
        bottlenecks[b] = bottlenecks.get(b, 0) + 1

        dacc = scores.get("dacc", {})
        if "total" in dacc:
            dacc_scores.append(dacc["total"])
        t = scores.get("transformative", {})
        if "score" in t:
            transformative_scores.append(t["score"])

        r = e.get("research", {})
        trl = r.get("trl")
        if trl is not None:
            trls.append(trl)

    return {
        "total": len(all_entities),
        "tier1_count": len(tier1),
        "tier2_count": len(tier2),
        "groups": dict(sorted(groups.items(), key=lambda x: -x[1])),
        "actions": dict(sorted(actions.items(), key=lambda x: -x[1])),
        "bottlenecks": dict(sorted(bottlenecks.items(), key=lambda x: -x[1])),
        "avg_dacc": round(sum(dacc_scores) / len(dacc_scores), 1) if dacc_scores else 0,
        "avg_transformative": round(sum(transformative_scores) / len(transformative_scores), 1) if transformative_scores else 0,
        "avg_trl": round(sum(trls) / len(trls), 1) if trls else 0,
        "trl_distribution": {k: trls.count(k) for k in sorted(set(trls))},
        "v2_matches": sum(1 for e in all_entities if e.get("v2_consensus")),
    }


def entity_summary_line(e):
    """One-line summary for an entity (used in prompts)."""
    scores = e.get("scores", {})
    dacc = scores.get("dacc", {}).get("total", "?")
    trans = scores.get("transformative", {}).get("score", "?")
    composite = scores.get("composite", "?")
    action = scores.get("actionability", {}).get("what_to_do_now", "?")
    return f"- {e['name']} | group={e.get('group', '?')} | d/acc={dacc}/20 | transformative={trans}/5 | composite={composite} | action={action}"


def entity_detail_block(e):
    """Detailed data block for a single entity (used in Tier 1 prompts)."""
    scores = e.get("scores", {})
    dacc = scores.get("dacc", {})
    act = scores.get("actionability", {})
    trans = scores.get("transformative", {})
    research = e.get("research", {})

    orgs = research.get("organizations", [])
    orgs_str = "; ".join(f"{o['name']} ({o.get('role', '')})" for o in orgs[:5]) if orgs else "None found"
    pubs = research.get("key_publications", [])
    pubs_str = "; ".join(f"{p['title']} ({p.get('date', '')})" for p in pubs[:3]) if pubs else "None found"

    return f"""Name: {e['name']}
Group: {e.get('group', '?')}
One-liner: {e.get('one_liner', '')}
Mechanism: {e.get('mechanism', '')}
Exists today: {e.get('exists_today', '')}
Source quote: "{e.get('source_quote', '')}"
Speaker: {e.get('speaker') or 'N/A'}
Source URL: {e.get('source_url', 'N/A')}

Organizations: {orgs_str}
Funding: {research.get('funding', 'None found')}
TRL: {research.get('trl', '?')} — {research.get('trl_justification', '')}
Publications: {pubs_str}
State of the art: {research.get('state_of_the_art', 'N/A')}
Barriers: {research.get('barriers', 'N/A')}

d/acc scores: Democratic={dacc.get('democratic', '?')}/5, Decentralized={dacc.get('decentralized', '?')}/5, Defensive={dacc.get('defensive', '?')}/5, Differential={dacc.get('differential', '?')}/5 (Total={dacc.get('total', '?')}/20)
d/acc summary: {dacc.get('dacc_summary', 'N/A')}
Transformative: {trans.get('score', '?')}/5 — {trans.get('evidence', '')}
Bottleneck: {act.get('readiness_bottleneck', '?')} — {act.get('readiness_bottleneck_evidence', '')}
Action: {act.get('what_to_do_now', '?')} — {act.get('what_to_do_now_evidence', '')}
Composite score: {scores.get('composite', '?')}
v2 consensus: {'Yes' if e.get('v2_consensus') else 'No'}"""


# ---------------------------------------------------------------------------
# API calling
# ---------------------------------------------------------------------------

async def call_api(client, sem, system, user, section_name):
    """Call Claude API with retry logic. Returns (text, in_tok, out_tok)."""
    for attempt in range(CONFIG["max_retries"]):
        async with sem:
            try:
                response = await client.messages.create(
                    model=CONFIG["model"],
                    max_tokens=CONFIG["max_tokens"],
                    temperature=CONFIG["temperature"],
                    system=system,
                    messages=[{"role": "user", "content": user}],
                )
                text = response.content[0].text
                in_tok = response.usage.input_tokens
                out_tok = response.usage.output_tokens
                print(f"  [{section_name}] {in_tok:,} in / {out_tok:,} out")
                return text, in_tok, out_tok

            except RateLimitError:
                wait = (2 ** attempt) * 2
                print(f"  [{section_name}] rate limited, waiting {wait}s (attempt {attempt + 1})")
                await asyncio.sleep(wait)
            except APIStatusError as e:
                wait = (2 ** attempt) * 2
                print(f"  [{section_name}] API error ({e.status_code}), retrying in {wait}s")
                await asyncio.sleep(wait)
            except Exception as e:
                print(f"  [{section_name}] unexpected error: {e}")
                return None, 0, 0

    print(f"  [{section_name}] all retries exhausted")
    return None, 0, 0


# ---------------------------------------------------------------------------
# Section generators
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an expert technology policy writer producing a professional report for the Foresight Institute. Write in clear, direct prose. Avoid AI writing patterns: no "tapestry", "landscape of", "paradigm shift", "delve into", "it's worth noting", "in conclusion". Use concrete language. Do not add meta-commentary about the report itself. Return ONLY the markdown content requested, no preamble."""


async def generate_intro(client, sem, tier1, tier2, stats):
    """Generate executive summary and methodology sections."""
    tier1_summaries = "\n".join(entity_summary_line(e) for e in tier1)
    groups_str = "\n".join(f"- {g}: {c} entities" for g, c in stats["groups"].items())
    actions_str = "\n".join(f"- {a}: {c} entities" for a, c in stats["actions"].items())
    bottleneck_str = "\n".join(f"- {b}: {c} entities" for b, c in stats["bottlenecks"].items())

    prompt = f"""Write two sections for a report on hyper-entities — future systems that don't exist yet but are already reorganizing coordination, investment, and narrative around their anticipated existence.

DATA:
- {stats['total']} candidates analyzed from 109 sources (Existential Hope podcast transcripts, world gallery submissions, AI pathways essays)
- {stats['tier1_count']} spotlight entities (Tier 1), {stats['tier2_count']} watch list (Tier 2)
- {stats['v2_matches']} entities also appeared in v2 analysis (cross-version consensus)
- Average d/acc score: {stats['avg_dacc']}/20
- Average transformative score: {stats['avg_transformative']}/5
- Average TRL: {stats['avg_trl']}
- TRL distribution: {stats['trl_distribution']}

GROUPS:
{groups_str}

ACTION TYPES:
{actions_str}

BOTTLENECKS:
{bottleneck_str}

TIER 1 ENTITIES:
{tier1_summaries}

Write:

## 1. Executive Summary (~500 words)
Cover: what hyper-entities are (coined by Michael Nielsen), key findings, the 19 spotlight vs 170 watch list, d/acc framework (Vitalik Buterin — democratic, decentralized, defensive, differential), most common bottlenecks and recommended actions. Reference that sources come from Existential Hope (existentialhope.com), the Foresight Institute's initiative.

## 2. Methodology (~300 words)
Cover: V3 pipeline (extract from 109 sources → deduplicate → web research → score on d/acc + transformative + actionability → curate into tiers), scoring dimensions, tiering criteria (composite score threshold), source categories. Mention that scoring was done by Claude API with human curation.

Use markdown headers as shown. Be specific with numbers. Write for an audience of funders, policymakers, and technologists."""

    text, in_tok, out_tok = await call_api(client, sem, SYSTEM_PROMPT, prompt, "intro")
    return text, in_tok, out_tok


async def generate_entity_writeup(client, sem, entity, idx, total):
    """Generate a ~200-300 word write-up for a single Tier 1 entity."""
    detail = entity_detail_block(entity)
    scores = entity.get("scores", {})
    composite = scores.get("composite", "?")

    prompt = f"""Write a spotlight entry (~200-300 words) for this hyper-entity. This is entity {idx + 1} of {total} in the Tier 1 section of a Foresight Institute report.

ENTITY DATA:
{detail}

FORMAT (use this exact structure):

### {entity['name']}
**{entity.get('group', '')}** | Composite: {composite}

[One-liner description]

**How it works.** [2-3 sentences on mechanism, drawn from the data above]

**Who's building toward this.** [List real organizations from the research data with their roles. Include funding and TRL.]

**d/acc alignment.** [Which dimensions score highest and why, 1-2 sentences. Reference actual scores.]

> **What can someone do RIGHT NOW?** [Based on the action type ({scores.get('actionability', {}).get('what_to_do_now', '?')}) and bottleneck ({scores.get('actionability', {}).get('readiness_bottleneck', '?')}), write 1-2 concrete sentences about what a funder/builder/researcher/advocate could do today.]

> "{entity.get('source_quote', '')}" — *Source: [{entity.get('source_url', '').split('/')[-2] if entity.get('source_url') else 'N/A'}]({entity.get('source_url', '')})*

Be factual. Use the research data provided — do not invent organizations or funding amounts."""

    text, in_tok, out_tok = await call_api(client, sem, SYSTEM_PROMPT, prompt, f"entity {idx + 1}/{total}")
    return text, in_tok, out_tok


# ---------------------------------------------------------------------------
# Pure Python sections (no API calls)
# ---------------------------------------------------------------------------

def generate_tier2_table(tier2):
    """Generate the Tier 2 watch list table."""
    lines = [
        "## 4. Watch List (Tier 2)\n",
        f"The remaining {len(tier2)} entities form the watch list — systems worth tracking but not yet meeting the composite score threshold for spotlight treatment.\n",
        "| Name | Group | d/acc | Trans. | Bottleneck | Action | TRL |",
        "|------|-------|-------|--------|------------|--------|-----|",
    ]
    for e in sorted(tier2, key=lambda x: -x.get("scores", {}).get("composite", 0)):
        scores = e.get("scores", {})
        dacc = scores.get("dacc", {}).get("total", "?")
        trans = scores.get("transformative", {}).get("score", "?")
        bottleneck = scores.get("actionability", {}).get("readiness_bottleneck", "?")
        action = scores.get("actionability", {}).get("what_to_do_now", "?")
        trl = e.get("research", {}).get("trl", "?")
        name = e.get("name", "?")
        group = e.get("group", "?")
        # Truncate long names for table readability
        if len(name) > 60:
            name = name[:57] + "..."
        if len(group) > 40:
            group = group[:37] + "..."
        lines.append(f"| {name} | {group} | {dacc}/20 | {trans}/5 | {bottleneck} | {action} | {trl} |")

    return "\n".join(lines)


def generate_involvement_matrix(tier1, tier2):
    """Generate the 'How to Get Involved' matrix grouped by action type."""
    all_entities = tier1 + tier2
    by_action = {}
    for e in all_entities:
        action = e.get("scores", {}).get("actionability", {}).get("what_to_do_now", "Unknown")
        by_action.setdefault(action, []).append(e)

    action_descriptions = {
        "Fund": "These entities have working concepts but need capital to scale. The bottleneck is money, not ideas.",
        "Build": "The research is done, the path is clear — these need engineering teams and implementation effort.",
        "Research": "Promising directions that need more investigation before they're ready for deployment.",
        "Advocate": "These need policy changes, regulatory frameworks, or public support to move forward.",
        "Convene": "The pieces exist separately — what's missing is coordination between stakeholders.",
    }

    lines = ["## 5. How to Get Involved\n"]

    for action in ["Fund", "Build", "Research", "Advocate", "Convene"]:
        entities = by_action.get(action, [])
        if not entities:
            continue
        desc = action_descriptions.get(action, "")
        tier1_in_action = [e for e in entities if e.get("tier") == 1]
        tier2_in_action = [e for e in entities if e.get("tier") == 2]

        lines.append(f"### {action} ({len(entities)} entities)")
        lines.append(f"{desc}\n")

        if tier1_in_action:
            lines.append("**Spotlight:**")
            for e in sorted(tier1_in_action, key=lambda x: -x.get("scores", {}).get("composite", 0)):
                bottleneck = e.get("scores", {}).get("actionability", {}).get("readiness_bottleneck", "")
                lines.append(f"- **{e['name']}** — {e.get('one_liner', '')} (Bottleneck: {bottleneck})")
            lines.append("")

        if tier2_in_action:
            lines.append(f"**Watch list** ({len(tier2_in_action)} entities):")
            # Show top 10 by composite
            for e in sorted(tier2_in_action, key=lambda x: -x.get("scores", {}).get("composite", 0))[:10]:
                bottleneck = e.get("scores", {}).get("actionability", {}).get("readiness_bottleneck", "")
                lines.append(f"- {e['name']} (Bottleneck: {bottleneck})")
            if len(tier2_in_action) > 10:
                lines.append(f"- *...and {len(tier2_in_action) - 10} more*")
            lines.append("")

    return "\n".join(lines)


def generate_appendix(tier1):
    """Generate the scoring appendix for Tier 1 entities."""
    lines = [
        "## 6. Appendix: Scoring Details\n",
        "Full scoring breakdown for all Tier 1 entities.\n",
    ]

    for e in sorted(tier1, key=lambda x: -x.get("scores", {}).get("composite", 0)):
        scores = e.get("scores", {})
        dacc = scores.get("dacc", {})
        act = scores.get("actionability", {})
        trans = scores.get("transformative", {})
        research = e.get("research", {})

        lines.append(f"### {e['name']}")
        lines.append(f"**Composite: {scores.get('composite', '?')}** | Group: {e.get('group', '?')} | TRL: {research.get('trl', '?')} | v2 consensus: {'Yes' if e.get('v2_consensus') else 'No'}\n")

        lines.append("| Dimension | Score | Evidence |")
        lines.append("|-----------|-------|----------|")
        for dim in ["democratic", "decentralized", "defensive", "differential"]:
            score = dacc.get(dim, "?")
            evidence = dacc.get(f"{dim}_evidence", "N/A")
            # Truncate long evidence for table
            if len(evidence) > 200:
                evidence = evidence[:197] + "..."
            lines.append(f"| d/acc: {dim.capitalize()} | {score}/5 | {evidence} |")

        lines.append(f"| **d/acc Total** | **{dacc.get('total', '?')}/20** | {dacc.get('dacc_summary', '')} |")
        lines.append(f"| Transformative | {trans.get('score', '?')}/5 | {trans.get('evidence', 'N/A')[:200]} |")
        lines.append(f"| Bottleneck | {act.get('readiness_bottleneck', '?')} | {act.get('readiness_bottleneck_evidence', 'N/A')[:200]} |")
        lines.append(f"| Action | {act.get('what_to_do_now', '?')} | {act.get('what_to_do_now_evidence', 'N/A')[:200]} |")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def async_main(args):
    # Load input
    input_file = CONFIG["input_file"]
    if not input_file.exists():
        print(f"ERROR: {input_file} not found")
        return

    with open(input_file) as f:
        data = json.load(f)

    tier1 = data["tier1"]
    tier2 = data["tier2"]
    print(f"Loaded {len(tier1)} Tier 1 + {len(tier2)} Tier 2 entities from {input_file}")

    # Resume support
    progress_file = CONFIG["progress_file"]
    output_file = CONFIG["output_file"]
    CONFIG["output_dir"].mkdir(parents=True, exist_ok=True)

    sections = {}
    if args.resume and progress_file.exists():
        sections, _ = load_progress(progress_file)
        print(f"Resuming: {len(sections)} sections already generated")

    # API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set")
        return
    client = anthropic.AsyncAnthropic(api_key=api_key)

    sem = asyncio.Semaphore(CONFIG["semaphore_limit"])
    stats = compute_stats(tier1, tier2)
    total_in_tok = 0
    total_out_tok = 0

    # --- Section 1+2: Executive Summary + Methodology ---
    if "intro" not in sections:
        print("\nGenerating executive summary + methodology...")
        text, in_tok, out_tok = await generate_intro(client, sem, tier1, tier2, stats)
        if text:
            sections["intro"] = text
            total_in_tok += in_tok
            total_out_tok += out_tok
            save_progress(sections, {"in_tok": total_in_tok, "out_tok": total_out_tok}, progress_file)
        else:
            print("ERROR: Failed to generate intro section")
            return
    else:
        print("Intro section: cached")

    # --- Section 3: Tier 1 entity write-ups ---
    print(f"\nGenerating Tier 1 write-ups ({len(tier1)} entities)...")
    entities_to_generate = []
    for idx, entity in enumerate(tier1):
        key = f"entity_{idx}"
        if key not in sections:
            entities_to_generate.append((idx, entity, key))
        else:
            print(f"  [entity {idx + 1}/{len(tier1)}] {entity['name'][:50]}: cached")

    if entities_to_generate:
        # Process in batches respecting semaphore
        tasks = []
        for idx, entity, key in entities_to_generate:
            task = generate_entity_writeup(client, sem, entity, idx, len(tier1))
            tasks.append((key, entity, task))

        results = await asyncio.gather(*[t for _, _, t in tasks])

        for (key, entity, _), (text, in_tok, out_tok) in zip(tasks, results):
            if text:
                sections[key] = text
                total_in_tok += in_tok
                total_out_tok += out_tok
            else:
                print(f"  WARNING: Failed to generate write-up for {entity['name']}")
                sections[key] = f"### {entity['name']}\n\n*Write-up generation failed.*\n"

        save_progress(sections, {"in_tok": total_in_tok, "out_tok": total_out_tok}, progress_file)

    # --- Sections 4-6: Pure Python (no API) ---
    print("\nGenerating tables and appendix (no API calls)...")
    sections["tier2_table"] = generate_tier2_table(tier2)
    sections["involvement"] = generate_involvement_matrix(tier1, tier2)
    sections["appendix"] = generate_appendix(tier1)

    # --- Assemble final report ---
    print("\nAssembling final report...")
    report_parts = [
        "# Hyper-Entities V3: Spotlight Report\n",
        "Linda Petrini  ",
        "Foresight Institute  ",
        f"March 2026\n",
        "---\n",
        sections.get("intro", ""),
        "\n---\n",
        "## 3. Spotlight Entities (Tier 1)\n",
        f"The following {len(tier1)} entities scored highest on our composite metric (d/acc alignment + transformative potential + actionability). Each represents a system that doesn't yet exist but is already shaping coordination and investment.\n",
    ]

    for idx in range(len(tier1)):
        key = f"entity_{idx}"
        report_parts.append(sections.get(key, ""))
        report_parts.append("")

    report_parts.extend([
        "\n---\n",
        sections.get("tier2_table", ""),
        "\n---\n",
        sections.get("involvement", ""),
        "\n---\n",
        sections.get("appendix", ""),
    ])

    report_text = "\n".join(report_parts)

    # Write output
    with open(output_file, "w") as f:
        f.write(report_text)

    # Cost calculation
    cost_in = (total_in_tok / 1_000_000) * INPUT_COST_PER_M
    cost_out = (total_out_tok / 1_000_000) * OUTPUT_COST_PER_M
    total_cost = round(cost_in + cost_out, 2)

    print(f"\n{'=' * 60}")
    print(f"DONE — Report generated: {output_file}")
    print(f"Tokens: {total_in_tok:,} input / {total_out_tok:,} output")
    print(f"Estimated cost: ${total_cost} (${cost_in:.2f} in + ${cost_out:.2f} out)")
    print(f"Report length: {len(report_text):,} chars, {report_text.count(chr(10)):,} lines")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Generate V3 hyper-entities report")
    parser.add_argument("--dry-run", type=int, metavar="N",
                        help="Generate write-ups for only N Tier 1 entities")
    parser.add_argument("--resume", action="store_true",
                        help="Skip already-generated sections from progress file")
    args = parser.parse_args()

    # Apply dry-run limit
    if args.dry_run is not None:
        # We'll handle this by truncating tier1 in async_main — but simpler
        # to just limit in CONFIG. Instead, monkey-patch after load.
        pass

    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate Report v2: restructured entity write-ups via Claude API.

Reads enriched_entities.json + entity_research.json + source_links.json,
calls Claude to generate new-format write-ups, outputs Markdown report.

Usage:
    python generate_report_v2.py                  # Generate all sections
    python generate_report_v2.py --section entities  # Only entity write-ups
    python generate_report_v2.py --section intro     # Only intro/exec sections
    python generate_report_v2.py --dry-run           # Print prompts, no API calls
"""

import json
import argparse
import os
import re
import time
from pathlib import Path
from anthropic import Anthropic

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────

ENRICHED_JSON = "results/report_v2_data/enriched_entities.json"
RESEARCH_JSON = "results/entity_research.json"
SOURCE_LINKS_JSON = "results/source_links.json"
CONSENSUS_JSON = "results/consensus_entities.json"
OUTPUT_DIR = Path("results/report_v2_data")
OUTPUT_MD = OUTPUT_DIR / "report_v2.md"

MODEL = "claude-sonnet-4-5-20250929"
MAX_TOKENS = 2000


# ──────────────────────────────────────────────
# Data loading
# ──────────────────────────────────────────────

def load_all_data():
    """Load all data sources."""
    with open(ENRICHED_JSON) as f:
        enriched = json.load(f)

    with open(RESEARCH_JSON) as f:
        research_list = json.load(f)

    with open(SOURCE_LINKS_JSON) as f:
        source_links = json.load(f)

    with open(CONSENSUS_JSON) as f:
        consensus = json.load(f)

    # Build lookup by entity name
    research_by_name = {r["name"]: r for r in research_list}

    # Build full entity data lookup by ID
    entity_by_id = {e["id"]: e for e in consensus["entities"]}

    return enriched, research_by_name, source_links, entity_by_id


# ──────────────────────────────────────────────
# Prompt templates
# ──────────────────────────────────────────────

TIER1_SYSTEM = """You are helping write a research report about "hyper-entities" — future systems that don't exist yet but are already reorganizing coordination, investment, and narrative around their anticipated existence.

Your audience is smart generalists — think policymakers, science funders, tech executives, and intellectually curious non-specialists. They don't know this field. Write clearly, avoid jargon, and always answer "why should I care?"

Key principles:
- Lead with the problem this entity solves, not the technology
- Be honest about what we don't know and what's contested
- Include specific actors, organizations, and milestones with hyperlinks
- Don't be a cheerleader — acknowledge real barriers and open questions
- Write in a voice that's rigorous but accessible, like a good Economist article
- Keep each section concise: total ~400-500 words for the full write-up"""

TIER1_PROMPT = """Write a new-format entity profile for "{name}" using the data below.

## Data
- **Description**: {description}
- **Problems solved**: {problems_solved}
- **Why new/different**: {why_new_different}
- **Why doesn't exist yet**: {why_not_exists}
- **Evidence from sources**: {evidence}
- **Maturity**: {maturity}
- **d/acc score**: {dacc_total}/20 (Democratic: {dacc_dem}, Decentralized: {dacc_dec}, Defensive: {dacc_def}, Differential: {dacc_dif})
- **Tech impact score**: {tech_total_str}
- **d/acc reasoning**: {dacc_reasoning}

## Current State of Art (from our research)
{sota}

## Next Steps & Challenges (from our research)
{next_steps}

## Available hyperlinks for inline citations
{source_links_str}

## Output format (Markdown)

### {name}
`{maturity}` {tier_badge}

**Why it matters.** [3-4 sentences for a smart generalist: what problem does this solve? What becomes possible? Why should you care about this for human flourishing?]

*d/acc: {dacc_total}/20 | Tech: {tech_total_str}*

**Where things stand.** [Current capability level in plain language — what can we actually do today? How far are we from the vision? Include inline hyperlinks like [Organization](url).]

**Who's pushing it forward.** [Key actors, organizations, recent milestones — with inline hyperlinks. Be specific: names, dates, what they're doing.]

**Open questions & key uncertainties.** [What we don't know. What's contested. What would need to be true for this to succeed. Be honest about epistemic limits.]

IMPORTANT:
- Use the provided hyperlinks for inline citations where relevant
- Do NOT invent URLs — only use links from the "Available hyperlinks" section
- Write the profile following the exact section structure above
- Keep total length to ~400-500 words
- The maturity badge and tier badge should be on the same line as the heading"""


TIER2_PROMPT = """Write a brief 2-3 sentence summary for the following hyper-entity. Focus on what problem it solves and why it matters. Write for smart generalists.

Entity: {name}
Description: {description}
Problems solved: {problems_solved}
Maturity: {maturity}
d/acc: {dacc_total}/20 | Tech: {tech_total_str}

Output just the 2-3 sentence summary, no heading or formatting."""


GROUP_INTRO_PROMPT = """Write a 2-3 sentence introduction for the "{group_name}" thematic group in our hyper-entities report. This group contains the following entities:

{entity_list}

The introduction should:
- Explain what these entities have in common / why they cluster
- Hint at what pattern they collectively reveal
- Be written for smart generalists

Output just the 2-3 sentences, no heading."""


EXEC_SUMMARY_PROMPT = """Write an executive summary (about 600-800 words) for our Hyper-Entities Consensus Highlights Report. Use the following data:

## What are hyper-entities
A hyper-entity is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence.

## What we did
- Analyzed 108 source documents (65 podcasts, 40 world-gallery submissions, 2 AI-pathways essays, 1 x-hope document) from the Foresight Institute research community
- Extracted 300+ candidate hyper-entities via AI pipeline, scored across 3 stages (hyper-entity qualification, technology impact, d/acc values alignment)
- Two independent reviewers curated to 39 consensus entities across 9 thematic groups

## Key findings
- The scatter plot shows: {scatter_summary}
- Most undervalued entities: {undervalued_list}
- Maturity distribution: {maturity_dist}
- 9 thematic groups spanning energy, manufacturing, truth infrastructure, governance, markets, ethics, AI agency, interfaces, and science

## The AGI crowding-out problem
AGI hype absorbs disproportionate attention and funding. We identified systems that deserve comparable attention but aren't getting it. Many of these entities represent critical infrastructure for human flourishing that gets overlooked in the rush toward artificial general intelligence.

## d/acc framework
We use Vitalik Buterin's d/acc framework (Democratic, Decentralized, Defensive, Differential) as a values-alignment lens to evaluate whether technologies distribute power broadly and create positive-sum outcomes.

Write the executive summary with these sections:
1. What are hyper-entities (1 paragraph)
2. What we did and why (1 paragraph)
3. Key findings: reference the scatter plot, undervalued shortlist, thematic patterns (2-3 paragraphs)
4. Call to action: what deserves funding and attention (1 paragraph)

Write for smart generalists. Be concrete and specific. This is the most important section — it determines whether a busy reader keeps going."""


SCORE_GUIDE_PROMPT = """Write a "How to Read the Scores" section (~300 words) for our report. The report uses two scoring systems:

1. **d/acc Values Alignment (0-20)**: Based on Vitalik Buterin's d/acc framework. 4 dimensions (Democratic, Decentralized, Defensive, Differential), 0-5 each. Higher = better alignment with human flourishing values.

2. **Technology Impact (0-70)**: 14 dimensions measuring magnitude of potential effect. Higher = greater transformative power AND greater systemic risk. This is NOT a "goodness" score — it measures impact magnitude.

The scatter plot positions entities along both axes:
- **High tech + high d/acc (upper-right)**: "Sweet spot" — high-impact technologies that align with human flourishing values. Deserve priority attention.
- **High tech + low d/acc (upper-left)**: High-impact but governance-concerning. Need careful oversight and d/acc-improving interventions.
- **Lower tech + high d/acc (lower-right)**: Values-aligned but niche impact. May be important for specific communities.
- **Lower tech + low d/acc (lower-left)**: Lower priority in this framework.

10 entities have no tech score (scored N/A) — these were assessed on d/acc values but not technology impact, often because they are too conceptual for meaningful technology assessment.

Write this section for smart generalists. Help them understand what the numbers mean and don't mean. Emphasize that tech impact is magnitude, not desirability."""


AGI_CROWDOUT_PROMPT = """Write a "Why This Matters: The AGI Crowding-Out Problem" section (~400 words) for our report on hyper-entities.

The argument:
- AGI (Artificial General Intelligence) dominates technology discourse, funding, and policy attention
- This creates a crowding-out effect: other transformative technologies that could significantly benefit humanity receive disproportionately less attention
- Our report identifies 39 "hyper-entities" — future systems already shaping coordination and investment — that represent this overlooked landscape
- Many of these systems (decentralized energy, epistemic infrastructure, governance tools, etc.) are critical infrastructure for human flourishing regardless of whether AGI arrives soon or not
- The d/acc framework provides a lens for identifying technologies that distribute power, protect more than they threaten, and create positive-sum outcomes

Key data points to weave in:
- Over $200B invested in AI/AGI companies in 2024 alone
- Our most undervalued entities score highly on values alignment but receive tiny fractions of this funding
- Several entities in our list (epistemic infrastructure, governance tools) would actually help society navigate AGI safely if it does arrive

Write for smart generalists. Be measured — this isn't anti-AGI, it's pro-portfolio-diversification. The argument is that a rational technology funder should be allocating to these areas regardless of AGI timelines."""


DACC_EXPLAINER = """We adopt Vitalik Buterin's d/acc framework — originally proposed in the context of technology acceleration debates — as a values-alignment lens. The four dimensions (Democratic, Decentralized, Defensive, Differential) capture whether a technology distributes power broadly, protects more than it threatens, and creates positive-sum outcomes. This lens is applicable regardless of one's views on crypto or acceleration debates.

- **Democratic**: Does this technology enable collective decision-making, or does it concentrate decisions in elites?
- **Decentralized**: Does it distribute power broadly, or create single points of control?
- **Defensive**: Does it favor protection over harm? Is it defense-favoring?
- **Differential**: Does it create positive asymmetries — improving defense and freedom more than enabling attack and control?

We score each entity 0-5 on each dimension (max 20). A high d/acc score signals that a technology, if realized, would likely expand human agency and resilience rather than concentrate power or create new vulnerabilities."""


# ──────────────────────────────────────────────
# API calling
# ──────────────────────────────────────────────

def get_api_key():
    """Get API key from environment or .env file."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        env_path = Path(".env")
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("ANTHROPIC_API_KEY="):
                    api_key = line.split("=", 1)[1].strip()
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not found in environment or .env file")
    return api_key


# Lazy-initialized client
_client = None


_api_call_count = 0
_api_errors = []


def call_claude(system: str, prompt: str, max_tokens: int = MAX_TOKENS, dry_run: bool = False) -> str:
    """Call Claude API and return the response text. Handles errors gracefully."""
    if dry_run:
        print(f"  [DRY RUN] Would send prompt ({len(prompt)} chars)")
        return "[DRY RUN — no output generated]"

    global _client, _api_call_count
    if _client is None:
        _client = Anthropic(api_key=get_api_key())

    _api_call_count += 1

    for attempt in range(3):
        try:
            message = _client.messages.create(
                model=MODEL,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": "user", "content": prompt}],
            )
            return message.content[0].text
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)

            # Credit / billing errors — don't retry
            if any(kw in error_msg.lower() for kw in ["credit", "billing", "insufficient", "quota", "rate_limit"]):
                print(f"\n  *** API ERROR (call #{_api_call_count}): {error_type}: {error_msg}")
                print(f"  *** Saving partial results and stopping. ***")
                _api_errors.append({"call": _api_call_count, "error": error_msg})
                raise

            # Transient errors — retry with backoff
            if attempt < 2:
                wait = (attempt + 1) * 5
                print(f"  ⚠ Retry {attempt+1}/2 after {error_type}: {error_msg[:80]}... (waiting {wait}s)")
                _api_errors.append({"call": _api_call_count, "error": error_msg, "retried": True})
                time.sleep(wait)
            else:
                print(f"\n  *** API ERROR after 3 attempts (call #{_api_call_count}): {error_type}: {error_msg}")
                _api_errors.append({"call": _api_call_count, "error": error_msg})
                return f"[ERROR: API call failed — {error_type}: {error_msg[:100]}]"

    return "[ERROR: unexpected fallthrough]"


def strip_leading_headings(text):
    """Strip leading markdown headings and downgrade remaining headings for structural
    sections where we add our own headings in the report assembly."""
    # Strip the very first heading line
    text = re.sub(r'^#{1,4}\s+.*\n+', '', text).strip()
    # Downgrade remaining headings by one level (## -> ###, ### -> ####)
    # so they nest properly under our ## section headings
    text = re.sub(r'^(#{2,5})\s', lambda m: m.group(1) + '# ', text, flags=re.MULTILINE)
    return text


# ──────────────────────────────────────────────
# Entity write-up generation
# ──────────────────────────────────────────────

def generate_tier1_writeup(entity, research, source_links, full_entity, dry_run=False):
    """Generate a Tier 1 entity write-up."""
    name = entity["name"]

    # Get research data
    sota = research.get("sota", "No state-of-art data available.")
    next_steps = research.get("next_steps", "No next-steps data available.")

    # Build source links string (filter to relevant ones)
    links_str = "\n".join(f"- [{k}]({v})" for k, v in source_links.items())

    # d/acc breakdown
    dacc = entity.get("dacc_breakdown") or {}

    tech_total_str = f"{entity['tech_total']}/70" if entity['tech_total'] else "N/A"

    tier_badge = ""  # Tier 1 entities don't need a badge — they're the full write-ups

    prompt = TIER1_PROMPT.format(
        name=name,
        description=entity.get("description", ""),
        problems_solved=entity.get("problems_solved", ""),
        why_new_different=entity.get("why_new_different", ""),
        why_not_exists=entity.get("why_not_exists", ""),
        evidence=entity.get("evidence", ""),
        maturity=entity.get("maturity", ""),
        dacc_total=entity.get("dacc_total", "N/A"),
        dacc_dem=dacc.get("democratic", "?"),
        dacc_dec=dacc.get("decentralized", "?"),
        dacc_def=dacc.get("defensive", "?"),
        dacc_dif=dacc.get("differential", "?"),
        tech_total_str=tech_total_str,
        dacc_reasoning=entity.get("dacc_reasoning", ""),
        sota=sota,
        next_steps=next_steps,
        source_links_str=links_str,
        tier_badge=tier_badge,
    )

    print(f"  Generating Tier 1: {name}...")
    result = call_claude(TIER1_SYSTEM, prompt, max_tokens=1500, dry_run=dry_run)
    time.sleep(0.5)  # Rate limiting
    return result


def generate_tier2_summary(entity, dry_run=False):
    """Generate a Tier 2 entity summary."""
    tech_total_str = f"{entity['tech_total']}/70" if entity['tech_total'] else "N/A"

    prompt = TIER2_PROMPT.format(
        name=entity["name"],
        description=entity.get("description", ""),
        problems_solved=entity.get("problems_solved", ""),
        maturity=entity.get("maturity", ""),
        dacc_total=entity.get("dacc_total", "N/A"),
        tech_total_str=tech_total_str,
    )

    print(f"  Generating Tier 2: {entity['name']}...")
    result = call_claude(TIER1_SYSTEM, prompt, max_tokens=300, dry_run=dry_run)
    time.sleep(0.3)
    return result


def generate_group_intro(group_name, entities_in_group, dry_run=False):
    """Generate a group introduction."""
    entity_list = "\n".join(
        f"- {e['name']} ({e['maturity']}, d/acc: {e.get('dacc_total', 'N/A')}/20)"
        for e in entities_in_group
    )

    prompt = GROUP_INTRO_PROMPT.format(
        group_name=group_name,
        entity_list=entity_list,
    )

    print(f"  Generating group intro: {group_name}...")
    result = call_claude(TIER1_SYSTEM, prompt, max_tokens=400, dry_run=dry_run)
    time.sleep(0.3)
    return result


# ──────────────────────────────────────────────
# Report assembly
# ──────────────────────────────────────────────

def generate_structural_sections(enriched, dry_run=False):
    """Generate exec summary, score guide, AGI crowding-out section."""
    sections = {}

    # Compute summary stats for exec summary
    entities = enriched["entities"]
    maturity_counts = {}
    for e in entities:
        m = e["maturity"]
        maturity_counts[m] = maturity_counts.get(m, 0) + 1
    maturity_dist = ", ".join(f"{k}: {v}" for k, v in maturity_counts.items())

    undervalued = [e for e in entities if e["id"] in enriched.get("undervalued_ids", [])]
    undervalued_list = ", ".join(e["name"] for e in undervalued)

    scatter_summary = (
        "29 entities plotted on d/acc alignment (x) vs technology impact (y). "
        "The upper-right quadrant ('sweet spot') contains entities with both high impact and "
        "strong values alignment, including Automated Scientific Publishing, LexCommons, and "
        "Competitive Governance Protocol Stack. The upper-left quadrant highlights high-impact "
        "technologies needing governance attention (BCIs, Mind Uploading). Most entities cluster "
        "in the mid-range, suggesting a landscape of emerging systems with moderate but growing impact."
    )

    # Executive summary
    print("\nGenerating executive summary...")
    prompt = EXEC_SUMMARY_PROMPT.format(
        scatter_summary=scatter_summary,
        undervalued_list=undervalued_list,
        maturity_dist=maturity_dist,
    )
    sections["exec_summary"] = strip_leading_headings(
        call_claude(TIER1_SYSTEM, prompt, max_tokens=2000, dry_run=dry_run))

    # How to read the scores
    print("Generating 'How to Read the Scores'...")
    sections["score_guide"] = strip_leading_headings(
        call_claude(TIER1_SYSTEM, SCORE_GUIDE_PROMPT, max_tokens=1000, dry_run=dry_run))

    # AGI crowding-out
    print("Generating 'AGI Crowding-Out Problem'...")
    sections["agi_crowdout"] = strip_leading_headings(
        call_claude(TIER1_SYSTEM, AGI_CROWDOUT_PROMPT, max_tokens=1200, dry_run=dry_run))

    return sections


def assemble_report(enriched, research_by_name, source_links, entity_by_id, dry_run=False, test=False):
    """Generate all content and assemble the full report."""
    entities = enriched["entities"]

    # ── Structural sections ──
    struct_sections = generate_structural_sections(enriched, dry_run=dry_run)

    # ── Entity write-ups by group ──
    groups = enriched["cluster_groups"]
    group_content = {}

    # In test mode, only process the first group that has both tiers
    if test:
        test_group = None
        for g in groups:
            ge = [e for e in entities if e["cluster_name"] == g]
            if any(e["tier"] == 1 for e in ge) and any(e["tier"] == 2 for e in ge):
                test_group = g
                break
        if test_group:
            groups = [test_group]
            print(f"\n  [TEST MODE] Only processing group: {test_group}")
        else:
            groups = groups[:1]
            print(f"\n  [TEST MODE] Only processing group: {groups[0]}")

    for group in groups:
        group_entities = [e for e in entities if e["cluster_name"] == group]
        tier1 = [e for e in group_entities if e["tier"] == 1]
        tier2 = [e for e in group_entities if e["tier"] == 2]

        # In test mode, limit to 1 of each
        if test:
            tier1 = tier1[:1]
            tier2 = tier2[:1]

        # Group intro
        group_intro = generate_group_intro(group, group_entities, dry_run=dry_run)

        # Tier 1 write-ups
        tier1_writeups = []
        for e in tier1:
            research = research_by_name.get(e["name"], {})
            writeup = generate_tier1_writeup(e, research, source_links, entity_by_id.get(e["id"], {}), dry_run=dry_run)
            tier1_writeups.append(writeup)

        # Tier 2 table
        tier2_rows = []
        for e in tier2:
            summary = generate_tier2_summary(e, dry_run=dry_run)
            tech_str = f"{e['tech_total']}/70" if e['tech_total'] else "N/A"
            tier2_rows.append({
                "name": e["name"],
                "maturity": e["maturity"],
                "dacc": f"{e.get('dacc_total', 'N/A')}/20",
                "tech": tech_str,
                "summary": summary,
            })

        group_content[group] = {
            "intro": group_intro,
            "tier1_writeups": tier1_writeups,
            "tier2_rows": tier2_rows,
        }

    # ── Assemble Markdown ──
    md = []

    # Title
    md.append("# Hyper-Entities: Consensus Highlights Report\n")
    md.append("Linda Petrini & Beatrice Erkers  ")
    md.append("Foresight Institute  ")
    md.append("February 2026\n")
    md.append("---\n")

    # Executive Summary
    md.append("## Executive Summary\n")
    md.append(struct_sections["exec_summary"])
    md.append("\n---\n")

    # Introduction
    md.append("## Introduction\n")
    md.append("### What Are Hyper-Entities?\n")
    md.append("""A *hyper-entity* is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence.

Three characteristics define a hyper-entity:

1. **Non-existent but treated as real** — the system doesn't exist yet, but people act as if it will.
2. **Creates new action spaces** — it would enable fundamentally new things humans can do.
3. **Pre-real effects** — it already reorganizes coordination, investment, and narrative *now*.

Historical examples include the Internet (pre-1990s), which reorganized telecoms R&D, policy, and venture capital before widespread deployment; the Space Race (1950s-60s), where Moon missions organized national budgets and education systems before any launches; and AGI today, which reshapes AI research priorities, corporate strategies, and policy discussions despite not yet existing.\n""")

    md.append("### Project Overview\n")
    md.append("""This project set out to systematically identify, score, and curate hyper-entities emerging from the discourse around the Foresight Institute's research community. The source material comprises:

- **65 podcast transcripts** from the Foresight Institute podcast series
- **40 world-gallery submissions** from the Foresight Institute's Existential Hope project
- **2 AI-pathways essays**, including Vitalik Buterin's d/acc framework
- **1 x-hope document** providing additional framing

From this corpus, over 300 candidate hyper-entities were extracted, scored across three assessment stages, clustered thematically, and then curated through an independent review process by two researchers (Linda Petrini and Beatrice Erkers) to arrive at a final consensus list of 39 highlighted entities.\n""")

    md.append("### Why This Matters: The AGI Crowding-Out Problem\n")
    md.append(struct_sections["agi_crowdout"])
    md.append("\n")

    # Methodology
    md.append("## Methodology\n")
    md.append("""### Three-Stage Scoring Pipeline

Scoring was performed by Claude (Anthropic's AI assistant) via API, with human review and curation at each stage. The final entity selection was entirely human-driven through independent shortlisting by two researchers.

**Stage 1: Hyper-Entity Qualification (max 27).** Each candidate is scored on 9 axes (0-3 per axis): Non-existence, Plausibility, Design specificity, New action space, Roadmap clarity, Coordination gravity, Resource pull, Narrative centrality, and Pre-real effects. A candidate must score 18 or above to qualify.

**Stage 2: Technology Impact Assessment (max 70).** Qualified entities are scored on 14 dimensions (0-5 each) measuring the magnitude of potential effect — not desirability. Higher scores indicate greater transformative power *and* greater systemic risk.

**Stage 3: d/acc Values Alignment (max 20).** Based on Vitalik Buterin's d/acc framework, evaluating whether a technology aligns with values that promote human flourishing.\n""")

    md.append("### The d/acc Framework\n")
    md.append(DACC_EXPLAINER)
    md.append("\n")

    md.append("### How to Read the Scores\n")
    md.append(struct_sections["score_guide"])
    md.append("\n")

    md.append("""### Curation Process

After automated extraction and scoring, entities were curated through independent review:

1. **Independent shortlisting**: Linda and Beatrice each independently reviewed the full set and starred those they considered most significant. Linda selected 88; Beatrice selected 67.
2. **Overlap identification**: 26 entities were starred by *both* reviewers (20.2% overlap rate), forming the core consensus set.
3. **Cross-review voting**: Each reviewer then reviewed the other's unique picks, voting Yes on entities they also found compelling.
4. **Final list**: The resulting 39 entities (26 shared + 8 + 5 cross-reviewed) constitute the consensus highlights.\n""")

    # Key Findings
    md.append("## Key Findings\n")

    md.append("### The Landscape: d/acc Alignment vs. Technology Impact\n")
    md.append("![Scatter plot: d/acc alignment vs technology impact](scatter_plot.png)\n")
    md.append("*29 of 39 entities plotted; 10 entities excluded due to missing technology impact scores.*\n\n")

    md.append("### Most Undervalued Shortlist\n")
    md.append("The following entities score well on our framework but receive disproportionately little attention and funding:\n\n")
    undervalued = [e for e in entities if e["id"] in enriched.get("undervalued_ids", [])]
    for e in undervalued:
        tech_str = f"Tech: {e['tech_total']}/70" if e['tech_total'] else "Tech: N/A"
        md.append(f"- **{e['name']}** — d/acc: {e.get('dacc_total', 'N/A')}/20, {tech_str}\n")
    md.append("\n")

    md.append("### Maturity Distribution\n")
    maturity_counts = {}
    for e in entities:
        m = e["maturity"]
        maturity_counts[m] = maturity_counts.get(m, 0) + 1
    md.append("| Maturity Level | Count |\n|---|---|\n")
    for level in ["Foundational Research", "Early Demonstrations", "Scaling Challenges", "Near Deployment"]:
        md.append(f"| {level} | {maturity_counts.get(level, 0)} |\n")
    md.append("\n")

    # Consensus Entities
    md.append("## Consensus Entities\n")
    md.append(f"The 39 consensus entities are organized into nine thematic groups. "
              f"{enriched['tier1_count']} entities receive full write-ups; "
              f"{enriched['tier2_count']} are presented in summary format.\n\n")

    for group in groups:
        gc = group_content[group]
        md.append(f"### {group}\n")
        md.append(gc["intro"])
        md.append("\n\n")

        # Tier 1 write-ups
        for writeup in gc["tier1_writeups"]:
            md.append(writeup)
            md.append("\n\n")

        # Tier 2 table
        if gc["tier2_rows"]:
            md.append("#### Additional Entities\n\n")
            md.append("| Entity | Maturity | d/acc | Tech | Summary |\n")
            md.append("|--------|----------|-------|------|---------|\n")
            for row in gc["tier2_rows"]:
                # Clean summary for table (remove newlines)
                summary = row["summary"].replace("\n", " ").strip()
                md.append(f"| {row['name']} | {row['maturity']} | {row['dacc']} | {row['tech']} | {summary} |\n")
            md.append("\n")

    # Conclusion
    md.append("## Conclusion\n")
    md.append("*[To be written after entity content review]*\n\n")

    # Appendix
    md.append("## Appendix: Full Scoring Tables\n")
    md.append("| Entity | Stage 1 | Tech Impact | d/acc | Maturity | Group |\n")
    md.append("|--------|---------|-------------|-------|----------|-------|\n")
    for e in sorted(entities, key=lambda x: x["name"]):
        tech_str = str(e['tech_total']) if e['tech_total'] else "N/A"
        dacc_str = str(e.get('dacc_total', 'N/A'))
        md.append(f"| {e['name']} | {e.get('stage1_total', 'N/A')} | {tech_str} | {dacc_str} | {e['maturity']} | {e['cluster_name']} |\n")
    md.append("\n")

    report = "\n".join(md)

    # Save
    with open(OUTPUT_MD, "w") as f:
        f.write(report)
    print(f"\nReport saved to {OUTPUT_MD}")

    # Also save the raw generated content as JSON for review
    raw_output = {
        "structural_sections": struct_sections,
        "group_content": {
            group: {
                "intro": gc["intro"],
                "tier1_writeups": gc["tier1_writeups"],
                "tier2_summaries": [r["summary"] for r in gc["tier2_rows"]],
            }
            for group, gc in group_content.items()
        },
    }
    with open(OUTPUT_DIR / "generated_content.json", "w") as f:
        json.dump(raw_output, f, indent=2)
    print(f"Raw content saved to {OUTPUT_DIR / 'generated_content.json'}")

    return report


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate Report v2")
    parser.add_argument("--section", choices=["entities", "intro", "all"], default="all",
                        help="Which sections to generate")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print prompts without making API calls")
    parser.add_argument("--test", action="store_true",
                        help="Test mode: generate 1 Tier 1, 1 Tier 2, 1 group intro, and structural sections only")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading data...")
    enriched, research_by_name, source_links, entity_by_id = load_all_data()
    print(f"Loaded {len(enriched['entities'])} entities, {len(research_by_name)} research entries, {len(source_links)} source links")

    entities = enriched["entities"]
    tier1 = [e for e in entities if e["tier"] == 1]
    tier2 = [e for e in entities if e["tier"] == 2]
    print(f"Tier 1: {len(tier1)} entities (full write-up)")
    print(f"Tier 2: {len(tier2)} entities (summary table)")
    print(f"Groups: {len(enriched['cluster_groups'])}")

    if args.dry_run:
        print("\n*** DRY RUN MODE — no API calls will be made ***\n")
    if args.test:
        print("\n*** TEST MODE — only generating a few sections ***\n")

    try:
        report = assemble_report(enriched, research_by_name, source_links, entity_by_id, dry_run=args.dry_run, test=args.test)
        word_count = len(report.split())
        print(f"\nTotal report: ~{word_count} words")
    except Exception as e:
        print(f"\n{'='*60}")
        print(f"FATAL ERROR: {type(e).__name__}: {e}")
        print(f"{'='*60}")
        print(f"API calls completed before failure: {_api_call_count}")
        if _api_errors:
            print(f"Errors encountered: {len(_api_errors)}")
            for err in _api_errors:
                print(f"  Call #{err['call']}: {err['error'][:120]}")

        # Try to save whatever we have
        partial_path = OUTPUT_DIR / "partial_content.json"
        try:
            partial = {"api_calls_completed": _api_call_count, "errors": _api_errors}
            with open(partial_path, "w") as f:
                json.dump(partial, f, indent=2)
            print(f"\nPartial error log saved to {partial_path}")
        except Exception:
            pass

        print("\nTo resume, fix the issue and re-run. Already-generated content")
        print("can be found in generated_content.json if it was saved before the error.")
        return

    # Summary
    print(f"\n{'='*60}")
    print(f"GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"API calls made: {_api_call_count}")
    if _api_errors:
        print(f"Errors (recovered): {len(_api_errors)}")
    print(f"Report: {OUTPUT_MD}")
    print(f"Raw content: {OUTPUT_DIR / 'generated_content.json'}")


if __name__ == "__main__":
    main()

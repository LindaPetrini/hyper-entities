# Hyper-Entities

Systematic identification, scoring, and curation of **hyper-entities** from the Foresight Institute research community.

A hyper-entity is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence.

## Key Links

| | |
|---|---|
| **[Entity Explorer Dashboard](https://lindapetrini.github.io/hyper-entities/results/dashboard.html)** | All 345 extracted entities with dual scoring, search, and cluster visualization |
| **[Consensus Highlights](https://lindapetrini.github.io/hyper-entities/results/highlights.html)** | 39 curated entities organized into 9 thematic groups with research summaries |
| **[Full Report (PDF)](results/report.pdf)** | Methodology, scoring framework, all 39 entities with state-of-the-art and next-steps analysis, 147 source links |
| **[Part II Proposal (PDF)](results/proposal_part2.pdf)** | One-pager for turning research into action via coordination.network, owockibot bounties, and Drips funding |

## Process

**Extraction** — 345 hyper-entities extracted from 108 Foresight Institute sources (podcasts, world-gallery submissions, essays) using a three-stage scoring pipeline:

- **Stage 1** (Hyper-Entity Qualification): 9 axes, 0–3 each, max 27. Threshold ≥18.
- **Stage 2** (Technology Impact): 14 dimensions, 0–5 each, max 70.
- **Stage 3** (d/acc Values Alignment): 4 dimensions (Democratic, Decentralized, Defensive, Differential), 0–5 each, max 20.

**Curation** — Linda Petrini and Beatrice Erkers independently reviewed all scored entities, then cross-voted on each other's unique picks, producing a consensus list of 39 highlighted entities.

**Research** — Each of the 39 entities was enriched with two paragraphs: current state of the art and viable next steps / key challenges.

**Grouping** — The 39 entities are organized into 9 thematic groups:

1. Energy & Infrastructure (3)
2. Manufacturing & Matter (4)
3. Truth & Epistemic Infrastructure (4)
4. Governance & Collective Intelligence (6)
5. Markets & Incentive Systems (3)
6. Ethics & Moral Expansion (2)
7. AI & Human Agency (4)
8. Interfaces & Augmentation (7)
9. Science & Discovery (6)

## Project Structure

```
├── results/
│   ├── dashboard.html                  # Full entity explorer (345 entities)
│   ├── highlights.html                 # Consensus highlights (39 entities)
│   ├── report.typ                      # Full report (Typst source)
│   ├── report.pdf                      # Full report (compiled)
│   ├── proposal_part2.typ              # Part II proposal (Typst source)
│   ├── proposal_part2.pdf              # Part II proposal (compiled)
│   ├── consensus_entities.json         # 39 consensus entities with scores
│   ├── consensus_meeting_notes.md      # Entities grouped by theme
│   ├── entity_research.json            # Research data (SOTA + next steps)
│   ├── entity_research.md              # Research (readable markdown)
│   ├── cluster_analysis.json           # Clustering data
│   └── stage1_extraction/              # Raw extraction results
├── create_dashboard.py                 # Dashboard generator
├── analyze_clusters.py                 # Thematic clustering
├── score_dacc.py                       # d/acc scoring (requires API key)
├── METHODOLOGY.md                      # Full scoring framework
└── CLAUDE.md                           # Project instructions
```

## Commands

```bash
python create_dashboard.py   # Regenerate main dashboard
python score_dacc.py         # Score entities on d/acc dimensions (requires API key)
typst compile results/report.typ results/report.pdf  # Compile report
```

## Credits

Linda Petrini & Beatrice Erkers, Foresight Institute. Extraction and analysis conducted with Claude.

---

**Last updated:** 2026-02-09

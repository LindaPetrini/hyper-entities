# Hyper-Entities

Systematic identification, scoring, and curation of **hyper-entities** from the Foresight Institute research community.

A hyper-entity is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence. Term coined by Michael Nielsen.

## Key Links

| | |
|---|---|
| **[Entity Explorer Dashboard](https://lindapetrini.github.io/hyper-entities/results/dashboard.html)** | All 345 extracted entities with scoring, search, and cluster visualization |
| **[Full Report (Markdown)](results/report_v2_data/report_v2.md)** | v2 report: methodology, all 39 consensus entities with deep write-ups, conclusion |
| **[Full Report (Word/GDoc)](results/report_v2_data/report_v2.docx)** | Same report as .docx — import to Google Docs to collaborate |
| **[Part II Proposal (PDF)](results/proposal_part2.pdf)** | One-pager for turning research into action |

## Process

**Extraction** — 345 hyper-entities extracted from 108 Foresight Institute sources (podcasts, world-gallery submissions, essays) using a three-stage scoring pipeline. All scores are displayed normalized to 0–100%:

- **Stage 1** (Hyper-Entity Qualification): 9 axes, max 27. Threshold ≥67% (18/27).
- **Stage 2** (Technology Impact): 14 dimensions, max 70.
- **Stage 3** (d/acc Values Alignment): 4 dimensions (Democratic, Decentralized, Defensive, Differential), max 20. Based on Vitalik Buterin's [d/acc framework](https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html).

**Curation** — Linda Petrini and Beatrice Erkers independently reviewed all scored entities, then cross-voted on each other's unique picks, producing a consensus list of 39 highlighted entities.

**Research** — Each of the 39 entities was enriched with full write-ups: why it matters, current state of the art, who's pushing it forward, and open questions.

**Grouping** — The 39 entities are organized into 9 thematic groups:

1. Energy & Infrastructure (3)
2. Manufacturing & Matter (4)
3. Truth & Epistemic Infrastructure (4)
4. Governance & Collective Intelligence (6)
5. Markets & Incentive Systems (2, after merge)
6. Ethics & Moral Expansion (2)
7. AI & Human Agency (4)
8. Mind, Brain & Human Augmentation (7)
9. Science & Discovery (6)

## Project Structure

```
├── results/
│   ├── dashboard.html                  # Full entity explorer (345 entities)
│   ├── report_v2_data/
│   │   ├── report_v2.md                # Full report (Markdown source)
│   │   ├── report_v2.docx              # Full report (Word/GDoc import)
│   │   ├── scatter_plot.svg/png        # d/acc vs Technology scatter plot
│   │   ├── enriched_entities.json      # Entity data with enriched metadata
│   │   └── generated_content.json      # AI-generated write-ups per entity
│   ├── proposal_part2.pdf              # Part II proposal
│   ├── cluster_analysis.json           # Clustering data
│   ├── stage1_extraction/              # Raw Stage 1 extraction results
│   ├── stage2_assessment/              # Stage 2 technology scoring
│   └── stage3_concrete/                # Stage 3 d/acc + concreteness scoring
├── create_dashboard.py                 # Dashboard generator
├── prepare_report_v2.py                # Prepares enriched entity data for report
├── generate_report_v2.py               # Generates full report from entity data
├── create_scatter_plot.py              # Generates d/acc vs Tech scatter plot
├── analyze_clusters.py                 # Thematic clustering
├── score_dacc.py                       # d/acc scoring (requires API key)
├── METHODOLOGY.md                      # Full scoring framework
└── CLAUDE.md                           # Project instructions
```

## Commands

```bash
python create_dashboard.py      # Regenerate main dashboard
python prepare_report_v2.py     # Prepare enriched data (requires API key)
python generate_report_v2.py    # Generate v2 report markdown + docx
python create_scatter_plot.py   # Regenerate scatter plot
python score_dacc.py            # Score entities on d/acc dimensions (requires API key)
```

## Collaboration Workflow

The `.docx` file can be imported directly into Google Docs (File → Open) for collaborative editing and comments. To incorporate feedback from GDoc back into the source:
1. Export the GDoc as HTML (File → Download → Web Page)
2. Drop the path here for Claude to extract comments and apply them to `report_v2.md`
3. Re-run `generate_report_v2.py` or regenerate the `.docx` via pandoc

## Credits

Linda Petrini & Beatrice Erkers, Foresight Institute. Extraction and analysis conducted with Claude.

---

**Last updated:** 2026-02-19

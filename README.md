# Hyper-Entities

Systematic identification, scoring, and curation of **hyper-entities** from the Foresight Institute research community.

A hyper-entity is a coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence. Term coined by Michael Nielsen.

## Key Links

| | |
|---|---|
| **[Entity Explorer Dashboard (v3)](https://lindapetrini.github.io/hyper-entities/results/v3/dashboard.html)** | All 189 entities with scoring, search, and cluster visualization |
| **[Spotlight Report (Typst source)](results/v3/report_v3.typ)** | v3 report: 19 Tier 1 spotlight entities, watch list, methodology |
| **[Entity Explorer Dashboard (v2)](https://lindapetrini.github.io/hyper-entities/results/dashboard.html)** | Legacy v2 dashboard with 345 entities |
| **[v2 Report (Markdown)](results/report_v2_data/report_v2.md)** | v2 report: methodology, 39 consensus entities with deep write-ups |
| **[Part II Proposal (PDF)](results/proposal_part2.pdf)** | One-pager for turning research into action |

## Process (v3)

**Extraction** — 189 hyper-entities extracted from 109 Foresight Institute sources (podcasts, world-gallery submissions, essays) using a multi-stage pipeline.

**Scoring** — Each entity scored on three dimensions:
- **d/acc Values Alignment**: 4 dimensions (Democratic, Decentralized, Defensive, Differential), max 20. Based on Vitalik Buterin's [d/acc framework](https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html).
- **Transformative Potential**: 1–5 scale.
- **Composite Score**: Combines d/acc, transformative potential, foresight relevance, and TRL.

**Research** — Each entity enriched via web search with organizations, funding, TRL (1–9), publications, state of the art, and barriers.

**Curation** — 19 Tier 1 spotlight entities and 170 Tier 2 watch list entities, based on composite score thresholds.

**Report** — Full write-ups for all 19 Tier 1 entities, involvement matrix, and action recommendations.

## Project Structure

```
├── results/
│   ├── v3/
│   │   ├── dashboard.html              # v3 entity explorer (189 entities)
│   │   ├── report_v3.typ               # v3 spotlight report (Typst source)
│   │   ├── report_v3.pdf               # v3 spotlight report (compiled PDF)
│   │   ├── scatter_plot_v3.svg/png     # d/acc vs Transformative scatter plot
│   │   └── *.json                      # Pipeline intermediate data
│   ├── dashboard.html                  # v2 entity explorer (345 entities)
│   ├── report_v2_data/
│   │   ├── report_v2.md                # v2 report (Markdown)
│   │   ├── report_v2.docx              # v2 report (Word/GDoc import)
│   │   └── scatter_plot.svg/png        # v2 scatter plot
│   ├── proposal_part2.pdf              # Part II proposal
│   ├── stage1_extraction/              # v2 Stage 1 extraction results
│   ├── stage2_assessment/              # v2 Stage 2 technology scoring
│   └── stage3_concrete/                # v2 Stage 3 d/acc scoring
├── v3_extract.py                       # v3 extraction
├── v3_dedup.py                         # v3 deduplication
├── v3_research.py                      # v3 web research enrichment
├── v3_score.py                         # v3 scoring
├── v3_curate.py                        # v3 tier curation
├── v3_report.py                        # v3 report generation
├── v3_dashboard.py                     # v3 dashboard generation
├── create_dashboard.py                 # v2 dashboard generator
├── METHODOLOGY.md                      # Full scoring framework
└── CLAUDE.md                           # Project instructions
```

## Commands

```bash
# v3 pipeline
python v3_extract.py        # Extract entities from sources
python v3_dedup.py          # Deduplicate candidates
python v3_research.py       # Enrich with web research
python v3_score.py          # Score on d/acc + transformative dimensions
python v3_curate.py         # Curate into tiers
python v3_report.py         # Generate report
python v3_dashboard.py      # Generate interactive dashboard

# v2 (legacy)
python create_dashboard.py  # Regenerate v2 dashboard
```

## Credits

Linda Petrini & Beatrice Erkers, Foresight Institute. Extraction and analysis conducted with Claude.

---

**Last updated:** 2026-03-09

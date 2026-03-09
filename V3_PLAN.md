# Hyper-Entities V3 Pipeline

## Context
The v2 pipeline produced 345 entities from 108 Existential Hope sources, but suffered from mushy extraction (vague compound nouns), circular LLM scoring (Claude scores its own extractions), poor evidence grounding, and weak deduplication. The 39 curated entities were saved by human curation, not the pipeline. V3 redesigns the pipeline to produce fewer, sharper, more actionable entities with real evidence grounding.

## Goal
Produce a report with ~15-20 spotlight entities and ~30-40 watch-list entities that are concrete, evidence-grounded, and actionable -- so a reader knows what to fund, build, research, or advocate for.

## Pipeline: 7 Scripts, 3 Human Checkpoints

```
sources/ (108 .md files)
  → [1] v3_extract.py        Sonnet 4.5    ~$15-20
  → results/v3/raw_candidates.json (60-100 candidates)
  → [2] v3_dedup.py           Haiku 3.5     ~$1-2
  → results/v3/deduplicated.json (40-70 unique)
  → === HUMAN CHECKPOINT 1: review list ===
  → [3] v3_research.py        Haiku 3.5     ~$3-5
  → results/v3/researched.json (+ orgs, funding, TRL, links)
  → [4] v3_score.py           Haiku 3.5     ~$1-2
  → results/v3/scored.json (d/acc + actionability + transformative potential)
  → [5] v3_curate.py          pure Python   $0
  → results/v3/curated.json (tiered)
  → === HUMAN CHECKPOINT 2: review tiers ===
  → [6] v3_report.py          Sonnet 4.5    ~$5-8
  → results/v3/report_v3.md
  → [7] v3_dashboard.py       pure Python   $0
  → results/v3/dashboard.html
  → === HUMAN CHECKPOINT 3: editorial review ===

Total estimated cost: $25-37
```

---

### Script 1: `v3_extract.py` -- Sharp Extraction

**Model:** Sonnet 4.5 | **Output:** `results/v3/raw_candidates.json`

Core change: the prompt forces specificity by requiring fields that can't be filled with vibes. NO scoring in this step -- extraction only.

**Prompt strategy** (abbreviated):
> Extract SPECIFIC proposals/systems/architectures that are:
> 1. NAMED or CONCRETE (someone could write a spec for it)
> 2. NOT YET BUILT at scale
> 3. DISCUSSED SERIOUSLY (not throwaway mentions)
>
> For each, provide: name (use speaker's name for it if given), verbatim source_quote, speaker, one_liner, mechanism (how it works), exists_today (partial existing work), source_file.
>
> ANTI-PATTERNS: generic field descriptions, vague values, already-deployed tech, compound nouns you invented. Most docs yield 0-3 candidates, not 5-10.

**Per-entity output:**
```json
{
  "name": "Deep Fision Micro Reactors",
  "source_quote": "a nuclear reactor that will fit through a manhole...",
  "speaker": "Mark Jacobson",
  "source_file": "podcast/ep42.md",
  "one_liner": "Factory-produced nuclear reactors buried underground",
  "mechanism": "Thorium-based sealed cores, 30-50yr autonomous operation...",
  "exists_today": "Deep Fision Inc. has prototype designs...",
  "source_type": "podcast"
}
```

**Reuse from v2:** chunking logic from `extract_hyperentities_v2.py`, incremental save pattern, API key loading.

---

### Script 2: `v3_dedup.py` -- Semantic Deduplication

**Model:** Haiku 3.5 | **Output:** `results/v3/deduplicated.json`

Replace TF-IDF K-means with LLM pairwise comparison:
1. TF-IDF cosine pre-filter (only compare pairs with cosine > 0.3) to reduce ~4950 pairs to ~200-500
2. Haiku judges each pair: SAME / OVERLAPPING / DISTINCT
3. Merge SAME entities (keep better name, combine sources)
4. Haiku assigns 8-12 thematic groups

---

### Script 3: `v3_research.py` -- Parallel Web Research

**Model:** Haiku 3.5 + WebSearch | **Output:** `results/v3/researched.json`

Launch parallel Haiku calls (semaphore of 10 concurrent), one per entity. Each agent:
1. **Web searches** for the entity name + key terms to find real orgs, projects, funding
2. **Synthesizes** findings into structured research output

Each must find:
- **Organizations**: 2-5 real orgs with URLs (verified via web search)
- **Funding**: specific amounts/sources/years, or "none found"
- **TRL level**: 1-9 scale with justification
- **Key publications/demos**: 1-3 with dates and URLs
- **State of the art**: 3-5 sentences on where things actually stand
- **Barriers**: 2-3 sentences on what's blocking progress

Implementation: use Claude Code's WebSearch tool within subagents, or if running as standalone scripts, use a search API (e.g., Tavily, SerpAPI) to fetch real results before passing to Haiku for synthesis.

---

### Script 4: `v3_score.py` -- Evidence-Grounded Scoring

**Model:** Haiku 3.5 | **Output:** `results/v3/scored.json`

**New scoring scheme (replaces 9+14+4 dimensions):**

**A. d/acc Values (kept, 4 dims x 0-5, max 20):**
- Democratic, Decentralized, Defensive, Differential
- NEW requirement: each score must cite specific evidence. No evidence = 0.

**B. Actionability (3 categorical dimensions, NEW):**
- **Readiness bottleneck**: Physics | Engineering | Funding | Regulation | Coordination | Social Acceptance
- **What to do now**: Fund | Build | Research | Advocate | Convene | Nothing Yet
- **Foresight connection** (0-3): how prominently discussed in source material

**C. Transformative potential (single 0-5 score, replaces 14-dim Stage 2):**
- 0=incremental, 3=transforms a field, 5=civilizational new action space
- Must cite evidence.

---

### Script 5: `v3_curate.py` -- Automated Tiering with V2 Curation Boost

**No API calls.** Two-step process:

**Step 1: Match v3 entities to v2 consensus list.**
Load `results/consensus_entities.json` (39 curated entities from v2). For each v3 entity, check if it maps to a v2 consensus entity (by name similarity or LLM match from dedup step). Matching entities get a `v2_consensus: true` flag and inherit their `voted_by` data.

**Step 2: Apply tiering rules.**
- **Tier 1 (Spotlight, ~15-20):** d/acc >= 12 AND transformative >= 3 AND foresight_connection >= 2 AND TRL >= 2. Entities with `v2_consensus: true` get a lower threshold (d/acc >= 10).
- **Tier 2 (Watch list, rest):** everything else that survived dedup + human checkpoint 1

**Human review is lighter:** Only genuinely NEW entities (not in v2 consensus) need careful manual review. V2-consensus entities are pre-validated.

Outputs `scatter_data.json` for visualization (d/acc vs transformative potential).

---

### Script 6: `v3_report.py` -- Report Generation

**Model:** Sonnet 4.5 | **Output:** `results/v3/report_v3.md`

Reuse `generate_report_v2.py` architecture. Key improvements:
- Tier 1 write-ups include research data (orgs, funding, TRL, publications, URLs)
- Standard "What can someone do RIGHT NOW?" callout per entity
- New section: "How to Get Involved" matrix (entities by actionability type)
- Keep d/acc explainer, methodology, exec summary sections

---

### Script 7: `v3_dashboard.py` -- Visualization

**No API calls.** Reuse `create_dashboard.py` as base.
- **Axes:** d/acc alignment (x) vs transformative potential (y)
- **Color:** by readiness bottleneck (Physics=red, Engineering=orange, Funding=green, Regulation=blue, Coordination=purple)
- **Shape:** Tier 1 = filled, Tier 2 = hollow
- **"What can I do?" view:** card view grouped by actionability type
- Filter by group, bottleneck, actionability, tier

---

## Key Differences from V2

| Aspect | V2 | V3 |
|--------|----|----|
| Entity count | 345 raw, 261 qualified | 60-100 raw, 40-70 final |
| Extraction | "find all potential hyper-entities" | "find SPECIFIC proposals with verbatim quotes" |
| Scoring | Claude scores its own extractions | Separate extraction → research → scoring steps |
| Evidence | Scores self-justify | No evidence = score 0 |
| Research | Manual/none | Parallel Haiku agents per entity |
| Stage 2 | 14 abstract dimensions | 1 transformative score + 3 actionability categories |
| Human checkpoints | 1 (after everything) | 3 (after dedup, after scoring, after report) |
| Actionability | Not tracked | Core dimension |

## Files to Modify/Create

**New files:**
- `v3_extract.py`
- `v3_dedup.py`
- `v3_research.py`
- `v3_score.py`
- `v3_curate.py`
- `v3_report.py`
- `v3_dashboard.py`
- `results/v3/` directory for all outputs

**Reuse patterns from:**
- `extract_hyperentities_v2.py` -- chunking, incremental saves, progress tracking
- `score_dacc.py` -- d/acc prompt structure, JSON extraction
- `generate_report_v2.py` -- report assembly, retry logic, prompt templates
- `prepare_report_v2.py` -- tiering logic, scatter data generation
- `create_dashboard.py` -- dashboard HTML/JS/D3 base

## Build Order: Incremental (build one, run, review, then next)

Each script is built, tested, and reviewed before moving to the next. This lets us course-correct early if extraction quality is off.

**Phase A: Build + run v3_extract.py**
- Build script, run on all 108 sources
- Review: check candidate count (target 60-100), verify verbatim quotes, speaker attribution
- Test: run a dry-run on 3-5 sources first to validate prompt quality before full run
- Course-correct prompt if needed, re-run

**Phase B: Build + run v3_dedup.py**
- Build script, run on raw_candidates.json
- Review: check merge log, verify no obvious duplicates, groups are coherent
- Test: print summary stats, inspect merged entities

**Phase C: Human checkpoint 1** (Linda reviews deduplicated list)

**Phase D: Build + run v3_research.py**
- Build script, test on 3 entities first (web search integration check)
- Run on full list
- Review: spot-check 5 entities -- are org names real? URLs valid? TRL reasonable?

**Phase E: Build + run v3_score.py**
- Build script, run on researched.json
- Review: verify no scores lack evidence. Check d/acc distribution isn't all clustered at same value.
- Test: print score histograms

**Phase F: Build + run v3_curate.py**
- Run, verify tier 1 count ~15-20, tier 2 ~30-40
- Check v2 consensus matching worked correctly

**Phase G: Human checkpoint 2** (Linda reviews tiers, promotes/demotes)

**Phase H: Build + run v3_report.py**
- Build, test on 2 tier-1 entities first
- Run full report generation
- Review: read report, check URLs, verify write-ups use research data

**Phase I: Build + run v3_dashboard.py**
- Build from create_dashboard.py base
- Test: open in browser, verify scatter plot, filters, "what can I do" view

**Phase J: Human checkpoint 3** (editorial review)

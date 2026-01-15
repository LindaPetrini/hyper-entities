# Hyper-Entities Version History

## v3.0 - Rigorous Dual Scoring (2026-01-14) ⭐ CURRENT

**Location:** `results/v3.0_rigorous_dual_scoring/`

First version with formal two-stage scoring framework.

**Stats:**
- 345 entities from 108 sources
- 261 qualified (≥18/27 on Stage 1)
- Dual scoring: 9 axes (Stage 1) + 14 dimensions (Stage 2)
- Cost: $5.38

**Files:**
- Dashboard: `results/v3.0_rigorous_dual_scoring/dashboard.html`
- JSON: `results/v3.0_rigorous_dual_scoring/entities.json`
- Full extraction: `results/v3.0_rigorous_dual_scoring/extraction_full.md`

**Methodology:**
- Stage 1: 9-axis qualification (Non-existence, Plausibility, Design specificity, New action space, Roadmap clarity, Coordination gravity, Resource pull, Narrative centrality, Pre-real effects)
- Stage 2: 14-dimension impact assessment (Capability Discontinuity, Cross-Domain Reach, Scalability, Autonomy, Composability, Feedback Intensity, Irreversibility, Power Concentration, Externality Magnitude, Misuse Asymmetry, Governance Lag, Narrative Lock-In, Path Dependency, Human Agency Impact)

---

## v3.1 - Organized & Expanded (PLANNED)

**Status:** In development

Refined version with entity clustering, expanded details, and consolidated scoring.

**Planned features:**
- Entity organization by similar themes/directions
- Clustering analysis to identify related entities
- Expanded descriptions with:
  - Exact problems being solved
  - Why it's new and different
  - Why it doesn't exist yet
- Consolidated 3-score system:
  - **Stage 1:** 3 consolidated scores from 9 axes
  - **Stage 2:** 3 consolidated scores from 14 dimensions
- Version dropdown in dashboard to switch between v3.0 and v3.1

**Consolidated scoring groups (proposed):**

*Stage 1 (from 9 axes → 3 scores):*
1. **Reality Gap** - How far from existing (Non-existence, Plausibility, Design specificity)
2. **Transformative Potential** - How much it changes things (New action space, Roadmap clarity)
3. **Current Momentum** - Pre-real effects now (Coordination gravity, Resource pull, Narrative centrality, Pre-real effects)

*Stage 2 (from 14 dimensions → 3 scores):*
1. **Transformative Power** - Capability & scale (Capability Discontinuity, Cross-Domain Reach, Scalability, Autonomy, Composability)
2. **Systemic Risk** - Dangers & governance gaps (Irreversibility, Power Concentration, Externality Magnitude, Misuse Asymmetry, Governance Lag)
3. **Lock-in Effects** - Path dependency & agency (Feedback Intensity, Narrative Lock-In, Path Dependency, Human Agency Impact)

---

## v2 - Early Extraction (ARCHIVED)

**Status:** Superseded by v3.0

**Issues:**
- 1,077 vague concepts extracted
- No rigorous scoring framework
- Many abstract ideas like "wonder", "care"
- No formal definition checking

**Location:** `archive/old_versions/`

---

## Version Naming Convention

- **Major version** (v3.x): Significant methodology change
- **Minor version** (v3.1): Refinements and expansions within same methodology
- **Dated snapshots**: `v3.0_rigorous_dual_scoring` (descriptive folder names)

---

**How to access versions:**
- Current: `results/hyperentities_dashboard_v4.html` (links to latest)
- Specific version: `results/v3.0_rigorous_dual_scoring/dashboard.html`
- Compare versions: Use version dropdown in dashboard (v3.1+)

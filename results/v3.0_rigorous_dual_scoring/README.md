# Hyper-Entities v3.0: Rigorous Dual Scoring

**Version:** 3.0
**Date:** 2026-01-14
**Status:** Baseline version with rigorous scoring framework

## Overview

This version represents the first rigorous extraction using a formal two-stage scoring framework.

## Key Characteristics

- **345 entities** extracted from 108 sources
- **Rigorous qualification**: 9-axis scoring (≥18/27 threshold)
- **Impact assessment**: 14-dimension scoring (0-70 scale)
- **261 qualified entities** (75.7%)
- **Average scores**: Stage 1: 19.3/27, Stage 2: 46.5/70

## Methodology

### Stage 1: Qualification Scoring (9 axes, 0-3 each)
1. Non-existence
2. Plausibility
3. Design specificity
4. New action space
5. Roadmap clarity
6. Coordination gravity
7. Resource pull
8. Narrative centrality
9. Pre-real effects

### Stage 2: Impact Assessment (14 dimensions, 0-5 each)
1. Capability Discontinuity
2. Cross-Domain Reach
3. Scalability
4. Autonomy
5. Composability
6. Feedback Intensity
7. Irreversibility
8. Power Concentration
9. Externality Magnitude
10. Misuse Asymmetry
11. Governance Lag
12. Narrative Lock-In
13. Path Dependency
14. Human Agency Impact

## Files

- `dashboard.html` - Interactive dashboard with dual scoring
- `entities.json` - All 345 entities with complete scoring (583KB)
- `extraction_full.md` - Full extraction results with justifications (13,689 lines)

## Top 10 Entities by Stage 2 Impact

1. AI-Designed Medical Nanobots (63/70)
2. AI Self-Diffusion Infrastructure (62/70)
3. Cosmological Constant Manipulation (60/70)
4. Adaptive AI-Driven Problem Solving (60/70)
5. AI Research Acceleration System (60/70)
6. Inference-Time Scaling Paradigm (60/70)
7. Brain Emulation (60/70)
8. Human Superintelligence via BCIs (60/70)
9. AI Scientist (59/70)
10. Neuroscience Architectural Understanding (59/70)

## Improvements from v2

- ❌ v2: 1,077 vague concepts → ✅ v3.0: 345 specific architectures
- ❌ v2: No scoring → ✅ v3.0: Dual scoring framework
- ❌ v2: Generic descriptions → ✅ v3.0: Evidence-based with source quotes
- ✅ 30k chunking with 3k overlap for thorough extraction
- ✅ Formal definition compliance checking

## Cost

- Extraction: $5.08
- Stage 2 Assessment: $0.30
- **Total: $5.38**

## Next Version

v3.1 will include:
- Entity clustering and organization by similar directions
- Expanded concrete details (problems solved, why new, why not exists)
- Consolidated 3-score system (3 for Stage 1, 3 for Stage 2)
- Version selection in dashboard

---

This version serves as the baseline for future iterations.

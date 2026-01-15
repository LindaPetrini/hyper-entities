# Hyper-Entities Extraction & Analysis v3

Rigorous extraction and dual-scoring assessment of hyper-entities from Foresight Institute's content collection.

## 📊 Interactive Dashboard

**[View Live Dashboard →](results/dashboard.html)**

Interactive dashboard with 345 hyper-entities, dual scoring framework, searchable list, and cluster visualization.

## 🎯 What's a Hyper-Entity?

A hyper-entity is:

> "A coherent, future-instantiated system that does not yet exist, but is treated as if it will; whose realization would create a new stable action space for humanity; and which already reorganizes coordination, investment, and narrative around its anticipated existence."

## 📐 Two-Stage Scoring Framework

### Stage 1: Qualification (9 axes, 0-3 each, max 27)
Entities must score **≥18/27** to qualify:
- Non-existence, Plausibility, Design specificity
- New action space, Roadmap clarity, Coordination gravity
- Resource pull, Narrative centrality, Pre-real effects

### Stage 2: Impact Assessment (14 dimensions, 0-5 each, max 70)
For qualified entities:
- Capability Discontinuity, Cross-Domain Reach, Scalability
- Autonomy, Composability, Feedback Intensity
- Irreversibility, Power Concentration, Externality Magnitude
- Misuse Asymmetry, Governance Lag, Narrative Lock-In
- Path Dependency, Human Agency Impact

See **[METHODOLOGY.md](METHODOLOGY.md)** for full scoring framework.

## 📁 Project Structure

```
├── results/
│   ├── hyperentities_dashboard_v4.html         # Interactive dashboard ⭐
│   ├── hyperentities_v3_with_stage2.json       # All entities with dual scoring (583KB)
│   ├── hyperentities_v3.json                   # Entities with Stage 1 only (461KB)
│   └── hyperentities_extracted_v3.md           # Full extraction results (13,689 lines)
├── METHODOLOGY.md                               # Scoring framework documentation
├── extract_hyperentities_v3.py                  # Main extraction script
├── assess_stage2_scoring.py                     # Stage 2 assessment script
├── create_dashboard_v4.py                       # Dashboard generator
├── convert_to_json_v3.py                        # MD to JSON converter
└── extraction_prompt_v3.txt                     # Extraction prompt
```

## 🚀 Key Results

- **345 hyper-entities** extracted from 108 sources
- **261 qualified entities** (≥18/27 on Stage 1)
- **Average Stage 1 score:** 19.3/27
- **Average Stage 2 score:** 46.5/70
- **12 thematic clusters** identified via semantic embeddings

## 🏆 Top 10 Entities by Stage 2 Impact Score

1. **AI-Designed Medical Nanobots** - S1: 21/27 | S2: 63/70
2. **AI Self-Diffusion Infrastructure** - S1: 22/27 | S2: 62/70
3. **Cosmological Constant Manipulation** - S1: 19/27 | S2: 60/70
4. **Adaptive AI-Driven Problem Solving** - S1: 24/27 | S2: 60/70
5. **AI Research Acceleration System** - S1: 23/27 | S2: 60/70
6. **Inference-Time Scaling Paradigm** - S1: 22/27 | S2: 60/70
7. **Brain Emulation (Ems)** - S1: 18/27 | S2: 60/70
8. **Human Superintelligence via BCIs** - S1: 21/27 | S2: 60/70
9. **AI Scientist** - S1: 24/27 | S2: 59/70
10. **Neuroscience Architectural Understanding** - S1: 22/27 | S2: 59/70

## 📈 Dashboard Features

- **Scrollable entity list** with live search
- **Sort by:** Stage 1 score, Stage 2 score, name, category
- **Interactive cluster visualization** with D3.js
- **Expandable detail view** - click "Open in Larger View" button for full-screen reading
- **Dual scoring display** - see both qualification and impact scores
- **Visual scoring bars** for all 9 Stage 1 axes and 14 Stage 2 dimensions

## 🔧 Usage

### Run Full Extraction (v3)
```bash
# Set API key
export ANTHROPIC_API_KEY='your-key'

# Run extraction
python3 extract_hyperentities_v3.py

# Run Stage 2 assessment (on qualified entities)
python3 assess_stage2_scoring.py

# Generate dashboard
python3 create_dashboard_v4.py
```

### Convert to JSON
```bash
python3 convert_to_json_v3.py
```

## 💰 Cost

**Total API cost: $5.38**
- Extraction (345 entities, 108 files): $5.08
- Stage 2 Assessment (261 entities): $0.30

## 📊 Statistics

**Category Distribution:**
- Technology / Institutional Architecture: 44 (12.8%)
- Institutional Architecture: 38 (11.0%)
- Technology: 29 (8.4%)
- Institutional Architecture / Technology: 24 (7.0%)
- Other categories: 210 (60.8%)

**Scoring Distribution:**
- Qualified (≥18/27): 261 entities (75.7%)
- Borderline (12-17/27): 73 entities (21.2%)
- Below threshold (<12/27): 11 entities (3.1%)

## 🔬 Methodology

This project uses a rigorous two-stage framework:

1. **Stage 1 Qualification:** Filters for genuine hyper-entities with specific system architectures and pre-real effects
2. **Stage 2 Impact Assessment:** Evaluates qualified entities on 14 dimensions of civilizational impact

The framework dramatically improves on v2 (which extracted 1,077 vague concepts) by:
- ✅ Requiring formal definition compliance
- ✅ Using 30k chunk size with 3k overlap for thorough extraction
- ✅ Applying explicit scoring thresholds (≥18/27)
- ✅ Providing detailed justification for each score

See **[METHODOLOGY.md](METHODOLOGY.md)** for complete details.

## 📝 License

For Foresight Institute internal use.

## 🤝 Credits

Extraction and analysis conducted with Claude Sonnet 4.5 via Claude Code.

---

**Last updated:** 2026-01-14
**Version:** 3.0 with dual scoring framework

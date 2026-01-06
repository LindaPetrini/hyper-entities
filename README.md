# Hyper-Entities Extraction & Analysis

Automated extraction and visualization of hyper-entities from Foresight Institute's content collection.

## 📊 Interactive Visualization

**[View Live Visualization →](results/hyperentities_visualization_v2.html)**

Interactive t-SNE clustering of 1,077 hyper-entities across 15 thematic clusters.

## 📁 Project Structure

```
├── results/
│   ├── hyperentities_visualization_v2.html  # Interactive visualization
│   └── synthesis/
│       ├── synthesis_report.md              # Comprehensive analysis report
│       └── entities_data.json               # Structured entity data
├── extract_hyperentities_v2.py             # Main extraction script
├── synthesize_smart.py                     # Analysis & synthesis
├── create_visualization_v2.py              # Visualization generator
└── extraction_prompt.txt                   # Entity extraction prompt
```

## 🚀 Key Results

- **1,077 total hyper-entities** extracted from 107 sources
- **500 unique entities** after deduplication
- **15 thematic clusters** identified via semantic embeddings
- **Top 30 priority recommendations** for Foresight Institute

## 📈 Statistics

- **Category Distribution:**
  - Technology: 35%
  - Value/Design Principle: 27%
  - Institutional/Policy Pattern: 22%
  - Vision/Future: 11%
  - Hybrid: 5%

- **Most Mentioned (showing consensus):**
  1. Defensive Accelerationism (d/acc) - 2x
  2. Assembly Theory - 2x

## 🔧 Usage

### Run Extraction
```bash
python3 extract_hyperentities_v2.py
```

### Generate Synthesis
```bash
python3 synthesize_smart.py
```

### Create Visualization
```bash
python3 create_visualization_v2.py
```

## 💰 Cost

Total API cost: **$6.98**
- Extraction: $6.82
- Synthesis: $0.16

## 📝 License

For Foresight Institute internal use.

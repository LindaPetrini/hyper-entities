"""
Quadrant plot: d/acc alignment (x) vs technology impact (y)
Highlights upper-right quadrant entities with labels.
Output: results/report_v2_data/quadrant_plot.png
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from adjustText import adjust_text

# ------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------
BASE = "/Users/lindapetrini/Documents/AI/Foresight/hyper-entities"

with open(f"{BASE}/results/report_v2_data/enriched_entities.json") as f:
    raw = json.load(f)

entities = raw["entities"]

# Normalise scores to 0-100%
# dacc_total max = 20 (4 dims × 5)
# tech_total max = 70 (14 dims × 5)
DACC_MAX = 20
TECH_MAX = 70

rows = []
for e in entities:
    dacc_pct = e["dacc_total"] / DACC_MAX * 100
    tech_raw = e["tech_total"]
    tech_pct = (tech_raw / TECH_MAX * 100) if tech_raw is not None else None
    rows.append(
        {
            "name": e["name"],
            "dacc": dacc_pct,
            "tech": tech_pct,
            "cluster": e["cluster_name"],
            "tier": e["tier"],
        }
    )

# Separate into those with tech scores and those without
has_tech = [r for r in rows if r["tech"] is not None]
no_tech = [r for r in rows if r["tech"] is None]

# ------------------------------------------------------------------
# Threshold for "upper right" highlight
# ------------------------------------------------------------------
DACC_THRESH = 75
TECH_THRESH = 70

highlighted = [r for r in has_tech if r["dacc"] > DACC_THRESH and r["tech"] > TECH_THRESH]
background = [r for r in has_tech if not (r["dacc"] > DACC_THRESH and r["tech"] > TECH_THRESH)]

print(f"Highlighted entities ({len(highlighted)}):")
for r in highlighted:
    print(f"  {r['name']:55s}  d/acc={r['dacc']:.0f}%  tech={r['tech']:.0f}%")

# ------------------------------------------------------------------
# Colours
# ------------------------------------------------------------------
TEAL = "#1A7A6E"
GREY = "#BBBBBB"
QUAD_LINE = "#DDDDDD"
BG = "#FAFAFA"

# ------------------------------------------------------------------
# Plot
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 8), dpi=200)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# Quadrant lines
ax.axvline(DACC_THRESH, color=QUAD_LINE, linewidth=1.0, zorder=1)
ax.axhline(TECH_THRESH, color=QUAD_LINE, linewidth=1.0, zorder=1)

# Faint shading for upper-right quadrant
ax.fill_betweenx(
    [TECH_THRESH, 100],
    DACC_THRESH,
    100,
    color=TEAL,
    alpha=0.05,
    zorder=0,
)

# Background dots (entities without tech score shown at bottom margin)
for r in no_tech:
    ax.scatter(r["dacc"], 5, s=30, color=GREY, alpha=0.4, zorder=2, marker="x")

# Background dots (has tech, not highlighted)
for r in background:
    ax.scatter(r["dacc"], r["tech"], s=40, color=GREY, alpha=0.5, zorder=3)

# Highlighted dots
for r in highlighted:
    ax.scatter(r["dacc"], r["tech"], s=80, color=TEAL, alpha=0.9, zorder=4)

# Labels for highlighted entities
texts = []
for r in highlighted:
    # Shorten long names
    name = r["name"]
    if len(name) > 38:
        # Try to break at a natural point
        parts = name.split(" ")
        mid = len(parts) // 2
        name = " ".join(parts[:mid]) + "\n" + " ".join(parts[mid:])

    t = ax.text(
        r["dacc"],
        r["tech"],
        name,
        fontsize=7.5,
        color="#1A1A1A",
        ha="center",
        va="bottom",
        zorder=5,
        linespacing=1.3,
    )
    texts.append(t)

if texts:
    adjust_text(
        texts,
        ax=ax,
        expand_points=(2.2, 2.2),
        expand_text=(1.6, 1.6),
        arrowprops=dict(arrowstyle="-", color="#AAAAAA", lw=0.6),
        force_points=(1.0, 1.0),
        force_text=(0.8, 0.8),
        ensure_inside_axes=True,
        lim=500,
    )

# Axes
ax.set_xlim(35, 100)
ax.set_ylim(0, 100)
ax.set_xlabel("d/acc Alignment  (%)", fontsize=10, labelpad=8, color="#333333")
ax.set_ylabel("Technology Impact  (%)", fontsize=10, labelpad=8, color="#333333")
ax.set_title(
    "Hyper-Entities: d/acc Alignment vs. Technology Impact",
    fontsize=12,
    fontweight="bold",
    color="#1A1A1A",
    pad=14,
)

# Quadrant labels
ax.text(
    DACC_THRESH + 1, TECH_THRESH + 1.5,
    "High alignment\nHigh impact",
    fontsize=7, color=TEAL, alpha=0.7, va="bottom",
)
ax.text(
    36, TECH_THRESH + 1.5,
    "Lower alignment\nHigh impact",
    fontsize=7, color="#999999", alpha=0.7, va="bottom",
)
ax.text(
    DACC_THRESH + 1, 3,
    "High alignment\nLower impact",
    fontsize=7, color="#999999", alpha=0.7, va="bottom",
)

# Tick styling
ax.tick_params(colors="#555555", labelsize=8)
for spine in ax.spines.values():
    spine.set_color("#DDDDDD")

# Small note for x-markers
ax.text(
    36, 5, "× no tech score", fontsize=6.5, color="#AAAAAA", va="center"
)

plt.tight_layout()

OUT = f"{BASE}/results/report_v2_data/quadrant_plot.png"
plt.savefig(OUT, dpi=200, bbox_inches="tight", facecolor=BG)
print(f"\nSaved to {OUT}")

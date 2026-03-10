#!/usr/bin/env python3
"""Generate a print-quality scatter plot of hyper-entities v3 data.

Plots d/acc Alignment Score (X) vs Transformative Potential (Y),
colored by readiness bottleneck. Tier 1 entities are large filled circles
with labels; Tier 2 are small hollow circles.

Outputs: scatter_plot_v3.png (300 DPI) and scatter_plot_v3.svg
"""

import json
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from adjustText import adjust_text

# ── Extract data from dashboard.html ─────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD = os.path.join(SCRIPT_DIR, "dashboard.html")

with open(DASHBOARD, "r") as f:
    content = f.read()

match = re.search(r"const allEntities = (\[.*?\]);", content, re.DOTALL)
if not match:
    raise RuntimeError("Could not find allEntities in dashboard.html")

raw = json.loads(match.group(1))

entities = []
for e in raw:
    s = e.get("scores", {})
    a = s.get("actionability", {})
    dacc = s.get("dacc", {})
    dacc_total = dacc.get("total") if isinstance(dacc, dict) else None
    trans = s.get("transformative", {})
    trans_score = trans.get("score") if isinstance(trans, dict) else trans
    bottleneck = a.get("readiness_bottleneck", "Unknown") if isinstance(a, dict) else "Unknown"

    if dacc_total is not None and trans_score is not None:
        entities.append({
            "name": e["name"],
            "dacc": dacc_total,
            "trans": trans_score,
            "tier": e.get("tier", 2),
            "bottleneck": bottleneck,
            "group": e.get("group", ""),
        })

print(f"Loaded {len(entities)} entities with valid scores")

# ── Bottleneck colors ────────────────────────────────────────────────
BOTTLENECK_COLORS = {
    "Physics": "#ef4444",
    "Engineering": "#f97316",
    "Funding": "#22c55e",
    "Regulation": "#3b82f6",
    "Coordination": "#a855f7",
    "Social Acceptance": "#ec4899",
}
DEFAULT_COLOR = "#94a3b8"

# ── Short names for Tier 1 labels ────────────────────────────────────
SHORT_NAMES = {
    "Community-Governed AI Mesh Systems": "Community AI Mesh",
    "Universal AI Learning UnCommons (UALU)": "AI Learning UnCommons",
    "AI cryptographic oracle with zero-knowledge IoT auditing and jury-DAO": "AI Crypto Oracle / Jury-DAO",
    "BCI Operating System (BCI-OS)": "BCI Operating System",
    "Tokenized neural data sharing with selective disclosure": "Tokenized Neural Data",
    "Civic Systems Co-Op": "Civic Systems Co-Op",
    "Interbeing Forum": "Interbeing Forum",
    "Interoperable Governance Protocol Stack": "Governance Protocol Stack",
    "Comprehensive AI Services (Drexler)": "Comprehensive AI Services",
    "Attack Dog DAO for Climate": "Attack Dog DAO",
    "Wisdom DAO": "Wisdom DAO",
    "Accord of Watersheds": "Accord of Watersheds",
    "DAO-governed open innovation platform for TLM documentation and training data": "DAO Innovation Platform",
    "Watershed Parliaments": "Watershed Parliaments",
    "Digital Twins for Communities and Ecosystems": "Digital Twins (Community)",
    "Loyal AI Assistance (Fiduciary AI Assistance)": "Fiduciary AI Assistance",
    "The Global Deliberation Coordinator": "Global Deliberation",
    "Epistemic stack": "Epistemic Stack",
    "Moral Trade": "Moral Trade",
}

# ── Add jitter to avoid overlapping points ───────────────────────────
np.random.seed(42)
for e in entities:
    e["x"] = e["dacc"] + np.random.uniform(-0.3, 0.3)
    e["y"] = e["trans"] + np.random.uniform(-0.08, 0.08)

# ── Separate tiers ───────────────────────────────────────────────────
tier1 = [e for e in entities if e["tier"] == 1]
tier2 = [e for e in entities if e["tier"] != 1]

print(f"Tier 1: {len(tier1)}, Tier 2: {len(tier2)}")

# ── Plot ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor("white")
ax.set_facecolor("#FAFAFA")

# Grid
ax.grid(True, alpha=0.3, linewidth=0.5, color="#CCCCCC")
ax.set_axisbelow(True)

# Plot Tier 2 (hollow circles)
for e in tier2:
    color = BOTTLENECK_COLORS.get(e["bottleneck"], DEFAULT_COLOR)
    ax.scatter(e["x"], e["y"], s=25, facecolors="none", edgecolors=color,
               linewidths=0.8, alpha=0.5, zorder=2)

# Plot Tier 1 (filled circles)
for e in tier1:
    color = BOTTLENECK_COLORS.get(e["bottleneck"], DEFAULT_COLOR)
    ax.scatter(e["x"], e["y"], s=90, facecolors=color, edgecolors="white",
               linewidths=0.8, alpha=0.9, zorder=3)

# Labels for Tier 1
texts = []
for e in tier1:
    label = SHORT_NAMES.get(e["name"], e["name"])
    txt = ax.text(e["x"], e["y"], label, fontsize=9, fontweight="medium",
                  ha="left", va="center", zorder=4,
                  path_effects=[pe.withStroke(linewidth=2.5, foreground="white")])
    texts.append(txt)

# Tier 1 scatter points for adjust_text reference
t1_x = [e["x"] for e in tier1]
t1_y = [e["y"] for e in tier1]

# Adjust labels to avoid overlaps
adjust_text(
    texts, x=t1_x, y=t1_y, ax=ax,
    arrowprops=dict(arrowstyle="-", color="#BBBBBB", lw=0.5, alpha=0.5),
    expand=(2.5, 3.0),
    force_text=(2.0, 3.0),
    force_points=(1.5, 2.0),
    max_move=None,
    only_move={"text": "xy", "points": "xy"},
)

# Axes
ax.set_xlabel("d/acc Alignment Score (0-20)", fontsize=12, labelpad=10)
ax.set_ylabel("Transformative Potential (1-4)", fontsize=12, labelpad=10)
ax.set_title("Hyper-Entities v3: d/acc Alignment vs. Transformative Potential",
             fontsize=15, fontweight="bold", pad=15)

# Axis limits with padding
ax.set_xlim(-1, 21)
ax.set_ylim(0.5, 5.0)
ax.set_xticks(range(0, 21, 2))
ax.set_yticks([1, 2, 3, 4])

# Spine styling
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
for spine in ["bottom", "left"]:
    ax.spines[spine].set_color("#666666")

# ── Legend for bottleneck colors ─────────────────────────────────────
from matplotlib.lines import Line2D

legend_elements = []
for bn, color in BOTTLENECK_COLORS.items():
    legend_elements.append(
        Line2D([0], [0], marker="o", color="w", markerfacecolor=color,
               markersize=8, label=bn)
    )
# Add tier markers
legend_elements.append(
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#666",
           markersize=10, label="Tier 1 (filled)")
)
legend_elements.append(
    Line2D([0], [0], marker="o", color="w", markerfacecolor="none",
           markeredgecolor="#666", markersize=8, markeredgewidth=1,
           label="Tier 2 (hollow)")
)

ax.legend(handles=legend_elements, loc="upper left", fontsize=8,
          framealpha=0.9, edgecolor="#CCCCCC", ncol=1,
          title="Readiness Bottleneck", title_fontsize=9)

# Caption
fig.text(0.5, 0.01,
         f"{len(entities)} hyper-entities plotted. Tier 1 ({len(tier1)}) labeled. "
         f"Tier 2 ({len(tier2)}) shown as hollow circles.",
         ha="center", fontsize=8, color="#666666")

plt.tight_layout(rect=[0, 0.03, 1, 1])

# ── Save ─────────────────────────────────────────────────────────────
png_path = os.path.join(SCRIPT_DIR, "scatter_plot_v3.png")
svg_path = os.path.join(SCRIPT_DIR, "scatter_plot_v3.svg")

fig.savefig(png_path, dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(svg_path, bbox_inches="tight", facecolor="white")
plt.close()

print(f"PNG saved: {png_path}")
print(f"SVG saved: {svg_path}")

# Verify
from PIL import Image
img = Image.open(png_path)
print(f"PNG dimensions: {img.width}x{img.height} px")
print(f"PNG file size: {os.path.getsize(png_path) / 1024:.0f} KB")

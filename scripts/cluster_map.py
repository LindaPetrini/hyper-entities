"""
Cluster bubble map: one bubble per thematic cluster.
Bubble size = entity count, color = average d/acc score.
Output: results/report_v2_data/cluster_map.png
"""

import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from collections import defaultdict

# ------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------
BASE = "/Users/lindapetrini/Documents/AI/Foresight/hyper-entities"

with open(f"{BASE}/results/report_v2_data/enriched_entities.json") as f:
    raw = json.load(f)

entities = raw["entities"]
DACC_MAX = 20

# Aggregate by cluster
cluster_data = defaultdict(list)
for e in entities:
    dacc_pct = e["dacc_total"] / DACC_MAX * 100
    cluster_data[e["cluster_name"]].append(dacc_pct)

clusters = []
for name, scores in cluster_data.items():
    clusters.append(
        {
            "name": name,
            "count": len(scores),
            "avg_dacc": np.mean(scores),
        }
    )

clusters.sort(key=lambda c: -c["avg_dacc"])

print("Clusters:")
for c in clusters:
    print(f"  {c['name']:45s}  n={c['count']}  avg_dacc={c['avg_dacc']:.1f}%")

n = len(clusters)

# ------------------------------------------------------------------
# Layout: arrange bubbles in a roughly circular / organic pattern
# Use a sunflower / golden-angle spiral so they're spread evenly
# without a rigid grid.
# ------------------------------------------------------------------
golden_angle = math.pi * (3 - math.sqrt(5))  # ~137.5 deg

# Scale bubble radii (in data units) by sqrt(count)
MAX_COUNT = max(c["count"] for c in clusters)
MIN_R, MAX_R = 0.35, 0.90  # relative units

def bubble_radius(count):
    return MIN_R + (MAX_R - MIN_R) * math.sqrt(count / MAX_COUNT)

# Place bubbles: spiral outward so they don't overlap
# We'll use a simple iterative placement
positions = []
radii = [bubble_radius(c["count"]) for c in clusters]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# First bubble at origin
positions.append((0.0, 0.0))

for i in range(1, n):
    angle = i * golden_angle
    # Try increasing ring radii until we find a non-overlapping spot
    for ring in np.linspace(0.5, 5.0, 300):
        cx = ring * math.cos(angle)
        cy = ring * math.sin(angle)
        ok = True
        for j, (px, py) in enumerate(positions):
            min_dist = radii[i] + radii[j] + 0.12  # small gap
            if distance((cx, cy), (px, py)) < min_dist:
                ok = False
                break
        if ok:
            positions.append((cx, cy))
            break
    else:
        # fallback: just use the angle at a large ring
        positions.append((5.0 * math.cos(angle), 5.0 * math.sin(angle)))

xs = [p[0] for p in positions]
ys = [p[1] for p in positions]

# ------------------------------------------------------------------
# Color scale: light to dark teal based on avg_dacc
# ------------------------------------------------------------------
dacc_vals = [c["avg_dacc"] for c in clusters]
norm = mcolors.Normalize(vmin=min(dacc_vals) - 2, vmax=max(dacc_vals) + 2)
cmap = plt.get_cmap("YlGnBu")

# ------------------------------------------------------------------
# Plot
# ------------------------------------------------------------------
BG = "#FAFAFA"
fig, ax = plt.subplots(figsize=(11, 9), dpi=200)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_aspect("equal")
ax.axis("off")

scatter_handles = []
for i, c in enumerate(clusters):
    x, y = positions[i]
    r = radii[i]
    color = cmap(norm(c["avg_dacc"]))

    # Draw filled circle
    circle = plt.Circle(
        (x, y), r,
        color=color,
        alpha=0.88,
        zorder=2,
    )
    ax.add_patch(circle)

    # Cluster label (split long names to two lines)
    name = c["name"]
    # Break at "&" or after ~16 chars
    if "&" in name:
        parts = name.split("&", 1)
        label = parts[0].strip() + "\n& " + parts[1].strip()
    elif len(name) > 18:
        words = name.split()
        mid = len(words) // 2
        label = " ".join(words[:mid]) + "\n" + " ".join(words[mid:])
    else:
        label = name

    # Count line below
    label_full = label + f"\n({c['count']} entities)"

    ax.text(
        x, y,
        label_full,
        ha="center",
        va="center",
        fontsize=7.2,
        color="#1A1A1A" if norm(c["avg_dacc"]) < 0.65 else "#F5F5F5",
        fontweight="bold" if r > 0.6 else "normal",
        linespacing=1.4,
        zorder=3,
    )

# ------------------------------------------------------------------
# Colorbar legend
# ------------------------------------------------------------------
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(
    sm,
    ax=ax,
    orientation="horizontal",
    fraction=0.025,
    pad=0.02,
    aspect=30,
    shrink=0.45,
)
cbar.set_label("Average d/acc Alignment (%)", fontsize=9, color="#333333")
cbar.ax.tick_params(labelsize=7.5, colors="#555555")

# Bubble size legend
legend_sizes = [1, 3, 6]
legend_x = max(xs) + max(radii) + 0.5
legend_y_start = max(ys)
for k, cnt in enumerate(legend_sizes):
    r = bubble_radius(cnt)
    ly = legend_y_start - k * (MAX_R * 2 + 0.35)
    ax.add_patch(
        plt.Circle((legend_x + r, ly), r, color="#CCCCCC", alpha=0.6, zorder=2)
    )
    ax.text(
        legend_x + r * 2 + 0.12,
        ly,
        f"n = {cnt}",
        va="center",
        fontsize=7,
        color="#666666",
    )

ax.text(
    legend_x,
    legend_y_start + MAX_R + 0.25,
    "Cluster size",
    fontsize=8,
    color="#333333",
    fontweight="bold",
)

# Title
ax.set_title(
    "Hyper-Entity Clusters by Size and d/acc Alignment",
    fontsize=13,
    fontweight="bold",
    color="#1A1A1A",
    pad=16,
)

# Auto-fit axes
padding = max(radii) + 0.4
ax.set_xlim(min(xs) - padding, max(xs) + padding + 2.5)
ax.set_ylim(min(ys) - padding - 0.5, max(ys) + padding + 0.5)

plt.tight_layout()

OUT = f"{BASE}/results/report_v2_data/cluster_map.png"
plt.savefig(OUT, dpi=200, bbox_inches="tight", facecolor=BG)
print(f"\nSaved to {OUT}")

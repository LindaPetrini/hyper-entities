#!/usr/bin/env python3
"""
Generate static scatter plot: d/acc (x) vs Tech Impact (y).
Colored by thematic group, sized by maturity tier.
Outputs PNG for PDF report and SVG for web.
"""

import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
import textwrap

DATA_FILE = "results/report_v2_data/enriched_entities.json"
OUTPUT_DIR = Path("results/report_v2_data")

# Color palette for 9 thematic groups (colorblind-friendly)
GROUP_COLORS = {
    "Energy & Infrastructure": "#e63946",
    "Manufacturing & Matter": "#f4a261",
    "Truth & Epistemic Infrastructure": "#2a9d8f",
    "Governance & Collective Intelligence": "#264653",
    "Markets & Incentive Systems": "#e9c46a",
    "Ethics & Moral Expansion": "#a8dadc",
    "AI & Human Agency": "#457b9d",
    "Interfaces & Augmentation": "#6a4c93",
    "Science & Discovery": "#1d3557",
}

# Marker sizes for maturity tiers
MATURITY_SIZES = {
    "Foundational Research": 60,
    "Early Demonstrations": 100,
    "Scaling Challenges": 160,
    "Near Deployment": 240,
}

MATURITY_MARKERS = {
    "Foundational Research": "D",       # diamond
    "Early Demonstrations": "o",        # circle
    "Scaling Challenges": "s",          # square
    "Near Deployment": "^",             # triangle up
}


def main():
    with open(DATA_FILE) as f:
        data = json.load(f)

    entities = data["entities"]

    # Filter to entities with both scores
    plottable = [e for e in entities if e["dacc_total"] and e["tech_total"]]
    excluded = [e for e in entities if not e["dacc_total"] or not e["tech_total"]]

    print(f"Plotting {len(plottable)} entities ({len(excluded)} excluded for missing scores)")

    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))

    # Normalize scores to 0-100
    for e in plottable:
        e["dacc_norm"] = round(e["dacc_total"] / 20 * 100)
        e["tech_norm"] = round(e["tech_total"] / 70 * 100)

    # Plot each entity
    for e in plottable:
        color = GROUP_COLORS.get(e["cluster_name"], "#999999")
        size = MATURITY_SIZES.get(e["maturity"], 100)
        marker = MATURITY_MARKERS.get(e["maturity"], "o")

        ax.scatter(
            e["dacc_norm"],
            e["tech_norm"],
            c=color,
            s=size,
            marker=marker,
            alpha=0.85,
            edgecolors="white",
            linewidths=0.5,
            zorder=3,
        )

    # Label entities (with smart positioning to reduce overlap)
    texts = []
    for e in plottable:
        name = e["name"]
        # Shorten long names
        if len(name) > 35:
            name = name[:32] + "..."
        texts.append((e["dacc_norm"], e["tech_norm"], name, e["tier"]))

    # Label Tier 1 entities always, Tier 2 only if space
    for x, y, name, tier in texts:
        fontsize = 7.5 if tier == 1 else 6.5
        fontweight = "bold" if tier == 1 else "normal"
        alpha = 0.95 if tier == 1 else 0.7

        # Offset labels slightly to reduce overlap
        ax.annotate(
            name,
            (x, y),
            textcoords="offset points",
            xytext=(6, 4),
            fontsize=fontsize,
            fontweight=fontweight,
            alpha=alpha,
            color="#333333",
        )

    # Quadrant annotations (normalized: d/acc=75, tech=74)
    ax.axhline(y=74, color="#cccccc", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.axvline(x=75, color="#cccccc", linestyle="--", linewidth=0.8, alpha=0.5)

    # Quadrant labels
    ax.text(
        57, 90, "High tech impact\nLow d/acc alignment\n(needs governance attention)",
        fontsize=8, color="#999999", ha="center", style="italic",
    )
    ax.text(
        92, 90, "High tech impact\nHigh d/acc alignment\n(\"sweet spot\")",
        fontsize=8, color="#999999", ha="center", style="italic",
    )
    ax.text(
        57, 60, "Lower tech impact\nLow d/acc alignment",
        fontsize=8, color="#999999", ha="center", style="italic",
    )
    ax.text(
        92, 60, "Lower tech impact\nHigh d/acc alignment\n(values-aligned, niche impact)",
        fontsize=8, color="#999999", ha="center", style="italic",
    )

    # Axis labels and title
    ax.set_xlabel("d/acc Values Alignment Score (0-100)", fontsize=12, labelpad=10)
    ax.set_ylabel("Technology Impact Score (0-100)", fontsize=12, labelpad=10)
    ax.set_title(
        "Hyper-Entities: d/acc Alignment vs. Technology Impact",
        fontsize=14, fontweight="bold", pad=15,
    )

    # Set axis limits with padding
    ax.set_xlim(30, 105)
    ax.set_ylim(54, 95)

    # Grid
    ax.grid(True, alpha=0.15, linestyle="-")
    ax.set_axisbelow(True)

    # Legend: thematic groups
    group_patches = [
        mpatches.Patch(color=color, label=group)
        for group, color in GROUP_COLORS.items()
    ]
    legend1 = ax.legend(
        handles=group_patches,
        loc="lower left",
        title="Thematic Groups",
        fontsize=7,
        title_fontsize=8,
        framealpha=0.9,
        ncol=2,
    )
    ax.add_artist(legend1)

    # Legend: maturity (marker shapes)
    maturity_handles = []
    for maturity, marker in MATURITY_MARKERS.items():
        size = MATURITY_SIZES[maturity]
        handle = ax.scatter(
            [], [], marker=marker, s=size * 0.5, c="gray",
            edgecolors="white", linewidths=0.5, label=maturity,
        )
        maturity_handles.append(handle)
    ax.legend(
        handles=maturity_handles,
        loc="upper left",
        title="Maturity",
        fontsize=7,
        title_fontsize=8,
        framealpha=0.9,
    )
    ax.add_artist(legend1)  # re-add group legend

    # Note about excluded entities
    if excluded:
        excluded_names = [e["name"][:30] for e in excluded[:5]]
        note = f"Note: {len(excluded)} entities excluded (no tech score)"
        ax.text(
            0.98, 0.02, note,
            transform=ax.transAxes,
            fontsize=7, color="#999999",
            ha="right", va="bottom",
        )

    plt.tight_layout()

    # Save
    png_path = OUTPUT_DIR / "scatter_plot.png"
    svg_path = OUTPUT_DIR / "scatter_plot.svg"
    plt.savefig(png_path, dpi=200, bbox_inches="tight")
    plt.savefig(svg_path, bbox_inches="tight")
    print(f"Saved: {png_path}")
    print(f"Saved: {svg_path}")
    plt.close()


if __name__ == "__main__":
    main()

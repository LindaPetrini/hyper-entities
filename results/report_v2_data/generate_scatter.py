#!/usr/bin/env python3
"""Generate d/acc Alignment vs Technology Impact scatter plot.

Uses matplotlib + adjustText for clean, readable label placement.
Outputs both SVG and PNG at high resolution.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────
entities = [
    {"name": "Decentralized Adaptive Energy Network", "dacc": 90, "tech": 73, "cluster": "Energy & Infrastructure"},
    {"name": "Deep Fision Micro Nuclear Reactors", "dacc": 80, "tech": 67, "cluster": "Energy & Infrastructure"},
    {"name": "End-User Programming Ecosystem", "dacc": 80, "tech": 77, "cluster": "Manufacturing & Matter"},
    {"name": "Atomically Precise Manufacturing", "dacc": 65, "tech": 81, "cluster": "Manufacturing & Matter"},
    {"name": "Chemputing", "dacc": 65, "tech": 63, "cluster": "Manufacturing & Matter"},
    {"name": "Epistemic Stack", "dacc": 85, "tech": 63, "cluster": "Truth & Epistemic Infrastructure"},
    {"name": "AI-Assisted Epistemological Enhancement", "dacc": 80, "tech": 77, "cluster": "Truth & Epistemic Infrastructure"},
    {"name": "Distributed Zero-Knowledge Security", "dacc": 80, "tech": 67, "cluster": "Truth & Epistemic Infrastructure"},
    {"name": "Epistemic Infrastructure for Truth Verification", "dacc": 80, "tech": 76, "cluster": "Truth & Epistemic Infrastructure"},
    {"name": "Competitive Governance Protocol Stack", "dacc": 90, "tech": 81, "cluster": "Governance & Collective Intelligence"},
    {"name": "LexCommons", "dacc": 90, "tech": 81, "cluster": "Governance & Collective Intelligence"},
    {"name": "Global Deliberation Coordinator", "dacc": 75, "tech": 74, "cluster": "Governance & Collective Intelligence"},
    {"name": "Habermas Machines", "dacc": 75, "tech": 60, "cluster": "Governance & Collective Intelligence"},
    {"name": "Reputational Markets", "dacc": 85, "tech": 73, "cluster": "Markets & Incentive Systems"},
    {"name": "Prediction Markets", "dacc": 80, "tech": 63, "cluster": "Markets & Incentive Systems"},
    {"name": "EgoLets", "dacc": 75, "tech": 69, "cluster": "AI & Human Agency"},
    {"name": "Empathetic Neuro-AI Coaching", "dacc": 65, "tech": 69, "cluster": "AI & Human Agency"},
    {"name": "Lifelong AI Guardians", "dacc": 65, "tech": 70, "cluster": "AI & Human Agency"},
    {"name": "Digital Mind Governance", "dacc": 80, "tech": 76, "cluster": "Interfaces & Augmentation"},
    {"name": "Translation Language Models", "dacc": 80, "tech": 76, "cluster": "Interfaces & Augmentation"},
    {"name": "Digital Twin Ecosystem", "dacc": 75, "tech": 79, "cluster": "Interfaces & Augmentation"},
    {"name": "Immune-Computer Interface", "dacc": 65, "tech": 83, "cluster": "Interfaces & Augmentation"},
    {"name": "Brain-Computer Interfaces", "dacc": 60, "tech": 86, "cluster": "Interfaces & Augmentation"},
    {"name": "Mind Uploading Infrastructure", "dacc": 40, "tech": 80, "cluster": "Interfaces & Augmentation"},
    {"name": "Automated Scientific Publishing", "dacc": 90, "tech": 86, "cluster": "Science & Discovery"},
    {"name": "Universal AI Learning UnCommons", "dacc": 85, "tech": 63, "cluster": "Science & Discovery"},
    {"name": "Decentralized Scientific Collaboration", "dacc": 90, "tech": 76, "cluster": "Science & Discovery"},
    {"name": "Protein Design for Global Challenges", "dacc": 65, "tech": 76, "cluster": "Science & Discovery"},
    {"name": "Origin of Life Platform", "dacc": 50, "tech": 66, "cluster": "Science & Discovery"},
]

# ── Short display names ───────────────────────────────────────────────
SHORT_NAMES = {
    "Atomically Precise Manufacturing": "Atomically Precise Mfg",
    "AI-Assisted Epistemological Enhancement": "AI Epistemological Enh.",
    "Distributed Zero-Knowledge Security": "ZK Security Systems",
    "Competitive Governance Protocol Stack": "Competitive Governance",
    "Epistemic Infrastructure for Truth Verification": "Truth Verification Infra",
    "Empathetic Neuro-AI Coaching": "Neuro-AI Coaching",
    "Translation Language Models": "Translation LMs",
    "Digital Mind Governance": "Digital Mind Gov.",
    "Automated Scientific Publishing": "Auto. Sci. Publishing",
    "Universal AI Learning UnCommons": "AI Learning UnCommons",
    "Decentralized Scientific Collaboration": "Decentr. Sci. Collab.",
    "Protein Design for Global Challenges": "Protein Design",
    "Origin of Life Platform": "Origin of Life",
    "Decentralized Adaptive Energy Network": "Decentr. Energy Network",
    "Deep Fision Micro Nuclear Reactors": "Micro Nuclear Reactors",
    "End-User Programming Ecosystem": "End-User Programming",
    "Prediction Markets": "Prediction Markets",
    "Brain-Computer Interfaces": "Brain-Computer Interfaces",
    "Mind Uploading Infrastructure": "Mind Uploading",
    "Digital Twin Ecosystem": "Digital Twin",
    "Immune-Computer Interface": "Immune-Computer Interface",
    "EgoLets": "EgoLets",
    "Lifelong AI Guardians": "Lifelong AI Guardians",
    "Chemputing": "Chemputing",
    "Global Deliberation Coordinator": "Global Deliberation",
    "Habermas Machines": "Habermas Machines",
    "Reputational Markets": "Reputational Markets",
    "Epistemic Stack": "Epistemic Stack",
    "LexCommons": "LexCommons",
}

# ── Deterministic jitter to separate overlapping points ──────────────
import hashlib

def _jitter(name, axis):
    h = hashlib.sha256(f"{name}:{axis}".encode()).hexdigest()
    val = int(h[:8], 16) / 0xFFFFFFFF
    return (val - 0.5) * 2.5

JITTER = {e["name"]: (_jitter(e["name"], "x"), _jitter(e["name"], "y")) for e in entities}


def generate_plot():
    # ── Style ────────────────────────────────────────────────────────
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "sans-serif"],
        "font.size": 11,
        "axes.linewidth": 1.2,
        "axes.edgecolor": "#333333",
        "axes.labelcolor": "#1A1A1A",
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "text.color": "#1A1A1A",
    })

    BLUE = "#2166AC"
    ORANGE = "#B35806"

    fig, ax = plt.subplots(figsize=(18, 14))
    fig.patch.set_facecolor("#FCFCFC")
    ax.set_facecolor("#F9F9F9")

    # ── Quadrant lines ───────────────────────────────────────────────
    ax.axvline(x=75, color="#CCCCCC", linewidth=0.8, linestyle="--", zorder=1)
    ax.axhline(y=75, color="#CCCCCC", linewidth=0.8, linestyle="--", zorder=1)

    # ── Plot points ──────────────────────────────────────────────────
    xs, ys, colors, labels = [], [], [], []
    for e in entities:
        jx, jy = JITTER[e["name"]]
        x = e["dacc"] + jx
        y = e["tech"] + jy
        xs.append(x)
        ys.append(y)
        colors.append(BLUE if e["dacc"] >= 75 else ORANGE)
        labels.append(SHORT_NAMES.get(e["name"], e["name"]))

    ax.scatter(xs, ys, c=colors, s=70, zorder=5, edgecolors="white", linewidths=0.6, alpha=0.9)

    # ── Labels with adjustText ───────────────────────────────────────
    texts = []
    for i, label in enumerate(labels):
        t = ax.annotate(
            label,
            (xs[i], ys[i]),
            fontsize=10,
            color="#1A1A1A",
            fontweight="normal",
            zorder=6,
        )
        texts.append(t)

    adjust_text(
        texts,
        x=xs,
        y=ys,
        ax=ax,
        force_text=(1.2, 1.2),
        force_points=(1.5, 1.5),
        expand=(1.8, 1.8),
        arrowprops=dict(
            arrowstyle="-",
            color="#BBBBBB",
            lw=0.5,
            alpha=0.45,
        ),
        ensure_inside_axes=True,
        max_move=18.0,
        only_move="xy",
        time_lim=10,
    )

    # ── Axes ─────────────────────────────────────────────────────────
    ax.set_xlim(32, 100)
    ax.set_ylim(56, 92)
    ax.set_xlabel("d/acc Values Alignment Score", fontsize=13, labelpad=12, fontweight="medium")
    ax.set_ylabel("Technology Impact Score", fontsize=13, labelpad=12, fontweight="medium")
    ax.set_title("d/acc Alignment vs. Technology Impact", fontsize=18, fontweight="bold", pad=20)

    ax.set_xticks(range(40, 101, 10))
    ax.set_yticks(range(60, 91, 5))
    ax.tick_params(axis="both", labelsize=11, length=5, width=1)

    # Remove top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Light grid
    ax.grid(True, alpha=0.15, linewidth=0.5, color="#999999")

    # ── Quadrant annotations ─────────────────────────────────────────
    ax.text(97, 91, "High impact, high d/acc alignment", ha="right", va="top",
            fontsize=9, fontstyle="italic", color="#777777", alpha=0.8)
    ax.text(35, 91, "High impact, needs governance", ha="left", va="top",
            fontsize=9, fontstyle="italic", color="#777777", alpha=0.8)
    ax.text(97, 58, "Values-aligned, niche impact", ha="right", va="bottom",
            fontsize=9, fontstyle="italic", color="#777777", alpha=0.8)

    # ── Legend ────────────────────────────────────────────────────────
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=BLUE, markersize=9,
               label='d/acc >= 75 (values-aligned)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=ORANGE, markersize=9,
               label='d/acc < 75 (needs governance)'),
    ]
    leg = ax.legend(handles=legend_elements, loc="lower left", fontsize=10,
                    frameon=True, framealpha=0.9, edgecolor="#DDDDDD",
                    borderpad=0.8, handletextpad=0.5)
    leg.get_frame().set_linewidth(0.5)

    # ── Caption ──────────────────────────────────────────────────────
    fig.text(0.5, 0.02, "29 of 39 hyper-entities plotted. 10 entities excluded (no technology impact score).",
             ha="center", fontsize=10, color="#777777")

    plt.tight_layout(rect=[0.02, 0.04, 0.98, 0.97])
    return fig


# ── Main ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(out_dir, "scatter_plot_v2.svg")
    png_path = os.path.join(out_dir, "scatter_plot_v2.png")

    fig = generate_plot()

    fig.savefig(svg_path, format="svg", bbox_inches="tight", dpi=150)
    print(f"SVG written: {svg_path}")

    fig.savefig(png_path, format="png", bbox_inches="tight", dpi=200)
    print(f"PNG written: {png_path}")

    plt.close(fig)

    # ── Verification ─────────────────────────────────────────────────
    print("\n-- Verification --")
    file_size = os.path.getsize(png_path)
    print(f"PNG size: {file_size:,} bytes ({file_size/1024:.0f} KB)")

    from PIL import Image
    img = Image.open(png_path)
    print(f"PNG dimensions: {img.width} x {img.height}")
    print(f"Aspect ratio: {img.width/img.height:.2f}")
    print("\nDone.")

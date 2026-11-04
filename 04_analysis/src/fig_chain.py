"""Schematic of the hazard-to-capital chain: which link each research question estimates or assumes.

No data. Writes 04_analysis/outputs/figures/fig_chain.{png,pdf}.
Run: .venv/bin/python -I 04_analysis/src/fig_chain.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
FIG = ROOT / "04_analysis/outputs/figures"
INK, INK2, SURF, BOX = "#0b0b0b", "#52514e", "#fcfcfb", "#eef3fb"
ACCENT = "#2a78d6"

NODES = ["Flood hazard\nand floods", "Official\nland values", "Bank collateral\nvalues",
         "PD and LGD\nunder relief", "Bank capital,\nreported and\neconomic"]
# (label above the arrow, line style, status word below)
LINKS = [("RQ1", "-", "estimated\n(public data)"),
         (r"$\lambda_B$", "--", "assumed analogy, 0 to 1,\nnot a causal link; loan\nappraisals can reveal it"),
         ("RQ2", ":", "estimated if loan\ndata are obtained"),
         ("RQ3", "-", "computed\n(reverse stress test)")]


def main() -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "figure.facecolor": SURF,
                         "savefig.facecolor": SURF})
    fig, ax = plt.subplots(figsize=(6.3, 1.5))
    ax.set_xlim(-0.02, 10.0)
    ax.set_ylim(0.42, 2.05)
    ax.axis("off")
    w, h, y = 1.28, 0.72, 0.95
    xs = [0.02 + i * 2.16 for i in range(len(NODES))]
    for x, name in zip(xs, NODES):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    fc=BOX, ec=ACCENT, lw=1.0))
        ax.text(x + w / 2, y + h / 2, name, ha="center", va="center", color=INK, fontsize=7.2)
    for i, (lab, ls, status) in enumerate(LINKS):
        x0, x1 = xs[i] + w + 0.05, xs[i + 1] - 0.05
        ax.add_patch(FancyArrowPatch((x0, y + h / 2), (x1, y + h / 2), arrowstyle="-|>", mutation_scale=9,
                                     lw=1.4, ls=ls, color=INK2))
        ax.text((x0 + x1) / 2, y + h / 2 + 0.08, lab, ha="center", va="bottom", fontsize=8,
                color=INK, fontweight="bold")
        ax.text((x0 + x1) / 2, y - 0.06, status, ha="center", va="top", fontsize=5.8, color=INK2)
    ax.text(0.02, 2.0, "Solid: estimated or computed in the thesis. Dashed: assumed. Dotted: conditional on access.",
            ha="left", va="top", fontsize=6.6, color=INK2)
    fig.tight_layout(pad=0.2)
    FIG.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(FIG / f"fig_chain.{ext}", dpi=300)


if __name__ == "__main__":
    main()

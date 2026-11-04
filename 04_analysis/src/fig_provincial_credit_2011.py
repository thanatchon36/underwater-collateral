"""Descriptive figure: commercial-bank loans by booking province around the 2011 floods.

Indexed total loans (Jun 2011 = 100), Jan 2010 - Dec 2013, summed over
(a) provinces with a high 2011 flood share and (b) all other provinces.
Group rule (fixed before looking at credit): parcel-weighted GFD DFO 3850 flood share
>= 0.20 among provinces with >= 90% of parcels inside the GFD footprint
(04_analysis/outputs/tables/province_flood_share_2011.csv, from panel_summary.py).
Bangkok is excluded from both groups: head-office balances are booked centrally and
are not Bangkok-local (see clean_bot_provincial_credit.py, issue 2).
2012 is missing (FI_CB_011_S3 not located), so the lines are broken there.
Descriptive only: no causal claim.

Inputs: 03_data/processed/bot_provincial_credit_monthly.csv,
        04_analysis/outputs/tables/province_flood_share_2011.csv
Output: 04_analysis/outputs/figures/fig_provincial_credit_2011.{png,pdf},
        04_analysis/outputs/tables/fig_provincial_credit_2011_data.csv
Usage : .venv/bin/python -I 04_analysis/src/fig_provincial_credit_2011.py
"""

import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "03_data" / "processed" / "bot_provincial_credit_monthly.csv"
SHARES = ROOT / "04_analysis" / "outputs" / "tables" / "province_flood_share_2011.csv"
OUT = ROOT / "04_analysis" / "outputs" / "figures" / "fig_provincial_credit_2011"
TAB = ROOT / "04_analysis" / "outputs" / "tables" / "fig_provincial_credit_2011_data.csv"
BASE = "2011-06-01"
MIN_SHARE, MIN_COVER = 0.20, 0.90
BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"


def flooded_provinces() -> list[str]:
    s = pd.read_csv(SHARES, keep_default_na=False, na_values=[""])
    keep = (s.share_parcels_with_gfd >= MIN_COVER) & (s.gfd_flood_share_2011 >= MIN_SHARE)
    return sorted(s.loc[keep & (s.province != "bangkok"), "province"])


def main() -> None:
    flooded = flooded_provinces()
    df = pd.read_csv(SRC, parse_dates=["date"], keep_default_na=False, na_values=[""])
    df = df[(df.level == "province") & df.date.between("2010-01-01", "2013-12-01")]
    df["slug"] = df.province_en.str.lower().str.replace(" ", "-")
    assert set(flooded) <= set(df.slug), set(flooded) - set(df.slug)
    df["group"] = df.slug.isin(flooded).map({True: "flooded", False: "other"})
    g = df.groupby(["date", "group"]).loans_mthb.sum().unstack()
    idx = 100 * g / g.loc[BASE]
    # reindex to a full monthly calendar so that the missing year 2012 shows as a gap
    idx = idx.reindex(pd.date_range("2010-01-01", "2013-12-01", freq="MS"))
    idx.to_csv(TAB, index_label="date")

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK,
        "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
        "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    })
    fig, ax = plt.subplots(figsize=(6.3, 3.6))
    ax.axvspan(pd.Timestamp("2011-08-01"), pd.Timestamp("2011-12-31"), color=GRID, lw=0)
    ax.axvspan(pd.Timestamp("2012-01-01"), pd.Timestamp("2012-12-31"), facecolor="none",
               hatch="////", edgecolor=GRID, lw=0)
    names = ", ".join(p.replace("-", " ").title().replace("Phra Nakhon Si ", "") for p in flooded)
    ax.plot(idx.index, idx["flooded"], color=BLUE, lw=2,
            label=f"Provinces with 2011 flood share ≥ {MIN_SHARE:.0%} ({len(flooded)})")
    ax.plot(idx.index, idx["other"], color=ORANGE, lw=2, label="All other provinces (excl. Bangkok)")
    ax.axhline(100, color=INK2, lw=0.6, ls=":")
    ax.text(pd.Timestamp("2011-10-15"), 0.97, "2011\nfloods", transform=ax.get_xaxis_transform(),
            ha="center", va="top", fontsize=7.5, color=INK2)
    ax.text(pd.Timestamp("2012-07-01"), 0.5, "2012: no data\n(series FI_CB_011_S3\nnot located)",
            transform=ax.get_xaxis_transform(), ha="center", va="center", fontsize=7.5,
            color=INK2, bbox=dict(fc=SURF, ec="none", pad=1.5))
    ax.set_xlim(pd.Timestamp("2010-01-01"), pd.Timestamp("2013-12-31"))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[4, 7, 10]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_ylabel("Total loans, index (Jun 2011 = 100)")
    ax.grid(axis="y", color=GRID, lw=0.6)
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    note = (f"High-flood group: {names} (parcel-weighted Global Flood Database DFO 3850 share ≥ {MIN_SHARE:.2f}, "
            f"≥ {MIN_COVER:.0%} of parcels in the event footprint). Sums of end-of-month commercial-bank loans by "
            "booking province; Jan 2010–Dec 2011 from FI_CB_011_S2, 2013 from FI_CB_011_S4 (same total-loan "
            "definition; levels not adjusted). Descriptive only. Source: Bank of Thailand, FI_CB_011_S2 and "
            "FI_CB_011_S4 (data.go.th ds-459, CC BY), accessed 2 Nov 2026; author's calculations.")
    fig.text(0.01, 0.005, textwrap.fill(note, 128), fontsize=6.3, color=INK2, va="bottom", ha="left")
    fig.tight_layout(rect=(0, 0.14, 1, 1))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(OUT.with_suffix(f".{ext}"), dpi=300)
    plt.close(fig)
    print("high-flood group:", flooded)
    print(idx.loc[["2010-01-01", "2011-06-01", "2011-09-01", "2011-12-01", "2013-01-01", "2013-12-01"]].round(1))


if __name__ == "__main__":
    main()

"""Motivating facts for RQ1 (descriptive only): appraisal values vs 2011 flood exposure.

Input:  03_data/processed/sheet_panel.csv.gz (build_sheet_panel.py)
        03_data/processed/sheet_landcover_basin.csv.gz (build_sheet_landcover.py; WorldCover 2021)
Sample: core Chao Phraya basin provinces (listed below), decoded sheets with GFD data,
        scales 1:4,000 (rural, 2 km) and 1:1,000 (urban, 500 m).
Outputs:
- figures/fig_appraisal_flood_binned.{png,pdf}: within-cell (province x 1:50,000 sheet x
  scale) effects of 2011 flood-share bins on mean parcel log value, relative to <1% flooded,
  sheets weighted equally (as in the planned design), with and without 2021 land-cover shares.
- figures/fig_basin_maps.{png,pdf}: 2011 flood share and log appraisal value by sheet.
- tables/appraisal_flood_binned.{csv,md} (bin effects by outcome, weighting and controls),
  tables/appraisal_flood_within.{csv,md}, tables/flood_share_support.{csv,md} (flood-share
  support and land-pixel counts by sheet type), tables/landcover_by_flood_bin.{csv,md}.
Nothing here is causal: flood-prone land differs in many ways (see 05_design/identification.md).

Run: .venv/bin/python -I 04_analysis/src/fig_appraisal_flood.py
"""

import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import statsmodels.api as sm  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PANEL = ROOT / "03_data/processed/sheet_panel.csv.gz"
LANDCOVER = ROOT / "03_data/processed/sheet_landcover_basin.csv.gz"
LC = ["lc_builtup", "lc_cropland", "lc_tree", "lc_water"]  # shares of 10 m pixels; rest = other
FIG = ROOT / "04_analysis/outputs/figures"
TAB = ROOT / "04_analysis/outputs/tables"
BASIN = ["bangkok", "nonthaburi", "pathum-thani", "phra-nakhon-si-ayutthaya", "ang-thong",
         "sing-buri", "chai-nat", "lop-buri", "nakhon-sawan", "suphan-buri", "uthai-thani",
         "phichit", "saraburi", "nakhon-pathom", "samut-prakan", "phitsanulok", "kamphaeng-phet"]
Y = "mean_logp"  # main outcome: parcel log value (parcel-weighted sheet mean); p90 is robustness
BINS = [-0.001, 0.01, 0.2, 0.4, 0.6, 0.8, 1.0]
LABELS = ["<1%", "1–20%", "20–40%", "40–60%", "60–80%", "80–100%"]
SCALES = {4000: ("Rural sheets (1:4,000, 2 km)", "#2a78d6"),
          1000: ("Urban sheets (1:1,000, 500 m)", "#eb6834")}
SOURCE = ("Source: Treasury Department official land values, round 2023–26 (snapshot 2026-11-02); "
          "Global Flood Database event DFO 3850 (Tellman et al. 2021); ESA WorldCover 2021 v200 "
          "(Zanaga et al. 2022); author's calculations.")
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
})


def load() -> pd.DataFrame:
    d = pd.read_csv(PANEL, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                     keep_default_na=False, na_values=[""])  # keep the province "nan" (Nan)
    d = d[d["province"].isin(BASIN) & d["gfd_flood_share"].notna() & d["scale"].isin(SCALES)].copy()
    lc = pd.read_csv(LANDCOVER, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str},
                     keep_default_na=False, na_values=[""])
    key = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
    for k in key:
        d[k], lc[k] = d[k].astype(str), lc[k].astype(str)
    d = d.merge(lc[key + LC], on=key, how="left", validate="1:1")
    assert d[LC].notna().all().all()
    d["cell"] = d["province"] + "|" + d["series_sheet"] + "|" + d["scale"].astype(str)
    w = d["n_parcels"]
    for c in ["mean_logp", "p90_logp", "gfd_flood_share"]:
        cm = (d[c] * w).groupby(d["cell"]).transform("sum") / w.groupby(d["cell"]).transform("sum")
        d[c + "_dm"] = d[c] - cm
    d["bin"] = pd.cut(d["gfd_flood_share"], BINS, labels=LABELS)
    return d


def bin_effects(d: pd.DataFrame) -> pd.DataFrame:
    """Within-cell flood-share bin effects (reference bin <1%), by outcome, weighting and controls.

    Bin dummies, controls and the outcome are demeaned within province x 1:50,000 sheet x scale
    cells using the regression weights (parcels, or 1 per sheet as in the planned design);
    standard errors are clustered by 1:50,000 sheet. With controls, the 2021 land-cover shares
    (built-up, cropland, tree, water) enter linearly; land cover may itself respond to flood
    risk, so the controlled estimates are descriptive, not a hazard discount.
    """
    rows = []
    for y in [Y, "p90_logp"]:
        for sc in SCALES:
            g = d[d["scale"] == sc]
            for wname in ["sheets", "parcels"]:
                w = g["n_parcels"].astype(float) if wname == "parcels" else pd.Series(1.0, index=g.index)
                for ctrl in [False, True]:
                    X = pd.get_dummies(g["bin"]).reindex(columns=LABELS, fill_value=0).astype(float)[LABELS[1:]]
                    if ctrl:
                        X = pd.concat([X, g[LC]], axis=1)
                    Z = pd.concat([X, g[y]], axis=1)
                    Z = Z - (Z.mul(w, axis=0)).groupby(g["cell"]).transform("sum").div(
                        w.groupby(g["cell"]).transform("sum"), axis=0)
                    res = sm.WLS(Z[y], Z[X.columns], weights=w).fit(
                        cov_type="cluster", cov_kwds={"groups": pd.factorize(g["series_sheet"])[0]})
                    for b in LABELS:
                        gb = g[g["bin"] == b]
                        rows.append({"outcome": y, "scale": sc, "weights": wname, "landcover_controls": ctrl,
                                     "flood_share_bin": b, "sheets": len(gb), "parcels": int(gb["n_parcels"].sum()),
                                     "clusters": gb["series_sheet"].nunique(),
                                     "effect": 0.0 if b == LABELS[0] else res.params[b],
                                     "se_cluster": np.nan if b == LABELS[0] else res.bse[b]})
    return pd.DataFrame(rows)


def landcover_by_bin(d: pd.DataFrame) -> pd.DataFrame:
    """Mean 2021 land-cover shares by scale and 2011 flood-share bin (sheets weighted equally)."""
    return (d.groupby(["scale", "bin"], observed=True)[LC].mean()
            .reset_index().rename(columns={"bin": "flood_share_bin"}))


def within_reg(d: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for y in [Y, "p90_logp"]:
        for sc in SCALES:
            g = d[d["scale"] == sc]
            res = sm.WLS(g[y + "_dm"], g[["gfd_flood_share_dm"]], weights=g["n_parcels"]).fit(
                cov_type="cluster", cov_kwds={"groups": pd.factorize(g["series_sheet"])[0]})
            rows.append({"outcome": y, "scale": sc, "coef_flood_share": res.params.iloc[0],
                         "se_cluster": res.bse.iloc[0], "sheets": len(g),
                         "clusters_1to50k": g["series_sheet"].nunique(), "parcels": int(g["n_parcels"].sum())})
    return pd.DataFrame(rows)


def note(fig, extra: str) -> None:
    fig.text(0.01, 0.005, textwrap.fill(SOURCE + " " + extra, 128), fontsize=6.3, color=INK2, va="bottom")


def fig_binned(t: pd.DataFrame) -> None:
    t = t[(t["outcome"] == Y) & (t["weights"] == "sheets")]
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 3.3), sharey=True)
    x = np.arange(len(LABELS))
    for ax, (sc, (lab, col)) in zip(axes, sorted(SCALES.items(), key=lambda kv: kv[0], reverse=True)):
        for k, (ctrl, name) in enumerate([(False, "Within cell"), (True, "+ 2021 land-cover shares")]):
            s = t[(t["scale"] == sc) & (t["landcover_controls"] == ctrl)].set_index("flood_share_bin").reindex(LABELS)
            xs = x + (k - 0.5) * 0.24
            ax.errorbar(xs, s["effect"], yerr=2 * s["se_cluster"], fmt="none", ecolor=col, elinewidth=1.2, capsize=0)
            ax.plot(xs, s["effect"], "o", ms=6 if not ctrl else 5, label=name, color=col if not ctrl else SURF,
                    markeredgecolor=col if ctrl else SURF, markeredgewidth=1.3)
            if not ctrl:
                for j, (xi, yi, n) in enumerate(zip(xs, s["effect"], s["sheets"])):
                    ax.annotate(f"{int(n):,}", (xi, yi), xytext=(-5, 7 if j == 0 else 0), textcoords="offset points",
                                ha="right", va="center", fontsize=5.5, color=INK2)
        ax.axhline(0, color=INK2, lw=0.8)
        ax.set_xticks(x, ["<1\n(ref.)"] + [b.rstrip("%") for b in LABELS[1:]], fontsize=7)
        ax.set_xlim(-0.6, len(LABELS) - 0.4)
        ax.set_title(lab, fontsize=8.5, color=INK, loc="left")
        ax.grid(axis="y", color=GRID, lw=0.6)
        ax.legend(frameon=False, loc="lower left", fontsize=7)
    axes[0].set_ylabel("Log official value relative to\n<1% flooded, within cell")
    fig.supxlabel("Share of sheet flooded in 2011, % (Global Flood Database, land pixels)", fontsize=8.5, color=INK)
    fig.tight_layout()  # sources and definitions are in the proposal caption, not repeated here
    for ext in ("png", "pdf"):
        fig.savefig(FIG / f"fig_appraisal_flood_binned.{ext}", dpi=300)
    plt.close(fig)


def fig_maps(d: pd.DataFrame) -> None:
    d = d.assign(cx=(d["lon0"] + d["lon1"]) / 2, cy=(d["lat0"] + d["lat1"]) / 2)
    d = d.sort_values("scale", ascending=False)  # draw 2 km sheets first, 500 m on top
    size = np.where(d["scale"] == 4000, 1.6, 0.4)
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 4.6), sharex=True, sharey=True)
    specs = [("gfd_flood_share", "Share flooded, 2011", "Blues", (0, 1)),
             (Y, "Mean log official value per parcel", "Oranges", None)]
    for ax, (col, title, cmap, lim) in zip(axes, specs):
        vmin, vmax = lim if lim else np.nanpercentile(d[col], [2, 98])
        sc = ax.scatter(d["cx"], d["cy"], c=d[col], s=size, marker="s", cmap=cmap, vmin=vmin, vmax=vmax,
                        linewidths=0, rasterized=True)
        ax.set_title(title, fontsize=9, color=INK, loc="left")
        ax.set_aspect("equal")
        ax.tick_params(labelsize=7)
        cb = fig.colorbar(sc, ax=ax, orientation="horizontal", fraction=0.045, pad=0.08)
        cb.ax.tick_params(labelsize=7)
        cb.outline.set_visible(False)
    axes[0].set_ylabel("Latitude (°N)")
    axes[0].set_ylim(13.4, 17.5)
    # Notes and sources are given in the paper's figure note (paper/sections/appendix.tex), not inside the image.
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIG / f"fig_basin_maps.{ext}", dpi=300)
    plt.close(fig)


def support(d: pd.DataFrame) -> pd.DataFrame:
    """How many distinct values the 2011 flood share takes per sheet type (MODIS 250 m quantisation)."""
    rows = []
    for sc, g in d.groupby("scale"):
        s = g["gfd_flood_share"]
        rows.append({"scale": sc, "sheets": len(g), "share_exactly_0": (s == 0).mean(),
                     "share_at_least_0999": (s >= 0.999).mean(), "share_interior": ((s > 0) & (s < 0.999)).mean(),
                     "distinct_values_4dp": s.round(4).nunique(),
                     "land_px_min": int(g["gfd_land_px"].min()), "land_px_max": int(g["gfd_land_px"].max()),
                     "land_px_median": float(g["gfd_land_px"].median()),
                     "share_land_px_eq_4": (g["gfd_land_px"] == 4).mean()})
    return pd.DataFrame(rows)


def reconciliation() -> pd.DataFrame:
    """Located parcels in the basin provinces by map scale, and how many enter the pilot."""
    d = pd.read_csv(PANEL, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                    keep_default_na=False, na_values=[""])
    d = d[d["province"].isin(BASIN)]
    g = d.groupby("scale").agg(sheets=("n_parcels", "size"), parcels=("n_parcels", "sum"))
    g["parcels_with_flood_data"] = d[d["gfd_flood_share"].notna()].groupby("scale")["n_parcels"].sum()
    g["in_pilot"] = g.index.isin(list(SCALES))
    g = g.reset_index().fillna({"parcels_with_flood_data": 0})
    tot = {"scale": "total", "sheets": g["sheets"].sum(), "parcels": g["parcels"].sum(),
           "parcels_with_flood_data": g["parcels_with_flood_data"].sum(), "in_pilot": False}
    pil = {"scale": "pilot (1:4,000 and 1:1,000 with flood data)", "sheets": None, "parcels": None,
           "parcels_with_flood_data": g.loc[g["in_pilot"], "parcels_with_flood_data"].sum(), "in_pilot": True}
    out = pd.concat([g.astype({"scale": str}), pd.DataFrame([tot, pil])], ignore_index=True)
    return out.astype({"sheets": "Int64", "parcels": "Int64", "parcels_with_flood_data": "Int64"})


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    TAB.mkdir(parents=True, exist_ok=True)
    d = load()
    t = bin_effects(d)
    r = within_reg(d)
    for name, df in [("appraisal_flood_binned", t), ("appraisal_flood_within", r),
                     ("flood_share_support", support(d)), ("landcover_by_flood_bin", landcover_by_bin(d)),
                     ("pilot_parcel_reconciliation", reconciliation())]:
        df.to_csv(TAB / f"{name}.csv", index=False)
        (TAB / f"{name}.md").write_text(
            f"<!-- {SOURCE} Descriptive only. -->\n\n" + df.round(4).to_markdown(index=False) + "\n", encoding="utf-8")
    fig_binned(t)
    fig_maps(d)
    print(t[(t["outcome"] == Y)].round(3).to_string(index=False))
    print(r.round(4).to_string(index=False))


if __name__ == "__main__":
    main()

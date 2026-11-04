"""Coverage and data-quality summary of the sheet panel (numbers quoted in pilot_report.md).

Input:  03_data/processed/sheet_panel.csv.gz (build_sheet_panel.py)
Outputs:
- tables/sheet_panel_coverage.{csv,md}: parcels, sheets, located / GFD / GSW coverage (parcel-weighted).
- tables/province_flood_share_2011.{csv,md}: parcel-weighted 2011 GFD flood share and mean GSW
  occurrence by province file, for spotting implausible exposure (salt pans, aquaculture, cities).
- tables/sheet_price_discreteness.{csv,md}: distinct values per sheet, by scale.
Descriptive only.

Run: .venv/bin/python -I 04_analysis/src/panel_summary.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PANEL = ROOT / "03_data/processed/sheet_panel.csv.gz"
TAB = ROOT / "04_analysis/outputs/tables"
SOURCE = ("Source: Treasury Department appraisal values, round 2023–26 (snapshot 2026-11-02); Global Flood "
          "Database DFO 3850; JRC Global Surface Water v1.4; author's calculations. Descriptive only.")


def wmean(x: pd.Series, w: pd.Series) -> float:
    ok = x.notna()
    return float(np.average(x[ok], weights=w[ok])) if ok.any() else np.nan


def write(df: pd.DataFrame, name: str) -> None:
    df.to_csv(TAB / f"{name}.csv", index=False)
    (TAB / f"{name}.md").write_text(f"<!-- {SOURCE} -->\n\n" + df.round(4).to_markdown(index=False) + "\n",
                                    encoding="utf-8")


def main() -> None:
    TAB.mkdir(parents=True, exist_ok=True)
    d = pd.read_csv(PANEL, usecols=["province", "n_parcels", "n_distinct_p", "scale", "lon0",
                                    "gfd_flood_share", "gsw_occurrence_mean"],
                    keep_default_na=False, na_values=[""])  # keep the province "nan" (Nan)
    w = d["n_parcels"]
    cov = pd.DataFrame([{
        "provinces": d["province"].nunique(), "sheet_refs": len(d), "parcels": int(w.sum()),
        "share_parcels_located": w[d["lon0"].notna()].sum() / w.sum(),
        "share_parcels_with_gfd": w[d["gfd_flood_share"].notna()].sum() / w.sum(),
        "share_parcels_with_gsw": w[d["gsw_occurrence_mean"].notna()].sum() / w.sum(),
    }])
    write(cov, "sheet_panel_coverage")

    prov = (d.groupby("province")
            .apply(lambda g: pd.Series({
                "parcels": int(g["n_parcels"].sum()),
                "share_parcels_with_gfd": g.loc[g["gfd_flood_share"].notna(), "n_parcels"].sum()
                / g["n_parcels"].sum(),
                "gfd_flood_share_2011": wmean(g["gfd_flood_share"], g["n_parcels"]),
                "gsw_occurrence_mean": wmean(g["gsw_occurrence_mean"], g["n_parcels"]),
            }), include_groups=False)
            .reset_index().sort_values("gfd_flood_share_2011", ascending=False))
    write(prov, "province_flood_share_2011")

    disc = (d[d["scale"].isin([4000, 2000, 1000, 500])].groupby("scale")
            .agg(sheets=("n_parcels", "size"), median_parcels=("n_parcels", "median"),
                 median_distinct_values=("n_distinct_p", "median"),
                 p90_distinct_values=("n_distinct_p", lambda s: s.quantile(0.9)))
            .reset_index())
    write(disc, "sheet_price_discreteness")
    print(cov.round(3).to_string(index=False))
    print(prov.head(12).round(3).to_string(index=False))
    print(prov[prov["share_parcels_with_gfd"] < 0.5].round(3).to_string(index=False))
    print(disc.to_string(index=False))


if __name__ == "__main__":
    main()

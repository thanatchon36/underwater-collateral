"""2024 northern floods: share of each cadastral sheet inside the UNOSAT water extent.

Input:  03_data/raw/flood/unosat_fl20240912tha_chiangrai/FL20240912THA_SHP.7z (UNOSAT
        activation FL20240912THA, CC BY-SA; layers *_AccumulatedFlood and *_AnalysisExtent
        for Chiang Rai, 1 Aug-12 Oct 2024, and Phayao, 1 Aug-10 Oct 2024),
        03_data/processed/sheet_panel.csv.gz.
Output: 03_data/processed/sheet_flood2024_north.csv.gz (sheet-level exposure),
        04_analysis/outputs/tables/flood2024_treated_sheets.{csv,md} (counts; descriptive).
The archive is extracted to 03_data/processed/unosat_fl20240912tha/ (raw stays untouched).
Sheets are WGS84 bounding boxes of the decoded Indian 1975 sheets; areas in EPSG:32647.

Run: .venv/bin/python -I 04_analysis/src/exposure_2024_north.py
"""

from pathlib import Path

import geopandas as gpd
import pandas as pd
import py7zr
from shapely.geometry import box

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "03_data/raw/flood/unosat_fl20240912tha_chiangrai/FL20240912THA_SHP.7z"
EXTRACT = ROOT / "03_data/processed/unosat_fl20240912tha"
PANEL = ROOT / "03_data/processed/sheet_panel.csv.gz"
OUT = ROOT / "03_data/processed/sheet_flood2024_north.csv.gz"
TAB = ROOT / "04_analysis/outputs/tables"
AREAS = {"chiang-rai": "CHIANGRAI_20240801_20241012", "phayao": "PHAYAO_20240801_20241010"}
EXTENT = {"chiang-rai": "CHIANGRAI_20240801_20241022", "phayao": "PHAYAO_20240801_20241010"}
UTM = "EPSG:32647"


def layer(name: str) -> gpd.GeoDataFrame:
    return gpd.read_file(EXTRACT / "FL20240912THA_SHP" / f"{name}.shp").to_crs(UTM)


def main() -> None:
    if not (EXTRACT / "FL20240912THA_SHP").exists():
        EXTRACT.mkdir(parents=True, exist_ok=True)
        with py7zr.SevenZipFile(ARCHIVE) as z:
            z.extractall(EXTRACT)
    panel = pd.read_csv(PANEL, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                     keep_default_na=False, na_values=[""])  # keep the province "nan" (Nan)
    parts = []
    for prov in AREAS:
        s = panel[(panel["province"] == prov) & panel["lon0"].notna()].copy()
        g = gpd.GeoDataFrame(s, geometry=[box(*b) for b in s[["lon0", "lat0", "lon1", "lat1"]].to_numpy()],
                             crs="EPSG:4326").to_crs(UTM)
        flood = layer(f"{AREAS[prov]}_AccumulatedFlood").union_all()
        extent = layer(f"{EXTENT[prov]}_AnalysisExtent").union_all()
        g["sheet_km2"] = g.area / 1e6
        g["flood2024_share"] = g.intersection(flood).area / g.area
        g["in_analysis_extent"] = g.centroid.within(extent)
        parts.append(pd.DataFrame(g.drop(columns="geometry")))
        print(prov, len(g), "sheets", flush=True)
    d = pd.concat(parts, ignore_index=True)
    d.to_csv(OUT, index=False, compression="gzip")

    rows = []
    a = d[d["in_analysis_extent"]]
    for prov, gp in a.groupby("province"):
        for sc, gs in gp.groupby("scale"):
            for thr in (0.0, 0.1, 0.25):
                t = gs[gs["flood2024_share"] > thr]
                rows.append({"province": prov, "scale": int(sc), "threshold_share_gt": thr,
                             "treated_sheets": len(t), "treated_parcels": int(t["n_parcels"].sum()),
                             "sheets_in_extent": len(gs), "parcels_in_extent": int(gs["n_parcels"].sum())})
    t = pd.DataFrame(rows)
    TAB.mkdir(parents=True, exist_ok=True)
    t.to_csv(TAB / "flood2024_treated_sheets.csv", index=False)
    (TAB / "flood2024_treated_sheets.md").write_text(
        "<!-- Source: UNOSAT FL20240912THA water extents (CC BY-SA); Treasury appraisal snapshot "
        "2026-11-02; author's calculations. Sheets whose centre lies in the UNOSAT analysis extent. "
        "Descriptive only. -->\n\n" + t.to_markdown(index=False) + "\n", encoding="utf-8")
    print(t.to_string(index=False))


if __name__ == "__main__":
    main()

"""District (amphoe) and subdistrict (tambon) of every RQ1 2024 radar sample sheet.

Used by the administrative-spillover sensitivity (PAP section 3): controls in areas with a 2024
emergency-zone declaration (DDPM) are dropped. Declarations name districts, subdistricts and
villages, so each sheet needs its district and subdistrict.

Data: OCHA COD-AB Thailand (Royal Thai Survey Department; CC BY-IGO), admin levels 2 (928
districts) and 3 (7,425 subdistricts), read in place from the downloaded geodatabase zip.

Rule (fixed before any declaration list was obtained, 2026-11-03):
- A sheet's district is the district of the sheet's own province that holds the largest share of
  the sheet's bounding box (areas in UTM 47N); its tambon is the tambon of that district holding
  the largest share. The share is recorded; a sheet whose box
  misses every unit of its province (boundary offsets) takes the nearest unit, with share 0.

Outputs: 03_data/processed/rq1_2024_sheet_admin.csv.gz (sheet key, adm2/adm3 P-code, Thai and
         English names, overlap shares)
         03_data/processed/rq1_admin_units.csv.gz (every district and subdistrict of the sample
         provinces, for matching declaration names, including units without sample sheets)
Run: .venv/bin/python -I 04_analysis/src/build_sheet_admin.py
"""

from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import box

ROOT = Path(__file__).resolve().parents[2]
GDB = ("/vsizip/" + str(ROOT / "03_data/raw/admin_boundaries/cod_ab_tha/tha_admin_boundaries.gdb.zip")
       + "/tha_admin_boundaries.gdb")
SAMPLE = ROOT / "03_data/processed/rq1_2024_sample_sheets.csv.gz"
OUT = ROOT / "03_data/processed/rq1_2024_sheet_admin.csv.gz"
UNITS = ROOT / "03_data/processed/rq1_admin_units.csv.gz"
SHEET = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
UTM = "EPSG:32647"


def slug(name):
    return name.strip().lower().replace(" ", "-")


def assign(sheets, units, level, parent=None):
    """Largest-overlap unit of the sheet's own province at one admin level (within `parent`, the
    sheet's assigned district, for tambons, so a sheet's tambon always lies in its district)."""
    code, th, en = f"adm{level}_pcode", f"adm{level}_name1", f"adm{level}_name"
    u = units[["province", code, th, en] + (["adm2_pcode"] if parent is not None else []) + ["geometry"]].to_crs(UTM)
    s = sheets.to_crs(UTM)
    s["box_area"] = s.area
    x = gpd.overlay(s[["sid", "province", "box_area", "geometry"]], u, how="intersection", keep_geom_type=True)
    x = x[x["province_1"] == x["province_2"]]
    if parent is not None:
        x = x[x["adm2_pcode"] == x["sid"].map(parent)]
    x["share"] = x.area / x["box_area"]
    best = x.sort_values("share").drop_duplicates("sid", keep="last").set_index("sid")
    out = pd.DataFrame(index=s["sid"])
    out[[code, th, en, f"adm{level}_share"]] = best[[code, th, en, "share"]]
    miss = out[code].isna()
    for i in out.index[miss]:          # nearest unit of the same province (and district, for tambons)
        g = s.loc[s["sid"] == i].iloc[0]
        cand = u[u["province"] == g["province"]]
        if parent is not None:
            cand = cand[cand["adm2_pcode"] == parent[i]]
        j = cand.distance(g.geometry).idxmin()
        out.loc[i, [code, th, en, f"adm{level}_share"]] = [cand.at[j, code], cand.at[j, th], cand.at[j, en], 0.0]
    return out, int(miss.sum())


def main() -> None:
    s = pd.read_csv(SAMPLE, dtype={c: str for c in SHEET})
    s["sid"] = range(len(s))
    sheets = gpd.GeoDataFrame(s, geometry=[box(*b) for b in s[["lon0", "lat0", "lon1", "lat1"]].to_numpy()],
                              crs="EPSG:4326")
    bbox = tuple(sheets.total_bounds + [-0.1, -0.1, 0.1, 0.1])
    out = s[SHEET + ["group"]].copy()
    for level in (2, 3):
        units = gpd.read_file(GDB, layer=f"tha_admin{level}", bbox=bbox, engine="pyogrio")
        units["province"] = units["adm1_name"].map(slug)
        a, missed = assign(sheets, units, level, parent=None if level == 2 else out["adm2_pcode"])
        out = out.join(a.reset_index(drop=True))
        print(f"adm{level}: {out[f'adm{level}_pcode'].nunique()} units; {missed} sheets by nearest unit; "
              f"median largest share {out[f'adm{level}_share'].median():.2f}")
    assert set(out["province"]) <= set(units["province"]), "sample province missing from COD-AB"
    out.to_csv(OUT, index=False)
    units[units["province"].isin(set(out["province"]))][
        ["province", "adm2_pcode", "adm2_name1", "adm2_name", "adm3_pcode", "adm3_name1", "adm3_name"]
    ].sort_values("adm3_pcode").to_csv(UNITS, index=False)
    print(out.groupby(["province", "group"])["adm2_pcode"].nunique().unstack())


if __name__ == "__main__":
    main()

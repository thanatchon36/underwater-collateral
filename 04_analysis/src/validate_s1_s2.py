"""Optical check of the Sentinel-1 flood rule in all four radar provinces (referee round 12, weakness 3).

Data: Copernicus Sentinel-2 L2A scene classification (SCL, 20 m), read in place from the Microsoft
Planetary Computer collection `sentinel-2-l2a` (anonymous SAS token; no account). Nothing is stored
except the scene list and per-sheet counts.

Sample: the RQ1 2024 radar sample written by rq1_2024_pooled.py
(03_data/processed/rq1_2024_sample_sheets.csv.gz): every treated sheet and every 5 km
hazard-comparable control that is dry in every source.

Rule (fixed before looking at the results; recorded in the pre-analysis plan draft, section 8):
- Window: 15 Aug - 31 Oct (the radar north window) in 2024 (flood season) and 2023 (reference).
- A scene is usable for a sheet if at least half of the sheet's bounding-box pixels are clear
  (SCL 4 vegetation, 5 bare, 6 water); cloud, shadow, cirrus, saturated and no-data are not clear.
- Water share on a usable scene = SCL 6 pixels / clear pixels.
- Optical new water = (largest 2024 water share) - (largest 2023 water share), over usable scenes.
- A sheet is optically flooded if new water > 0.10 (lower than the radar's 25% because optical
  scenes are rarer and cloud hides the flood peak); a sheet with no usable scene in either year
  is "unobserved".
Reported by province and group: sheets, observed sheets, share optically flooded (for treated
sheets, optical precision; for controls, optical contamination), and the median new-water share.
Optical SCL water misses water under vegetation and among buildings, so for treated sheets this is
a lower bound on precision.

Outputs: 03_data/raw/flood/s2_l2a_scenes/scenes_rq1_2024.csv (scene ids, dates, cloud cover)
         03_data/processed/s2_sheet_water_rq1_2024.csv.gz  (per sheet and scene: clear, water px)
         03_data/processed/s2_sheet_keys_rq1_2024.csv.gz   (sheet_id -> sheet key and box; first written
                                                            2026-11-02 from the sample the counts were made on,
                                                            after check_alignment passed on every sheet)
         04_analysis/outputs/tables/s1_s2_validation.{csv,md}
Run: .venv/bin/python -I 04_analysis/src/validate_s1_s2.py
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
import requests
from rasterio.warp import transform_bounds
from rasterio.windows import from_bounds

ROOT = Path(__file__).resolve().parents[2]
SAMPLE = ROOT / "03_data/processed/rq1_2024_sample_sheets.csv.gz"
SCENES = ROOT / "03_data/raw/flood/s2_l2a_scenes/scenes_rq1_2024.csv"
COUNTS = ROOT / "03_data/processed/s2_sheet_water_rq1_2024.csv.gz"
KEYS = ROOT / "03_data/processed/s2_sheet_keys_rq1_2024.csv.gz"
SHEET = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
TAB = ROOT / "04_analysis/outputs/tables"
UA = {"User-Agent": "underwater-collateral-datafetch/0.1"}
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1/search"
TOKEN = "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel-2-l2a"
WINDOW = ("08-15", "10-31")
YEARS = [2023, 2024]
CLEAR, WATER = (4, 5, 6), 6
MIN_CLEAR, NEW_WATER = 0.5, 0.10
WORKERS = 8


def check_alignment(keys, counts, tol=1.5):
    """Sheet ids of `counts` whose pixel counts do not fit the box in `keys` (empty if aligned).

    Each scene read covers the sheet's box in the scene's UTM zone (47N or 48N) at 20 m, so every
    recorded px must equal W x H with W and H within `tol` pixels of the box's width and height.
    """
    px = counts.groupby("sheet_id")["px"].unique()
    k = keys.set_index("sheet_id")
    bad = []
    for i, vals in px.items():
        r = k.loc[i]
        fits = []
        for crs in ("EPSG:32647", "EPSG:32648"):
            b = transform_bounds("EPSG:4326", crs, r.lon0, r.lat0, r.lon1, r.lat1)
            w, h = (b[2] - b[0]) / 20, (b[3] - b[1]) / 20
            fits.append({v for v in vals for W in range(int(w - tol), int(w + tol) + 2)
                         if v % W == 0 and abs(v // W - h) <= tol})
        if set(vals) - (fits[0] | fits[1]):
            bad.append(i)
    return bad


def search(bbox, year):
    body = {"collections": ["sentinel-2-l2a"], "bbox": list(bbox),
            "datetime": f"{year}-{WINDOW[0]}/{year}-{WINDOW[1]}", "limit": 500}
    out, url = [], STAC
    while url:
        r = requests.post(url, json=body, headers=UA, timeout=120)
        r.raise_for_status()
        j = r.json()
        out += j["features"]
        nxt = [lnk for lnk in j.get("links", []) if lnk.get("rel") == "next"]
        url, body = (nxt[0]["href"], nxt[0].get("body", body)) if nxt else (None, None)
        time.sleep(1)
    return [f for f in out if "SCL" in f["assets"]]


_TOK = {"t": 0.0, "v": ""}
_LOCK = threading.Lock()


def token():
    """Anonymous SAS token, refreshed every 20 minutes (tokens expire after about an hour)."""
    with _LOCK:
        if time.time() - _TOK["t"] > 1200:
            _TOK["v"] = requests.get(TOKEN, headers=UA, timeout=60).json()["token"]
            _TOK["t"] = time.time()
        return _TOK["v"]


def read_scene(feat, sheets):
    """Clear and water pixel counts for every sample sheet whose box intersects the scene."""
    w, s, e, n = feat["bbox"]
    sub = sheets[(sheets.lon1 > w) & (sheets.lon0 < e) & (sheets.lat1 > s) & (sheets.lat0 < n)]
    if sub.empty:
        return []
    for attempt in range(3):
        try:
            rows = []
            with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", VSI_CACHE=True), \
                    rasterio.open(feat["assets"]["SCL"]["href"] + "?" + token()) as src:
                for r in sub.itertuples():
                    b = transform_bounds("EPSG:4326", src.crs, r.lon0, r.lat0, r.lon1, r.lat1)
                    win = from_bounds(*b, transform=src.transform).round_offsets().round_lengths()
                    a = src.read(1, window=win, boundless=True, fill_value=0)
                    if a.size == 0:
                        continue
                    clear = np.isin(a, CLEAR)
                    rows.append({"sheet_id": r.sheet_id, "scene": feat["id"], "date": feat["properties"]["datetime"][:10],
                                 "px": int(a.size), "clear": int(clear.sum()), "water": int((a == WATER).sum())})
            return rows
        except Exception:  # transient network errors
            if attempt == 2:
                return [{"sheet_id": None, "scene": feat["id"], "date": None, "px": -1, "clear": 0, "water": 0}]
            time.sleep(5)


def main() -> None:
    sh = pd.read_csv(SAMPLE, dtype={c: str for c in SHEET})   # keys stay strings ("03" is not "3")
    sh["sheet_id"] = np.arange(len(sh))
    sh[["sheet_id"] + SHEET + ["lon0", "lat0", "lon1", "lat1"]].to_csv(KEYS, index=False)
    feats = {}
    for _, g in sh.groupby("province"):  # one search per province box (the four are far apart)
        bbox = (g.lon0.min(), g.lat0.min(), g.lon1.max(), g.lat1.max())
        for y in YEARS:
            feats |= {f["id"]: f for f in search(bbox, y)}
    feats = list(feats.values())
    SCENES.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([{"id": f["id"], "datetime": f["properties"]["datetime"],
                   "cloud_cover": f["properties"].get("eo:cloud_cover")} for f in feats]).to_csv(SCENES, index=False)
    print(f"{len(feats)} Sentinel-2 L2A scenes over {len(sh)} sample sheets", flush=True)
    rows, failed, t0 = [], 0, time.time()
    with ThreadPoolExecutor(WORKERS) as ex:
        futs = [ex.submit(read_scene, f, sh) for f in feats]
        for i, fu in enumerate(as_completed(futs), 1):
            res = fu.result()
            failed += sum(r["px"] < 0 for r in res)
            rows += [r for r in res if r["px"] >= 0]
            if i % 50 == 0:
                print(f"  {i}/{len(feats)} scenes, {time.time() - t0:.0f} s", flush=True)
    c = pd.DataFrame(rows)
    c.to_csv(COUNTS, index=False)
    c["year"] = c["date"].str[:4].astype(int)
    u = c[c["clear"] >= MIN_CLEAR * c["px"]].assign(share=lambda d: d["water"] / d["clear"])
    mx = u.groupby(["sheet_id", "year"])["share"].max().unstack()
    sh = sh.join(mx.rename(columns={2023: "water_2023", 2024: "water_2024"}), on="sheet_id")
    sh["observed"] = sh["water_2023"].notna() & sh["water_2024"].notna()
    sh["new_water"] = sh["water_2024"] - sh["water_2023"]
    sh["optical_flooded"] = sh["new_water"] > NEW_WATER
    o = sh[sh["observed"]]
    by = lambda g: pd.Series({"sheets": len(g), "observed": int(g["observed"].sum()),  # noqa: E731
                              "share_optically_flooded": o.loc[o.index.intersection(g.index), "optical_flooded"].mean(),
                              "median_new_water": o.loc[o.index.intersection(g.index), "new_water"].median()})
    out = pd.concat([sh.groupby(["group", "province"]).apply(by, include_groups=False).reset_index(),
                     sh.groupby("group").apply(by, include_groups=False).reset_index().assign(province="all")])
    TAB.mkdir(parents=True, exist_ok=True)
    out.to_csv(TAB / "s1_s2_validation.csv", index=False)
    (TAB / "s1_s2_validation.md").write_text(
        "<!-- Optical (Sentinel-2 L2A SCL) check of the Sentinel-1 rule, RQ1 2024 radar sample. Observed = at least one "
        f"scene with >= {MIN_CLEAR:.0%} clear pixels in both 2023 and 2024 (15 Aug - 31 Oct). Optically flooded = largest 2024 "
        f"water share minus largest 2023 water share > {NEW_WATER}. For treated sheets the share is a lower bound on precision; "
        f"for controls it is a contamination rate. {failed} scene reads failed. Sources: Copernicus Sentinel-2 L2A via "
        "Microsoft Planetary Computer; author's calculations. -->\n\n" + out.round(3).to_markdown(index=False) + "\n",
        encoding="utf-8")
    print(out.round(3).to_string(index=False))


if __name__ == "__main__":
    main()

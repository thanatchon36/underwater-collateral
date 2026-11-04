"""Rule-based Sentinel-1 flood maps for Thailand, 2024 and 2025 seasons (pooled RQ1 sample).

Data: Copernicus Sentinel-1 GRD (IW, VV), read in place from the Microsoft Planetary Computer
collection `sentinel-1-grd` (anonymous SAS token; no account; Copernicus Sentinel data legal
notice). Nothing is stored except the scene list and the derived maps.

Fixed rule (to be copied verbatim into the pre-analysis plan):
- Regions and windows. North (11.0-20.5 N): 15 Aug-31 Oct. South (5.6-11.0 N): 15 Nov-31 Dec.
  Flood seasons 2024 and 2025; reference season 2023 with the same windows.
- Each scene: VV band at overview level 2 (8 x 8 pixels of the 10 m GRDH grid), calibrated to
  sigma0 with the product's sigmaNought LUT (sigma0 = DN^2 / A^2), in dB; geocoded with the
  product's GCPs onto a 0.001-degree WGS84 grid (bilinear). DN = 0 is no data.
- A pixel is water in a scene if sigma0_VV < -18 dB.
- Flooded in season Y if water in at least one season-Y scene, water in no 2023 scene, and seen
  in at least two 2023 scenes. Permanent water, radar shadow and paddy flooded in both years are
  thereby excluded.
- Sheet flood share = flooded pixels / valid pixels (seen in season Y, seen in >= 2 reference
  scenes and dry in all of them) inside the sheet's WGS84 bounding box.

Outputs:
  03_data/raw/flood/s1_grd_scenes/scenes.csv          scene ids, dates, orbits (metadata only)
  03_data/processed/flood_s1/s1_flood_{north,south}.tif  uint8 bit flags: 1 flood 2024,
      2 flood 2025, 4 valid 2024, 8 valid 2025
  03_data/processed/sheet_flood_s1.csv.gz              per sheet: s1_share_2024, s1_share_2025,
      s1_valid_px_2024, s1_valid_px_2025 (all located sheets nationwide)

Run: .venv/bin/python -I 04_analysis/src/flood_s1_grd.py   (about 3,000 scenes; 15-30 min)
"""

import csv
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
import requests
from rasterio.control import GroundControlPoint
from rasterio.transform import from_origin
from rasterio.warp import reproject, Resampling
from scipy.interpolate import RegularGridInterpolator

ROOT = Path(__file__).resolve().parents[2]
PANEL = ROOT / "03_data/processed/sheet_panel.csv.gz"
SCENES = ROOT / "03_data/raw/flood/s1_grd_scenes/scenes.csv"
OUTD = ROOT / "03_data/processed/flood_s1"
OUT = ROOT / "03_data/processed/sheet_flood_s1.csv.gz"
UA = {"User-Agent": "underwater-collateral-datafetch/0.1"}
STAC = "https://planetarycomputer.microsoft.com/api/stac/v1/search"
TOKEN = "https://planetarycomputer.microsoft.com/api/sas/v1/token/sentinel-1-grd"
RES = 0.001
REGIONS = {  # name: (bbox west, south, east, north), (window start MM-DD, end MM-DD)
    "north": ((97.3, 11.0, 105.7, 20.5), ("08-15", "10-31")),
    "south": ((97.3, 5.6, 102.2, 11.0), ("11-15", "12-31")),
}
YEARS = [2023, 2024, 2025]
WATER_DB, MIN_REF_OBS, OV = -18.0, 2, 2  # OV = overview index (factor 8)


def grid(region):
    (w, s, e, n), _ = REGIONS[region]
    return int(round((n - s) / RES)), int(round((e - w) / RES)), from_origin(w, n, RES, RES)


def search(region, year):
    (bbox, (a, b)) = REGIONS[region]
    body = {"collections": ["sentinel-1-grd"], "bbox": list(bbox), "datetime": f"{year}-{a}/{year}-{b}",
            "limit": 500, "query": {"sar:instrument_mode": {"eq": "IW"}}}
    out, url = [], STAC
    while url:
        r = requests.post(url, json=body, headers=UA, timeout=120)
        r.raise_for_status()
        j = r.json()
        out += j["features"]
        nxt = [lnk for lnk in j.get("links", []) if lnk.get("rel") == "next"]
        url, body = (nxt[0]["href"], nxt[0].get("body", body)) if nxt else (None, None)
        time.sleep(1)
    return [f for f in out if "vv" in f["assets"]]


def calib_lut(xml_text):
    root = ET.fromstring(xml_text)
    lines, pix, vals = [], None, []
    for v in root.iter("calibrationVector"):
        lines.append(int(v.find("line").text))
        p = np.array(v.find("pixel").text.split(), dtype=float)
        s = np.array(v.find("sigmaNought").text.split(), dtype=float)
        if pix is None:
            pix = p
        vals.append(np.interp(pix, p, s))
    return RegularGridInterpolator((np.array(lines, float), pix), np.array(vals), bounds_error=False, fill_value=None)


def process(job):
    """Read one scene and return its water/valid masks on the region grid window."""
    region, year, href, cal_href, token = job
    H, W, tr = grid(region)
    for attempt in range(3):
        try:
            with rasterio.open(href + "?" + token) as full:
                fh, fw = full.height, full.width
                gcps, _ = full.gcps
            with rasterio.open(href + "?" + token, overview_level=OV) as s:
                dn = s.read(1).astype("float64")
            cal = requests.get(cal_href + "?" + token, headers=UA, timeout=120).text
            break
        except Exception:  # transient network errors
            if attempt == 2:
                return None
            time.sleep(5)
    oh, ow = dn.shape
    fy, fx = fh / oh, fw / ow
    rr, cc = np.meshgrid((np.arange(oh) + 0.5) * fy, (np.arange(ow) + 0.5) * fx, indexing="ij")
    lut = calib_lut(cal)
    a = lut(np.c_[np.clip(rr.ravel(), lut.grid[0][0], lut.grid[0][-1]),
                  np.clip(cc.ravel(), lut.grid[1][0], lut.grid[1][-1])]).reshape(oh, ow)
    with np.errstate(divide="ignore"):
        db = np.where(dn > 0, 10 * np.log10(dn ** 2 / a ** 2), np.nan).astype("float32")
    g2 = [GroundControlPoint(row=g.row / fy, col=g.col / fx, x=g.x, y=g.y) for g in gcps]
    xs, ys = [g.x for g in gcps], [g.y for g in gcps]
    c0 = max(int(np.floor((min(xs) - tr.c) / RES)), 0)
    c1 = min(int(np.ceil((max(xs) - tr.c) / RES)), W)
    r0 = max(int(np.floor((tr.f - max(ys)) / RES)), 0)
    r1 = min(int(np.ceil((tr.f - min(ys)) / RES)), H)
    if c1 <= c0 or r1 <= r0:
        return None
    dst = np.full((r1 - r0, c1 - c0), np.nan, dtype="float32")
    reproject(db, dst, gcps=g2, src_crs="EPSG:4326", src_nodata=np.nan,
              dst_transform=tr * rasterio.Affine.translation(c0, r0), dst_crs="EPSG:4326",
              dst_nodata=np.nan, resampling=Resampling.bilinear)
    valid = ~np.isnan(dst)
    return region, year, r0, c0, valid, valid & (dst < WATER_DB)


def main() -> None:
    OUTD.mkdir(parents=True, exist_ok=True)
    SCENES.parent.mkdir(parents=True, exist_ok=True)
    acc = {r: {y: [np.zeros(grid(r)[:2], np.uint8), np.zeros(grid(r)[:2], np.uint8)] for y in YEARS} for r in REGIONS}
    jobs, rows = [], []
    token = requests.get(TOKEN, headers=UA, timeout=30).json()["token"]
    for r in REGIONS:
        for y in YEARS:
            for f in search(r, y):
                p = f["properties"]
                rows.append({"region": r, "season": y, "id": f["id"], "datetime": p["datetime"],
                             "relative_orbit": p.get("sat:relative_orbit"), "orbit_state": p.get("sat:orbit_state"),
                             "vv_href": f["assets"]["vv"]["href"]})
                jobs.append((r, y, f["assets"]["vv"]["href"], f["assets"]["schema-calibration-vv"]["href"]))
    with open(SCENES, "w", newline="", encoding="utf-8") as fo:
        w = csv.DictWriter(fo, fieldnames=list(rows[0]) + ["accessed"])
        w.writeheader()
        w.writerows([{**x, "accessed": "2026-11-02"} for x in rows])
    print(len(jobs), "scenes", flush=True)
    done, failed, t0 = 0, 0, time.time()
    for i0 in range(0, len(jobs), 400):  # refresh the SAS token for each batch
        token = requests.get(TOKEN, headers=UA, timeout=30).json()["token"]
        with ProcessPoolExecutor(max_workers=10) as ex:
            futs = [ex.submit(process, j + (token,)) for j in jobs[i0:i0 + 400]]
            for fu in as_completed(futs):
                res = fu.result()
                done += 1
                if res is None:
                    failed += 1
                    continue
                r, y, r0, c0, valid, water = res
                sl = (slice(r0, r0 + valid.shape[0]), slice(c0, c0 + valid.shape[1]))
                acc[r][y][0][sl] = np.minimum(acc[r][y][0][sl].astype(np.uint16) + valid, 255).astype(np.uint8)
                acc[r][y][1][sl] = np.minimum(acc[r][y][1][sl].astype(np.uint16) + water, 255).astype(np.uint8)
                if done % 100 == 0:
                    print(done, "done", failed, "failed", round(time.time() - t0), "s", flush=True)
    print(done, "done", failed, "failed", flush=True)

    d = pd.read_csv(PANEL, dtype={"UTMMAP1": str, "UTMMAP3": str, "UTMMAP4": str, "prov_code": str},
                    keep_default_na=False, na_values=[""])
    d = d[d["lon0"].notna()].reset_index(drop=True)
    for c in ["s1_share_2024", "s1_share_2025", "s1_valid_px_2024", "s1_valid_px_2025"]:
        d[c] = np.nan
    for r in REGIONS:
        H, W, tr = grid(r)
        (w_, s_, e_, n_), _ = REGIONS[r]
        ref_ok = (acc[r][2023][1] == 0) & (acc[r][2023][0] >= MIN_REF_OBS)
        flags = np.zeros((H, W), np.uint8)
        layers = {}
        for k, y in [(1, 2024), (2, 2025)]:
            valid = ref_ok & (acc[r][y][0] > 0)
            flood = ref_ok & (acc[r][y][1] > 0)
            flags |= (flood * k).astype(np.uint8) | (valid * (4 * k)).astype(np.uint8)
            layers[y] = (np.pad(flood, ((1, 0), (1, 0))).cumsum(0).cumsum(1, dtype=np.int64),
                         np.pad(valid, ((1, 0), (1, 0))).cumsum(0).cumsum(1, dtype=np.int64))
        with rasterio.open(OUTD / f"s1_flood_{r}.tif", "w", driver="GTiff", height=H, width=W, count=1,
                           dtype="uint8", crs="EPSG:4326", transform=tr, compress="deflate") as o:
            o.write(flags, 1)
        cy = (d["lat0"] + d["lat1"]) / 2
        cx = (d["lon0"] + d["lon1"]) / 2
        m = (cy >= s_) & (cy < n_) & (cx >= w_) & (cx < e_)
        idx = d.index[m]
        c0 = np.clip(np.floor((d.loc[m, "lon0"] - w_) / RES).astype(int), 0, W)
        c1 = np.clip(np.ceil((d.loc[m, "lon1"] - w_) / RES).astype(int), 0, W)
        r0 = np.clip(np.floor((n_ - d.loc[m, "lat1"]) / RES).astype(int), 0, H)
        r1 = np.clip(np.ceil((n_ - d.loc[m, "lat0"]) / RES).astype(int), 0, H)
        for y in (2024, 2025):
            fs, vs = layers[y]
            box = lambda S: S[r1, c1] - S[r0, c1] - S[r1, c0] + S[r0, c0]  # noqa: E731
            fl, va = box(fs), box(vs)
            d.loc[idx, f"s1_valid_px_{y}"] = va
            d.loc[idx, f"s1_share_{y}"] = np.where(va > 0, fl / np.maximum(va, 1), np.nan)
    keep = ["prov_code", "province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE", "scale",
            "series_sheet", "n_parcels", "mean_logp", "lon0", "lat0", "lon1", "lat1",
            "s1_share_2024", "s1_share_2025", "s1_valid_px_2024", "s1_valid_px_2025"]
    d[keep].to_csv(OUT, index=False, compression="gzip")
    print((d["s1_share_2024"] > 0.25).sum(), "sheets > 25% flooded in 2024")


if __name__ == "__main__":
    main()

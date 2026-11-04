"""Sentinel-1 water in the 2021 and 2022 flood windows, for the RQ1 "2021-23 radar reference" sensitivity.

The primary flood rule (flood_s1_grd.py) uses 2023 as the reference season: a pixel is flooded in
2024 if it shows water in a 2024 scene and in no 2023 scene. The sensitivity (PAP section 3) also
requires no water in any 2021 or 2022 scene of the same window (15 Aug-31 Oct, north region), so
land that floods in most years drops out. This script maps, on the north grid of flood_s1_grd.py,
every pixel seen and every pixel with water in at least one 2021-22 scene, over the bounding box
of the four primary sample provinces only (the sensitivity holds provinces fixed).

Data and processing: as flood_s1_grd.py (Planetary Computer `sentinel-1-grd`, anonymous SAS token;
VV overview level 2, sigma0 < -18 dB; the same `process` function).

Outputs:
  03_data/raw/flood/s1_grd_scenes/scenes_2021_22.csv        scene ids, dates, orbits (metadata only)
  03_data/raw/flood/s1_grd_scenes/scenes_2021_22_failed.csv scenes whose read failed (not in the map)
  03_data/processed/flood_s1/s1_water_2021_22_north.tif     uint8: 1 water in any 2021-22 scene,
                                                            2 seen in at least one 2021-22 scene
Run: .venv/bin/python -I 04_analysis/src/flood_s1_reference_2122.py   (network; not in run_all)
"""

import csv
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flood_s1_grd import OUTD, REGIONS, STAC, TOKEN, UA, grid, process  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SAMPLE = ROOT / "03_data/processed/rq1_2024_sample_sheets.csv.gz"
SCENES = ROOT / "03_data/raw/flood/s1_grd_scenes/scenes_2021_22.csv"
OUT = OUTD / "s1_water_2021_22_north.tif"
YEARS = [2021, 2022]
MARGIN = 0.05


def sample_bbox():
    s = pd.read_csv(SAMPLE)
    return [s["lon0"].min() - MARGIN, s["lat0"].min() - MARGIN, s["lon1"].max() + MARGIN, s["lat1"].max() + MARGIN]


def search(bbox, year):
    a, b = REGIONS["north"][1]
    body = {"collections": ["sentinel-1-grd"], "bbox": bbox, "datetime": f"{year}-{a}/{year}-{b}",
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


def main() -> None:
    bbox = sample_bbox()
    H, W, tr = grid("north")
    seen = np.zeros((H, W), bool)
    water = np.zeros((H, W), bool)
    jobs, rows = [], []
    for y in YEARS:
        for f in search(bbox, y):
            p = f["properties"]
            rows.append({"season": y, "id": f["id"], "datetime": p["datetime"],
                         "relative_orbit": p.get("sat:relative_orbit"), "orbit_state": p.get("sat:orbit_state"),
                         "vv_href": f["assets"]["vv"]["href"]})
            jobs.append(("north", y, f["assets"]["vv"]["href"], f["assets"]["schema-calibration-vv"]["href"]))
    SCENES.parent.mkdir(parents=True, exist_ok=True)
    with open(SCENES, "w", newline="", encoding="utf-8") as fo:
        w = csv.DictWriter(fo, fieldnames=list(rows[0]) + ["accessed"])
        w.writeheader()
        w.writerows([{**x, "accessed": "2026-11-02"} for x in rows])
    print(len(jobs), "scenes in", [round(v, 2) for v in bbox], flush=True)
    done, failed, lost, t0 = 0, 0, [], time.time()
    for i0 in range(0, len(jobs), 400):
        token = requests.get(TOKEN, headers=UA, timeout=30).json()["token"]
        with ProcessPoolExecutor(max_workers=8) as ex:
            futs = {ex.submit(process, j + (token,)): j[2] for j in jobs[i0:i0 + 400]}
            for fu in as_completed(futs):
                res = fu.result()
                done += 1
                if res is None:
                    failed += 1
                    lost.append(futs[fu])
                    continue
                _, _, r0, c0, valid, wat = res
                sl = (slice(r0, r0 + valid.shape[0]), slice(c0, c0 + valid.shape[1]))
                seen[sl] |= valid
                water[sl] |= wat
                if done % 50 == 0:
                    print(done, "done", failed, "failed", round(time.time() - t0), "s", flush=True)
    print(done, "done", failed, "failed", flush=True)
    pd.DataFrame({"vv_href": lost}).to_csv(SCENES.with_name("scenes_2021_22_failed.csv"), index=False)
    OUTD.mkdir(parents=True, exist_ok=True)
    with rasterio.open(OUT, "w", driver="GTiff", height=H, width=W, count=1, dtype="uint8", crs="EPSG:4326",
                       transform=tr, compress="deflate") as o:
        o.write(water.astype(np.uint8) | (seen.astype(np.uint8) * 2), 1)
    print("written", OUT)


if __name__ == "__main__":
    main()

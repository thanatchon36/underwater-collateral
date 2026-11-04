"""Sentinel-1 flood shares of the RQ1 2024 sample sheets in the 2026 season (later-flood sensitivity).

Why: a flood between the 2024 event and the survey of R1 (the first schedule after 2023-26) would
contaminate both groups. The primary rule already requires controls to be dry in 2025 and treated
sheets not to flood again in 2025. In 2026 there were local floods in the sample provinces (for
example, the Governor of Nakhon Phanom declared Mueang Nakhon Phanom an emergency disaster zone in
August 2026; Bangkok Biz News, read 2026-11-03). This script measures the 2026 season with the
registered radar rule so that the PAP sensitivity (section 5, "later floods") can drop such sheets.

Rule: identical to flood_s1_grd.py with season 2026 and reference 2023 (north window 15 Aug-31 Oct;
VV overview level 2, sigma0 < -18 dB; flooded if water in at least one 2026 scene, in no 2023 scene,
and seen in at least two 2023 scenes; share = flooded / valid pixels in the sheet's WGS84 box).
The 2023 reference is re-read over the sample's bounding box with the same `process` function.
2023 scenes are Sentinel-1A; 2026 scenes are Sentinel-1C and 1D (same C-band SAR, same product).
Fixed on 2026-11-03, the day the 2026 shares were computed, and before R1 exists. The decision to
add the sensitivity followed press reports of 2026 floods; the drop rule copies the primary thresholds
(controls >= 1%, treated > 25%) and the usable-sheet rule (valid pixels >= half the box, applied in
rq1_round_change.later_floods). 2026 has more scenes than 2023 (Sentinel-1C and 1D: 228 scenes on 65
dates against 174 on 42), so the any-scene rule flags water more readily in 2026; the count of
sheets dropped more likely errs high than low, and the rule is registered, not the count.

Check: the 2023 reference re-read here must reproduce the primary map. Every pixel the primary map
marks valid in 2024 (flood_s1/s1_flood_north.tif, bit 4) must be reference-valid here; the share of
such pixels that are not is printed and must be below 0.5% (scene-read failures), or the run stops.
The check runs one way: pixels reference-valid here but not valid in the primary map are not tested,
and such pixels could add 2026 water that the primary reference would have excluded (disclosed in PAP
section 9; it can only add to the sheets dropped).

Outputs:
  03_data/raw/flood/s1_grd_scenes/scenes_2026.csv          scene ids, dates, orbits (metadata only)
  03_data/raw/flood/s1_grd_scenes/scenes_2026_failed.csv   scenes whose read failed
  03_data/processed/rq1_2024_sheet_flood_2026.csv.gz       sample sheet key, group, s1_share_2026,
                                                           s1_valid_px_2026, valid_frac_2026
Run: .venv/bin/python -I 04_analysis/src/flood_s1_2026.py   (network; about 400 scenes; not in run_all)
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
from flood_s1_grd import MIN_REF_OBS, OUTD, RES, TOKEN, UA, grid, process  # noqa: E402
from flood_s1_reference_2122 import sample_bbox, search  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SAMPLE = ROOT / "03_data/processed/rq1_2024_sample_sheets.csv.gz"
PRIMARY = OUTD / "s1_flood_north.tif"
SCENES = ROOT / "03_data/raw/flood/s1_grd_scenes/scenes_2026.csv"
OUT = ROOT / "03_data/processed/rq1_2024_sheet_flood_2026.csv.gz"
SHEET = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
REF, SEASON = 2023, 2026
MAX_REF_MISMATCH = 0.005


def box_sums(layer, d, H, W, w_, n_):
    S = np.pad(layer, ((1, 0), (1, 0))).cumsum(0).cumsum(1, dtype=np.int64)
    c0 = np.clip(np.floor((d["lon0"] - w_) / RES).astype(int), 0, W)
    c1 = np.clip(np.ceil((d["lon1"] - w_) / RES).astype(int), 0, W)
    r0 = np.clip(np.floor((n_ - d["lat1"]) / RES).astype(int), 0, H)
    r1 = np.clip(np.ceil((n_ - d["lat0"]) / RES).astype(int), 0, H)
    return S[r1, c1] - S[r0, c1] - S[r1, c0] + S[r0, c0]


def main() -> None:
    bbox = sample_bbox()
    H, W, tr = grid("north")
    w_, n_ = tr.c, tr.f
    seen = {y: np.zeros((H, W), np.uint8) for y in (REF, SEASON)}
    water = {y: np.zeros((H, W), np.uint8) for y in (REF, SEASON)}
    jobs, rows = [], []
    for y in (REF, SEASON):
        for f in search(bbox, y):
            p = f["properties"]
            rows.append({"season": y, "id": f["id"], "datetime": p["datetime"], "platform": p.get("platform"),
                         "relative_orbit": p.get("sat:relative_orbit"), "orbit_state": p.get("sat:orbit_state"),
                         "vv_href": f["assets"]["vv"]["href"]})
            jobs.append(("north", y, f["assets"]["vv"]["href"], f["assets"]["schema-calibration-vv"]["href"]))
    SCENES.parent.mkdir(parents=True, exist_ok=True)
    with open(SCENES, "w", newline="", encoding="utf-8") as fo:
        w = csv.DictWriter(fo, fieldnames=list(rows[0]) + ["accessed"])
        w.writeheader()
        w.writerows([{**x, "accessed": "2026-11-03"} for x in rows])
    print(len(jobs), "scenes", pd.Series([r["season"] for r in rows]).value_counts().to_dict(), flush=True)
    done, lost, t0 = 0, [], time.time()
    for i0 in range(0, len(jobs), 300):
        token = requests.get(TOKEN, headers=UA, timeout=30).json()["token"]
        with ProcessPoolExecutor(max_workers=8) as ex:
            futs = {ex.submit(process, j + (token,)): j for j in jobs[i0:i0 + 300]}
            for fu in as_completed(futs):
                res = fu.result()
                done += 1
                if res is None:
                    lost.append({"season": futs[fu][1], "vv_href": futs[fu][2]})
                    continue
                _, y, r0, c0, valid, wat = res
                sl = (slice(r0, r0 + valid.shape[0]), slice(c0, c0 + valid.shape[1]))
                seen[y][sl] = np.minimum(seen[y][sl].astype(np.uint16) + valid, 255).astype(np.uint8)
                water[y][sl] = np.minimum(water[y][sl].astype(np.uint16) + wat, 255).astype(np.uint8)
                if done % 50 == 0:
                    print(done, "done", len(lost), "failed", round(time.time() - t0), "s", flush=True)
    print(done, "done", len(lost), "failed", flush=True)
    pd.DataFrame(lost, columns=["season", "vv_href"]).to_csv(SCENES.with_name("scenes_2026_failed.csv"), index=False)

    ref_ok = (water[REF] == 0) & (seen[REF] >= MIN_REF_OBS)
    with rasterio.open(PRIMARY) as src:
        prim_valid24 = (src.read(1) & 4) > 0
    s = pd.read_csv(SAMPLE, dtype={c: str for c in SHEET})
    c0 = int(np.floor((bbox[0] - w_) / RES)); c1 = int(np.ceil((bbox[2] - w_) / RES))
    r0 = int(np.floor((n_ - bbox[3]) / RES)); r1 = int(np.ceil((n_ - bbox[1]) / RES))
    win = (slice(max(r0, 0), min(r1, H)), slice(max(c0, 0), min(c1, W)))
    pv = prim_valid24[win]
    mismatch = float((pv & ~ref_ok[win]).sum() / max(pv.sum(), 1))
    print(f"2023 reference check: {mismatch:.4%} of primary-valid pixels not reference-valid here", flush=True)
    if mismatch > MAX_REF_MISMATCH:
        raise SystemExit("2023 reference does not reproduce the primary map; not written")

    valid = ref_ok & (seen[SEASON] > 0)
    flood = ref_ok & (water[SEASON] > 0)
    fl, va = box_sums(flood, s, H, W, w_, n_), box_sums(valid, s, H, W, w_, n_)
    area_px = (s["lon1"] - s["lon0"]) * (s["lat1"] - s["lat0"]) / RES ** 2
    out = s[SHEET].copy()
    out["s1_valid_px_2026"] = va
    out["s1_share_2026"] = np.where(va > 0, fl / np.maximum(va, 1), np.nan)
    out["valid_frac_2026"] = va / area_px
    out["group"] = s["group"]
    out.to_csv(OUT, index=False, compression="gzip")
    g = s.assign(sh=out["s1_share_2026"])
    print(g.groupby(["province", "group"])["sh"].agg(["count", "median", lambda x: (x > 0.01).mean(),
                                                  lambda x: (x > 0.25).mean()]).round(3))
    print("written", OUT)


if __name__ == "__main__":
    main()

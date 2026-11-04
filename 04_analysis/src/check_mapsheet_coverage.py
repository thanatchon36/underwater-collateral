"""Decode coverage of the Treasury appraisal map-sheet references, by province.

Reads every complete province CSV in the appraisal snapshot (skips any file with a
matching ``.part``), decodes each distinct (UTMMAP1-4, UTMSCALE) reference with
``mapsheet.sheet_bounds`` and writes parcel-weighted coverage to
``04_analysis/outputs/tables/mapsheet_decode_coverage.csv``.

Run: .venv/bin/python -I 04_analysis/src/check_mapsheet_coverage.py
"""

import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mapsheet as m  # noqa: E402

ROOT = HERE.parents[1]
SNAP = ROOT / "03_data/raw/treasury_land_appraisal/snapshot_2026-11-02"
OUT = ROOT / "04_analysis/outputs/tables/mapsheet_decode_coverage.csv"
COLS = ["UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]


def classify(ref):
    try:
        fit = m.locate_4000(*ref[:3]) if int(float(ref[4])) != 5000 else None
        m.sheet_bounds(*ref)
        return "decoded_inside" if fit.miss_m == 0 else "decoded_edge"
    except ValueError as exc:
        msg = str(exc)
        if "UTMSCALE 5000" in msg:
            return "scale_5000"
        if "not a 1:50,000 sheet" in msg:
            return "bad_series_sheet"
        if "no candidate" in msg:
            return "inconsistent_code"
        return "invalid_field"


def main():
    rows = []
    for f in sorted(SNAP.glob("land_*.csv")):
        if f.with_suffix(".part").exists() or Path(str(f) + ".part").exists():
            continue
        df = pd.read_csv(f, dtype=str, usecols=COLS + ["EVAPRICE"]).fillna("")
        counts = df.groupby(COLS).size().rename("n").reset_index()
        counts["status"] = [classify(tuple(r)) for r in counts[COLS].itertuples(index=False)]
        by = counts.groupby("status")["n"].sum()
        scale = df["UTMSCALE"].value_counts()
        rows.append({
            "file": f.name,
            "parcels": len(df),
            "distinct_refs": len(counts),
            **{f"n_{s}": int(by.get(s, 0)) for s in
               ["decoded_inside", "decoded_edge", "scale_5000", "inconsistent_code", "bad_series_sheet", "invalid_field"]},
            **{f"n_scale_{s}": int(scale.get(s, 0)) for s in ["4000", "2000", "1000", "500", "5000"]},
        })
        print(rows[-1]["file"], rows[-1]["parcels"], flush=True)
    out = pd.DataFrame(rows)
    out["share_decoded"] = (out["n_decoded_inside"] + out["n_decoded_edge"]) / out["parcels"]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)
    tot = out.drop(columns=["file", "share_decoded"]).sum()
    print(tot.to_string())
    print("share decoded (parcel-weighted):", (tot["n_decoded_inside"] + tot["n_decoded_edge"]) / tot["parcels"])


if __name__ == "__main__":
    main()

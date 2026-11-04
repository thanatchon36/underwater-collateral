"""SHA-256 of the RQ1 sample files registered with the pre-analysis plan.

03_data/processed/ is not in git, so the registration records these hashes. Each hash is of the
decompressed CSV text: the gzip header stores a timestamp, so the compressed bytes change on every
rebuild while the content does not.

Output: 04_analysis/outputs/tables/registration_hashes.csv
Run: .venv/bin/python -I 04_analysis/src/hash_registration_inputs.py
"""

import gzip
import hashlib
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
FILES = ["03_data/processed/rq1_2024_sample_sheets.csv.gz",
         "03_data/processed/rq1_2024_unosat_sample_sheets.csv.gz",
         "03_data/processed/rq1_2025_sample_sheets.csv.gz",
         "03_data/processed/s2_sheet_water_rq1_2024.csv.gz",
         "03_data/processed/s2_sheet_keys_rq1_2024.csv.gz",
         "03_data/processed/rq1_2024_sheet_admin.csv.gz",
         "03_data/processed/rq1_admin_units.csv.gz",
         "03_data/processed/rq1_2024_sheet_flood_2026.csv.gz"] + [
         f"03_data/processed/rq1_2024_sens_{v}_sample_sheets.csv.gz"
         for v in ("thr10", "thr50", "prov20", "prov30", "buf2", "buf10", "nocap", "ref2123", "nocrop")]


def main() -> None:
    rows = []
    for f in FILES:
        raw = gzip.decompress((ROOT / f).read_bytes())
        rows.append({"file": f, "rows": raw.count(b"\n") - 1, "sha256_decompressed": hashlib.sha256(raw).hexdigest()})
    out = pd.DataFrame(rows)
    out.to_csv(ROOT / "04_analysis/outputs/tables/registration_hashes.csv", index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()

"""Regional BOT residential price indices around the 2024 northern and 2025 southern floods.

Descriptive only, for the no-access branch (a coarse read of lambda_B): the BOT index is
built from lenders' APPRAISAL prices in the mortgage-collateral database (hedonic,
rolling window, 3-month moving average; bib `bot2025rppi`, `bot2026rppislides`), so it
tracks bank collateral values, not transactions. It is regional, from representative
provinces (North includes Chiang Mai and Chiang Rai; South includes Songkhla, Phuket,
Surat Thani, Nakhon Si Thammarat), so most of each region's collateral did not flood.
Nothing here is a causal estimate.

Step 1 (clean): parse EC_EI_008_S4 (Jan 2011 - Sep 2026, 2011 = 100) to a long panel.
Step 2 (windows): for each flood (2011 Bangkok and vicinity, 2024 North, 2025 South), the region's log change minus the mean log change of
the other non-Bangkok regions, over the 12 months before the flood and over 3, 6 and 10
months after it (month -1 as base).

Input : 03_data/raw/bot_rppi/snapshot_2026-11-02/EC_EI_008_S4_monthly_2011-01_2026-09.csv
Output: 03_data/processed/bot_rppi_monthly.csv
        04_analysis/outputs/tables/rppi_flood_windows.{csv,md}
Run   : .venv/bin/python -I 04_analysis/src/rppi_flood_windows.py
"""

import csv
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "03_data/raw/bot_rppi/snapshot_2026-11-02/EC_EI_008_S4_monthly_2011-01_2026-09.csv"
PROC = ROOT / "03_data/processed/bot_rppi_monthly.csv"
TAB = ROOT / "04_analysis/outputs/tables"

TH_MONTH = {m: i + 1 for i, m in enumerate(
    ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."])}
TYPE_EN = {"ดัชนีราคารวมทุกประเภทที่อยู่อาศัย": "all", "ดัชนีราคาบ้านเดี่ยวพร้อมที่ดิน": "detached",
           "ดัชนีราคาทาวน์เฮ้าส์พร้อมที่ดิน": "townhouse", "ดัชนีราคาอาคารชุด": "condo"}
REGION_EN = {"ทั้งประเทศ": "Whole kingdom", "กรุงเทพ ฯ และปริมณฑล": "Bangkok and vicinity",
             "ภาคกลาง (ไม่รวมกรุงเทพ ฯ และปริมณฑล)": "Central", "ภาคเหนือ": "North",
             "ภาคตะวันออกเฉียงเหนือ": "Northeast", "ภาคใต้": "South"}
NON_BKK = ["Central", "North", "Northeast", "South"]
# 2011: comparison regions are the four non-Bangkok regions (Central's representative
# provinces, Chon Buri and Rayong, did not flood much); the series starts in January 2011,
# so there is no 12-month pre-period.
# flood month: first month of the event. North: flooding from August 2024 (UNOSAT window
# from 1 Aug 2024; BOT relief circular 30 Aug 2024, policy_timeline row 22), peak in Chiang
# Rai in September. South: "from mid-November 2025" (MoF release 164/2568, p. 1;
# 02_policy_context/level4_2025_notes.md B1).
EVENTS = [("Bangkok and vicinity", "2011-10", "Chao Phraya floods reach Bangkok's vicinity, Oct-Nov 2011"),
          ("North", "2024-08", "Northern floods incl. Chiang Rai, Aug-Oct 2024"),
          ("South", "2025-11", "Southern floods incl. Hat Yai (Songkhla), from mid-Nov 2025")]
HORIZONS = [3, 6, 10]


def clean() -> pd.DataFrame:
    rows = list(csv.reader(RAW.open(encoding="utf-8-sig")))
    hdr_i = next(i for i, r in enumerate(rows) if len(r) > 2 and re.match(r"\S+\.\S*\.? 25\d\d", r[2].strip()))
    dates, flags = [], []
    for c in rows[hdr_i][2:]:
        m = re.match(r"\s*(\S+\.\S*\.?)\s*(25\d\d)\s*(.*)", c)
        dates.append(f"{int(m.group(2)) - 543}-{TH_MONTH[m.group(1)]:02d}-01")
        flags.append({"p": "preliminary", "r": "revised"}.get(m.group(3).strip().lower(), ""))
    out, typ = [], None
    for r in rows[hdr_i + 1:]:
        if not r or not r[0].strip().isdigit():
            continue
        if not r[1].startswith(" "):
            typ = TYPE_EN[r[1].strip()]
            continue
        for d, f, v in zip(dates, flags, r[2:]):
            if v.strip() not in ("", "-"):
                out.append({"date": d, "type": typ, "region": REGION_EN[r[1].strip()],
                            "index_2011_100": float(v), "flag": f})
    df = pd.DataFrame(out).sort_values(["type", "region", "date"])
    PROC.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROC, index=False)
    return df


def shift(month: str, k: int) -> str:
    return (pd.Period(month, "M") + k).strftime("%Y-%m-01")


def main() -> None:
    df = clean()
    w = df[df.type == "all"].pivot(index="date", columns="region", values="index_2011_100")
    lw = np.log(w)
    res = []
    for region, month, label in EVENTS:
        others = [r for r in NON_BKK if r != region]
        base = shift(month, -1)

        def rel(a: str, b: str) -> float:
            if a not in lw.index or b not in lw.index:
                return np.nan
            return 100 * ((lw.loc[b, region] - lw.loc[a, region]) - (lw.loc[b, others] - lw.loc[a, others]).mean())

        row = {"region": region, "event": label, "base_month": base[:7],
               "pre_12m_rel_pct": rel(shift(month, -13), base)}
        for h in HORIZONS:
            end = shift(month, h)
            row[f"post_{h}m_rel_pct"] = rel(base, end) if end in lw.index else np.nan
        res.append(row)
    out = pd.DataFrame(res)
    TAB.mkdir(parents=True, exist_ok=True)
    out.to_csv(TAB / "rppi_flood_windows.csv", index=False)
    (TAB / "rppi_flood_windows.md").write_text(
        "<!-- Regional all-types residential price index (BOT EC_EI_008_S4, appraisal-based, 3-month moving "
        "average): log change of the flooded region minus the mean log change of the other non-Bangkok "
        "regions, in per cent. Pre = 12 months to month -1; post = month -1 to month +h. Descriptive only; "
        "the regions are mostly unflooded. -->\n\n" + out.round(2).to_markdown(index=False) + "\n",
        encoding="utf-8")
    print(f"{len(df):,} rows, {df.date.min()} to {df.date.max()}, flags: {df.flag.value_counts().to_dict()}")
    print(out.round(2).to_string(index=False))


if __name__ == "__main__":
    main()

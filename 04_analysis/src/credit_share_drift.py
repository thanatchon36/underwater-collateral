"""How much does the provincial mix of commercial-bank credit change? (RQ3 allocation)

RQ3 allocates credit by the latest public provincial shares: the latest December in the panel
that is not flagged preliminary (December 2025 in the 2026-11-02 snapshot; the BOT series
FI_CB_011_S5 runs to July 2026). As a gauge of how fast shares go stale, this computes the
dissimilarity index (half the sum of absolute share changes, i.e. the share of credit that would
have to move province) over several spans, for provinces outside Bangkok (Nong Khai and Bueng Kan
harmonised) and for all provinces with Bangkok as one unit. Booking location, not borrower
location (see clean_bot_provincial_credit.py).

Input:  03_data/processed/bot_provincial_credit_monthly.csv
Output: 04_analysis/outputs/tables/credit_share_drift.{csv,md}
        04_analysis/outputs/tables/credit_shares_allocation.csv (shares used by RQ3)
Run: .venv/bin/python -I 04_analysis/src/credit_share_drift.py
"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "03_data/processed/bot_provincial_credit_monthly.csv"
TAB = ROOT / "04_analysis/outputs/tables"
NK = {"Nong Khai", "Bueng Kan"}


def shares(d: pd.DataFrame, date: str, with_bkk: bool) -> pd.Series:
    m = d[d["date"] == date]
    prov = m[(m["level"] == "province") & ~m["province_en"].isin(NK)]
    parts = [prov, m[m["level"] == "harmonised"]]
    if with_bkk:
        parts.append(m[m["level"] == "bkk_total"])
    s = pd.concat(parts).set_index("province_en")["loans_mthb"]
    return s / s.sum()


def allocation_month(d: pd.DataFrame) -> str:
    """Latest December whose rows are not flagged preliminary."""
    prelim = d["flags"].fillna("").str.contains("preliminary")
    dec = d.loc[~prelim & d["date"].str[5:7].eq("12"), "date"]
    return dec.max()


def main() -> None:
    d = pd.read_csv(SRC)
    alloc = allocation_month(d)
    spans = [("2005-12-01", "2015-12-01"), ("2010-12-01", "2015-12-01"), ("2015-12-01", alloc), ("2019-12-01", alloc)]
    rows = []
    for start, end in spans:
        if start >= end or end not in set(d["date"]):
            continue
        for with_bkk in (False, True):
            a, b = shares(d, start, with_bkk), shares(d, end, with_bkk)
            a, b = a.align(b, fill_value=0)
            top = (b - a).abs().sort_values(ascending=False)
            rows.append({"from": start[:7], "to": end[:7], "units": "with Bangkok" if with_bkk else "outside Bangkok",
                         "n_units": len(a), "dissimilarity": 0.5 * (b - a).abs().sum(),
                         "largest_change_unit": top.index[0], "largest_change_pp": 100 * (b - a)[top.index[0]]})
    out = pd.DataFrame(rows)
    TAB.mkdir(parents=True, exist_ok=True)
    out.to_csv(TAB / "credit_share_drift.csv", index=False)
    (TAB / "credit_share_drift.md").write_text(
        f"<!-- Dissimilarity index of provincial loan shares (commercial banks, booking location). RQ3 allocation "
        f"month: {alloc[:7]}. Source: Bank of Thailand FI_CB_011_S2/S4/S5; author's calculations. -->\n\n"
        + out.round(3).to_markdown(index=False) + "\n", encoding="utf-8")
    sh = shares(d, alloc, with_bkk=True).rename("share").rename_axis("province_en").reset_index()
    sh.insert(1, "month", alloc[:7])
    sh.sort_values("share", ascending=False).to_csv(TAB / "credit_shares_allocation.csv", index=False)
    print(f"allocation month {alloc[:7]}")
    print(out.round(3).to_string(index=False))


if __name__ == "__main__":
    main()

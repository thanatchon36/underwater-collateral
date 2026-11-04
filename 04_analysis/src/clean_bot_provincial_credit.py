"""Clean BOT commercial-bank deposits and loans by province into a long monthly panel.

Input : 03_data/raw/bot_provincial_credit/snapshot_2026-11-02/FI_CB_011_*_YYYY-MM.csv
        (one CSV per month, exported unchanged from the BOT web table; see
        download_bot_provincial_credit.py)
Output: 03_data/processed/bot_provincial_credit_monthly.csv with columns
        province_th, province_en, date, loans_mthb, deposits_mthb, series_id,
        level, flags
        (level and flags are extra columns that document the issues below.)

Units: million baht, end-of-month outstanding, commercial banks, by BOOKING
location (the branch/office where the account is booked), not borrower location.

loans_mthb    = "รวมเงินให้สินเชื่อ" (total credit: overdrafts + loans + bills
                [+ "other" in S4]); the column total is identical in both series.
deposits_mthb = "รวมเงินรับฝาก" ("รวมเงินฝาก" in S5) (total deposits: demand, savings, fixed,
                promissory notes, certificates of deposit).

Issues handled (each is also flagged in the `flags` column):

1. Bueng Kan (บึงกาฬ) was created as a province in March 2011 out of Nong Khai
   (หนองคาย). In FI_CB_011_S2 its row exists but is BLANK in every month
   (footnote 2/), i.e. its offices are still reported inside Nong Khai up to
   Dec 2011. In FI_CB_011_S4 (from Jan 2013) it is reported separately, so Nong
   Khai drops by Bueng Kan's amount at the series break. Blank Bueng Kan cells
   are kept as missing (not zero). A harmonised unit
   "หนองคาย+บึงกาฬ" (level = harmonised) is added for every month so that
   cross-series comparisons use a stable boundary. Analyses on a consistent
   77->76 unit basis should use it instead of the two separate rows.

2. Bangkok head office versus branches. Both series split Bangkok into
   "สำนักงานใหญ่" (head offices: loans booked centrally, largely nationwide
   corporate and retail books) and "อื่น ๆ" (other Bangkok offices/branches).
   Rows: level = bkk_total (Bangkok as published), bkk_head_office,
   bkk_branches. The province-level panel (level = province) includes Bangkok
   only through its branches row ("กรุงเทพมหานคร (สาขา)"), because head-office
   balances are not Bangkok-local. The national total (level = national) is
   kept for reference.

3. FI_CB_011_S4 footnote 3/: from January 2015 some banks moved hire-purchase
   car loans from the branch to head office. Provincial loans (and Bangkok
   branches) can step down, and Bangkok head office up, in Jan 2015 for a
   reporting reason. Flag `hp_to_head_office_2015` on every S4 row from
   2015-01. Values are NOT adjusted (the bank-level shift is not published).

4. Series breaks.
   - FI_CB_011_S2 (Jul 2005 - Dec 2011) -> FI_CB_011_S4 (Jan 2013 -): province
     names and loan/deposit totals are defined the same way, but the regional
     groupings change (nine zones "เขต 1-9" in S2; four regions in S4) and S4
     adds an "other" loan component inside the same total. Regional subtotals
     are therefore dropped; only provinces, Bangkok rows and the national total
     are kept. Flag `series_break_2013` on Jan 2013 rows.
   - 2012 is MISSING: FI_CB_011_S3 (presumably 2012) could not be located on
     the BOT server on 2026-11-02. No interpolation is done.
   - FI_CB_011_S2 footnote 1/: from October 2006 the data no longer include
     international banking facilities (OUT-IN, OUT-OUT). Flag `no_ibf_from_2006_10`
     on S2 rows before Oct 2006 (they include IBF; mostly a Bangkok head-office
     issue).
   - FI_CB_011_S4 -> FI_CB_011_S5 (reportID 1008, Jul 2024 -): same columns,
     province rows and Bangkok split. S4 was frozen at its 8 Aug 2025 update with
     Nov 2024 - Feb 2025 and Jun 2025 still "p"; S5 is the live series (updated
     10 Sep 2026 in this snapshot). For the overlap (Jul 2024 - Jun 2025) the S5
     row is kept and the S4 row dropped; the size of the S4-S5 difference over the
     overlap is printed. Checked 2026-11-02: national loans differ by -0.2% (Dec
     2024), the median province by -0.4%; the largest gaps are Trang (-7%) and
     Krabi (+6%) to Mar 2025 and Bangkok other offices (-1.6%), i.e. revised
     booking, not a change of coverage (both are commercial banks, about THB 18
     trillion). S5 footnote 2/ repeats the Jan 2015 hire-purchase move,
     so S5 rows carry `hp_to_head_office_2015` too.
   - Month headers marked "r" (revised) in the source get the flag `revised`;
     "p" (preliminary, e.g. the latest months) get `preliminary`. A few older
     months (May 2007, Jul 2021, Apr 2022) are still marked "p" at source.

Usage: .venv/bin/python -I 04_analysis/src/clean_bot_provincial_credit.py
"""

import csv
import io
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "03_data" / "raw" / "bot_provincial_credit" / "snapshot_2026-11-02"
OUT = ROOT / "03_data" / "processed" / "bot_provincial_credit_monthly.csv"

LOANS_COL = "รวมเงินให้สินเชื่อ"
DEPOSITS_COL = "รวมเงินรับฝาก"

PROVINCE_EN = {
    "กรุงเทพมหานคร": "Bangkok", "กระบี่": "Krabi", "กาญจนบุรี": "Kanchanaburi",
    "กาฬสินธุ์": "Kalasin", "กำแพงเพชร": "Kamphaeng Phet", "ขอนแก่น": "Khon Kaen",
    "จันทบุรี": "Chanthaburi", "ฉะเชิงเทรา": "Chachoengsao", "ชลบุรี": "Chon Buri",
    "ชัยนาท": "Chai Nat", "ชัยภูมิ": "Chaiyaphum", "ชุมพร": "Chumphon",
    "เชียงราย": "Chiang Rai", "เชียงใหม่": "Chiang Mai", "ตรัง": "Trang",
    "ตราด": "Trat", "ตาก": "Tak", "นครนายก": "Nakhon Nayok", "นครปฐม": "Nakhon Pathom",
    "นครพนม": "Nakhon Phanom", "นครราชสีมา": "Nakhon Ratchasima",
    "นครศรีธรรมราช": "Nakhon Si Thammarat", "นครสวรรค์": "Nakhon Sawan",
    "นนทบุรี": "Nonthaburi", "นราธิวาส": "Narathiwat", "น่าน": "Nan",
    "บึงกาฬ": "Bueng Kan", "บุรีรัมย์": "Buri Ram", "ปทุมธานี": "Pathum Thani",
    "ประจวบคีรีขันธ์": "Prachuap Khiri Khan", "ปราจีนบุรี": "Prachin Buri",
    "ปัตตานี": "Pattani", "พระนครศรีอยุธยา": "Phra Nakhon Si Ayutthaya",
    "พะเยา": "Phayao", "พังงา": "Phangnga", "พัทลุง": "Phatthalung",
    "พิจิตร": "Phichit", "พิษณุโลก": "Phitsanulok", "เพชรบุรี": "Phetchaburi",
    "เพชรบูรณ์": "Phetchabun", "แพร่": "Phrae", "ภูเก็ต": "Phuket",
    "มหาสารคาม": "Maha Sarakham", "มุกดาหาร": "Mukdahan", "แม่ฮ่องสอน": "Mae Hong Son",
    "ยโสธร": "Yasothon", "ยะลา": "Yala", "ร้อยเอ็ด": "Roi Et", "ระนอง": "Ranong",
    "ระยอง": "Rayong", "ราชบุรี": "Ratchaburi", "ลพบุรี": "Lop Buri",
    "ลำปาง": "Lampang", "ลำพูน": "Lamphun", "เลย": "Loei", "ศรีสะเกษ": "Si Sa Ket",
    "สกลนคร": "Sakon Nakhon", "สงขลา": "Songkhla", "สตูล": "Satun",
    "สมุทรปราการ": "Samut Prakan", "สมุทรสงคราม": "Samut Songkhram",
    "สมุทรสาคร": "Samut Sakhon", "สระแก้ว": "Sa Kaeo", "สระบุรี": "Saraburi",
    "สิงห์บุรี": "Sing Buri", "สุโขทัย": "Sukhothai", "สุพรรณบุรี": "Suphan Buri",
    "สุราษฎร์ธานี": "Surat Thani", "สุรินทร์": "Surin", "หนองคาย": "Nong Khai",
    "หนองบัวลำภู": "Nong Bua Lam Phu", "อ่างทอง": "Ang Thong",
    "อำนาจเจริญ": "Amnat Charoen", "อุดรธานี": "Udon Thani", "อุตรดิตถ์": "Uttaradit",
    "อุทัยธานี": "Uthai Thani", "อุบลราชธานี": "Ubon Ratchathani",
}
TH_MONTH = {m: i + 1 for i, m in enumerate(
    ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.",
     "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."])}
AGGREGATE = re.compile(r"^(เขต \d|ภาค)")  # regional subtotals, dropped (issue 4)


def num(x: str):
    x = (x or "").replace(",", "").strip()
    return float(x) if x not in ("", "-") else float("nan")  # blank = missing, not zero


def parse_file(path: Path) -> list[dict]:
    series_id, ym = re.match(r"(FI_CB_011(?:_S\d)?)_(\d{4}-\d{2})\.csv$", path.name).groups()
    rows = list(csv.reader(io.StringIO(path.read_text(encoding="utf-8-sig"))))
    hdr_i = next(i for i, r in enumerate(rows) if LOANS_COL in r)
    hdr, period = rows[hdr_i], " ".join(c for c in rows[hdr_i - 1] if c.strip())
    m = re.match(r"\s*(\S+\.\S*\.?)\s*(25\d\d)\s*(.*)", period)
    assert m and f"{int(m.group(2)) - 543}-{TH_MONTH[m.group(1)]:02d}" == ym, (path, period)
    revised = "r" in m.group(3).lower()
    preliminary = "p" in m.group(3).lower()
    li = hdr.index(LOANS_COL)
    di = hdr.index(DEPOSITS_COL if DEPOSITS_COL in hdr else "รวมเงินฝาก")  # S5 header wording

    out, parent = [], None
    for r in rows[hdr_i + 1:]:
        if not r or not r[0].strip().isdigit():
            continue
        raw = r[1]
        indented = raw.startswith(" ")
        name = re.sub(r"\s*\d/\s*$", "", raw).strip()  # drop footnote markers like "2/"
        if not indented:
            parent = name
        if AGGREGATE.match(name):
            continue
        if name == "รวมทั้งสิ้น":
            level = "national"
        elif name == "กรุงเทพมหานคร":
            level = "bkk_total"
        elif parent == "กรุงเทพมหานคร" and indented:  # issue 2
            level = "bkk_head_office" if name == "สำนักงานใหญ่" else "bkk_branches"
            name = "กรุงเทพมหานคร (สำนักงานใหญ่)" if level == "bkk_head_office" else "กรุงเทพมหานคร (สาขา)"
        else:
            level = "province"
            if name not in PROVINCE_EN:
                raise ValueError(f"unknown province {name!r} in {path.name}")
        flags = []
        if revised:
            flags.append("revised")
        if preliminary:
            flags.append("preliminary")
        if series_id == "FI_CB_011_S2" and ym < "2006-10":
            flags.append("no_ibf_from_2006_10")
        if series_id in ("FI_CB_011_S4", "FI_CB_011_S5") and ym >= "2015-01":
            flags.append("hp_to_head_office_2015")  # issue 3
        if ym == "2013-01":
            flags.append("series_break_2013")  # issue 4
        if name in ("บึงกาฬ", "หนองคาย") and series_id == "FI_CB_011_S2":
            flags.append("bueng_kan_inside_nong_khai")  # issue 1
        out.append({"province_th": name, "level": level, "date": f"{ym}-01",
                    "loans_mthb": num(r[li]), "deposits_mthb": num(r[di]),
                    "series_id": series_id, "flags": ";".join(flags)})
    return out


def main() -> None:
    files = sorted(RAW.glob("FI_CB_011*_????-??.csv"))
    df = pd.DataFrame([row for f in files for row in parse_file(f)])

    # issue 4: S4/S5 overlap -> keep S5, report the difference first
    s5_dates = set(df.loc[df.series_id == "FI_CB_011_S5", "date"])
    ov = df[df.date.isin(s5_dates) & df.series_id.isin(["FI_CB_011_S4", "FI_CB_011_S5"])]
    if ov.series_id.nunique() == 2:
        w = ov.pivot_table(index=["date", "province_th"], columns="series_id", values="loans_mthb")
        rel = ((w["FI_CB_011_S5"] - w["FI_CB_011_S4"]).abs() / w["FI_CB_011_S4"]).dropna()
        print(f"S4 vs S5 overlap, {rel.index.get_level_values(0).nunique()} months: "
              f"max relative loan difference {rel.max():.2e}, rows differing > 0.1%: {(rel > 1e-3).sum()}")
    df = df[~(df.date.isin(s5_dates) & (df.series_id == "FI_CB_011_S4"))]

    # issue 1: harmonised Nong Khai + Bueng Kan unit (blank Bueng Kan counts as 0
    # here only because its offices are inside Nong Khai's figure in S2).
    nk = df[df.province_th.isin(["หนองคาย", "บึงกาฬ"])]
    combo = (nk.groupby(["date", "series_id"], as_index=False)
               .agg(loans_mthb=("loans_mthb", lambda s: s.sum(min_count=1)),
                    deposits_mthb=("deposits_mthb", lambda s: s.sum(min_count=1)),
                    flags=("flags", "first")))
    combo["province_th"], combo["level"] = "หนองคาย+บึงกาฬ", "harmonised"
    df = pd.concat([df, combo], ignore_index=True)

    en = dict(PROVINCE_EN)
    en.update({"กรุงเทพมหานคร (สำนักงานใหญ่)": "Bangkok (head office)",
               "กรุงเทพมหานคร (สาขา)": "Bangkok (other offices)",
               "หนองคาย+บึงกาฬ": "Nong Khai + Bueng Kan", "รวมทั้งสิ้น": "Whole kingdom"})
    df["province_en"] = df.province_th.map(en)
    df = df[["province_th", "province_en", "date", "loans_mthb", "deposits_mthb",
             "series_id", "level", "flags"]].sort_values(["date", "level", "province_th"])

    # sanity check: provinces + Bangkok (head office + other) add up to the national total
    chk = df[df.level.isin(["province", "bkk_head_office", "bkk_branches"])].groupby("date").loans_mthb.sum()
    nat = df[df.level == "national"].set_index("date").loans_mthb
    gap = ((chk - nat).abs() / nat).max()
    print(f"max relative gap, sum of units vs national loans: {gap:.2e}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False, encoding="utf-8")
    print(f"{len(files)} files, {len(df):,} rows, {df.date.min()} to {df.date.max()} -> {OUT}")
    months = sorted(df.date.unique())
    print("months:", len(months), "| by series:", df.groupby("series_id").date.nunique().to_dict())


if __name__ == "__main__":
    main()

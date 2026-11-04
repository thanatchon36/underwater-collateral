"""2024 emergency-zone declarations (DDPM) for the RQ1 administrative-spillover sensitivity (PAP section 3).

Administrative responses (debt relief, fee waivers, compensation) follow declarations, which can
cover dry land near floods. The sensitivity drops controls in declared areas.

Input list (built by hand from the provincial DDPM offices' replies or published notices; raw,
never edited after entry): 03_data/raw/ddpm_declarations/declarations_2024.csv, UTF-8, one row per
declared unit and declaration, columns
  province      sample slug (chiang-rai, phayao, nong-khai, nakhon-phanom)
  district_th   district (amphoe) name in Thai, with or without the prefix อำเภอ / อ.
  tambon_th     subdistrict name in Thai (blank if the whole district is declared)
  village       village name or number (optional; a village row declares its tambon)
  declared_on   date of the declaration (YYYY-MM-DD)
  source        document or reply it comes from (file name, letter reference)
Schema: 03_data/schemas/ddpm_declarations_2024.md.

Rules (fixed 2026-11-03, before any list was obtained):
- Names are matched to OCHA COD-AB (build_sheet_admin.py) within the province after removing the
  prefixes อำเภอ/อ./ตำบล/ต., spaces and zero-width characters (decomposed ำ recomposed); "เมือง" alone means the province's Mueang district. Any
  unmatched name stops the run; a correction is applied by hand to the list's matching (not to the
  raw rows) and reported as a deviation.
- Declarations dated 1 July - 31 December 2024 count (the 2024 flood season and its aftermath).
  Dates must be Gregorian YYYY-MM-DD in 2023-2025 (a B.E. year or another format stops the run), and
  a village row must name its tambon; either error stops the run.
- District variant: a control is dropped if its district (largest-overlap unit) appears in any
  counted row. Tambon variant: dropped if its tambon is declared, or its whole district is.
- A province left without controls leaves that sensitivity's estimate, and this is reported.
"""

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DECLARATIONS = ROOT / "03_data/raw/ddpm_declarations/declarations_2024.csv"
ADMIN = ROOT / "03_data/processed/rq1_2024_sheet_admin.csv.gz"      # build_sheet_admin.py
UNITS = ROOT / "03_data/processed/rq1_admin_units.csv.gz"             # build_sheet_admin.py
SHEET = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
WINDOW = ("2024-07-01", "2024-12-31")
PROVINCE_TH = {"chiang-rai": "เชียงราย", "phayao": "พะเยา", "nong-khai": "หนองคาย", "nakhon-phanom": "นครพนม"}


def norm(name, province=None):
    s = str(name or "").replace("\u0e4d\u0e32", "\u0e33")      # decomposed sara am -> ำ
    s = re.sub(r"[\s\u200b-\u200d\ufeff]+", "", s)            # spaces and zero-width characters
    s = re.sub(r"^(อำเภอ|อ\.|ตำบล|ต\.)", "", s)
    if s == "เมือง" and province in PROVINCE_TH:
        s = "เมือง" + PROVINCE_TH[province]
    return s


def load_admin(path=ADMIN):
    return pd.read_csv(path, dtype={c: str for c in SHEET})


def load_units(path=UNITS):
    return pd.read_csv(path, dtype=str)


def declared_units(decl, units):
    """Declared district and tambon P-codes, and the rows whose names match no unit of the province."""
    on = pd.to_datetime(decl["declared_on"].str.strip(), format="%Y-%m-%d", errors="coerce")
    if on.isna().any() or not on.dt.year.between(2023, 2025).all():
        bad_dates = decl.loc[on.isna() | ~on.dt.year.between(2023, 2025), "declared_on"].tolist()
        raise SystemExit(f"declared_on must be a Gregorian YYYY-MM-DD date in 2023-2025: {bad_dates[:10]}")
    vil = decl.get("village", pd.Series("", index=decl.index)).fillna("").astype(str).str.strip()
    if ((vil != "") & (decl["tambon_th"].fillna("").map(norm) == "")).any():
        raise SystemExit("a village row needs its tambon (tambon_th blank); add the tambon from the notice")
    d = decl[(on >= WINDOW[0]) & (on <= WINDOW[1])]
    a2 = {(r.province, norm(r.adm2_name1)): r.adm2_pcode for r in units.drop_duplicates("adm2_pcode").itertuples()}
    a3 = {(r.province, r.adm2_pcode, norm(r.adm3_name1)): r.adm3_pcode for r in units.itertuples()}
    dist, whole, tamb, bad = set(), set(), set(), []
    for r in d.itertuples():
        k2 = a2.get((r.province, norm(r.district_th, r.province)))
        if k2 is None:
            bad.append(("district", r.province, r.district_th))
            continue
        dist.add(k2)
        t = norm(r.tambon_th)
        if not t:
            whole.add(k2)
            continue
        k3 = a3.get((r.province, k2, t))
        if k3 is None:
            bad.append(("tambon", r.province, f"{r.district_th}/{r.tambon_th}"))
            continue
        tamb.add(k3)
    return dist, whole, tamb, bad


def drop_masks(sample, decl, admin, units):
    """Boolean Series (index of `sample`): controls to drop under the district and tambon variants."""
    dist, whole, tamb, bad = declared_units(decl, units)
    if bad:
        raise SystemExit(f"unmatched declaration names (match them by hand, report as a deviation): {bad[:10]}")
    m = sample[SHEET].astype(str).merge(admin[SHEET + ["adm2_pcode", "adm3_pcode"]], on=SHEET, how="left",
                                        validate="one_to_one")
    if m["adm2_pcode"].isna().any():
        raise SystemExit(f"{int(m['adm2_pcode'].isna().sum())} sample sheets missing from {ADMIN.name}")
    ctrl = (sample["T"] == 0).to_numpy()
    by_district = ctrl & m["adm2_pcode"].isin(dist).to_numpy()
    by_tambon = ctrl & (m["adm3_pcode"].isin(tamb) | m["adm2_pcode"].isin(whole)).to_numpy()
    return pd.Series(by_district, index=sample.index), pd.Series(by_tambon, index=sample.index)


def synthetic_declarations(sample, admin):
    """Stand-in list for the synthetic check: every district holding a treated sheet is declared."""
    m = sample[SHEET + ["T"]].astype({c: str for c in SHEET}).merge(admin[SHEET + ["adm2_pcode", "adm2_name1"]],
                                                                    on=SHEET)
    t = m[m["T"] == 1].drop_duplicates("adm2_pcode")
    return pd.DataFrame({"province": t["province"], "district_th": t["adm2_name1"], "tambon_th": "",
                         "village": "", "declared_on": "2024-09-15", "source": "synthetic"})


def load_declarations(path=DECLARATIONS):
    d = pd.read_csv(path, dtype=str, keep_default_na=False)
    need = {"province", "district_th", "tambon_th", "declared_on", "source"}
    if need - set(d.columns):
        raise SystemExit(f"{path.name} lacks columns {sorted(need - set(d.columns))}")
    return d


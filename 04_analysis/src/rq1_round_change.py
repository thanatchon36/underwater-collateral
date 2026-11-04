"""RQ1 primary analysis, written and tested before the first post-flood round exists.

This is the code the pre-analysis plan registers (sections 2, 5 and 6). It runs unchanged on the
first schedule published after 2023-26 ("R1"); until then it runs on a synthetic R1 built from the
2023-26 snapshot with a planted effect, to show that it recovers what was planted.

Inputs
  03_data/processed/rq1_{2024,2025}_sample_sheets.csv.gz   treated and control sheets with pre-flood
                                                     covariates (rq1_2024_pooled.py, rq1_sample_sensitivity.py)
  03_data/processed/rq1_2024_unosat_sample_sheets.csv.gz   UNOSAT sample, Chiang Rai-Phayao
                                                     (rq1_2024_design_power.py)
  03_data/raw/treasury_land_appraisal/snapshot_2026-11-02/land_<code>_<province>.csv   2023-26 parcels
  03_data/raw/flood/jrc_gsw_v1_4_occurrence{,_30N,_10N}/*.tif   permanent water (distance covariate;
                                                     0-10 N tiles from download_gsw_south.py)
  R1 parcels (real mode only): a directory of land_<code>_<province>.csv files in the same layout
  (UTMMAP1-4, UTMSCALE, LAND_NO, EVAPRICE).

Outcome (PAP section 2)
- Parcels are identified by sheet (province, UTMMAP1-4, UTMSCALE) and LAND_NO, as strings with
  surrounding whitespace removed; duplicated identifiers within a round are averaged; rows with a
  missing parcel number or a non-numeric or non-positive EVAPRICE are dropped.
- Pseudo land unit: parcels sharing a sheet and a 2023-26 value.
- A unit's R1 value is the mean R1 value over its parcels still present; parcel numbers new in R1
  (subdivisions, mergers) are ignored, and parcels missing from R1 count as attrition.
- Unit change = log(R1 value) - log(2023-26 value); carried over = every present parcel's value
  unchanged.
- Sheet outcome = mean unit change over units with at least one parcel present (units weighted
  equally); carry-over share likewise; attrition = share of 2023-26 parcels missing from R1.
- R1 checks (real mode, PAP sections 5 and 9): one file per sample province, none byte-identical to
  a 2023-26 file, and no province in which more than 99% of matched single-row parcels keep their
  2023-26 value (check_post, check_content). Matching stop: if more than 10% of a province's treated or control sheets have no
  parcel found in R1, the run stops before any estimate (primary run, every --sensitivities sample and
  rq1_lee_bounds.py alike; check_matching); identifiers are then checked and any harmonisation is
  applied to every sheet alike and reported as a deviation.

Estimation (PAP section 5)
- Weighted least squares of the sheet change on treatment, province fixed effects, elevation
  (sheet mean), distance to permanent water (km to the nearest 90 m cell holding JRC GSW
  occurrence >= 50), WorldCover 2021 built-up, cropland, tree and water shares, and a rural-sheet
  indicator (scale 1:4,000).
- Weights: treated sheets 1; controls entropy-balanced within province on pre-flood mean log value,
  height above the valley floor, built-up and cropland shares and the rural indicator (so controls
  match the treated scale mix), scaled to sum to the province's treated count. Standardised gaps
  use the controls' SD; fallback in balance_weights.
- H1a interaction: adds height above the valley floor and treatment x height (height centred at
  the treated mean). H1a predicts a negative interaction (smaller falls where hazard is high, i.e.
  low-lying land).
- H1b (descriptive): the same model with the carry-over share as outcome.
- Sensitivities: unweighted; weights times sheet area (bounding box); weights times 2023-26 parcel
  count; 1:50,000-sheet fixed effects instead of province effects (within-cluster); 1:1,000 and
  1:4,000 sheets only.

Inference (PAP section 6)
- Primary: randomisation inference over 1,000 placebo footprints. In each draw and province, a
  random treated sheet is placed on a random eligible control (controls whose height above the
  valley floor lies within the treated range), the whole treated footprint is shifted by that
  vector, and each shifted sheet, in random order, takes the nearest unused eligible control. The
  real treated sheets are dropped, the weights are re-estimated for the placebo group and the
  estimate recomputed (the 5 km buffer and height cap are not re-applied around placebo sheets).
  Two-sided p = (1 + number of placebo estimates at least as large in absolute value) / (1 + 1,000).
  If a province has fewer than twice as many eligible controls as treated sheets (the UNOSAT
  sample), footprints cannot be drawn and the wild bootstrap p-value is the primary p-value.
- Check: wild cluster restricted bootstrap (null imposed), Rademacher weights, 9,999 draws,
  clusters = 1:50,000 sheets, CR1 t-statistic, two-sided. Also used for the interaction and for
  H0: beta = -0.05 (wcb_p_fall_005: a small p rules out a fall of 0.05).
- Multiplicity: the primary p-values of the 2024 radar and UNOSAT samples are Holm-adjusted
  (rq1_round_change_holm.csv, real mode). With mixed timing (PAP section 9) the case (b) provinces'
  runs on R2 (--round R2) form a second family, adjusted separately.
- R1 content checks: the run stops if more than 99% of matched parcels keep their value (the old
  round) or more than 50% move by one common ratio to three significant figures (a unit change or
  rescaling, e.g. 0.25 for square wah to square metre).

Outputs
  synthetic mode: 04_analysis/outputs/tables/rq1_round_change[_2025]_synthetic.{csv,md} (one draw each with
                  planted effects -0.05 and 0, all registered estimates) and
                  rq1_round_change[_2025]_montecarlo.{csv,md} (100 draws each: bias, SD, size and power)
  both modes:     rq1_round_change[_unosat|_2025]_balance.{csv,md} (balancing diagnostics, pre-period)
  real mode:      04_analysis/outputs/tables/rq1_round_change[_unosat|_2025].{csv,md}, _matching.{csv,md},
                  rq1_round_change_holm.{csv,md} and 03_data/processed/rq1_round_change[...]_sheets.csv.gz
The 2025-flood design (PAP section 10) uses the same code on rq1_2025_sample_sheets.csv.gz (--event 2025).

Run: .venv/bin/python -I 04_analysis/src/rq1_round_change.py                     (synthetic, all three samples)
     .venv/bin/python -I 04_analysis/src/rq1_round_change.py --post DIR            (R1: 2024 radar, UNOSAT, Holm)
     .venv/bin/python -I 04_analysis/src/rq1_round_change.py --post DIR --event 2025   (second event)
     .venv/bin/python -I 04_analysis/src/rq1_round_change.py --post R2DIR --provinces P --round R2   (case (b), R2)
     .venv/bin/python -I 04_analysis/src/rq1_round_change.py --post DIR --provinces a,b   (province subset, PAP
          section 9: the case (b) provinces as the R1 placebo, or the provinces published so far; no Holm table)
     .venv/bin/python -I 04_analysis/src/rq1_round_change.py [--post DIR] --sensitivities   (secondary sensitivities:
          rebuilt samples from rq1_sensitivity_samples.py, weighting and subset variants, stacked 2024 + 2025;
          estimate, CR1 SE and wild bootstrap p, no placebo footprints)
"""

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import rasterio
from rasterio.merge import merge
from scipy import stats
from scipy.spatial import cKDTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rq1_2024_pooled import ebal  # noqa: E402
from geo import planar_km  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SAMPLES = {"2024": ROOT / "03_data/processed/rq1_2024_sample_sheets.csv.gz",          # rq1_2024_pooled.py
           "unosat": ROOT / "03_data/processed/rq1_2024_unosat_sample_sheets.csv.gz",  # rq1_2024_design_power.py
           "2025": ROOT / "03_data/processed/rq1_2025_sample_sheets.csv.gz"}          # rq1_sample_sensitivity.py
TAGS = {"2024": "", "unosat": "_unosat", "2025": "_2025"}
SENS = ["thr10", "thr50", "prov20", "prov30", "buf2", "buf10", "nocap", "ref2123", "nocrop"]   # rq1_sensitivity_samples.py
SENS_FILE = ROOT / "03_data/processed/rq1_2024_sens_{}_sample_sheets.csv.gz"
S2_COUNTS = ROOT / "03_data/processed/s2_sheet_water_rq1_2024.csv.gz"     # validate_s1_s2.py
S2_KEYS = ROOT / "03_data/processed/s2_sheet_keys_rq1_2024.csv.gz"        # validate_s1_s2.py
S1_2026 = ROOT / "03_data/processed/rq1_2024_sheet_flood_2026.csv.gz"     # flood_s1_2026.py
FAMILY = ("2024", "unosat")   # H1a's confirmatory family, Holm-adjusted
PRE = ROOT / "03_data/raw/treasury_land_appraisal/snapshot_2026-11-02"
GSW = sorted(p for d in ("", "_30N", "_10N") for p in (ROOT / f"03_data/raw/flood/jrc_gsw_v1_4_occurrence{d}").glob("*.tif"))
TAB = ROOT / "04_analysis/outputs/tables"
SHEETS_OUT = ROOT / "03_data/processed/rq1_round_change_sheets.csv.gz"
SHEET = ["province", "UTMMAP1", "UTMMAP2", "UTMMAP3", "UTMMAP4", "UTMSCALE"]
BAL = ["mean_logp", "rel_elev_m", "lc_builtup", "lc_cropland", "rural"]
COVS = ["elev_m", "river_km", "lc_builtup", "lc_cropland", "lc_tree", "lc_water", "rural"]
# Province-specific height slopes (author's decisions, 2026-11-03, before registration): in Phayao
# (2024 radar and UNOSAT samples) and Phatthalung (2025 sample) the controls cannot reach the treated
# sheets' height above the valley floor, so the balance fallback drops height from the weights; the
# regression adds height x 1[province]. Fixed by name, not by the fallback, so the model does not
# depend on R1. Province labels may carry an event prefix ("2024:phayao", stacked test).
HEIGHT_COV_PROVINCES = ["phayao", "phatthalung"]
MARGIN_TEST = -0.05   # the fall the design should be able to rule out (PAP section 7)
MATCH_ALERT = 0.10    # share of a province's sample sheets without any matched parcel that triggers the check
MAX_UNCHANGED = 0.99  # share of matched single-row parcels keeping their 2023-26 value above which R1 is the old round
MAX_COMMON_RATIO = 0.50  # share of matched single-row parcels moved by one common ratio (3 s.f.) above which R1 is rescaled
N_PLACEBO, N_BOOT, SEED = 1000, 9999, 20261102
BLOCK, RIVER_OCC, MARGIN = 3, 50, 0.15  # as in build_north_covariates.py


# ---------------------------------------------------------------- data

def province_of(f):
    """Province name from a file called land_<code>_<province>.csv; any other land_*.csv stops the run."""
    m = re.match(r"land_\d+_(.+)\.csv$", Path(f).name)
    if m is None:
        raise SystemExit(f"{Path(f).name}: not named land_<code>_<province>.csv; rename it or move it out of the folder")
    return m.group(1)


def load_parcels(folder, provinces, rows=False):
    """Parcels of the given provinces from a snapshot folder: SHEET + LAND_NO + p (baht per sq. wah);
    rows=True adds the number of file rows averaged into each parcel."""
    parts = []
    for f in sorted(Path(folder).glob("land_*.csv")):
        prov = province_of(f)
        if prov not in provinces:
            continue
        df = pd.read_csv(f, dtype=str, usecols=SHEET[1:] + ["LAND_NO", "EVAPRICE"], encoding="utf-8-sig")
        for k in SHEET[1:] + ["LAND_NO"]:
            df[k] = df[k].str.strip()
        df["p"] = pd.to_numeric(df.pop("EVAPRICE"), errors="coerce")
        df = df[(df["p"] > 0) & df["LAND_NO"].notna() & (df["LAND_NO"] != "")]
        df.insert(0, "province", prov)
        parts.append(df)
    out = pd.concat(parts, ignore_index=True)
    if rows:
        return out.groupby(SHEET + ["LAND_NO"], as_index=False).agg(p=("p", "mean"), rows=("p", "size"))
    return out.groupby(SHEET + ["LAND_NO"], as_index=False)["p"].mean()


def check_post(folder, provinces, manifest=PRE / "manifest.csv"):
    """R1 files for `provinces` (PAP section 9): each province must have exactly one file in `folder`
    (load_parcels reads every land_*.csv, so a second file would enter the estimate unchecked), and
    that file must differ from every 2023-26 snapshot file (SHA-256 against the snapshot manifest).
    A missing, duplicated or byte-identical file stops the run. Returns {province: sha256} for the record.
    A re-encoded copy of the old round passes this byte check; check_content catches it."""
    import hashlib
    old = set(pd.read_csv(manifest, dtype=str)["sha256"])
    files = {}
    for f in sorted(Path(folder).glob("land_*.csv")):
        files.setdefault(province_of(f), []).append(f)
    missing = sorted(set(provinces) - set(files))
    if missing:
        raise SystemExit(f"--post: no R1 file for {missing}; run only the provinces published (--provinces)")
    dup = {p: [f.name for f in files[p]] for p in sorted(provinces) if len(files[p]) > 1}
    if dup:
        raise SystemExit(f"--post: more than one R1 file per province {dup}; keep one file per province")
    sha = {}
    for p in sorted(provinces):
        h = hashlib.sha256()
        with open(files[p][0], "rb") as fo:
            for chunk in iter(lambda: fo.read(1 << 20), b""):
                h.update(chunk)
        sha[p] = h.hexdigest()
    same = sorted(p for p, v in sha.items() if v in old)
    if same:
        raise SystemExit(f"--post: the files for {same} are identical to the 2023-26 snapshot; not a new round")
    return sha


def check_content(pre, post, max_same=MAX_UNCHANGED):
    """Content check of R1 (PAP section 9): a province in which more than `max_same` of the parcels
    matched between the rounds keep exactly their 2023-26 value is the old round again (re-saved with
    another encoding or line ending, which passes the byte check, or re-issued with a few corrections),
    and stops the run. Parcels listed on more than one row in either round are left out (if `rows` is
    given), since dropping one such row changes the averaged value without a new appraisal."""
    m = pre.merge(post.rename(columns={"p": "p_post", "rows": "rows_post"}), on=SHEET + ["LAND_NO"], how="inner")
    if "rows" in m and "rows_post" in m:
        m = m[(m["rows"] == 1) & (m["rows_post"] == 1)]
    if m.empty:
        return
    same = pd.Series(np.isclose(m["p_post"], m["p"], rtol=1e-9, atol=0)).groupby(m["province"].to_numpy()).mean()
    old = same[same > max_same]
    if len(old):
        raise SystemExit(f"--post: share of matched parcels keeping their 2023-26 value above {max_same:.0%} in "
                         f"{old.round(4).to_dict()}; this is the old round (re-saved or re-issued?), not a new one")
    common = common_ratio_share(m)
    hit = common[common["share"] > MAX_COMMON_RATIO]
    if len(hit):
        raise SystemExit(f"--post: more than {MAX_COMMON_RATIO:.0%} of matched parcels share one new/old value ratio "
                         f"in {hit.round(4).to_dict('index')}; a unit change or rescaling (e.g. 0.25 for square wah "
                         "to square metre), not an appraisal: check the Treasury's publication (PAP section 5)")


def common_ratio_share(m):
    """By province, the most common new/old value ratio among matched parcels whose value changed, to three
    significant figures, and its share of all matched parcels (PAP section 5: a unit change or a uniform
    rescaling moves nearly every parcel by one ratio; a reappraisal moves land units by different ratios)."""
    ratio = (m["p_post"] / m["p"]).to_numpy(float)
    moved = ~np.isclose(ratio, 1.0, rtol=1e-9, atol=0)
    e = np.floor(np.log10(ratio[moved]))
    r3 = np.round(np.round(ratio[moved] / 10 ** e, 2) * 10 ** e, 10)
    prov = m["province"].to_numpy()
    n = pd.Series(prov).value_counts()
    rows = []
    for p in n.index:
        c = pd.Series(r3[prov[moved] == p]).value_counts()
        rows.append({"province": p, "ratio": float(c.index[0]) if len(c) else np.nan,
                     "share": float(c.iloc[0]) / n[p] if len(c) else 0.0})
    return pd.DataFrame(rows).set_index("province")


def load_post(folder, pre):
    """R1 parcels for the provinces of `pre`, after the file and content checks."""
    provinces = set(pre["province"])
    sha = check_post(folder, provinces)
    post = load_parcels(folder, provinces, rows=True)
    old = load_parcels(PRE, provinces, rows=True).merge(pre[SHEET + ["LAND_NO"]], on=SHEET + ["LAND_NO"])
    check_content(old, post)
    return post.drop(columns="rows"), sha


def unit_changes(pre, post):
    """Pseudo-land-unit changes between rounds (see module docstring)."""
    m = pre.merge(post.rename(columns={"p": "p_post"}), on=SHEET + ["LAND_NO"], how="left")
    m["present"] = m["p_post"].notna()
    m["same"] = np.isclose(m["p_post"], m["p"], rtol=1e-9, atol=0) | ~m["present"]
    g = m.groupby(SHEET + ["p"], as_index=False).agg(
        n_parcels=("present", "size"), n_present=("present", "sum"), post_mean=("p_post", "mean"),
        all_same=("same", "all"))
    g["dlog"] = np.log(g["post_mean"]) - np.log(g["p"])
    g["carried"] = (g["all_same"] & (g["n_present"] > 0)).astype(float)
    return g.drop(columns="all_same")


def sheet_outcomes(units):
    present = units[units["n_present"] > 0]
    s = present.groupby(SHEET).agg(dlog=("dlog", "mean"), carry=("carried", "mean"),
                                   units_present=("dlog", "size"))
    a = units.groupby(SHEET).agg(units=("p", "size"), parcels_pre=("n_parcels", "sum"),
                                 parcels_present=("n_present", "sum"))
    a["attrition"] = 1 - a["parcels_present"] / a["parcels_pre"]
    return a.join(s).reset_index()


def river_km(d):
    """Distance from each sheet centre to the nearest permanent-water cell, per province box."""
    out = pd.Series(np.nan, index=d.index)
    for _, g in d.groupby("province"):
        bb = (g.lon0.min() - MARGIN, g.lat0.min() - MARGIN, g.lon1.max() + MARGIN, g.lat1.max() + MARGIN)
        srcs = [rasterio.open(p) for p in GSW]
        arr, tr = merge(srcs, bounds=bb)
        for s in srcs:
            s.close()
        occ = np.where(arr[0] == 255, 0, arr[0])
        h, w = (occ.shape[0] // BLOCK) * BLOCK, (occ.shape[1] // BLOCK) * BLOCK
        river = (occ[:h, :w] >= RIVER_OCC).reshape(h // BLOCK, BLOCK, w // BLOCK, BLOCK).any(axis=(1, 3))
        rr, cc = np.nonzero(river)
        kx = 111.32 * np.cos(np.radians((g.lat0.mean() + g.lat1.mean()) / 2))
        tree = cKDTree(np.c_[(tr.c + (cc + 0.5) * BLOCK * tr.a) * kx, (tr.f + (rr + 0.5) * BLOCK * tr.e) * 110.57])
        cx, cy = (g.lon0 + g.lon1) / 2 * kx, (g.lat0 + g.lat1) / 2 * 110.57
        out[g.index] = tree.query(np.c_[cx, cy])[0]
    if not np.isfinite(out).all():
        raise ValueError("river_km: sheets outside the GSW tiles on disk")
    return out


def load_sample(path=SAMPLES["2024"]):
    d = pd.read_csv(path, dtype={k: str for k in SHEET}, keep_default_na=False, na_values=[""])
    d["T"] = (d["group"] == "treated").astype(int)
    d["rural"] = (d["UTMSCALE"] == "4000").astype(float)   # 1:4,000 rural sheets; other scales urban
    lat = np.radians((d.lat0 + d.lat1) / 2)
    d["x"], d["y"] = planar_km(d)   # one reference latitude per province (geo.py), for placebo shifts
    d["area_km2"] = (d.lon1 - d.lon0) * 111.32 * np.cos(lat) * (d.lat1 - d.lat0) * 110.57
    d["river_km"] = river_km(d)
    return d


# ---------------------------------------------------------------- estimation

GAP_TOL = 0.01  # largest standardised mean gap (control SD units) counted as balanced


def _gaps(xc, target, w):
    mu, sd = xc.mean(0), xc.std(0)
    sd = np.where(sd > 0, sd, 1.0)
    return np.abs(w @ ((xc - mu) / sd) - (target - mu) / sd)


def balance_weights(d, cols=BAL, log=None):
    """Treated 1; controls entropy-balanced within province, summing to the province's treated count.

    Registered fallback: while the largest standardised mean gap in a province exceeds GAP_TOL, the
    balancing variable with the largest gap leaves that province's set and the weights are
    re-estimated; with no variable left, the province's controls are unweighted. Each fallback is
    appended to `log` as (province, balancing set used).
    """
    w = pd.Series(1.0, index=d.index)
    for prov, g in d.groupby("province"):
        t, c = g[g["T"] == 1], g[g["T"] == 0]
        use = list(cols)
        while use:
            xc, target = c[use].values, t[use].values.mean(0)
            wc = ebal(xc, target)
            gaps = _gaps(xc, target, wc)
            if gaps.max() <= GAP_TOL:
                break
            use.pop(int(gaps.argmax()))
        if not use:
            wc = np.full(len(c), 1 / len(c))
        if use != list(cols) and log is not None:
            log.append((prov, "+".join(use) or "unweighted"))
        w[c.index] = wc * len(t)
    return w


def design(d, fe="province", interaction=False):
    X = [d["T"].to_numpy(float)]
    names = ["T"]
    if interaction:
        h = d["rel_elev_m"] - d.loc[d["T"] == 1, "rel_elev_m"].mean()
        X += [d["T"] * h, h]
        names += ["T_x_height", "height"]
    X += [d[c].to_numpy(float) for c in COVS]
    names += COVS
    for prov in HEIGHT_COV_PROVINCES:
        inp = d["province"].astype(str).str.split(":").str[-1].eq(prov).to_numpy()
        if inp.any():
            X.append(d["rel_elev_m"].to_numpy(float) * inp)
            names.append(f"height_x_{prov}")
    dummies = pd.get_dummies(d[fe], drop_first=False).to_numpy(float)
    return np.column_stack(X + [dummies]), names


def wls(y, X, w):
    sw = np.sqrt(w)
    beta, *_ = np.linalg.lstsq(X * sw[:, None], y * sw, rcond=None)
    return beta


def cluster_se(X, w, u, groups, j):
    """CR1 standard error of coefficient j for WLS."""
    A = np.linalg.pinv((X * w[:, None]).T @ X)
    h = (X @ A[j]) * w
    s = pd.Series(h * u).groupby(groups).sum().to_numpy()
    n, k, G = len(u), np.linalg.matrix_rank(X), len(s)
    return np.sqrt(G / (G - 1) * (n - 1) / (n - k) * (s ** 2).sum())


def estimate(d, w, y="dlog", fe="province", interaction=False):
    X, names = design(d, fe, interaction)
    yy, ww = d[y].to_numpy(float), w.to_numpy(float)
    b = wls(yy, X, ww)
    u = yy - X @ b
    g = d["series_sheet"].to_numpy()
    out = {"estimate": b[0], "se": cluster_se(X, ww, u, g, 0)}
    if interaction:
        out |= {"interaction": b[1], "interaction_se": cluster_se(X, ww, u, g, 1)}
    return out


def wild_cluster_p(d, w, y="dlog", fe="province", n_boot=N_BOOT, seed=SEED, chunk=1000, interaction=False, j=0, null=0.0):
    """Wild cluster restricted bootstrap p-value (Rademacher, two-sided) for coefficient j against H0: b_j = null.

    j = 0 is the treatment coefficient; with interaction=True, j = 1 is treatment x height."""
    X, _ = design(d, fe, interaction)
    yy, ww = d[y].to_numpy(float) - null * X[:, j], w.to_numpy(float)
    g_codes, groups = pd.factorize(d["series_sheet"])
    G = len(groups)
    Xr = np.delete(X, j, axis=1)
    er = yy - Xr @ wls(yy, Xr, ww)
    XtW = (X * ww[:, None]).T
    A = np.linalg.pinv(XtW @ X)
    P = A @ XtW                                   # k x n: beta = P y
    h = (X @ A[j]) * ww                           # score weights for coefficient j
    n, k = len(yy), np.linalg.matrix_rank(X)
    c = G / (G - 1) * (n - 1) / (n - k)
    S = np.zeros((G, n))
    S[g_codes, np.arange(n)] = 1.0                # cluster-sum matrix

    def tstats(Z):                                # Z: n x B perturbed residual parts (y* - fitted_r)
        B = P @ Z
        U = Z - X @ B                             # residuals of the full model (fitted_r is in span X)
        se = np.sqrt(c * ((S @ (h[:, None] * U)) ** 2).sum(0))
        return B[j] / se

    b_full = P @ yy
    u_full = yy - X @ b_full
    t0 = b_full[j] / np.sqrt(c * ((S @ (h * u_full)) ** 2).sum())
    rng = np.random.default_rng(seed)
    hits = 0
    for start in range(0, n_boot, chunk):
        m = min(chunk, n_boot - start)
        v = rng.choice([-1.0, 1.0], size=(G, m))
        hits += int((np.abs(tstats(er[:, None] * v[g_codes])) >= abs(t0)).sum())
    return hits / n_boot


def placebo_assignment(d, rng, elig=None, min_ratio=2.0):
    """Placebo treated indicator over the controls (see module docstring); real treated dropped.

    `elig`: the controls a footprint may land on; default (the registered rule) is every control within
    the treated height range. rq1_placebo_restricted_mc.py passes a propensity-restricted pool.
    """
    t = d[d["T"] == 1]
    lo, hi = t["rel_elev_m"].min(), t["rel_elev_m"].max()
    c = d[d["T"] == 0]
    if elig is None:
        elig = c[(c["rel_elev_m"] >= lo) & (c["rel_elev_m"] <= hi)]
    flag = pd.Series(0, index=c.index)
    for pr, tp in t.groupby("province"):
        pool = elig[elig["province"] == pr]
        if len(pool) < min_ratio * len(tp):
            raise ValueError(f"{pr}: too few eligible controls for placebo footprints")
        anchor_t = tp.iloc[rng.integers(len(tp))]
        anchor_c = pool.iloc[rng.integers(len(pool))]
        shifted = tp[["x", "y"]].to_numpy() + (anchor_c[["x", "y"]].to_numpy(float) - anchor_t[["x", "y"]].to_numpy(float))
        free = np.ones(len(pool), bool)
        xy = pool[["x", "y"]].to_numpy()
        for i in rng.permutation(len(shifted)):
            dist = np.hypot(*(xy - shifted[i]).T)
            dist[~free] = np.inf
            j = int(np.argmin(dist))
            free[j] = False
            flag[pool.index[j]] = 1
    return c.assign(T=flag)


def randomisation_p(d, est, n=N_PLACEBO, seed=SEED, y="dlog"):
    rng = np.random.default_rng(seed)
    draws = np.empty(n)
    for r in range(n):
        p = placebo_assignment(d, rng)
        draws[r] = estimate(p, balance_weights(p), y=y)["estimate"]
    return float((1 + (np.abs(draws) >= abs(est)).sum()) / (1 + n)), draws


GAP_REPORT = BAL + ["lc_tree", "lc_water"]


def _gap_after(t, c, wc, v):
    """(treated mean - weighted control mean) / controls' SD; a reported diagnostic, not a balancing rule."""
    sd = c[v].std(ddof=0)
    return float((t[v].mean() - np.average(c[v], weights=wc)) / sd) if sd > 0 else np.nan


def balance_table(d, cols=BAL):
    """Per province: sheets, effective controls, balancing set used, treated sheets beyond the control range,
    and the standardised gap left after weighting on each balancing variable and on tree and water shares
    (row "all": pooled over provinces, weights summing to each province's treated count)."""
    log = []
    w = balance_weights(d, cols, log=log)
    used = dict(log)
    rows = []
    for prov, g in d.groupby("province"):
        t, c = g[g["T"] == 1], g[g["T"] == 0]
        wc = w[c.index]
        r = {"province": prov, "treated": len(t), "controls": len(c),
             "effective_controls": wc.sum() ** 2 / (wc ** 2).sum(), "balancing_set": used.get(prov, "+".join(cols))}
        for v in cols:
            r[f"treated_beyond_controls_{v}"] = int(((t[v] < c[v].min()) | (t[v] > c[v].max())).sum())
        for v in GAP_REPORT:
            r[f"gap_after_{v}"] = _gap_after(t, c, wc, v)
        rows.append(r)
    out = pd.DataFrame(rows)
    # whole sample: Kish effective controls and the MDE of the weighted design (80% power, 5% two-sided,
    # SD of sheet changes 0.10, ICC 0.2 across 1:50,000 sheets; same formula as rq1_2024_pooled.py)
    t, c = d[d["T"] == 1], d[d["T"] == 0]
    wc = w[c.index]
    a_g = t.groupby("series_sheet").size() / len(t)
    b_g = wc.groupby(c["series_sheet"]).sum() / wc.sum()
    a_g, b_g = a_g.align(b_g, fill_value=0)
    G = int(((a_g > 0) | (b_g > 0)).sum())
    ess = wc.sum() ** 2 / (wc ** 2).sum()
    se1 = np.sqrt(0.2 * ((a_g - b_g) ** 2).sum() + 0.8 * (1 / len(t) + 1 / ess))
    mde = (stats.t.ppf(0.975, G - 1) + stats.t.ppf(0.80, G - 1)) * 0.10 * se1
    tot = {"province": "all", "treated": len(t), "controls": len(c), "effective_controls": ess,
           "balancing_set": "", "treated_clusters": t["series_sheet"].nunique(), "mde_sd0.10_icc0.2": mde,
           **{f"gap_after_{v}": _gap_after(t, c, wc, v) for v in GAP_REPORT}}
    return pd.concat([out, pd.DataFrame([tot])], ignore_index=True)


def match_report(sh):
    """Per province and group: sample sheets and the share with no 2023-26 parcel found in R1."""
    sh = sh.assign(unmatched=sh["dlog"].isna(), group=np.where(sh["T"] == 1, "treated", "control"))
    r = sh.groupby(["province", "group"]).agg(sheets=("unmatched", "size"), unmatched_share=("unmatched", "mean"))
    r = r.reset_index()
    r["alert"] = r["unmatched_share"] > MATCH_ALERT
    return r


def check_matching(sh, label):
    """Matching stop (PAP section 5) on any real-R1 sample: raises if a province-group alert fires."""
    mr = match_report(sh)
    if mr["alert"].any():
        raise SystemExit(f"MATCHING ALERT (PAP section 5), {label}: identifiers must be checked before any estimate "
                         f"is computed; harmonise and log a deviation, then rerun\n{mr[mr['alert']]}")
    return mr


def analyse(d, n_placebo=N_PLACEBO, n_boot=N_BOOT):
    """All registered estimates for a sheet table d (sample covariates plus dlog, carry, attrition).

    Sheets with no 2023-26 parcel present in R1 are dropped (counted by group first) and the weights
    re-estimated on the rest. If placebo footprints cannot be drawn (a province has fewer than twice
    as many eligible controls as treated sheets), ri_p is missing and the wild bootstrap p-value is the
    test's p-value (`p_primary`).
    """
    absent = d[d["dlog"].isna()].groupby("T").size()
    att_all = d.assign(attrition=d["attrition"].fillna(1.0)).groupby("T")["attrition"].mean()
    d = d[d["dlog"].notna()].reset_index(drop=True)
    fallback = []
    w = balance_weights(d, log=fallback)
    rows = []
    main = estimate(d, w)
    wcb = wild_cluster_p(d, w, n_boot=n_boot)
    try:
        ri_p, _ = randomisation_p(d, main["estimate"], n=n_placebo)
    except ValueError:
        ri_p = np.nan
    rows.append({"spec": "primary: weighted, province FE", **main, "ri_p": ri_p, "wcb_p": wcb,
                 "p_primary": wcb if np.isnan(ri_p) else ri_p,
                 "wcb_p_fall_005": wild_cluster_p(d, w, n_boot=n_boot, null=MARGIN_TEST)})
    inter = estimate(d, w, interaction=True)
    rows.append({"spec": "H1a interaction (treated x height above valley floor)", **inter,
                 "wcb_p_interaction": wild_cluster_p(d, w, n_boot=n_boot, interaction=True, j=1)})
    rows.append({"spec": "H1b carry-over share (descriptive)", **estimate(d, w, y="carry"),
                 "wcb_p": wild_cluster_p(d, w, y="carry", n_boot=n_boot)})
    one = pd.Series(1.0, index=d.index)
    rows.append({"spec": "unweighted", **estimate(d, one), "wcb_p": wild_cluster_p(d, one, n_boot=n_boot)})
    rows.append({"spec": "weights x sheet area", **estimate(d, w * d["area_km2"])})
    rows.append({"spec": "weights x 2023-26 parcels", **estimate(d, w * d["parcels_pre"])})
    rows.append({"spec": "within cluster (1:50,000-sheet FE)", **estimate(d, w, fe="series_sheet")})
    keep = d["UTMSCALE"].isin(["1000", "4000"]).to_numpy()
    dk = d[keep].reset_index(drop=True)
    rows.append({"spec": "1:1,000 and 1:4,000 sheets only", **estimate(dk, balance_weights(dk))})
    out = pd.DataFrame(rows)
    out["sheets_treated"], out["sheets_control"] = int(d["T"].sum()), int((d["T"] == 0).sum())
    out["sheets_absent_treated"], out["sheets_absent_control"] = int(absent.get(1, 0)), int(absent.get(0, 0))
    out["clusters"] = d["series_sheet"].nunique()
    out["treated_clusters"] = d.loc[d["T"] == 1, "series_sheet"].nunique()
    out["balance_fallback"] = "; ".join(f"{p}: {u}" for p, u in fallback) or "none"
    out["attrition_treated"], out["attrition_control"] = att_all.get(1), att_all.get(0)
    return out


def optical_flooded(sample, counts=S2_COUNTS, keys=S2_KEYS, min_clear=0.5, new_water=0.10, check=True):
    """Sentinel-2 flag per sample sheet, as in validate_s1_s2.py, joined on the sheet key.

    The counts' sheet ids are resolved through the key file; with check=True every sheet's recorded
    pixel counts must fit its box (validate_s1_s2.check_alignment), else the run stops. Sample
    sheets without counts are not flagged."""
    c = pd.read_csv(counts)
    k = pd.read_csv(keys, dtype={col: str for col in SHEET})
    if check:
        from validate_s1_s2 import check_alignment
        bad = check_alignment(k, c)
        if bad:
            raise SystemExit(f"Sentinel-2 counts do not fit the key file's boxes for {len(bad)} sheets: {bad[:10]}")
    c["year"] = c["date"].str[:4].astype(int)
    u = c[c["clear"] >= min_clear * c["px"]].assign(share=lambda x: x["water"] / x["clear"])
    mx = u.groupby(["sheet_id", "year"])["share"].max().unstack()
    nw = (mx.get(2024) - mx.get(2023)).rename("nw").reset_index().merge(k[["sheet_id"] + SHEET], on="sheet_id")
    known = sample[SHEET].astype(str).merge(k[SHEET], on=SHEET, how="left", indicator=True)
    if (known["_merge"] != "both").any():
        raise SystemExit(f"{int((known['_merge'] != 'both').sum())} sample sheets missing from {Path(keys).name}")
    keyed = sample[SHEET].astype(str).merge(nw[SHEET + ["nw"]], on=SHEET, how="left", validate="one_to_one")
    return pd.Series((keyed["nw"] > new_water).to_numpy(), index=sample.index)


def later_floods(sample, path=S1_2026, min_valid=0.5):
    """2026-season radar share of each sample sheet (flood_s1_2026.py). As in the primary usable-sheet
    rule, a share counts only if the sheet's valid 2026 pixels cover at least half its box
    (valid_frac_2026); a sheet below that, or not covered at all, counts as not flooded and is reported."""
    f = pd.read_csv(path, dtype={c: str for c in SHEET})[SHEET + ["s1_share_2026", "valid_frac_2026"]]
    m = sample[SHEET].merge(f, on=SHEET, how="left", validate="one_to_one", indicator=True)
    if (m["_merge"] != "both").any():
        raise SystemExit(f"{int((m['_merge'] != 'both').sum())} sample sheets missing from {Path(path).name}")
    m.loc[~(m["valid_frac_2026"] >= min_valid), "s1_share_2026"] = np.nan
    n_na = int(m["s1_share_2026"].isna().sum())
    if n_na:
        print(f"later floods: {n_na} sample sheets without 2026 radar cover of half their box kept as not flooded")
    return m[SHEET + ["s1_share_2026"]].fillna({"s1_share_2026": 0.0})


def quick(d, cols=BAL, n_boot=N_BOOT, seed=SEED):
    """Primary estimate with CR1 SE and wild bootstrap p (no placebo footprints) for a sensitivity,
    with the registered balancing weights on `cols` and their fallbacks logged."""
    fallback = []
    w = balance_weights(d, cols=cols, log=fallback)
    e = estimate(d, w)
    return {**e, "wcb_p": wild_cluster_p(d, w, n_boot=n_boot, seed=seed),
            "sheets_treated": int(d["T"].sum()), "sheets_control": int((d["T"] == 0).sum()),
            "treated_clusters": d.loc[d["T"] == 1, "series_sheet"].nunique(),
            "balance_fallback": "; ".join(f"{p}: {u}" for p, u in fallback) or "none"}


def sensitivities(post_of, n_boot=N_BOOT, declarations="real", keep=None, real=False):
    """Secondary sensitivities of the 2024 radar estimate (PAP sections 3-5, 8).

    post_of(pre, sample) returns R1 parcels for a sample (real or synthetic). Rebuilt samples:
    SENS (rq1_sensitivity_samples.py). On the primary sample: weighting on value, height and the
    rural indicator only; treated sheets wetter than their province's controls' 99th percentile
    dropped; optically flooded controls dropped (Sentinel-2). Also the stacked 2024 + 2025 test:
    both samples with province x event fixed effects and weights, clustered by 1:50,000 sheet.
    Controls in districts / tambons with a 2024 emergency-zone declaration dropped (rq1_declarations):
    declarations="real" reads the DDPM list if it exists (else the rows are skipped and a note is
    printed), "synthetic" uses the stand-in list of the synthetic check.
    Sheets flooded again in the 2026 season (flood_s1_2026.py) dropped: controls with a 2026 share of
    at least 1% and treated sheets above 25%.
    keep: provinces of the 2024 radar sample to run on (PAP section 9, timing by province); every
    rebuilt sample is cut to them (a rebuilt sample left without sheets gets a skipped row) and the
    stacked 2024 + 2025 row is skipped.
    real: post_of returns the real R1; every sample then passes the matching stop (PAP section 5)."""
    rows = []

    def load(path):
        s = load_sample(path)
        return s[s["province"].isin(keep)].reset_index(drop=True) if keep else s

    def outcome(sample, label):
        pre = load_parcels(PRE, set(sample["province"])).merge(sample[SHEET], on=SHEET)
        sh = sample.merge(sheet_outcomes(unit_changes(pre, post_of(pre, sample))), on=SHEET, how="left")
        if real:
            check_matching(sh, label)
        return sh[sh["dlog"].notna()].reset_index(drop=True)

    for name in SENS:
        s = load(Path(str(SENS_FILE).format(name)))
        if s.empty or not (s["T"] == 1).any() or not (s["T"] == 0).any():
            print(f"{name}: no treated or no control sheets in {keep}; row skipped")
            rows.append({"sensitivity": name, "skipped": f"no treated or control sheets in {'+'.join(keep or [])}"})
            continue
        rows.append({"sensitivity": name, **quick(outcome(s, name), n_boot=n_boot)})
    sample = load(SAMPLES["2024"])
    sample["optical_flooded"] = optical_flooded(sample)
    sample = sample.merge(later_floods(sample), on=SHEET, how="left", validate="one_to_one")
    d = outcome(sample, "2024 radar sample")
    rows.append({"sensitivity": "weights on value, height, rural only",
                 **quick(d, cols=["mean_logp", "rel_elev_m", "rural"], n_boot=n_boot)})
    c = d[d["T"] == 0]
    q99 = d["province"].map(c.groupby("province")["lc_water"].quantile(0.99))
    k = d[(d["T"] == 0) | (d["lc_water"] <= q99)].reset_index(drop=True)
    rows.append({"sensitivity": "high-water treated dropped", **quick(k, n_boot=n_boot)})
    k = d[(d["T"] == 1) | ~d["optical_flooded"].astype(bool)].reset_index(drop=True)
    rows.append({"sensitivity": "optically flooded controls dropped", **quick(k, n_boot=n_boot)})
    wet26 = np.where(d["T"] == 1, d["s1_share_2026"] > 0.25, d["s1_share_2026"] >= 0.01)
    k = d[~wet26].reset_index(drop=True)
    gone = sorted(set(d.loc[d["T"] == 0, "province"]) - set(k.loc[k["T"] == 0, "province"]))
    k = k[~k["province"].isin(gone)].reset_index(drop=True)
    rows.append({"sensitivity": "sheets flooded in 2026 dropped", **quick(k, n_boot=n_boot),
                 "dropped_treated": int((wet26 & (d["T"] == 1)).sum()),
                 "dropped_control": int((wet26 & (d["T"] == 0)).sum()),
                 "provinces_without_controls": "+".join(gone) or "none"})
    import rq1_declarations as dec
    admin, units = dec.load_admin(), dec.load_units()
    decl = (dec.synthetic_declarations(d, admin) if declarations == "synthetic"
            else dec.load_declarations() if dec.DECLARATIONS.exists() else None)
    if decl is None:
        print(f"DDPM declaration list not found ({dec.DECLARATIONS.name}): declared-area rows skipped")
    else:
        for label, drop in zip(("district", "tambon"), dec.drop_masks(d, decl, admin, units)):
            k = d[~drop.to_numpy()].reset_index(drop=True)
            gone = sorted(set(d.loc[d["T"] == 0, "province"]) - set(k.loc[k["T"] == 0, "province"]))
            k = k[~k["province"].isin(gone)].reset_index(drop=True)
            rows.append({"sensitivity": f"declared-{label} controls dropped", **quick(k, n_boot=n_boot),
                         "provinces_without_controls": "+".join(gone) or "none"})
    if keep:
        print("stacked 2024 + 2025 row skipped with --provinces")
        return pd.DataFrame(rows)
    # stacked 2024 radar + 2025 (PAP section 7): province x event effects and weights, clusters shared
    d25 = outcome(load_sample(SAMPLES["2025"]), "2025 sample")
    st = pd.concat([d.assign(province="2024:" + d["province"]), d25.assign(province="2025:" + d25["province"])],
                   ignore_index=True)
    rows.append({"sensitivity": "stacked 2024 radar + 2025", **quick(st, n_boot=n_boot)})
    return pd.DataFrame(rows)


def holm(p):
    """Holm-adjusted p-values for a dict {name: p}."""
    names = sorted(p, key=p.get)
    m, run, out = len(names), 0.0, {}
    for i, k in enumerate(names):
        run = max(run, min(1.0, (m - i) * p[k]))
        out[k] = run
    return out


# ---------------------------------------------------------------- synthetic R1

def synthetic_post(pre, sample, effect, rng, sd=0.10, icc=0.2, unit_sd=0.05, carry=0.3, attrit=0.02, new=0.01):
    """A synthetic R1 for the sample sheets: province shift + cluster + sheet + unit noise + effect x treated;
    a share `carry` of units keeps its value; `attrit` of parcels disappears; `new` parcel numbers appear."""
    s = sample.set_index(SHEET)
    pre = pre.merge(sample[SHEET], on=SHEET)
    units = pre[SHEET + ["p"]].drop_duplicates().reset_index(drop=True)
    sh = units[SHEET].drop_duplicates().reset_index(drop=True)
    sh["T"] = s.loc[list(sh.itertuples(index=False, name=None)), "T"].to_numpy()
    clusters = s["series_sheet"].unique()
    c_eff = pd.Series(rng.normal(0, sd * np.sqrt(icc), len(clusters)), index=clusters)
    p_eff = pd.Series(rng.normal(0.08, 0.03, s.index.get_level_values("province").nunique()),
                      index=s.index.get_level_values("province").unique())
    sh["shift"] = (p_eff[sh["province"]].to_numpy()
                   + c_eff[s.loc[list(sh[SHEET].itertuples(index=False, name=None)), "series_sheet"]].to_numpy()
                   + rng.normal(0, sd * np.sqrt(1 - icc), len(sh)) + effect * sh["T"])
    units = units.merge(sh, on=SHEET)
    units["dl"] = np.where(rng.random(len(units)) < carry, 0.0, units["shift"] + rng.normal(0, unit_sd, len(units)))
    post = pre.merge(units[SHEET + ["p", "dl"]], on=SHEET + ["p"])
    post["p"] = post["p"] * np.exp(post.pop("dl"))
    post = post[rng.random(len(post)) >= attrit]
    add = post.sample(frac=new, random_state=int(rng.integers(2 ** 31))).assign(
        LAND_NO=lambda x: "N" + x["LAND_NO"].astype(str), p=lambda x: x["p"] * 1.5)
    return pd.concat([post, add], ignore_index=True)[SHEET + ["LAND_NO", "p"]]


def monte_carlo(pre, sample, effects=(0.0, -0.05), reps=100, n_boot=999):
    """Bias, spread and wild-bootstrap rejection rate of the primary estimate over synthetic R1 draws."""
    rows = []
    for effect in effects:
        est, se, rej = [], [], []
        for k in range(reps):
            rng = np.random.default_rng(SEED + 7919 * (k + 1) + int(round(-effect * 1000)))
            sh = sample.merge(sheet_outcomes(unit_changes(pre, synthetic_post(pre, sample, effect, rng))), on=SHEET, how="left")
            d = sh[sh["dlog"].notna()].reset_index(drop=True)
            w = balance_weights(d)
            e = estimate(d, w)
            est.append(e["estimate"])
            se.append(e["se"])
            rej.append(wild_cluster_p(d, w, n_boot=n_boot, seed=SEED + k) < 0.05)
        rows.append({"planted_effect": effect, "expected_sheet_effect": effect * 0.7, "replications": reps,
                     "mean_estimate": np.mean(est), "sd_estimate": np.std(est, ddof=1), "mean_cluster_se": np.mean(se),
                     "rejection_rate_wcb_5pct": np.mean(rej)})
    return pd.DataFrame(rows)


def write(df, name, note):
    TAB.mkdir(parents=True, exist_ok=True)
    df.to_csv(TAB / f"{name}.csv", index=False)
    (TAB / f"{name}.md").write_text(f"<!-- {note} -->\n\n" + df.round(4).to_markdown(index=False) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--post", help="folder with the first post-flood round (land_<code>_<province>.csv)")
    ap.add_argument("--event", choices=list(SAMPLES), default=None,
                    help="sample: 2024 radar, unosat (2024, Chiang Rai-Phayao) or 2025; default: 2024 and unosat "
                         "with --post (the Holm family), all three in synthetic mode")
    ap.add_argument("--provinces", help="comma-separated province subset (PAP section 9: case (b) provinces run as "
                    "the R1 placebo, or the provinces published so far); outputs get the suffix _prov-<names>")
    ap.add_argument("--placebo", action="store_true",
                    help="with --post and --provinces: the case (b) R1 placebo (outputs suffixed _placebo; not in Holm)")
    ap.add_argument("--round", choices=["R1", "R2"], default="R1",
                    help="post-period of a confirmatory run: R1 (default), or R2 for case (b) provinces, whose tests form "
                         "a second Holm family (PAP section 9)")
    ap.add_argument("--holm", action="store_true",
                    help="Holm within each family (R1, R2) over the confirmatory runs recorded so far "
                         "(rq1_round_change_primary_p_*.csv; PAP section 9)")
    ap.add_argument("--sensitivities", action="store_true",
                    help="secondary sensitivities of the 2024 radar estimate (rebuilt samples and subsets)")
    args = ap.parse_args()
    if args.holm:
        final_holm()
        return
    if args.post and not Path(args.post).is_dir():
        raise SystemExit(f"--post: {args.post} is not a folder")
    if args.placebo and not (args.post and args.provinces):
        raise SystemExit("--placebo needs --post and --provinces")
    if args.round == "R2" and (args.placebo or args.sensitivities or not args.post):
        raise SystemExit("--round R2 is a confirmatory run: it needs --post and excludes --placebo and --sensitivities")
    keep = sorted({x.strip() for x in args.provinces.split(",") if x.strip()}) if args.provinces else None
    if keep:
        events = [args.event] if args.event else (list(FAMILY) if args.post else list(SAMPLES))
        held = set().union(*(set(load_sample(SAMPLES[e])["province"]) for e in events))
        if set(keep) - held:
            raise SystemExit(f"--provinces: {sorted(set(keep) - held)} not in the {events} samples ({sorted(held)})")
    if args.sensitivities:
        if args.event:
            raise SystemExit("--sensitivities runs on the 2024 radar sample only; drop --event")
        if keep and set(keep) - set(load_sample(SAMPLES["2024"])["province"]):
            raise SystemExit(f"--provinces: {sorted(set(keep) - set(load_sample(SAMPLES['2024'])['province']))} "
                             "not in the 2024 radar sample")
        sfx = ("_prov-" + "-".join(keep)) if keep else ""
        if args.post:
            def post_of(pre, sample):
                return load_post(args.post, pre)[0]
            out = sensitivities(post_of, keep=keep, real=True)
            name, note = "rq1_round_change_sensitivities" + sfx, "RQ1 secondary sensitivities (pre-registered), 2024 radar"
        else:
            rng = np.random.default_rng(SEED + 50)
            out = sensitivities(lambda pre, sample: synthetic_post(pre, sample, -0.05, rng), n_boot=999,
                                declarations="synthetic", keep=keep)
            name, note = ("rq1_round_change_sensitivities_synthetic" + sfx, "Synthetic check that every RQ1 sensitivity "
                          "runs: one synthetic R1 per sample with a planted fall of 0.05 on changed units (0.035 at sheet "
                          "level); wild bootstrap 999 draws. Not results")
        write(out, name, note + ". Author's calculations.")
        print(out.round(4).to_string(index=False))
        return
    primary_p = {}
    for event in ([args.event] if args.event else (list(FAMILY) if args.post else list(SAMPLES))):
        sample = load_sample(SAMPLES[event])
        tag = TAGS[event]
        if keep:
            if not set(keep) & set(sample["province"]):
                print(f"skipped: none of {keep} in the {event} sample ({sorted(sample['province'].unique())})")
                continue
            sample = sample[sample["province"].isin(keep)].reset_index(drop=True)
            tag += "_prov-" + "-".join(p for p in keep if p in set(sample["province"]))
            if args.placebo:
                tag += "_placebo"
        if args.round == "R2":
            tag += "_r2"
        pre = load_parcels(PRE, set(sample["province"]))
        pre = pre.merge(sample[SHEET], on=SHEET)
        write(balance_table(sample), f"rq1_round_change{tag}_balance",
              f"Entropy-balancing diagnostics, {event} sample, pre-period data: effective controls (Kish), balancing set "
              "after the registered fallback, treated sheets beyond the controls' range on each balancing variable, "
              "and standardised gaps after weighting (controls' SD), by province and pooled. Author's calculations.")
        if args.post:
            post, sha = load_post(args.post, pre)
            sh = sample.merge(sheet_outcomes(unit_changes(pre, post)), on=SHEET, how="left")
            sh.to_csv(SHEETS_OUT.with_name(f"rq1_round_change{tag}_sheets.csv.gz"), index=False)
            write(match_report(sh), f"rq1_round_change{tag}_matching", f"Parcel matching between 2023-26 and R1, {event} "
                  f"sample: share of sample sheets with no 2023-26 parcel found in R1; alert above {MATCH_ALERT:.0%} "
                  "(PAP section 5).")
            check_matching(sh, f"{event} sample")
            out = analyse(sh)
            write(out, f"rq1_round_change{tag}", f"RQ1 analysis (pre-registered), {event} sample: change in log official "
                  "value per square wah between 2023-26 and the first post-flood round. Sources: Treasury Department; "
                  "author's calculations.")
            print(out.round(4).to_string(index=False))
            primary_p[event] = float(out.loc[0, "p_primary"])
            if event in FAMILY and not args.placebo:   # record for the final Holm (PAP section 9)
                pd.DataFrame([{"family": args.round, "sample": event,
                               "provinces": "+".join(sorted(sample["province"].unique())),
                               "post": str(Path(args.post).resolve()),
                               "r1_sha256": "; ".join(f"{k}={v}" for k, v in sha.items()),
                               "estimate": float(out.loc[0, "estimate"]),
                               "p_primary": primary_p[event]}]).to_csv(TAB / f"rq1_round_change_primary_p{tag}.csv",
                                                                       index=False)
            continue
        rows = []
        for effect in (-0.05, 0.0):
            rng = np.random.default_rng(SEED + int(round(-effect * 1000)))
            post = synthetic_post(pre, sample, effect, rng)
            sh = sample.merge(sheet_outcomes(unit_changes(pre, post)), on=SHEET, how="left")
            out = analyse(sh)
            out.insert(0, "planted_effect", effect)
            out.insert(1, "expected_sheet_effect", effect * (1 - 0.3))
            rows.append(out)
            print(event, flush=True)
            print(out.round(4).to_string(index=False), flush=True)
        write(pd.concat(rows, ignore_index=True), f"rq1_round_change{tag}_synthetic",
              f"Synthetic check of the pre-registered RQ1 code, {event} sample: R1 simulated from the 2023-26 snapshot of "
              "the sample sheets (province shift N(0.08, 0.03); sheet changes SD 0.10 with ICC 0.2 at 1:50,000 sheets; "
              "unit noise SD 0.05; 30% of units carried over; 2% of parcels dropped, 1% new parcel numbers) with the "
              "planted treatment effect on log values of changed units; expected sheet effect = planted x 0.7 "
              "(carry-over dilutes it). ri_p: 1,000 placebo footprints; wcb_p: wild cluster restricted bootstrap, "
              "9,999 draws. Not results. Sources: Treasury Department 2023-26 snapshot; author's calculations.")
        mc = monte_carlo(pre, sample)
        write(mc, f"rq1_round_change{tag}_montecarlo",
              f"Monte Carlo of the pre-registered primary estimate on synthetic R1 draws, {event} sample (same "
              "simulation as the synthetic table): mean and SD of the estimate, mean CR1 cluster SE, and the share of "
              "draws rejecting zero at 5% by the wild cluster restricted bootstrap (999 draws each); with a planted "
              "effect of 0 this is the test's size, with -0.05 its power. Not results. Author's calculations.")
        print(mc.round(4).to_string(index=False), flush=True)
    if args.post and not primary_p:
        raise SystemExit("no sample ran")
    if set(FAMILY) <= set(primary_p) and not keep and not args.event and args.round == "R1":
        final_holm()        # every province in case (a): the family is the two samples of this run
    elif args.post and not args.placebo and set(primary_p) & set(FAMILY):
        print("recorded for the final Holm; run --holm after the last confirmatory run (PAP section 9)")


def final_holm():
    """Holm over every recorded confirmatory run (PAP sections 3 and 9).

    Two families, each Holm-adjusted on its own. R1: the radar and UNOSAT runs on R1 (with mixed
    timing, each sample's case-(a) provinces), closed by the waiting rule of section 9. R2: the
    case-(b) provinces' runs on R2 (`--round R2`), adjusted once the last of them is recorded.
    Case-(b) placebo runs on R1 are not recorded."""
    files = sorted(TAB.glob("rq1_round_change_primary_p*.csv"))
    if not files:
        raise SystemExit("no confirmatory run recorded")
    rec = pd.concat([pd.read_csv(f, dtype={"sample": str, "provinces": str}).assign(file=f.name) for f in files],
                    ignore_index=True)
    rec["family"] = rec["family"].fillna("R1") if "family" in rec else "R1"
    pairs = rec.assign(province=rec["provinces"].str.split("+")).explode("province")
    dup = pairs[pairs.duplicated(["family", "sample", "province"], keep=False)]
    if len(dup):
        raise SystemExit(f"a province enters two recorded runs of one sample and family; remove the stale record:\n{dup}")
    rec["test"] = rec["family"] + ":" + rec["sample"] + ":" + rec["provinces"]
    rec["p_holm"] = np.nan
    for fam, g in rec.groupby("family"):
        adj = holm(dict(zip(g["test"], g["p_primary"])))
        rec.loc[g.index, "p_holm"] = g["test"].map(adj)
    hp = rec[["family", "sample", "provinces", "post", "estimate", "p_primary", "p_holm"]]
    write(hp, "rq1_round_change_holm", f"H1a confirmatory families (PAP sections 3 and 9): Holm-adjusted primary p-values "
          f"within each family (R1; R2 for case (b) provinces) over {len(hp)} recorded runs (placebo-footprint p for the "
          "radar sample; wild cluster bootstrap p for UNOSAT, where placebo footprints cannot be drawn).")
    print(hp.to_string(index=False))


if __name__ == "__main__":
    main()

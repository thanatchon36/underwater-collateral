"""Tests of the pre-registered RQ1 code on hand-made data: .venv/bin/python -I -m pytest 04_analysis/src/test_rq1_round_change.py"""
import pathlib
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import rq1_round_change as r  # noqa: E402

S = dict(province="p", UTMMAP1="1", UTMMAP2="2", UTMMAP3="3", UTMMAP4="00", UTMSCALE="4000")


def parcels(rows, sheet=S):
    return pd.DataFrame([{**sheet, "LAND_NO": n, "p": p} for n, p in rows])


def test_units_follow_parcels_and_ignore_new_numbers():
    pre = parcels([("1", 100), ("2", 100), ("3", 200), ("4", 300)])
    post = parcels([("1", 110), ("2", 130), ("3", 200), ("9", 999)])  # 4 lost, 9 new
    u = r.unit_changes(pre, post).set_index("p")
    assert np.isclose(u.loc[100, "dlog"], np.log(120 / 100))      # mean over present parcels
    assert u.loc[200, "carried"] == 1 and u.loc[100, "carried"] == 0
    assert u.loc[300, "n_present"] == 0 and np.isnan(u.loc[300, "dlog"])
    s = r.sheet_outcomes(u.reset_index()).iloc[0]
    assert s["units"] == 3 and s["units_present"] == 2
    assert np.isclose(s["attrition"], 1 / 4)
    assert np.isclose(s["dlog"], np.log(1.2) / 2) and np.isclose(s["carry"], 0.5)


def toy(n=400, effect=-0.05, seed=0):
    rng = np.random.default_rng(seed)
    d = pd.DataFrame({"province": rng.choice(["a", "b"], n), "series_sheet": rng.integers(0, 40, n).astype(str),
                      "T": (rng.random(n) < 0.2).astype(int), "x": rng.random(n) * 50, "y": rng.random(n) * 50})
    for c in r.COVS + ["mean_logp", "rel_elev_m"]:
        d[c] = rng.random(n)
    d["dlog"] = 0.1 * (d["province"] == "b") + 0.3 * d["elev_m"] + effect * d["T"]
    d["carry"] = 0.0
    return d


def test_estimate_recovers_effect_without_noise():
    d = toy()
    e = r.estimate(d, r.balance_weights(d))
    assert np.isclose(e["estimate"], -0.05, atol=1e-10)


def test_balance_weights_match_treated_means():
    d = toy()
    w = r.balance_weights(d)
    for pr, g in d.groupby("province"):
        c, t = g[g["T"] == 0], g[g["T"] == 1]
        assert np.isclose(w[c.index].sum(), len(t))
        assert np.allclose(np.average(c[r.BAL], weights=w[c.index], axis=0), t[r.BAL].mean(), atol=1e-3)


def test_balance_falls_back_when_treated_lie_outside_control_range():
    d = toy()
    pr = d["province"].iloc[0]
    d.loc[(d["province"] == pr) & (d["T"] == 1), "lc_cropland"] = 5.0  # unreachable by any control mix
    log = []
    w = r.balance_weights(d, log=log)
    assert log == [(pr, "+".join(v for v in r.BAL if v != "lc_cropland"))]
    g = d[d["province"] == pr]
    assert np.isclose(w[g.index[g["T"] == 0]].sum(), (g["T"] == 1).sum())


def test_placebo_footprint_uses_controls_only_and_keeps_counts():
    d = toy()
    p = r.placebo_assignment(d, np.random.default_rng(1))
    assert len(p) == int((d["T"] == 0).sum())
    for pr, g in d.groupby("province"):
        assert p.loc[p["province"] == pr, "T"].sum() == g["T"].sum()


def test_wild_bootstrap_p_small_for_large_effect_and_not_for_none():
    rng = np.random.default_rng(3)
    d = toy(effect=-0.5)
    d["dlog"] += rng.normal(0, 0.1, len(d))
    w = r.balance_weights(d)
    assert r.wild_cluster_p(d, w, n_boot=199) < 0.01
    d["dlog"] = d["dlog"] + 0.5 * d["T"]
    assert r.wild_cluster_p(d, w, n_boot=199) > 0.05


def test_holm_adjustment():
    adj = r.holm({"a": 0.01, "b": 0.04})
    assert np.isclose(adj["a"], 0.02) and np.isclose(adj["b"], 0.04)
    adj = r.holm({"a": 0.03, "b": 0.02})
    assert np.isclose(adj["b"], 0.04) and np.isclose(adj["a"], 0.04)


def test_wild_bootstrap_null_shift_and_interaction():
    rng = np.random.default_rng(4)
    d = toy(effect=-0.05)
    d["dlog"] += rng.normal(0, 0.01, len(d))
    w = r.balance_weights(d)
    assert r.wild_cluster_p(d, w, n_boot=199, null=-0.05) > 0.05   # the true value is not rejected
    assert r.wild_cluster_p(d, w, n_boot=199, null=0.0) < 0.01
    assert 0 <= r.wild_cluster_p(d, w, n_boot=199, interaction=True, j=1) <= 1


def test_randomisation_p_is_never_zero():
    d = toy(effect=-5.0)
    p, draws = r.randomisation_p(d, r.estimate(d, r.balance_weights(d))["estimate"], n=9)
    assert np.isclose(p, 1 / 10) and len(draws) == 9


def test_optical_flag_needs_clear_scenes_and_new_water(tmp_path):
    rows = [  # sheet 0: new water 0.5 -> flagged; sheet 1: cloudy 2024 scene ignored -> not flagged;
              # sheet 2: water in both years -> not flagged; sheet 3: no scenes -> not flagged
        (0, "2023-09-01", 100, 100, 0), (0, "2024-09-01", 100, 100, 50),
        (1, "2023-09-01", 100, 100, 0), (1, "2024-09-01", 100, 40, 40), (1, "2024-09-10", 100, 100, 5),
        (2, "2023-09-01", 100, 100, 60), (2, "2024-09-01", 100, 100, 65),
    ]
    f, kf = tmp_path / "s2.csv", tmp_path / "keys.csv"
    pd.DataFrame(rows, columns=["sheet_id", "date", "px", "clear", "water"]).to_csv(f, index=False)
    sheets = pd.DataFrame([{**S, "UTMMAP4": str(i)} for i in range(4)])
    # key file lists the sheets in another order: the flag must follow the key, not the row
    pd.DataFrame({"sheet_id": [0, 1, 2, 3], **{c: sheets[c][::-1].to_numpy() for c in r.SHEET}}).to_csv(kf, index=False)
    flag = r.optical_flooded(sheets, counts=f, keys=kf, check=False)
    assert flag.tolist() == [False, False, False, True]


def test_s2_alignment_check_catches_shifted_sheet_ids():
    from rasterio.warp import transform_bounds
    import validate_s1_s2 as v
    boxes = pd.DataFrame({"sheet_id": [0, 1], "lon0": [100.0, 100.0], "lat0": [18.0, 18.0],
                          "lon1": [100.125, 100.25], "lat1": [18.125, 18.25]})
    px = []
    for b in boxes.itertuples():
        x = transform_bounds("EPSG:4326", "EPSG:32647", b.lon0, b.lat0, b.lon1, b.lat1)
        px.append(round((x[2] - x[0]) / 20) * round((x[3] - x[1]) / 20))
    counts = pd.DataFrame({"sheet_id": [0, 1], "px": px})
    assert v.check_alignment(boxes, counts) == []
    assert v.check_alignment(boxes.assign(sheet_id=[1, 0]), counts) == [0, 1]


def test_lee_bounds_trim_the_group_that_moves_more():
    import rq1_lee_bounds as lb
    # treated: 4 units, all moved (dlog 1,2,3,4); controls: 4 units, 2 moved (dlog 0, 0) -> trim half of treated
    u = pd.DataFrame({"T": [1] * 4 + [0] * 4, "moved": [1, 1, 1, 1, 1, 1, 0, 0],
                      "dlog": [1, 2, 3, 4, 0, 0, 0, 0], "wu": 1.0})
    b = lb.province_bounds(u)
    assert np.isclose(b["trim_share"], 0.5) and np.isclose(b["naive"], 2.5)
    assert np.isclose(b["lower"], 1.5) and np.isclose(b["upper"], 3.5)
    # fractional trim of the boundary unit: drop 0.25 of weight 4 -> one unit from the top
    assert np.isclose(lb.trimmed_mean(np.array([1., 2., 3., 4.]), np.ones(4), 0.25, top=True), 2.0)
    assert np.isclose(lb.trimmed_mean(np.array([1., 2.]), np.ones(2), 0.25, top=True), (1 + 0.5 * 2) / 1.5)


def test_lee_bounds_skip_provinces_without_moved_units_in_a_group():
    import rq1_lee_bounds as lb
    ok = pd.DataFrame({"province": "a", "T": [1, 1, 0, 0], "moved": [1, 1, 1, 0], "dlog": [1., 2., 0., 0.], "wu": 1.0})
    none_c = pd.DataFrame({"province": "b", "T": [1, 1, 0, 0], "moved": [1, 1, 0, 0], "dlog": 0.0, "wu": 1.0})
    u = pd.concat([ok, none_c], ignore_index=True)
    assert lb.usable(ok) and not lb.usable(none_c)
    est, rows = lb.bounds(u, pd.Series({"a": 2.0}))
    assert list(rows) == ["a"] and np.isclose(est["naive"], 1.5)
    assert lb.bounds(none_c, pd.Series({"b": 2.0}))[0] is None


def test_declarations_match_thai_names_and_drop_controls_only():
    import pytest
    import rq1_declarations as dec
    units = pd.DataFrame({"province": "nong-khai", "adm2_pcode": ["TH4301", "TH4301", "TH4302"],
                          "adm2_name1": ["เมืองหนองคาย", "เมืองหนองคาย", "ท่าบ่อ"],
                          "adm3_pcode": ["TH430101", "TH430102", "TH430201"],
                          "adm3_name1": ["ในเมือง", "มีชัย", "ท่าบ่อ"]})
    sheets = pd.DataFrame([{**S, "province": "nong-khai", "UTMMAP4": str(i)} for i in range(4)])
    sheets["T"] = [1, 0, 0, 0]
    admin = sheets[r.SHEET].assign(adm2_pcode=["TH4301", "TH4301", "TH4301", "TH4302"],
                                   adm3_pcode=["TH430101", "TH430101", "TH430102", "TH430201"])
    decl = pd.DataFrame({"province": "nong-khai", "district_th": ["อำเภอเมือง", "อ. ท่าบ่อ"],
                         "tambon_th": ["ต.ในเมือง", ""], "declared_on": ["2024-09-01", "2023-09-01"],
                         "source": "test"})
    by_d, by_t = dec.drop_masks(sheets, decl, admin, units)
    # the 2023 row is outside the window; "เมือง" means Mueang Nong Khai; the treated sheet is never dropped
    assert by_d.tolist() == [False, True, True, False]
    assert by_t.tolist() == [False, True, False, False]
    with pytest.raises(SystemExit):
        dec.drop_masks(sheets, decl.assign(district_th=["อำเภอไม่มี", "ท่าบ่อ"]), admin, units)


def test_final_holm_spans_recorded_runs_and_refuses_overlaps(tmp_path, monkeypatch):
    import pytest
    monkeypatch.setattr(r, "TAB", tmp_path)
    rec = lambda name, sample, provs, p: pd.DataFrame([{"sample": sample, "provinces": provs, "post": "x",  # noqa: E731
                                                        "estimate": -0.05, "p_primary": p}]).to_csv(
        tmp_path / f"rq1_round_change_primary_p{name}.csv", index=False)
    rec("", "2024", "chiang-rai+phayao", 0.01)            # case (a) provinces on R1
    rec("_prov-nong-khai", "2024", "nong-khai", 0.04)     # case (b) province on R2
    rec("_unosat", "unosat", "chiang-rai+phayao", 0.03)
    r.final_holm()
    h = pd.read_csv(tmp_path / "rq1_round_change_holm.csv")
    assert len(h) == 3 and np.isclose(h["p_holm"].min(), 0.03)   # 3 x 0.01
    rec("_prov-phayao", "2024", "phayao", 0.2)            # stale record: Phayao twice in the radar sample
    with pytest.raises(SystemExit):
        r.final_holm()


def test_r2_runs_form_their_own_holm_family(tmp_path, monkeypatch):
    monkeypatch.setattr(r, "TAB", tmp_path)

    def rec(name, fam, sample, provs, p):
        pd.DataFrame([{"family": fam, "sample": sample, "provinces": provs, "post": "x", "estimate": -0.05,
                       "p_primary": p}]).to_csv(tmp_path / f"rq1_round_change_primary_p{name}.csv", index=False)
    rec("_prov-chiang-rai-phayao", "R1", "2024", "chiang-rai+phayao", 0.01)   # case (a) on R1
    rec("_unosat", "R1", "unosat", "chiang-rai+phayao", 0.03)
    rec("_prov-nong-khai_r2", "R2", "2024", "nong-khai", 0.04)                # case (b) on R2, years later
    rec("_prov-nakhon-phanom_r2", "R2", "2024", "nakhon-phanom", 0.30)
    r.final_holm()
    h = pd.read_csv(tmp_path / "rq1_round_change_holm.csv").set_index(["family", "provinces"])
    assert np.isclose(h.loc[("R1", "chiang-rai+phayao"), "p_holm"].min(), 0.02)   # 2 x 0.01: R2 not in R1's family
    assert np.isclose(h.loc[("R2", "nong-khai"), "p_holm"], 0.08)                 # 2 x 0.04 within R2
    # the same province may appear once per family (R1 placebo is not recorded; R2 primary is)
    rec("_prov-nong-khai", "R1", "2024", "nong-khai", 0.5)
    r.final_holm()


def test_content_check_refuses_a_rescaled_round():
    pre = parcels([(str(i), 1000 + 50 * i) for i in range(200)])
    try:   # square wah to square metre: every value divided by 4
        r.check_content(pre, parcels([(str(i), (1000 + 50 * i) / 4) for i in range(200)]))
        raise AssertionError("should stop")
    except SystemExit as e:
        assert "rescaling" in str(e)
    rng = np.random.default_rng(0)   # a reappraisal: units move by different ratios, 30% unchanged
    post = [(str(i), (1000 + 50 * i) * (1.0 if i < 60 else float(rng.uniform(0.9, 1.3)))) for i in range(200)]
    r.check_content(pre, parcels(post))


def test_buffer_distance_is_great_circle():
    import geo
    # 0.045 deg of latitude is about 5.004 km anywhere; one degree of longitude at 18 N about 105.8 km
    assert abs(geo.nearest_km([100.0], [18.0], [100.0], [18.045])[0] - 5.004) < 0.01
    assert abs(geo.nearest_km([100.0], [18.0], [101.0], [18.0])[0] - 105.75) < 0.2
    # two sheets 0.3 deg apart in latitude and 0.05 deg in longitude: the old per-sheet cos(lat) x
    # coordinate put them more than 9 km apart east-west; on the sphere they are about 33.6 km apart in all
    d = pd.DataFrame({"lon0": [100.0, 100.05], "lon1": [100.0, 100.05], "lat0": [18.0, 18.3], "lat1": [18.0, 18.3]})
    gc = geo.dist_to_treated(d, [True, False])[1]
    assert abs(gc - 33.6) < 0.3


def test_post_check_refuses_missing_and_unchanged_files(tmp_path):
    import hashlib
    old = tmp_path / "pre"
    old.mkdir()
    (old / "land_56_phayao.csv").write_bytes(b"same bytes")
    pd.DataFrame({"file": ["land_56_phayao.csv"],
                  "sha256": [hashlib.sha256(b"same bytes").hexdigest()]}).to_csv(old / "manifest.csv", index=False)
    post = tmp_path / "post"
    post.mkdir()
    (post / "land_56_phayao.csv").write_bytes(b"same bytes")
    for provs in ({"phayao"}, {"phayao", "nan"}):
        try:
            r.check_post(post, provs, manifest=old / "manifest.csv")
            raise AssertionError("should stop")
        except SystemExit:
            pass
    (post / "land_56_phayao.csv").write_bytes(b"new round")
    assert r.check_post(post, {"phayao"}, manifest=old / "manifest.csv")["phayao"] == hashlib.sha256(b"new round").hexdigest()


def test_post_check_refuses_two_files_for_one_province(tmp_path):
    import hashlib
    old = tmp_path / "pre"
    old.mkdir()
    pd.DataFrame({"file": ["land_56_phayao.csv"],
                  "sha256": [hashlib.sha256(b"old round").hexdigest()]}).to_csv(old / "manifest.csv", index=False)
    post = tmp_path / "post"
    post.mkdir()
    (post / "land_56_phayao.csv").write_bytes(b"new round")
    (post / "land_99_phayao.csv").write_bytes(b"old round")   # load_parcels would read both
    try:
        r.check_post(post, {"phayao"}, manifest=old / "manifest.csv")
        raise AssertionError("should stop")
    except SystemExit as e:
        assert "more than one" in str(e)


def test_content_check_refuses_a_resaved_old_round():
    pre = parcels([(str(i), 100 + i) for i in range(200)])
    try:   # same values, one parcel lost (a re-saved copy with a row dropped is still the old round)
        r.check_content(pre, parcels([(str(i), 100.0 + i) for i in range(199)]))
        raise AssertionError("should stop")
    except SystemExit as e:
        assert "old round" in str(e)
    try:   # re-issued with one correction in 200: still above 99% unchanged
        r.check_content(pre, parcels([(str(i), 100 + i + (i == 0)) for i in range(200)]))
        raise AssertionError("should stop")
    except SystemExit:
        pass
    r.check_content(pre, parcels([(str(i), 100 + i + (i < 10)) for i in range(200)]))   # 5% moved: a new round
    r.check_content(pre, parcels([("x", 100)]))                                      # nothing matched: matching stop
    # a parcel on two rows in one round is left out: dropping one of its rows moves its average, not its appraisal
    pre_r, post_r = pre.assign(rows=1), parcels([(str(i), 100 + i + (i < 10)) for i in range(200)]).assign(rows=1)
    pre_r.loc[:9, "rows"] = 2
    try:
        r.check_content(pre_r, post_r)
        raise AssertionError("should stop")
    except SystemExit:
        pass


def test_r1_files_need_the_registered_name(tmp_path):
    (tmp_path / "land_phayao.csv").write_text("x")
    pd.DataFrame({"file": ["a"], "sha256": ["b"]}).to_csv(tmp_path / "manifest.csv", index=False)
    try:
        r.check_post(tmp_path, {"phayao"}, manifest=tmp_path / "manifest.csv")
        raise AssertionError("should stop")
    except SystemExit as e:
        assert "land_<code>_<province>.csv" in str(e)


def test_matching_stop_fires_on_any_real_sample(monkeypatch):
    sh = pd.DataFrame({"province": ["p"] * 10, "T": [1] * 5 + [0] * 5,
                       "dlog": [0.1, np.nan, 0.0, 0.0, 0.0] + [0.0] * 5})   # 20% of treated unmatched
    try:
        r.check_matching(sh, "test")
        raise AssertionError("should stop")
    except SystemExit as e:
        assert "MATCHING ALERT" in str(e)
    sh.loc[1, "dlog"] = 0.0
    assert not r.check_matching(sh, "test")["alert"].any()
    # behaviour on the two other real-R1 paths: an R1 matching no parcel stops before any estimate
    import rq1_lee_bounds as lb
    sample = pd.DataFrame([{**S, "UTMMAP4": str(k), "T": int(k < 2)} for k in range(4)])
    pre = pd.concat([parcels([("1", 100)], {**S, "UTMMAP4": str(k)}) for k in range(4)], ignore_index=True)
    empty = pre.iloc[:0]
    monkeypatch.setattr(r, "load_parcels", lambda folder, provinces, rows=False: pre)
    monkeypatch.setattr(r, "SENS", ["x"])
    monkeypatch.setattr(r, "load_sample", lambda path: sample)
    for call in (lambda: r.sensitivities(lambda pre_, s: empty, real=True),
                 lambda: lb.run(sample, lambda pre_, s: empty, real=True)):
        try:
            call()
            raise AssertionError("should stop")
        except SystemExit as e:
            assert "MATCHING ALERT" in str(e)


def test_sensitivities_skip_a_rebuilt_sample_left_empty(monkeypatch, capsys):
    class Stop(Exception):
        pass
    fake = pd.DataFrame({"province": ["a", "a"], "T": [1, 0]})

    def load_sample(path):
        if "empty" in str(path):
            return fake
        raise Stop
    monkeypatch.setattr(r, "SENS", ["empty"])
    monkeypatch.setattr(r, "load_sample", load_sample)
    try:
        r.sensitivities(lambda pre, s: None, keep=["b"])
    except Stop:
        pass
    assert "row skipped" in capsys.readouterr().out


def test_phayao_gets_its_own_height_slope():
    d = pd.DataFrame({"T": [1, 0, 1, 0], "province": ["phayao", "phayao", "2024:phayao", "nan"],
                      "rel_elev_m": [5.0, 1.0, 4.0, 2.0], **{c: 0.0 for c in r.COVS}})
    X, names = r.design(d)
    j = names.index("height_x_phayao")
    assert X[:, j].tolist() == [5.0, 1.0, 4.0, 0.0]
    _, names = r.design(d[d["province"] == "nan"])
    assert "height_x_phayao" not in names and "height_x_phatthalung" not in names
    _, names = r.design(d.assign(province=["2025:phatthalung", "phatthalung", "phayao", "nan"]))
    assert {"height_x_phayao", "height_x_phatthalung"} <= set(names)

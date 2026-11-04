"""Tests for mapsheet.py, built on worked examples from the sources.

Sources (full citations in 04_analysis/groundwork_notes.md):
[DOL47]  DOL, คำอธิบายระเบียบกรมที่ดินว่าด้วยการสร้างและการใช้ระวางแผนที่ พ.ศ. ๒๕๔๗:
         ข้อ ๑๗ (sub-sheet sizes and numbering figures), ข้อ ๒๐ (naming rule and
         example "5638 II 2606"), รูปที่ ๑ (example 1:4,000 sheet 5638 II 2606 with
         grid ticks 326000-328000 m E, 1606000-1608000 m N, adjacent-sheet index).
[DOLQA]  DOL question-and-answer compilation (คำถาม-คำตอบ), items ๓๑-๓๓, ๓๘.
[ALRO]   ALRO, มาตรฐานระวางแผนที่และแผนที่รูปแปลงที่ดินในที่ดินของรัฐ, กมร. 103-2551 and the
         data dictionary (UTMMAP4 domain 00 / 01-04 / 01-16 / 01-64).
[RTSD]   RTSD L7018 1:50,000 sheet index (data.go.th dataset l7018_index).
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))
import mapsheet as m  # noqa: E402


# [DOL47] รูปที่ ๑: sheet "5638 II 2606" at 1:4,000, ticks 326000/328000 m E and
# 1606000/1608000 m N, อำเภอปราสาท (Prasat, Surin), zone 48.
def test_dol_figure_example_4000():
    assert m.sheet_bounds("5638", "2", "2606", "00", "4000") == (48, 326000.0, 1606000.0, 328000.0, 1608000.0)


def test_roman_quadrant_accepted():
    assert m.sheet_bounds("5638", "II", "2606", "00", 4000) == m.sheet_bounds("5638", 2, "2606", "00", 4000)


# [DOL47] รูปที่ ๑ adjacent-sheet index ("สารบัญระวางติดต่อ"): neighbours of 2606 are
# 2408 2608 2808 / 2406 . 2806 / 2404 2604 2804, all in 5638 II.
@pytest.mark.parametrize(
    "code,de,dn",
    [("2408", -2, 2), ("2608", 0, 2), ("2808", 2, 2), ("2406", -2, 0), ("2806", 2, 0),
     ("2404", -2, -2), ("2604", 0, -2), ("2804", 2, -2)],
)
def test_dol_figure_adjacent_sheets(code, de, dn):
    z, x0, y0, _, _ = m.sheet_bounds("5638", "2", code, "00", "4000")
    assert (z, x0, y0) == (48, 326000.0 + de * 1000, 1606000.0 + dn * 1000)


# [DOL47] ข้อ ๒๐: the inverse rule, the even-km tens/units of the lower-left corner.
# [DOLQA] ข้อ ๓๑: corner E 280,000 N 1,632,000 -> "8032"; ข้อ ๓๒: E 500,600 N 2,049,000
# lies in the sheet whose corner is E 500,000 N 2,048,000 -> "0048". (These exam
# coordinates are not geographically consistent with the 1:50,000 sheets named in
# the questions, so they test only the digit rule.)
@pytest.mark.parametrize(
    "e,n,code",
    [(326000, 1606000, "2606"), (280000, 1632000, "8032"), (500000, 2048000, "0048")],
)
def test_grid_code_digit_rule(e, n, code):
    assert m.grid_code(e, n) == code


def test_odd_km_rejected():
    with pytest.raises(ValueError):
        m.sheet_bounds("5136", "4", "8134", "00", "4000")


# [DOL47] ข้อ ๑๗: 1:2,000 = 1,000 m sheets numbered 1 2 / 3 4 from the top-left.
@pytest.mark.parametrize("k,col,row", [(1, 0, 0), (2, 1, 0), (3, 0, 1), (4, 1, 1)])
def test_subsheets_2000(k, col, row):
    _, x0, y0, x1, y1 = m.sheet_bounds("5638", "2", "2606", f"{k:02d}", "2000")
    assert (x1 - x0, y1 - y0) == (1000.0, 1000.0)
    assert x0 == 326000.0 + 1000 * col
    assert y1 == 1608000.0 - 1000 * row


# [DOL47] ข้อ ๑๗ and ข้อ ๒๐ example "5638 II 2606 - 5 (1:1,000)": 4 x 4 sheets of 500 m,
# 1-4 on the top row; sheet 5 starts the second row on the west edge.
def test_dol_example_1000_sheet5():
    assert m.sheet_bounds("5638", "2", "2606", "05", "1000") == (48, 326000.0, 1607000.0, 326500.0, 1607500.0)


# [DOLQA] ข้อ ๓๓: the sheet adjoining the lower edge of 1:1,000 sheet "-6" is "-10".
def test_dol_qa_sheet_below_6_is_10():
    _, x6, y6, _, _ = m.sheet_bounds("5638", "2", "2606", "06", "1000")
    _, x10, _, _, y10top = m.sheet_bounds("5638", "2", "2606", "10", "1000")
    assert x10 == x6 and y10top == y6


# [DOL47] ข้อ ๑๗: 1:500 = 64 sheets of 250 m; [ALRO] domain 01-64.
def test_subsheets_500_corners():
    assert m.sheet_bounds("5638", "2", "2606", "01", "500")[1:] == (326000.0, 1607750.0, 326250.0, 1608000.0)
    assert m.sheet_bounds("5638", "2", "2606", "64", "500")[1:] == (327750.0, 1606000.0, 328000.0, 1606250.0)


# [ALRO] UTMMAP4 domains.
@pytest.mark.parametrize("k,scale", [("01", "4000"), ("05", "2000"), ("17", "1000"), ("65", "500"), ("00", "1000")])
def test_out_of_domain_subsheet(k, scale):
    with pytest.raises(ValueError):
        m.sheet_bounds("5638", "2", "2606", k, scale)


def test_scale_5000_not_decoded():
    with pytest.raises(ValueError):
        m.sheet_bounds("5739", "1", "0000", "023", "5000")


# [RTSD] L7018 index polygons: 5136 IV = Amphoe Bang Khen, 100.50-100.75 E,
# 13.75-14.00 N; 5638 II = Amphoe Prasat, 103.25-103.50 E, 14.50-14.75 N.
def test_series_sheet_extent():
    assert m.series_sheet_lonlat("5136", "IV") == (100.5, 13.75, 100.75, 14.0)
    assert m.series_sheet_lonlat("5638", 2) == (103.25, 14.5, 103.5, 14.75)


def test_tm_round_trip():
    for lon, lat, zone in [(100.6, 13.8, 47), (103.4, 14.6, 48), (98.9, 18.8, 47)]:
        for ellps in (m.EVEREST_1830, m.WGS84):
            e, n = m.lonlat_to_utm(lon, lat, zone, ellps)
            lo, la = m.utm_to_lonlat(e, n, zone, ellps)
            assert abs(lo - lon) < 1e-9 and abs(la - lat) < 1e-9


def test_centroid_and_datum_shift_magnitude():
    z, cx, cy = m.sheet_centroid("5638", "2", "2606", "00", "4000")
    assert (z, cx, cy) == (48, 327000.0, 1607000.0)
    lon, lat = m.sheet_centroid("5638", "2", "2606", "00", "4000", wgs84=True)
    assert 103.25 < lon < 103.5 and 14.5 < lat < 14.75
    # Indian 1975 -> WGS84 moves points by several hundred metres in Thailand.
    e_w, n_w = m.lonlat_to_utm(lon, lat, z, m.WGS84)
    shift = ((e_w - cx) ** 2 + (n_w - cy) ** 2) ** 0.5
    assert 300 < shift < 700

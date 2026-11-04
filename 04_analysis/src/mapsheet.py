"""Decode Thai Department of Lands (DOL) UTM cadastral map-sheet references.

The Treasury appraisal files identify each parcel by the fields
``UTMMAP1, UTMMAP2, UTMMAP3, UTMMAP4, UTMSCALE`` plus a parcel number. These are
the DOL "ระวางแผนที่ระบบพิกัดฉาก ยู ที เอ็ม" (UTM cadastral map sheet) reference.
This module turns a reference into the sheet's extent in UTM metres.

Convention (sources: see ``04_analysis/groundwork_notes.md``):

* DOL, คำอธิบายระเบียบกรมที่ดินว่าด้วยการสร้างและการใช้ระวางแผนที่ พ.ศ. ๒๕๔๗, ข้อ ๑๗ and ข้อ ๒๐
  (explanatory notes to the DOL Regulation on Making and Using Map Sheets, 2004).
* ALRO, มาตรฐานระวางแผนที่และแผนที่รูปแปลงที่ดินในที่ดินของรัฐ, กมร. 103-2551 and the data
  dictionary table TITLE (field definitions of UTMMAP1-4 and UTMSCALE).

1. ``UTMMAP1`` (4 digits, e.g. ``5638``) and ``UTMMAP2`` (1-4 = I-IV) name the
   1:50,000 topographic sheet of series L7017 (RTSD) in which the *lower-left
   corner* of the 1:4,000 sheet lies (e.g. ``5638 II``). If that 1:50,000 sheet is
   not in official use, the sheet holding the lower-right corner is used instead.
2. ``UTMMAP3`` (4 digits, e.g. ``2606``) gives the lower-left corner of the
   1:4,000 sheet: the tens and units of the UTM easting in km (even), then the
   tens and units of the UTM northing in km (even). A 1:4,000 sheet covers
   2,000 m x 2,000 m (50 cm x 50 cm of map). The 100-km digits are not in the
   code; they follow from the 1:50,000 sheet's location.
3. ``UTMMAP4`` is the sub-sheet number within the 1:4,000 sheet, and
   ``UTMSCALE`` the scale: 4,000 -> ``00`` (whole sheet); 2,000 -> 01-04 (2 x 2,
   1,000 m); 1,000 -> 01-16 (4 x 4, 500 m); 500 -> 01-64 (8 x 8, 250 m). Sub-sheets
   are numbered row by row from the top-left (north-west) corner, left to right.
4. 1:50,000 sheet numbering (L7017/L7018): ``CCRR`` names a 30' x 30' block whose
   south-west corner is at longitude ``75 + 0.5*CC`` deg E and latitude
   ``-4.5 + 0.5*RR`` deg N; quadrants I = NE, II = SE, III = SW, IV = NW, each
   15' x 15'. Checked against all 826 polygons of the RTSD L7018 sheet index
   (exact for rows 34-49, i.e. north of 12.5 deg N; some coastal sheets in the
   peninsula are irregular, offset by up to about 0.15 deg). The sheet extent is
   used only to resolve the 100-km digits, which tolerates such offsets.

Datum. DOL cadastral sheets are computed on Indian 1975 (Everest 1830 ellipsoid),
UTM zones 47/48 (EPSG:24047 / EPSG:24048). ``sheet_bounds`` therefore returns
Indian 1975 UTM metres. Indian 1975 and WGS84 positions in Thailand differ by
several hundred metres, so convert (``to_wgs84_lonlat``) before overlaying
WGS84 rasters. Whether sheets re-issued on WGS84 keep the same names could not be
verified; see the notes.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# --------------------------------------------------------------------------
# Ellipsoids and the Indian 1975 -> WGS84 shift
# --------------------------------------------------------------------------

EVEREST_1830 = (6377276.345, 1 / 300.8017)  # Indian 1975 (EPSG:7015)
WGS84 = (6378137.0, 1 / 298.257223563)

# Three-parameter geocentric shift Indian 1975 -> WGS84 (metres), RTSD
# announcement of 10 Jan 2008 as quoted in ALRO กมร. 102-2551 (204.5, 837.9,
# 294.8 m; ALRO prints them with minus signs, i.e. the WGS84 -> Indian 1975
# direction). The positive sign for Indian 1975 -> WGS84 matches EPSG:1812
# ("Indian 1975 to WGS 84 (4)", scope "Cadastre", Thailand onshore: Position
# Vector, +293, +836, +318 m, rotations 0.5, 1.6, -2.8", scale 2.1 ppm, accuracy
# 3 m). The two parameter sets differ by metres, which is immaterial for sheets
# of 250 m or more.
INDIAN1975_TO_WGS84 = (204.5, 837.9, 294.8)

SHEET_SIZE_M = {4000: 2000.0, 2000: 1000.0, 1000: 500.0, 500: 250.0}
SUBSHEETS_PER_SIDE = {4000: 1, 2000: 2, 1000: 4, 500: 8}
QUADRANT_OFFSET = {1: (0.25, 0.25), 2: (0.25, 0.0), 3: (0.0, 0.0), 4: (0.0, 0.25)}
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4}

# --------------------------------------------------------------------------
# Transverse Mercator (Krueger series, Karney 2011), accurate to well under 1 mm
# within a UTM zone.
# --------------------------------------------------------------------------


def _tm_constants(ellps):
    a, f = ellps
    n = f / (2 - f)
    n2, n3, n4, n5, n6 = n**2, n**3, n**4, n**5, n**6
    A = a / (1 + n) * (1 + n2 / 4 + n4 / 64 + n6 / 256)
    alpha = (
        n / 2 - 2 * n2 / 3 + 5 * n3 / 16 + 41 * n4 / 180 - 127 * n5 / 288 + 7891 * n6 / 37800,
        13 * n2 / 48 - 3 * n3 / 5 + 557 * n4 / 1440 + 281 * n5 / 630 - 1983433 * n6 / 1935360,
        61 * n3 / 240 - 103 * n4 / 140 + 15061 * n5 / 26880 + 167603 * n6 / 181440,
        49561 * n4 / 161280 - 179 * n5 / 168 + 6601661 * n6 / 7257600,
        34729 * n5 / 80640 - 3418889 * n6 / 1995840,
        212378941 * n6 / 319334400,
    )
    beta = (
        n / 2 - 2 * n2 / 3 + 37 * n3 / 96 - n4 / 360 - 81 * n5 / 512 + 96199 * n6 / 604800,
        n2 / 48 + n3 / 15 - 437 * n4 / 1440 + 46 * n5 / 105 - 1118711 * n6 / 3870720,
        17 * n3 / 480 - 37 * n4 / 840 - 209 * n5 / 4480 + 5569 * n6 / 90720,
        4397 * n4 / 161280 - 11 * n5 / 504 - 830251 * n6 / 7257600,
        4583 * n5 / 161280 - 108847 * n6 / 3991680,
        20648693 * n6 / 638668800,
    )
    e = math.sqrt(f * (2 - f))
    return A, alpha, beta, e


def lonlat_to_utm(lon, lat, zone, ellps=EVEREST_1830):
    """Geographic (deg) -> UTM easting, northing (m), northern hemisphere."""
    A, alpha, _, e = _tm_constants(ellps)
    k0, lon0 = 0.9996, math.radians(zone * 6 - 183)
    phi, lam = math.radians(lat), math.radians(lon) - lon0
    t = math.sinh(math.atanh(math.sin(phi)) - e * math.atanh(e * math.sin(phi)))
    xi_p = math.atan2(t, math.cos(lam))
    eta_p = math.atanh(math.sin(lam) / math.sqrt(1 + t * t))
    xi, eta = xi_p, eta_p
    for j, al in enumerate(alpha, start=1):
        xi += al * math.sin(2 * j * xi_p) * math.cosh(2 * j * eta_p)
        eta += al * math.cos(2 * j * xi_p) * math.sinh(2 * j * eta_p)
    return 500000.0 + k0 * A * eta, k0 * A * xi


def utm_to_lonlat(easting, northing, zone, ellps=EVEREST_1830):
    """UTM easting, northing (m), northern hemisphere -> geographic (deg)."""
    A, _, beta, e = _tm_constants(ellps)
    k0, lon0 = 0.9996, math.radians(zone * 6 - 183)
    xi, eta = northing / (k0 * A), (easting - 500000.0) / (k0 * A)
    xi_p, eta_p = xi, eta
    for j, b in enumerate(beta, start=1):
        xi_p -= b * math.sin(2 * j * xi) * math.cosh(2 * j * eta)
        eta_p -= b * math.cos(2 * j * xi) * math.sinh(2 * j * eta)
    tau_p = math.sin(xi_p) / math.sqrt(math.sinh(eta_p) ** 2 + math.cos(xi_p) ** 2)
    lam = math.atan2(math.sinh(eta_p), math.cos(xi_p))
    tau = tau_p  # Newton iteration for tau = tan(phi)
    for _ in range(8):
        sigma = math.sinh(e * math.atanh(e * tau / math.sqrt(1 + tau * tau)))
        tp = tau * math.sqrt(1 + sigma * sigma) - sigma * math.sqrt(1 + tau * tau)
        dtau = (tau_p - tp) / math.sqrt(1 + tp * tp) * (1 + (1 - e * e) * tau * tau) / (
            (1 - e * e) * math.sqrt(1 + tau * tau)
        )
        tau += dtau
        if abs(dtau) < 1e-14:
            break
    return math.degrees(lon0 + lam), math.degrees(math.atan(tau))


def _geodetic_to_ecef(lon, lat, ellps):
    a, f = ellps
    e2 = f * (2 - f)
    phi, lam = math.radians(lat), math.radians(lon)
    N = a / math.sqrt(1 - e2 * math.sin(phi) ** 2)
    return (N * math.cos(phi) * math.cos(lam), N * math.cos(phi) * math.sin(lam), N * (1 - e2) * math.sin(phi))


def _ecef_to_geodetic(x, y, z, ellps):
    a, f = ellps
    e2 = f * (2 - f)
    lon = math.atan2(y, x)
    p = math.hypot(x, y)
    lat = math.atan2(z, p * (1 - e2))
    for _ in range(10):
        N = a / math.sqrt(1 - e2 * math.sin(lat) ** 2)
        lat = math.atan2(z + e2 * N * math.sin(lat), p)
    return math.degrees(lon), math.degrees(lat)


def indian1975_to_wgs84(lon, lat):
    """Indian 1975 geographic -> WGS84 geographic (deg), 3-parameter shift, height 0."""
    x, y, z = _geodetic_to_ecef(lon, lat, EVEREST_1830)
    dx, dy, dz = INDIAN1975_TO_WGS84
    return _ecef_to_geodetic(x + dx, y + dy, z + dz, WGS84)


def to_wgs84_lonlat(easting, northing, zone):
    """Indian 1975 UTM (m) -> WGS84 lon, lat (deg)."""
    return indian1975_to_wgs84(*utm_to_lonlat(easting, northing, zone, EVEREST_1830))


# --------------------------------------------------------------------------
# 1:50,000 series sheets (L7017 / L7018)
# --------------------------------------------------------------------------


def series_sheet_lonlat(utmmap1, utmmap2):
    """Nominal (lon_min, lat_min, lon_max, lat_max) of a 1:50,000 sheet, e.g. ('5638', 2)."""
    code = f"{int(utmmap1):04d}"
    q = ROMAN[utmmap2] if isinstance(utmmap2, str) and utmmap2 in ROMAN else int(utmmap2)
    if q not in QUADRANT_OFFSET:
        raise ValueError(f"UTMMAP2 must be 1-4 (I-IV), got {utmmap2!r}")
    col, row = int(code[:2]), int(code[2:])
    if not (44 <= col <= 62 and 18 <= row <= 50):
        raise ValueError(f"UTMMAP1 {code} is not a 1:50,000 sheet over Thailand")
    dlon, dlat = QUADRANT_OFFSET[q]
    lon0, lat0 = 75 + 0.5 * col + dlon, -4.5 + 0.5 * row + dlat
    return lon0, lat0, lon0 + 0.25, lat0 + 0.25


def nominal_zone(lon):
    return 47 if lon < 102.0 else 48


def _series_sheet_utm_box(utmmap1, utmmap2, zone):
    lon0, lat0, lon1, lat1 = series_sheet_lonlat(utmmap1, utmmap2)
    pts = [lonlat_to_utm(lo, la, zone) for lo in (lon0, lon1) for la in (lat0, lat1)]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


# --------------------------------------------------------------------------
# Cadastral sheets
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class SheetFit:
    zone: int
    e_ll: float  # lower-left corner of the 1:4,000 sheet, Indian 1975 UTM
    n_ll: float
    miss_m: float  # distance of the lower-left corner outside the nominal 1:50,000 sheet


def grid_code(e_ll, n_ll):
    """Lower-left corner (m) of a 1:4,000 sheet -> 4-digit UTMMAP3 code (inverse rule)."""
    ek, nk = int(e_ll // 1000), int(n_ll // 1000)
    if ek % 2 or nk % 2:
        raise ValueError("1:4,000 sheet corners lie on even kilometres")
    return f"{ek % 100:02d}{nk % 100:02d}"


def _gap(v, lo, hi):
    return max(lo - v, 0.0, v - hi)


def _resolve(utmmap1, utmmap2, utmmap3, zone):
    code = f"{int(utmmap3):04d}"
    ee, nn = int(code[:2]), int(code[2:])
    if ee % 2 or nn % 2:
        raise ValueError(f"UTMMAP3 digits must be even km, got {code}")
    xmin, ymin, xmax, ymax = _series_sheet_utm_box(utmmap1, utmmap2, zone)
    best = None
    for cand_e in range(int(xmin // 100000) - 1, int(xmax // 100000) + 2):
        for cand_n in range(int(ymin // 100000) - 1, int(ymax // 100000) + 2):
            e, n = cand_e * 100000 + ee * 1000, cand_n * 100000 + nn * 1000
            # Lower-left rule, with the DOL fallback: lower-right corner (e + 2 km).
            miss = min(
                math.hypot(_gap(e, xmin, xmax), _gap(n, ymin, ymax)),
                math.hypot(_gap(e + 2000, xmin, xmax), _gap(n, ymin, ymax)),
            )
            if best is None or miss < best.miss_m:
                best = SheetFit(zone, float(e), float(n), miss)
    return best


def locate_4000(utmmap1, utmmap2, utmmap3, tol_m=5000.0):
    """Resolve the 1:4,000 sheet's lower-left corner and UTM zone.

    The nominal zone comes from the 1:50,000 sheet's longitude. Sheets that
    straddle 102 deg E are drawn in both zones (DOL ข้อ ๑๙), so if the code does not
    fit in the nominal zone the other zone is tried. ``tol_m`` is how far (m) the
    corner may fall outside the nominal 1:50,000 sheet before the reference is
    rejected as inconsistent; in the central provinces checked, valid references
    miss by at most about 4.6 km (irregular sheet edges, lower-right fallback).
    """
    lon0, _, lon1, _ = series_sheet_lonlat(utmmap1, utmmap2)
    z0 = nominal_zone(0.5 * (lon0 + lon1))
    fit = _resolve(utmmap1, utmmap2, utmmap3, z0)
    if fit.miss_m > tol_m:
        other = _resolve(utmmap1, utmmap2, utmmap3, 95 - z0)  # 47 <-> 48
        if other.miss_m < fit.miss_m:
            fit = other
    if fit.miss_m > tol_m:
        raise ValueError(
            f"{utmmap1} {utmmap2} {utmmap3}: no candidate within {tol_m:.0f} m of the 1:50,000 sheet"
        )
    return fit


def sheet_bounds(utmmap1, utmmap2, utmmap3, utmmap4, utmscale):
    """Return (zone, xmin, ymin, xmax, ymax) in Indian 1975 / UTM metres.

    Example: ``sheet_bounds('5638', '2', '2606', '00', '4000')`` ->
    ``(48, 326000.0, 1606000.0, 328000.0, 1608000.0)``.
    """
    scale = int(float(utmscale))
    if scale == 5000:
        raise ValueError(
            "UTMSCALE 5000 rows (UTMMAP3 '0000', 3-digit UTMMAP4) are not UTM cadastral "
            "sheets; their numbering is undocumented here. Locate them at 1:50,000-sheet "
            "level with series_sheet_lonlat(UTMMAP1, UTMMAP2)."
        )
    if scale not in SHEET_SIZE_M:
        raise ValueError(f"UTMSCALE must be 4000, 2000, 1000 or 500, got {utmscale!r}")
    k = int(utmmap4)
    per_side = SUBSHEETS_PER_SIDE[scale]
    if scale == 4000:
        if k != 0:
            raise ValueError("UTMMAP4 must be 00 at 1:4,000")
    elif not 1 <= k <= per_side**2:
        raise ValueError(f"UTMMAP4 must be 01-{per_side**2:02d} at 1:{scale}, got {utmmap4!r}")
    fit = locate_4000(utmmap1, utmmap2, utmmap3)
    size = SHEET_SIZE_M[scale]
    row, col = (0, 0) if scale == 4000 else divmod(k - 1, per_side)  # row 0 = northern row
    xmin = fit.e_ll + col * size
    ymax = fit.n_ll + 2000.0 - row * size
    return fit.zone, xmin, ymax - size, xmin + size, ymax


def sheet_centroid(utmmap1, utmmap2, utmmap3, utmmap4, utmscale, wgs84=False):
    """Centre of the sheet: (zone, easting, northing) in Indian 1975 UTM, or
    (lon, lat) in WGS84 degrees if ``wgs84=True``."""
    zone, x0, y0, x1, y1 = sheet_bounds(utmmap1, utmmap2, utmmap3, utmmap4, utmscale)
    cx, cy = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
    if wgs84:
        return to_wgs84_lonlat(cx, cy, zone)
    return zone, cx, cy

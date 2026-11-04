"""Distances between sheet centres for the RQ1 samples (round 13g, 2026-11-03).

- `nearest_km`: great-circle distance (spherical Earth, mean radius 6,371.0088 km) from each query
  point to the nearest reference point. Used for every buffer rule ("centre at least 5 km from every
  treated sheet centre"). Exact on the sphere; the sphere differs from WGS84 by under 0.5%.
- `planar_km`: x, y in km on a local equirectangular plane with one reference latitude per province
  (the mean of its sheets' centre latitudes). Used only to shift placebo footprints within a province,
  which needs a plane; over a province's span (under 2 degrees of latitude) the scale error is under 1%.

Before round 13g each sheet's x used its own latitude (lon * 111.32 * cos(lat_i)), which is not a
projection: east-west differences between sheets at different latitudes were off by several km.
"""

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

R_KM = 6371.0088


def unit_xyz(lon, lat):
    lo, la = np.radians(np.asarray(lon, float)), np.radians(np.asarray(lat, float))
    return np.c_[np.cos(la) * np.cos(lo), np.cos(la) * np.sin(lo), np.sin(la)]


def nearest_km(ref_lon, ref_lat, lon, lat):
    """Great-circle km from each (lon, lat) to the nearest (ref_lon, ref_lat)."""
    chord = cKDTree(unit_xyz(ref_lon, ref_lat)).query(unit_xyz(lon, lat))[0]
    return 2 * R_KM * np.arcsin(np.clip(chord / 2, 0, 1))


def centres(d):
    return (d["lon0"] + d["lon1"]) / 2, (d["lat0"] + d["lat1"]) / 2


def dist_to_treated(p, treated_mask):
    """Great-circle km from every sheet centre in `p` to the nearest centre where `treated_mask` holds."""
    lon, lat = centres(p)
    m = np.asarray(treated_mask, bool)
    return nearest_km(lon[m], lat[m], lon, lat)


def planar_km(d):
    """(x, y) km per sheet centre on a plane with one reference latitude per province."""
    lon, lat = centres(d)
    ref = lat.groupby(d["province"]).transform("mean")
    return pd.Series(lon * 111.32 * np.cos(np.radians(ref)), index=d.index), pd.Series(lat * 110.57, index=d.index)

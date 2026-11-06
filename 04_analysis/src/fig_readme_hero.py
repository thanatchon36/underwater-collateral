"""README banner: Figure 2 of the paper (2011 flood share and official land value by sheet) restyled.

Same sample, variables and colour limits as fig_maps() in fig_appraisal_flood.py. Differences, all
presentational: each sheet is painted at its true footprint rather than as a fixed-size marker, the
aspect ratio is corrected for latitude, the value scale is labelled in baht rather than log points,
and province outlines and place names are added for orientation. Descriptive only, nothing causal.

Input:  03_data/processed/sheet_panel.csv.gz, sheet_landcover_basin.csv.gz (via fig_appraisal_flood.load)
        03_data/raw/admin_boundaries/cod_ab_tha/tha_admin_boundaries.gdb.zip
Output: docs/assets/hero_flood_value.png (1600 x 800)
Fonts:  Fira Sans if installed (SIL OFL, Google Fonts), otherwise DejaVu Sans.

Run: .venv/bin/python -I 04_analysis/src/fig_readme_hero.py
"""

import io
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script directory
from fig_appraisal_flood import BASIN, Y, load  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/assets/hero_flood_value.png"
ADMIN = ROOT / "03_data/raw/admin_boundaries/cod_ab_tha/tha_admin_boundaries.gdb.zip"

WIDTH, HEIGHT, SUPERSAMPLE, CORNER = 1600, 800, 2, 28
LON, LAT = (99.2, 101.8), (13.4, 17.5)  # the paper's figure crops to the same latitudes
CELL = 0.0045  # degrees; slightly finer than a 500 m urban sheet
BG, INK, MUTED, FAINT, LINE = "#0a1626", "#f2f6fb", "#a9b8ca", "#74859b", "#2c3e55"
ACCENT_WATER, ACCENT_VALUE = "#5fd0f3", "#ffb45c"

# Low end sits just above the background so that the sampled area stays visible.
WATER = LinearSegmentedColormap.from_list(
    "water", ["#16283f", "#17456f", "#1a76ad", "#35b4e3", "#a9ecff"])
VALUE = LinearSegmentedColormap.from_list(
    "value", ["#1d2438", "#54263f", "#a33a33", "#ea7b2b", "#ffc765", "#fff4cf"])

CITIES = {  # name: (lon, lat, label dx, label dy), city coordinates; offsets in degrees
    "Phitsanulok": (100.26, 16.82, 0.42, 0.20),
    "Nakhon Sawan": (100.12, 15.70, -0.86, 0.16),
    "Ayutthaya": (100.57, 14.35, 0.58, 0.20),
    "Bangkok": (100.52, 13.75, 0.45, -0.09),
}


def paint(d, col) -> np.ndarray:
    """Rasterise one value per sheet at its footprint; 2 km sheets first, 500 m sheets on top."""
    nx, ny = int((LON[1] - LON[0]) / CELL), int((LAT[1] - LAT[0]) / CELL)
    grid = np.full((ny, nx), np.nan)
    d = d.sort_values("scale", ascending=False)
    x0 = np.clip(((d["lon0"].to_numpy() - LON[0]) / CELL).round().astype(int), 0, nx)
    x1 = np.clip(((d["lon1"].to_numpy() - LON[0]) / CELL).round().astype(int), 0, nx)
    y0 = np.clip(((d["lat0"].to_numpy() - LAT[0]) / CELL).round().astype(int), 0, ny)
    y1 = np.clip(((d["lat1"].to_numpy() - LAT[0]) / CELL).round().astype(int), 0, ny)
    for a, b, c, e, v in zip(x0, x1, y0, y1, d[col].to_numpy()):
        grid[c:max(e, c + 1), a:max(b, a + 1)] = v
    return grid


def draw_map(fig, rect, grid, cmap, vmin, vmax, outlines, title, subtitle, accent, cities):
    ax = fig.add_axes(rect)
    ax.set_facecolor(BG)
    outlines.boundary.plot(ax=ax, color=LINE, linewidth=0.55, zorder=1)
    ax.imshow(grid, origin="lower", extent=(*LON, *LAT), cmap=cmap, vmin=vmin, vmax=vmax,
              interpolation="nearest", zorder=2)
    outlines.boundary.plot(ax=ax, color="#ffffff", alpha=0.10, linewidth=0.45, zorder=3)
    ax.set(xlim=LON, ylim=LAT, xticks=[], yticks=[], xlabel="", ylabel="")  # geopandas labels axes from the CRS
    ax.set_aspect(1 / np.cos(np.radians(sum(LAT) / 2)))
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(0, 1.052, title, transform=ax.transAxes, color=INK, fontsize=15.5, fontweight="semibold")
    ax.text(0, 1.018, subtitle, transform=ax.transAxes, color=accent, fontsize=10.5)
    for name in cities:
        lon, lat, dx, dy = CITIES[name]
        ax.plot([lon, lon + dx * 0.9], [lat, lat + dy * 0.9], color=INK, lw=0.7, alpha=0.8, zorder=5)
        ax.plot(lon, lat, "o", ms=4, mfc="none", mec=INK, mew=0.9, zorder=5)
        ax.text(lon + dx, lat + dy, name, color=INK, fontsize=10.5, va="center",
                ha="left" if dx > 0 else "right", zorder=5)
    return ax


def text_block(fig, x, top, lines, leading, **kwargs):
    """One text object per line: matplotlib's multi-line leading varies with each line's glyphs."""
    for i, line in enumerate(lines):
        fig.text(x, top - i * leading, line, va="baseline", **kwargs)


def colourbar(fig, rect, cmap, vmin, vmax, ticks, labels):
    cax = fig.add_axes(rect)
    cax.imshow(np.linspace(0, 1, 512)[None, :], aspect="auto", cmap=cmap, extent=(vmin, vmax, 0, 1))
    cax.set(yticks=[], xticks=ticks, xticklabels=labels, xlim=(vmin, vmax))
    cax.tick_params(axis="x", length=3, width=0.7, color=MUTED, labelcolor=MUTED, labelsize=10, pad=3)
    for s in cax.spines.values():
        s.set_visible(False)


def main() -> None:
    for path in font_manager.findSystemFonts():
        if "FiraSans" in Path(path).name:
            font_manager.fontManager.addfont(path)
    plt.rcParams["font.family"] = ["Fira Sans", "DejaVu Sans"]

    d = load()
    n_sheets, n_parcels = len(d), int(d["n_parcels"].sum())
    water = paint(d, "gfd_flood_share")
    value = paint(d, Y)
    vmin, vmax = np.nanpercentile(d[Y], [2, 98])  # as in the paper's figure

    adm1 = gpd.read_file(ADMIN, layer="tha_admin1")
    outlines = adm1.cx[LON[0] - 1:LON[1] + 1, LAT[0] - 1:LAT[1] + 1]

    fig = plt.figure(figsize=(WIDTH / 100, HEIGHT / 100), dpi=100, facecolor=BG)
    h = 0.775
    w = h * (HEIGHT / WIDTH) * (LON[1] - LON[0]) * np.cos(np.radians(sum(LAT) / 2)) / (LAT[1] - LAT[0])
    y = 0.115
    x1, x2 = 0.405, 0.405 + w + 0.055

    ax = draw_map(fig, [x1, y, w, h], water, WATER, 0, 1, outlines, "Share of sheet flooded",
                  "2011 flood, satellite-detected", ACCENT_WATER, ["Phitsanulok", "Nakhon Sawan", "Ayutthaya"])
    ax.plot(100.52, 13.75, "o", ms=4, mfc="none", mec=INK, mew=0.9, zorder=6)
    ax.annotate("Bangkok: the low share reflects\nurban under-detection by\noptical satellites, not an\nabsence of flooding",
                xy=(100.55, 13.75), xytext=(101.02, 13.72), color=MUTED, fontsize=9, linespacing=1.25,
                va="center", arrowprops=dict(arrowstyle="-", color=INK, lw=0.7, shrinkA=2, shrinkB=2), zorder=6)
    km100 = 100 / (111.32 * np.cos(np.radians(sum(LAT) / 2)))  # degrees of longitude in 100 km
    ax.plot([99.3, 99.3 + km100], [13.55, 13.55], color=MUTED, lw=1.2, solid_capstyle="butt")
    ax.text(99.3, 13.61, "100 km", color=MUTED, fontsize=9.5, va="bottom")

    draw_map(fig, [x2, y, w, h], value, VALUE, vmin, vmax, outlines, "Official land value",
             "Baht per square wah, round 2023–26, log scale", ACCENT_VALUE, ["Phitsanulok", "Nakhon Sawan", "Bangkok"])

    bar_y, bar_h = 0.062, 0.0125
    colourbar(fig, [x1, bar_y, w, bar_h], WATER, 0, 1, [0, .25, .5, .75, 1], ["0%", "25%", "50%", "75%", "100%"])
    baht = [100, 1000, 10000]
    colourbar(fig, [x2, bar_y, w, bar_h], VALUE, vmin, vmax, np.log(baht),
              ["฿100", "฿1,000", "฿10,000"])

    # Left column
    left = 0.042
    fig.text(left, 0.845, "UNDERWATER COLLATERAL", color=ACCENT_WATER, fontsize=13.5, fontweight="semibold")
    text_block(fig, left, 0.745, ["Where the 2011 flood", "reached, and where", "land is valued"], 0.085,
               color=INK, fontsize=39, fontweight="semibold")
    text_block(fig, left, 0.472, ["How flood risk reaches bank capital", "in Thailand, from flood maps through",
                                  "official land values to a reverse", "stress test."], 0.0445,
               color=MUTED, fontsize=16.5)
    fig.add_artist(plt.Line2D([left, left + 0.30], [0.262, 0.262], color=LINE, lw=1))
    fig.text(left, 0.195, f"{n_sheets:,}", color=INK, fontsize=25, fontweight="semibold")
    fig.text(left, 0.158, "cadastral sheets", color=MUTED, fontsize=12)
    fig.text(left + 0.15, 0.195, f"{n_parcels / 1e6:.1f} million", color=INK, fontsize=25, fontweight="semibold")
    fig.text(left + 0.15, 0.158, "parcels, Chao Phraya basin", color=MUTED, fontsize=12)
    text_block(fig, left, 0.088, ["Descriptive, not causal. Treasury Department official land values;",
                                  "Global Flood Database event DFO 3850 (Tellman et al. 2021)."], 0.027,
               color=FAINT, fontsize=9.5)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100 * SUPERSAMPLE, facecolor=BG)
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf).convert("RGB").resize((WIDTH, HEIGHT), Image.LANCZOS)

    mask = Image.new("L", (WIDTH * 4, HEIGHT * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, WIDTH * 4 - 1, HEIGHT * 4 - 1), CORNER * 4, fill=255)
    img.putalpha(mask.resize((WIDTH, HEIGHT), Image.LANCZOS))
    img.save(OUT, optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1e6:.2f} MB); "
          f"{n_sheets:,} sheets, {n_parcels:,} parcels, value limits {np.exp(vmin):,.0f}-{np.exp(vmax):,.0f} baht")


if __name__ == "__main__":
    main()

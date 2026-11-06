"""README banner and social-media image: Figure 2 of the paper restyled.

Figure 2 (2011 flood share and official land value by cadastral sheet, Chao Phraya basin) is
re-drawn from the same sample, variables and colour limits as fig_maps() in fig_appraisal_flood.py.
The differences are presentational: each sheet is painted at its true footprint rather than as a
fixed-size marker, the aspect ratio is corrected for latitude, the value scale is labelled in baht
rather than log points, and province outlines and place names are added for orientation.
Descriptive only, nothing causal.

Input:  03_data/processed/sheet_panel.csv.gz, sheet_landcover_basin.csv.gz (via fig_appraisal_flood.load)
        03_data/raw/admin_boundaries/cod_ab_tha/tha_admin_boundaries.gdb.zip
Output: docs/assets/hero_flood_value.png           1600 x 800, README banner (rounded corners)
        docs/assets/hero_flood_value_portrait.png  2160 x 2700 (4:5), for LinkedIn and similar feeds
Fonts:  Fira Sans if installed (SIL OFL, Google Fonts), otherwise DejaVu Sans.

Run: .venv/bin/python -I 04_analysis/src/fig_readme_hero.py
"""

import io
import logging
import sys
import warnings
from pathlib import Path

import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import font_manager, patheffects  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script directory
from fig_appraisal_flood import Y, load  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "docs/assets"
ADMIN = ROOT / "03_data/raw/admin_boundaries/cod_ab_tha/tha_admin_boundaries.gdb.zip"
URL = "thanatchon36.github.io/underwater-collateral"

LON, LAT = (99.2, 101.8), (13.4, 17.5)  # the paper's figure crops to the same latitudes
COS = float(np.cos(np.radians(sum(LAT) / 2)))  # longitude shrink at the mid latitude
CELL_BANNER, CELL_PORTRAIT = 0.0045, 0.0015  # degrees; a 500 m urban sheet is about 0.0047 wide
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
BANNER_NOTE = "Bangkok: the low share reflects\nurban under-detection by\noptical satellites, not an\nabsence of flooding"
PORTRAIT_NOTE = ["Bangkok: low share", "reflects urban", "under-detection by", "optical satellites,",
                 "not an absence", "of flooding"]
LEFT_TITLE, LEFT_SUB = "Share of sheet flooded", "2011 flood, satellite-detected"
RIGHT_TITLE, RIGHT_SUB = "Official land value", "Baht per square wah, round 2023–26, log scale"
BAHT_TICKS = [100, 1000, 10000]


def paint(d, col, cell) -> np.ndarray:
    """Rasterise one value per sheet at its footprint; 2 km sheets first, 500 m sheets on top."""
    nx, ny = int((LON[1] - LON[0]) / cell), int((LAT[1] - LAT[0]) / cell)
    grid = np.full((ny, nx), np.nan)
    d = d.sort_values("scale", ascending=False)
    x0 = np.clip(((d["lon0"].to_numpy() - LON[0]) / cell).round().astype(int), 0, nx)
    x1 = np.clip(((d["lon1"].to_numpy() - LON[0]) / cell).round().astype(int), 0, nx)
    y0 = np.clip(((d["lat0"].to_numpy() - LAT[0]) / cell).round().astype(int), 0, ny)
    y1 = np.clip(((d["lat1"].to_numpy() - LAT[0]) / cell).round().astype(int), 0, ny)
    for a, b, c, e, v in zip(x0, x1, y0, y1, d[col].to_numpy()):
        grid[c:max(e, c + 1), a:max(b, a + 1)] = v
    return grid


def map_box(width, height, w=None, h=None):
    """Figure-fraction (w, h) of a map box with the right aspect, given its width or its height."""
    ratio = (LAT[1] - LAT[0]) / ((LON[1] - LON[0]) * COS)  # map height over width, in pixels
    if h is None:
        return w, w * width / height * ratio
    return h * height / width / ratio, h


def halo(width):
    """A background-coloured outline that keeps text legible over the map; none if width is 0."""
    return [patheffects.withStroke(linewidth=width, foreground=BG)] if width else None


def draw_map(fig, rect, grid, cmap, vmin, vmax, outlines, title, subtitle, accent, cities,
             title_fs=15.5, sub_fs=10.5, city_fs=10.5, title_y=1.052, sub_y=1.018, offsets=None, text_halo=0):
    ax = fig.add_axes(rect)
    ax.set_facecolor(BG)
    outlines.boundary.plot(ax=ax, color=LINE, linewidth=0.55, zorder=1)
    ax.imshow(grid, origin="lower", extent=(*LON, *LAT), cmap=cmap, vmin=vmin, vmax=vmax,
              interpolation="nearest", zorder=2)
    outlines.boundary.plot(ax=ax, color="#ffffff", alpha=0.10, linewidth=0.45, zorder=3)
    ax.set(xlim=LON, ylim=LAT, xticks=[], yticks=[], xlabel="", ylabel="")  # geopandas labels axes from the CRS
    ax.set_aspect(1 / COS)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(0, title_y, title, transform=ax.transAxes, color=INK, fontsize=title_fs, fontweight="semibold")
    ax.text(0, sub_y, subtitle, transform=ax.transAxes, color=accent, fontsize=sub_fs)
    for name in cities:
        lon, lat, dx, dy = CITIES[name]
        if offsets and name in offsets:
            dx, dy = offsets[name]
        ax.plot([lon, lon + dx * 0.9], [lat, lat + dy * 0.9], color=INK, lw=0.7, alpha=0.8, zorder=5)
        ax.plot(lon, lat, "o", ms=4, mfc="none", mec=INK, mew=0.9, zorder=5)
        ax.text(lon + dx, lat + dy, name, color=INK, fontsize=city_fs, va="center",
                ha="left" if dx > 0 else "right", zorder=5, path_effects=halo(text_halo))
    return ax


def bangkok_note(ax, text, xytext, fontsize=9, text_halo=0) -> None:
    lon, lat = CITIES["Bangkok"][:2]
    ax.plot(lon, lat, "o", ms=4, mfc="none", mec=INK, mew=0.9, zorder=6)
    ax.annotate(text, xy=(lon + 0.03, lat), xytext=xytext, color=MUTED, fontsize=fontsize,
                linespacing=1.25, va="center", path_effects=halo(text_halo),
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7, shrinkA=2, shrinkB=2), zorder=6)


def bangkok_note_lines(ax, lines, lon_text, lat_top, step, fontsize, text_halo) -> None:
    """The same note, one text object per line so that the leading is even at large sizes."""
    lon, lat = CITIES["Bangkok"][:2]
    ax.plot(lon, lat, "o", ms=4, mfc="none", mec=INK, mew=0.9, zorder=6)
    ax.plot([lon + 0.03, lon_text - 0.03], [lat, lat], color=INK, lw=0.7, zorder=6)
    for i, line in enumerate(lines):
        ax.text(lon_text, lat_top - i * step, line, color=MUTED, fontsize=fontsize, va="center", zorder=6,
                path_effects=halo(text_halo))


def scale_bar(ax, fontsize=9.5) -> None:
    km100 = 100 / (111.32 * COS)  # degrees of longitude in 100 km
    ax.plot([99.3, 99.3 + km100], [13.55, 13.55], color=MUTED, lw=1.2, solid_capstyle="butt")
    ax.text(99.3, 13.61, "100 km", color=MUTED, fontsize=fontsize, va="bottom")


def text_block(fig, x, top, lines, leading, **kwargs):
    """One text object per line: matplotlib's multi-line leading varies with each line's glyphs."""
    for i, line in enumerate(lines):
        fig.text(x, top - i * leading, line, va="baseline", **kwargs)


def colourbar(fig, rect, cmap, vmin, vmax, ticks, labels, labelsize):
    cax = fig.add_axes(rect)
    cax.imshow(np.linspace(0, 1, 512)[None, :], aspect="auto", cmap=cmap, extent=(vmin, vmax, 0, 1))
    cax.set(yticks=[], xticks=ticks, xticklabels=labels, xlim=(vmin, vmax))
    cax.tick_params(axis="x", length=3, width=0.7, color=MUTED, labelcolor=MUTED, labelsize=labelsize, pad=3)
    for s in cax.spines.values():
        s.set_visible(False)


def colourbars(fig, left_rect, right_rect, vlim, labelsize=10):
    colourbar(fig, left_rect, WATER, 0, 1, [0, .25, .5, .75, 1], ["0%", "25%", "50%", "75%", "100%"], labelsize)
    colourbar(fig, right_rect, VALUE, *vlim, np.log(BAHT_TICKS), [f"฿{b:,}" for b in BAHT_TICKS], labelsize)


def to_image(fig, out_w, out_h, render_dpi) -> Image.Image:
    """Render above the output size and shrink, which anti-aliases the sheet cells."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=render_dpi, facecolor=BG)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB").resize((out_w, out_h), Image.LANCZOS)


def rounded(img: Image.Image, radius: int) -> Image.Image:
    w, h = img.size
    mask = Image.new("L", (w * 4, h * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w * 4 - 1, h * 4 - 1), radius * 4, fill=255)
    img.putalpha(mask.resize((w, h), Image.LANCZOS))
    return img


def render_landscape(d, vlim, outlines, stats) -> Image.Image:
    """1600 x 800 README banner: text column on the left, the two maps on the right."""
    W, H = 1600, 800
    grids = {"water": paint(d, "gfd_flood_share", CELL_BANNER), "value": paint(d, Y, CELL_BANNER)}
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor=BG)
    w, h = map_box(W, H, h=0.775)
    y, x1 = 0.115, 0.405
    x2 = x1 + w + 0.055

    ax = draw_map(fig, [x1, y, w, h], grids["water"], WATER, 0, 1, outlines, LEFT_TITLE, LEFT_SUB,
                  ACCENT_WATER, ["Phitsanulok", "Nakhon Sawan", "Ayutthaya"])
    bangkok_note(ax, BANNER_NOTE, (101.02, 13.72))
    scale_bar(ax)
    draw_map(fig, [x2, y, w, h], grids["value"], VALUE, *vlim, outlines, RIGHT_TITLE, RIGHT_SUB,
             ACCENT_VALUE, ["Phitsanulok", "Nakhon Sawan", "Bangkok"])
    colourbars(fig, [x1, 0.062, w, 0.0125], [x2, 0.062, w, 0.0125], vlim)

    left = 0.042
    fig.text(left, 0.845, "UNDERWATER COLLATERAL", color=ACCENT_WATER, fontsize=13.5, fontweight="semibold")
    text_block(fig, left, 0.745, ["Where the 2011 flood", "reached, and where", "land is valued"], 0.085,
               color=INK, fontsize=39, fontweight="semibold")
    text_block(fig, left, 0.472, ["How flood risk reaches bank capital", "in Thailand, from flood maps through",
                                  "official land values to a reverse", "stress test."], 0.0445,
               color=MUTED, fontsize=16.5)
    fig.add_artist(plt.Line2D([left, left + 0.30], [0.262, 0.262], color=LINE, lw=1))
    (n_sheets, s_sheets), (n_parcels, s_parcels) = stats[0], stats[1]
    fig.text(left, 0.195, n_sheets, color=INK, fontsize=25, fontweight="semibold")
    fig.text(left, 0.158, s_sheets, color=MUTED, fontsize=12)
    fig.text(left + 0.15, 0.195, n_parcels, color=INK, fontsize=25, fontweight="semibold")
    fig.text(left + 0.15, 0.158, f"{s_parcels}, Chao Phraya basin", color=MUTED, fontsize=12)
    text_block(fig, left, 0.088, ["Descriptive, not causal. Treasury Department official land values;",
                                  "Global Flood Database event DFO 3850 (Tellman et al. 2021)."], 0.027,
               color=FAINT, fontsize=9.5)
    return rounded(to_image(fig, W, H, 200), 28)


def render_portrait(d, vlim, outlines, stats) -> Image.Image:
    """2160 x 2700 (4:5) image for feeds: large type, so that it reads at phone width."""
    W, H = 1080, 1350  # design size; rendered above twice this and shrunk
    grids = {"water": paint(d, "gfd_flood_share", CELL_PORTRAIT), "value": paint(d, Y, CELL_PORTRAIT)}
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor=BG)
    left = 0.045
    w, h = map_box(W, H, w=0.424)
    x1, y = left, 0.178
    x2 = 1 - left - w

    fig.text(left, 0.966, "UNDERWATER COLLATERAL", color=ACCENT_WATER, fontsize=17, fontweight="semibold")
    fig.text(1 - left, 0.966, URL, color=MUTED, fontsize=13, ha="right")
    text_block(fig, left, 0.915, ["Where the 2011 flood reached,", "and where land is valued"], 0.055,
               color=INK, fontsize=48, fontweight="semibold")
    fig.text(left, 0.815, "How flood risk reaches bank capital in Thailand", color=MUTED, fontsize=20)

    style = dict(title_fs=21, sub_fs=14.5, city_fs=15, title_y=1.056, sub_y=1.016,
                 offsets={"Nakhon Sawan": (0.62, 0.22)}, text_halo=3)
    ax = draw_map(fig, [x1, y, w, h], grids["water"], WATER, 0, 1, outlines, LEFT_TITLE, LEFT_SUB,
                  ACCENT_WATER, ["Phitsanulok", "Nakhon Sawan", "Ayutthaya"], **style)
    bangkok_note_lines(ax, PORTRAIT_NOTE, 100.97, 14.25, 0.122, fontsize=12.5, text_halo=3)
    scale_bar(ax, fontsize=13)
    draw_map(fig, [x2, y, w, h], grids["value"], VALUE, *vlim, outlines, RIGHT_TITLE, RIGHT_SUB,
             ACCENT_VALUE, ["Phitsanulok", "Nakhon Sawan", "Bangkok"], **style)
    colourbars(fig, [x1, 0.160, w, 0.012], [x2, 0.160, w, 0.012], vlim, labelsize=14)

    fig.add_artist(plt.Line2D([left, 1 - left], [0.127, 0.127], color=LINE, lw=1))
    for x, (number, label) in zip([left, left + 0.30, left + 0.60], stats):
        fig.text(x, 0.094, number, color=INK, fontsize=33, fontweight="semibold")
        fig.text(x, 0.070, label, color=MUTED, fontsize=15)
    text_block(fig, left, 0.040, ["Descriptive, not causal. Each cell is one cadastral sheet (2 km rural, "
                                  "500 m urban); the 2011 flood share is from MODIS at 250 m.",
                                  "Sources: Treasury Department official land values, round 2023–26; "
                                  "Global Flood Database event DFO 3850 (Tellman et al. 2021)."], 0.017,
               color=FAINT, fontsize=11.5)
    return to_image(fig, 2 * W, 2 * H, 400)


def main() -> None:
    logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)  # weight-fallback chatter
    warnings.filterwarnings("ignore", message=".*organizePolygons.*")
    for path in font_manager.findSystemFonts():
        if "FiraSans" in Path(path).name:
            font_manager.fontManager.addfont(path)
    plt.rcParams["font.family"] = ["Fira Sans", "DejaVu Sans"]

    d = load()
    n_sheets, n_parcels, n_prov = len(d), int(d["n_parcels"].sum()), d["province"].nunique()
    stats = [(f"{n_sheets:,}", "cadastral sheets"), (f"{n_parcels / 1e6:.1f} million", "parcels"),
             (f"{n_prov}", "provinces, Chao Phraya basin")]
    vlim = tuple(np.nanpercentile(d[Y], [2, 98]))  # as in the paper's figure

    adm1 = gpd.read_file(ADMIN, layer="tha_admin1")
    outlines = adm1.cx[LON[0] - 1:LON[1] + 1, LAT[0] - 1:LAT[1] + 1]

    for name, render in [("hero_flood_value.png", render_landscape),
                         ("hero_flood_value_portrait.png", render_portrait)]:
        out = ASSETS / name
        img = render(d, vlim, outlines, stats)
        img.save(out, optimize=True)
        print(f"wrote {out.relative_to(ROOT)} {img.size[0]}x{img.size[1]} ({out.stat().st_size / 1e6:.2f} MB)")
    print(f"{n_sheets:,} sheets, {n_parcels:,} parcels, {n_prov} provinces, "
          f"value limits {np.exp(vlim[0]):,.0f}-{np.exp(vlim[1]):,.0f} baht")


if __name__ == "__main__":
    main()

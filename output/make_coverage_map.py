"""Coverage map of Indonesia for the IFLS analysis.

Colors each kabupaten by the number of IFLS adults in our analysis dataset who live
there. Uses actual sample counts (not just match status) so migrant-tracked
households that ended up outside the original IFLS-13 provinces show up as
small/sparse, while the densely-sampled Java/Sumatra/Bali/Sulsel kab look bold.

Outlines the 13 ORIGINAL IFLS sampling-frame provinces (per RAND documentation):
  Sumatra:    Sumut (12), Sumbar (13), Sumsel (16), Lampung (18)
  Java:       DKI Jakarta (31), Jabar (32), Jateng (33), DIY (34), Jatim (35)
  Other:      Bali (51), NTB (52), Kalsel (63), Sulsel (73)
plus Banten (36) which split off from West Java in 2000 and is effectively in-sample
for split-off households.

Output: output/figures/coverage_map.png
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code" / "data"))
from config import FIGURES as OUT, GADM_PATH, GENERATED  # noqa: E402

OUT.mkdir(parents=True, exist_ok=True)

# Original IFLS-13 sampling-frame provinces (per RAND IFLS documentation), plus
# Banten (36) which split from Jabar (32) in 2000.
IFLS13_PROVS = {12, 13, 16, 18, 31, 32, 33, 34, 35, 36, 51, 52, 63, 73}


def normalize(s: str) -> str:
    if not isinstance(s, str): return ""
    s = s.lower()
    s = re.sub(r"\b(kabupaten|kab\.?|kota|kotamadya|administrasi|provinsi)\b", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def main() -> None:
    # 1. Sample counts per (prov_code, kab name) from the actual analysis dataset
    df = pd.read_parquet(GENERATED / "analysis_dataset.parquet")
    n_per_kab = df.groupby("kab_code").size().rename("n_ifls").reset_index()

    kab_lookup = pd.read_parquet(GENERATED / "kabupaten_polygons.parquet")
    kab_lookup = kab_lookup.merge(n_per_kab, on="kab_code", how="left").fillna({"n_ifls": 0})

    # 2. GADM polygons
    g1 = gpd.read_file(GADM_PATH, layer="ADM_ADM_1").to_crs(4326)
    g2 = gpd.read_file(GADM_PATH, layer="ADM_ADM_2").to_crs(4326)
    g2["kab_norm"] = g2["NAME_2"].map(normalize)
    g2["prov_norm"] = g2["NAME_1"].map(normalize)

    # 3. Build per-(prov_norm, kab_norm) -> sample size dictionary
    kab_lookup["kab_norm"] = kab_lookup.nama_kab.map(normalize)
    kab_lookup["prov_norm"] = kab_lookup.nama_prov.map(normalize)
    sample_lookup = kab_lookup.set_index(["prov_norm", "kab_norm"])["n_ifls"].to_dict()

    g2["n_ifls"] = g2.apply(
        lambda r: sample_lookup.get((r.prov_norm, r.kab_norm), 0), axis=1
    )

    # 4. Identify the 12 fallback kab — get their kab_codes and find their
    #    GADM polygons by (prov_norm, kab_norm). Some won't match (that's the point —
    #    that's why they're fallback). For those, mark the whole province lightly.
    fb_kab = kab_lookup[kab_lookup.match_level == "prov"]
    fb_set = set(zip(fb_kab.prov_norm, fb_kab.kab_norm))
    g2["is_fallback"] = g2.apply(
        lambda r: (r.prov_norm, r.kab_norm) in fb_set, axis=1
    )
    # Provinces hosting fallback kab (for the lighter highlight)
    fb_provs_norm = set(fb_kab.prov_norm)

    # 5. Color scheme: sample size → blue intensity; fallback kab → orange ring
    #    Province outline in green for the 13 original IFLS provinces.
    bins = [0, 1, 50, 200, 500, 1000, 5000]
    bin_colors = ["#f0f0f0", "#dceaf6", "#a8c8e1", "#5a9bcc", "#2c7bb6", "#08519c"]
    bin_labels = ["0", "1–49", "50–199", "200–499", "500–999", "1000+"]
    g2["bin_idx"] = pd.cut(g2.n_ifls, bins=bins, labels=False, include_lowest=True, right=False)
    g2["color"] = g2["bin_idx"].apply(lambda i: bin_colors[int(i)] if pd.notna(i) else bin_colors[0])

    # 6. Plot
    fig, ax = plt.subplots(1, 1, figsize=(15, 7), dpi=140)

    # All GADM kab, colored by sample size
    g2.plot(ax=ax, color=g2["color"], edgecolor="white", linewidth=0.15)

    # Province outlines (light grey)
    g1.boundary.plot(ax=ax, edgecolor="#888", linewidth=0.4)

    # Highlight original IFLS-13 provinces with thick green outline
    g1["prov_norm"] = g1["NAME_1"].map(normalize)
    bps_to_norm = {
        12: "sumaterautara", 13: "sumaterabarat", 16: "sumateraselatan", 18: "lampung",
        31: "dkijakarta", 32: "jawabarat", 33: "jawatengah", 34: "daerahistimewayogyakarta",
        35: "jawatimur", 36: "banten", 51: "bali", 52: "nusatenggarabarat",
        63: "kalimantanselatan", 73: "sulawesiselatan",
    }
    ifls13_norms = set(bps_to_norm.values())
    g1_ifls = g1[g1.prov_norm.isin(ifls13_norms)]
    g1_ifls.boundary.plot(ax=ax, edgecolor="#1d6f42", linewidth=1.5, alpha=0.85)

    # Note: the 12 fallback kab don't appear as separate GADM polygons (that's
    # why they fall back) so they have no visible kab-level geometry on the map.
    # Their adults are still in the analysis, just averaged over the province polygon.

    # Indonesia bounds
    ax.set_xlim(95, 141.5)
    ax.set_ylim(-11.5, 6.5)
    ax.set_aspect("equal")

    # Legend
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    n_kab_in_sample = (g2.n_ifls > 0).sum()
    n_kab_substantial = (g2.n_ifls >= 50).sum()
    n_fb = int(g2.is_fallback.sum())

    # Sample-size legend (color bins)
    legend_elements = []
    for c, lab in zip(bin_colors, bin_labels):
        legend_elements.append(Patch(facecolor=c, edgecolor="#777", linewidth=0.3,
                                     label=f"  {lab} adults"))
    # Outline legend
    outline_elements = [
        Line2D([0], [0], color="#1d6f42", linewidth=1.6,
               label="Original IFLS-13 sampling-frame province (+ Banten)"),
    ]
    leg1 = ax.legend(handles=legend_elements, loc="lower left",
                     title="IFLS adults per kabupaten\n(in pooled IFLS4 + IFLS5 analysis sample)",
                     fontsize=8.5, title_fontsize=9, frameon=True, framealpha=0.95,
                     edgecolor="#cccccc", labelspacing=0.3)
    leg2 = ax.legend(handles=outline_elements, loc="lower right",
                     fontsize=8.5, frameon=True, framealpha=0.95, edgecolor="#cccccc")
    ax.add_artist(leg1)

    # Title and footer
    ax.set_title(
        f"IFLS coverage  —  {n_kab_in_sample} kabupaten with at least 1 sampled adult, "
        f"{n_kab_substantial} with ≥ 50 adults",
        fontsize=13, loc="left", weight="bold", pad=10,
    )
    ax.text(
        0.99, -0.05,
        "IFLS originally sampled 13 provinces (1993; outlined in green; ≈ 83 % of Indonesia's population) plus Banten which split off in 2000.\n"
        "Light blue patches outside the green outline are migrant-tracked households who moved out of the original sampling frame.\n"
        "12 IFLS kabupaten lack a polygon in GADM v4.1 — their adults still enter the analysis but with temperature averaged over the province polygon.\n"
        "Polygons: GADM v4.1. Sample counts: pooled IFLS4 + IFLS5 analysis dataset (n = 60,355).",
        transform=ax.transAxes, ha="right", va="top", fontsize=8.5, color="#555",
    )
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)

    fig.tight_layout()
    out_path = OUT / "coverage_map.png"
    fig.savefig(out_path, bbox_inches="tight", dpi=180)
    print(f"wrote {out_path}")
    print(f"  Kab with ≥1 IFLS adult: {n_kab_in_sample}")
    print(f"  Kab with ≥50 IFLS adults: {n_kab_substantial}")
    print(f"  Fallback kab matched: {n_fb}")
    print()
    print("Sample-size distribution by province:")
    by_prov = df.merge(
        kab_lookup[["kab_code", "nama_prov"]], on="kab_code", how="left"
    ).groupby("nama_prov").size().sort_values(ascending=False)
    print(by_prov.head(30))


if __name__ == "__main__":
    main()

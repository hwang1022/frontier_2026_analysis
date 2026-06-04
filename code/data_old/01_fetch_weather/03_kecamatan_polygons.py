"""Build a clean kecamatan polygon parquet from GADM v4.1 Indonesia.

Source: E:/gadm41_IDN_shp/gadm41_IDN_3.shp
        (or wherever the user has saved it; also tries data/raw/gadm41_IDN/)

GADM's CC_3 column contains the 7-digit BPS kecamatan code, so we can merge
directly to our IFLS analysis_dataset.kec_code with no name-matching.

For the 1.5-2.5% of IFLS kecs not in GADM (mostly post-2014 splits), the
parent kabupaten polygon serves as a fallback at the analysis layer.

Output:
  data/generated/kecamatan_polygons.parquet
    kec_code, kab_code, prov_code, nama_kec, nama_kab, nama_prov,
    centroid_lat, centroid_lon, area_km2, geometry_wkt
"""
from __future__ import annotations

from pathlib import Path
import geopandas as gpd
import pandas as pd

PROJECT = Path(__file__).resolve().parents[2]
OUT = PROJECT / "data" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

CANDIDATE_PATHS = [
    Path("E:/gadm41_IDN_shp/gadm41_IDN_3.shp"),
    PROJECT / "data" / "raw" / "gadm41_IDN" / "gadm41_IDN_3.shp",
]


def find_shp() -> Path:
    for p in CANDIDATE_PATHS:
        if p.exists():
            return p
    raise FileNotFoundError(
        f"Couldn't find GADM kecamatan shapefile. Tried:\n  "
        + "\n  ".join(str(p) for p in CANDIDATE_PATHS)
    )


def main() -> None:
    shp_path = find_shp()
    print(f"loading {shp_path}")
    g = gpd.read_file(shp_path)
    print(f"  rows: {len(g):,}; CRS: {g.crs}")

    # CC_3 is the 7-digit BPS kecamatan code
    g["kec_code"] = pd.to_numeric(g.CC_3, errors="coerce")
    g = g.dropna(subset=["kec_code"]).copy()
    g["kec_code"] = g.kec_code.astype(int)
    # Derive parent kab_code (4-digit), prov_code (2-digit)
    g["kab_code"] = g.kec_code // 1000
    g["prov_code"] = g.kab_code // 100

    # Ensure WGS84 lon/lat
    if g.crs is None:
        g.set_crs(epsg=4326, inplace=True)
    elif g.crs.to_epsg() != 4326:
        g = g.to_crs(epsg=4326)

    # Compute centroid + area (use Mollweide equal-area for area in km^2)
    cen = g.geometry.centroid
    g["centroid_lat"] = cen.y
    g["centroid_lon"] = cen.x
    g_eq = g.to_crs("ESRI:54009")  # World Mollweide (equal-area)
    g["area_km2"] = g_eq.geometry.area / 1e6

    g["nama_kec"] = g.NAME_3
    g["nama_kab"] = g.NAME_2
    g["nama_prov"] = g.NAME_1
    g["geometry_wkt"] = g.geometry.to_wkt()

    out = pd.DataFrame(g.drop(columns="geometry"))[[
        "kec_code", "kab_code", "prov_code",
        "nama_kec", "nama_kab", "nama_prov",
        "centroid_lat", "centroid_lon", "area_km2", "geometry_wkt",
    ]].drop_duplicates("kec_code").sort_values("kec_code").reset_index(drop=True)

    out.to_parquet(OUT / "kecamatan_polygons.parquet", index=False)
    print(f"\nwrote {len(out):,} kec polygons to {OUT / 'kecamatan_polygons.parquet'}")
    print(out[["kec_code","kab_code","prov_code","nama_kec","area_km2"]].head(8).to_string())

    # Quick coverage check vs IFLS data
    ind_path = OUT / "individuals.parquet"
    if ind_path.exists():
        ind = pd.read_parquet(ind_path)
        polys = set(out.kec_code.unique())
        for w in ("IFLS4", "IFLS5"):
            sub_kecs = set(ind[ind.wave == w].kec_code.dropna().astype(int).unique())
            covered = sub_kecs & polys
            print(f"\n{w} kecamatan IFLS coverage: {len(covered):,} of {len(sub_kecs):,} "
                  f"({100*len(covered)/len(sub_kecs):.1f}%)")


if __name__ == "__main__":
    main()

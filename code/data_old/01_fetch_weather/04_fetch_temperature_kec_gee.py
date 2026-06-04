"""Pull ERA5-Land daily polygon-mean temperature for every IFLS kecamatan over
the IFLS4 + IFLS5 fielding windows.

Same approach as 03_fetch_temperature_gee.py but at kecamatan resolution
(6,648 polygons vs 303 kabupaten). Polygons from
data/generated/kecamatan_polygons.parquet (built by 02b_kecamatan_polygons.py
from GADM v4.1, where CC_3 = BPS 7-digit kec code).

Why kecamatan: spatial resolution gain for big or mountainous kabupaten;
exact polygon-level merge to IFLS HHs via kec_code; fallback to kabupaten
mean for ~1.5-2.5% of IFLS HHs whose kec_code isn't in GADM.

Approach
--------
For each wave's fielding window (30 days BEFORE earliest interview to 7 days
AFTER latest), run ONE GEE reduceRegions over a batch of kecamatan polygons
per 15-day sub-window. With 6,648 polygons we batch the polygons too (~1500
per call) so total payload stays under getInfo limits.

Variables (ERA5-Land native ~9km, polygon-mean):
  tmean_c, tmax_c, tmin_c, dewp_c, rh_pct, precip_mm, heat_idx_c
  (same as kabupaten file for drop-in compatibility)

Output: data/generated/daily_temperature_kec.parquet  (long, ~7.7M rows)

To run from terminal:
    cd "C:/Users/jingy/Dropbox/frontier_2026"
    python individual_folders/jingyao/code/data/20_fetch_temperature_kec_gee.py

Prerequisites:
  - earthengine-api installed: pip install earthengine-api
  - GEE auth: run `earthengine authenticate` once if not already
  - kecamatan_polygons.parquet exists (run 02b first)
  - individuals.parquet exists (run 01 first)
"""
from __future__ import annotations

import math
import os
import time
from datetime import timedelta
from pathlib import Path

import ee
import pandas as pd
import shapely.wkt

PROJECT = Path(__file__).resolve().parents[2]
OUT = PROJECT / "data" / "generated"
TMP = OUT / "_tmp_temperature_kec"


def init_gee() -> None:
    """Initialise GEE. Uses project ID from env or .env file."""
    env_path = Path("C:/Users/jingy/Dropbox/solar panel/.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("GEE_PROJECT_ID="):
                os.environ["GEE_PROJECT_ID"] = line.split("=", 1)[1].strip()
    project_id = os.environ.get("GEE_PROJECT_ID")
    if not project_id:
        raise RuntimeError(
            "GEE_PROJECT_ID not set. Add it to env or .env file, "
            "or run: ee.Initialize(project='your-project-id')"
        )
    ee.Initialize(project=project_id)


def shapely_to_ee(g) -> ee.Geometry:
    # Simplify to ~0.01° (~1 km) — finer than for kabupaten because kecamatan
    # are smaller polygons; preserves polygon-mean integrity at ERA5's 9 km grid.
    g = g.simplify(0.01, preserve_topology=True)
    return ee.Geometry(g.__geo_interface__, opt_geodesic=False, opt_evenOdd=True)


def build_polygon_collection(kec_chunk: pd.DataFrame) -> ee.FeatureCollection:
    feats = []
    for r in kec_chunk.itertuples(index=False):
        g = shapely.wkt.loads(r.geometry_wkt)
        feats.append(ee.Feature(shapely_to_ee(g), {"kec_code": int(r.kec_code)}))
    return ee.FeatureCollection(feats)


BANDS = [
    "temperature_2m",
    "temperature_2m_max",
    "temperature_2m_min",
    "dewpoint_temperature_2m",
    "total_precipitation_sum",
]


def pull_window(start: pd.Timestamp, end_excl: pd.Timestamp,
                fc: ee.FeatureCollection) -> pd.DataFrame:
    """One server-side reduceRegions across N days x M polygons."""
    ic = (
        ee.ImageCollection("ECMWF/ERA5_LAND/DAILY_AGGR")
        .filterDate(start.strftime("%Y-%m-%d"), end_excl.strftime("%Y-%m-%d"))
        .select(BANDS)
    )

    def reduce_one(img):
        means = img.reduceRegions(
            collection=fc, reducer=ee.Reducer.mean(), scale=11132, tileScale=8
        )
        return means.map(lambda f: f.set("date", img.date().format("YYYY-MM-dd")))

    flat = ic.map(reduce_one).flatten()
    info = flat.getInfo()
    rows = []
    for f in info["features"]:
        p = f["properties"]
        if "temperature_2m" not in p:
            continue
        rows.append({
            "kec_code": int(p["kec_code"]),
            "date": p["date"],
            "tmean_c": p["temperature_2m"] - 273.15,
            "tmax_c":  p["temperature_2m_max"] - 273.15,
            "tmin_c":  p["temperature_2m_min"] - 273.15,
            "dewp_c":  p["dewpoint_temperature_2m"] - 273.15,
            "precip_mm": (p.get("total_precipitation_sum") or 0.0) * 1000.0,
        })
    return pd.DataFrame(rows)


def derive_humidity_and_heat_index(df: pd.DataFrame) -> pd.DataFrame:
    """RH from T and Td via Magnus; heat-index via Steadman (NWS) approximation."""
    T = df.tmean_c
    Td = df.dewp_c
    a, b = 17.625, 243.04
    es = lambda x: 6.1094 * (math.e ** ((a * x) / (b + x)))
    df["rh_pct"] = 100.0 * (es(Td) / es(T))
    Tf = T * 9 / 5 + 32
    R = df.rh_pct
    HI_f = (
        -42.379 + 2.04901523 * Tf + 10.14333127 * R
        - 0.22475541 * Tf * R - 6.83783e-3 * Tf**2
        - 5.481717e-2 * R**2 + 1.22874e-3 * Tf**2 * R
        + 8.5282e-4 * Tf * R**2 - 1.99e-6 * Tf**2 * R**2
    )
    HI_f = HI_f.where(Tf >= 80, Tf)
    df["heat_idx_c"] = (HI_f - 32) * 5 / 9
    return df


# Tunable: polygons per reduceRegions call. With 15-day windows that means
# ~15 * POLYGONS_PER_CHUNK features returned per getInfo. Conservative default
# keeps each response well under GEE's 5000-feature soft limit.
POLYGONS_PER_CHUNK = 300
BATCH_DAYS = 15


def main() -> None:
    init_gee()
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)

    kec = pd.read_parquet(OUT / "kecamatan_polygons.parquet")
    kec = kec.dropna(subset=["geometry_wkt"]).reset_index(drop=True)
    print(f"polygons to process: {len(kec):,}")

    ind = pd.read_parquet(OUT / "individuals.parquet")
    w4 = ind[ind.wave == "IFLS4"]
    w5 = ind[ind.wave == "IFLS5"]
    windows = [
        ("IFLS4", w4.interview_date.min() - timedelta(days=30),
                  w4.interview_date.max() + timedelta(days=7)),
        ("IFLS5", w5.interview_date.min() - timedelta(days=30),
                  w5.interview_date.max() + timedelta(days=7)),
    ]
    print("windows:")
    for tag, a, b in windows:
        print(f"  {tag}: {a.date()} -> {b.date()}  ({(b-a).days} days)")

    # Pre-chunk polygons (built once, reused across all date batches)
    n_chunks = (len(kec) + POLYGONS_PER_CHUNK - 1) // POLYGONS_PER_CHUNK
    chunks = [kec.iloc[i*POLYGONS_PER_CHUNK:(i+1)*POLYGONS_PER_CHUNK].reset_index(drop=True)
              for i in range(n_chunks)]
    fcs = [build_polygon_collection(c) for c in chunks]
    print(f"  pre-built {n_chunks} polygon FeatureCollections of "
          f"~{POLYGONS_PER_CHUNK} kecs each")

    all_frames = []
    for tag, start, end in windows:
        out_path = TMP / f"{tag}_daily_temp_kec.parquet"
        if out_path.exists():
            print(f"\n  {tag}: cached at {out_path}")
            all_frames.append(pd.read_parquet(out_path))
            continue

        starts = pd.date_range(start, end, freq=f"{BATCH_DAYS}D")
        n_calls = len(starts) * n_chunks
        print(f"\n  {tag}: {(end-start).days+1} days x {len(kec):,} polygons "
              f"-> {len(starts)} date-batches x {n_chunks} polygon-chunks "
              f"= {n_calls} GEE calls")

        wave_frames = []
        t0 = time.time()
        call = 0
        for di, s in enumerate(starts, 1):
            e_excl = min(s + timedelta(days=BATCH_DAYS), end + timedelta(days=1))
            for ci, fc in enumerate(fcs, 1):
                call += 1
                try:
                    df = pull_window(s, e_excl, fc)
                    wave_frames.append(df)
                except Exception as exc:
                    print(f"    {s.date()}-{e_excl.date()} chunk {ci}/{n_chunks}  "
                          f"ERROR: {exc}; sleeping 30s and retrying")
                    time.sleep(30)
                    df = pull_window(s, e_excl, fc)
                    wave_frames.append(df)
                if call % 10 == 0 or call == n_calls:
                    el = time.time() - t0
                    eta = el / call * (n_calls - call)
                    print(f"    [{call}/{n_calls}] {s.date()}-{e_excl.date()} "
                          f"chunk {ci}/{n_chunks}  elapsed={el:.0f}s  eta={eta:.0f}s "
                          f"rows={len(df)}")
        wave_df = pd.concat(wave_frames, ignore_index=True)
        wave_df.to_parquet(out_path, index=False)
        print(f"  {tag}: wrote {len(wave_df):,} rows to {out_path}")
        all_frames.append(wave_df)

    combined = pd.concat(all_frames, ignore_index=True)
    combined = derive_humidity_and_heat_index(combined)
    combined["date"] = pd.to_datetime(combined.date)
    combined = combined.sort_values(["kec_code", "date"]).reset_index(drop=True)
    out_path = OUT / "daily_temperature_kec.parquet"
    combined.to_parquet(out_path, index=False)
    print(f"\nwrote {len(combined):,} rows to {out_path}")
    print("variable summary (degC / mm):")
    print(combined[["tmean_c", "tmax_c", "tmin_c", "dewp_c", "rh_pct",
                    "precip_mm", "heat_idx_c"]].describe().round(2))


if __name__ == "__main__":
    main()

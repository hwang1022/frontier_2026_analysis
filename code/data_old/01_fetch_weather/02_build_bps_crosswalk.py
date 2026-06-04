"""Build a clean BPS kec/kab/prov crosswalk from IFLS5's Volume 14 file.

Source: E:/IFLS/IFLS5/IFLS5_all_doc/IFLS5_BPS_2014_codes/kec_9899000714.dta
        (the IFLS5 "Volume 14" crosswalk covering BPS codes for 1998, 1999,
        2000, 2007, and 2014)

The source file has 7,212 rows -- one row per (parent, descendant) pair
across the five years. A 2007 kecamatan that later split into three
kecamatan by 2014 appears as 3 rows.

Outputs:
  data/generated/bps_crosswalk_kec.parquet
     Long form, one row per (kecid07, kecid14) pair. Contains both 2007
     and 2014 prov+kab+kec codes + names.
  data/generated/bps_unified_kec.parquet
     Per-kecamatan-IFLS5 lookup keyed by kec_code (7-digit 2014 BPS), with
     a kec_id_unified column = the 2007-parent kecid (lossless cross-wave
     merge key). For 2007 kecs that split, multiple 2014 kecs map back to
     the same 2007 parent.
  data/generated/bps_kab_lookup.parquet
     kab_code (4-digit) -> kab_name + prov_code + prov_name, for table
     labeling.
"""
from __future__ import annotations

from pathlib import Path
import pandas as pd

PROJECT = Path(__file__).resolve().parents[3]
SOURCE = PROJECT / "data" / "raw" / "IFLS" /"IFLS5" / "IFLS5_all_doc" / "IFLS5_BPS_2014_codes" / "kec_9899000714.dta"
OUT = PROJECT / "data" / "generated"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Missing IFLS5 crosswalk file: {SOURCE}\n"
            f"Make sure IFLS5_BPS_2014_codes.zip is extracted."
        )
    d = pd.read_stata(SOURCE, convert_categoricals=False)
    print(f"loaded source: {len(d):,} rows, {len(d.columns)} cols")

    # Subset to 2007 + 2014 columns (our IFLS waves) -- drop 1998/1999/2000
    keep = ["provid07", "provid14", "nmprov2007", "nmprov2014",
            "kabid07",  "kabid14",  "nmkab2007",  "nmkab2014",
            "kecid07",  "kecid14",  "nmkec2007",  "nmkec2014"]
    cw = d[keep].copy()
    cw = cw.rename(columns={
        "nmprov2007": "prov_name_07", "nmprov2014": "prov_name_14",
        "nmkab2007":  "kab_name_07",  "nmkab2014":  "kab_name_14",
        "nmkec2007":  "kec_name_07",  "nmkec2014":  "kec_name_14",
    })
    # Cast IDs to numeric, drop rows missing any of the 2007/2014 codes
    id_cols = ["provid07","provid14","kabid07","kabid14","kecid07","kecid14"]
    for c in id_cols:
        cw[c] = pd.to_numeric(cw[c], errors="coerce")
    cw = cw.dropna(subset=id_cols).copy()
    cw["prov_code_07"] = cw.provid07.astype(int)
    cw["prov_code_14"] = cw.provid14.astype(int)
    cw["kab_code_07"]  = cw.kabid07.astype(int)
    cw["kab_code_14"]  = cw.kabid14.astype(int)
    cw["kec_code_07"]  = cw.kecid07.astype(int)
    cw["kec_code_14"]  = cw.kecid14.astype(int)
    cw = cw.drop(columns=id_cols)

    out_cols = ["prov_code_07","prov_code_14","prov_name_07","prov_name_14",
                "kab_code_07","kab_code_14","kab_name_07","kab_name_14",
                "kec_code_07","kec_code_14","kec_name_07","kec_name_14"]
    cw = cw[out_cols].drop_duplicates().reset_index(drop=True)
    cw.to_parquet(OUT / "bps_crosswalk_kec.parquet", index=False)
    print(f"wrote {OUT / 'bps_crosswalk_kec.parquet'}  ({len(cw):,} kec-pair rows)")

    # ---- Unified IFLS5-keyed lookup ----
    # For each 2014 kec, find the 2007 parent kec (if a 2007 kec split into
    # multiple 2014 kecs, the parent is the same for all children).
    # Some 2014 kecs may map to multiple 2007 parents (unusual mergers);
    # for those, keep the smallest (most common case = no merger).
    parent = (cw.groupby("kec_code_14")
                .agg(kec_id_unified=("kec_code_07", "min"),
                     parent_kab=("kab_code_07", "min"),
                     parent_prov=("prov_code_07", "min"),
                     parent_kec_name=("kec_name_07", "first"),
                     parent_kab_name=("kab_name_07", "first"),
                     parent_prov_name=("prov_name_07", "first"),
                     n_parents=("kec_code_07", "nunique"))
                .reset_index())
    # The unified key: prefer the 2007 parent; if no 2007 parent exists (new kec
    # post-2007), use the 2014 code itself.
    parent["kec_id_unified"] = parent.kec_id_unified.fillna(parent.kec_code_14)
    # Attach 2014 name for context
    name14 = cw[["kec_code_14","kec_name_14","kab_code_14","kab_name_14",
                 "prov_code_14","prov_name_14"]].drop_duplicates("kec_code_14")
    unified = parent.merge(name14, on="kec_code_14", how="left")
    unified.to_parquet(OUT / "bps_unified_kec.parquet", index=False)
    print(f"wrote {OUT / 'bps_unified_kec.parquet'}  ({len(unified):,} IFLS5 kecs)")

    # ---- Kabupaten lookup (4-digit, IFLS5-keyed) ----
    kab = (cw[["kab_code_14","kab_name_14","prov_code_14","prov_name_14"]]
             .drop_duplicates("kab_code_14")
             .rename(columns={"kab_code_14":"kab_code","kab_name_14":"kab_name",
                              "prov_code_14":"prov_code","prov_name_14":"prov_name"})
             .reset_index(drop=True))
    kab.to_parquet(OUT / "bps_kab_lookup.parquet", index=False)
    print(f"wrote {OUT / 'bps_kab_lookup.parquet'}  ({len(kab):,} kabs)")

    # ---- Diagnostics ----
    print(f"\nDiagnostics:")
    # How many 2007 kecs are unchanged?
    same = (cw.kec_code_07 == cw.kec_code_14).sum()
    print(f"  Unchanged 2007 -> 2014 kec pairs: {same:,} of {len(cw):,} ({100*same/len(cw):.1f}%)")
    # How many 2014 kecs trace back to a 2007 parent?
    n_with_parent = unified.kec_id_unified.notna().sum()
    print(f"  IFLS5 kecs with 2007 parent: {n_with_parent:,} of {len(unified):,}")
    # Split kecs (one 2007 -> multiple 2014)
    n_split_parents = (cw.groupby("kec_code_07").kec_code_14.nunique() > 1).sum()
    print(f"  2007 kecs that split into multiple 2014 kecs: {n_split_parents:,}")
    # Verify against IFLS4 unmatched kecs
    try:
        ind = pd.read_parquet(OUT / "individuals.parquet")
        kec4 = set(ind[ind.wave=="IFLS4"].kec_code.dropna().astype(int).unique())
        kec5 = set(ind[ind.wave=="IFLS5"].kec_code.dropna().astype(int).unique())
        cwset_07 = set(cw.kec_code_07.unique())
        cwset_14 = set(cw.kec_code_14.unique())
        print(f"  IFLS4 kecs in crosswalk (as 2007): {len(kec4 & cwset_07):,} of {len(kec4):,} ({100*len(kec4 & cwset_07)/len(kec4):.1f}%)")
        print(f"  IFLS5 kecs in crosswalk (as 2014): {len(kec5 & cwset_14):,} of {len(kec5):,} ({100*len(kec5 & cwset_14)/len(kec5):.1f}%)")
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()

# IFLS Data Summary (post-unpack)

Generated after running `code/data/00_unpack_ifls.py`. All 20 archives extracted to `E:/IFLS/extracted/`.

## 1. Wave coverage and field dates

| Wave  | Field period                | HH (interviewed) | Adult resp (pidlink) | Communities |
|-------|------------------------------|------------------|----------------------|-------------|
| IFLS1 | 1993 (Aug–Jan 1994)          | 7,730            | n/a (no b3a_cov)     | 321 EAs     |
| IFLS2 | 1997 (Aug–Jan 1998)          | 7,538            | n/a                  | 321         |
| IFLS3 | 2000 (Jun–Nov)               | 10,085           | 25,829               | 311         |
| IFLS4 | **2007-07-06 to 2008-08-18** | 12,786           | 29,967               | 313         |
| IFLS5 | **2014-09-06 to 2015-12-18** | 15,160           | 36,391               | 311         |

IFLS4 / IFLS5 carry exact interview day-month-year per book (`b*_time.dta` in IFLS5; `ivwday1/ivwmth1/ivwyr1` in IFLS4 cover, with `ivwyr1∈{7,8}`). IFLS1–3 will need date imputation from cover modules (visit day/month available; year inferred from wave context).

## 2. Mental-health module availability

The CES-D depression scale only enters in IFLS4 and is **fully implemented in IFLS5**.

| Wave  | Module           | Items                                                                 | Use as outcome?           |
|-------|------------------|-----------------------------------------------------------------------|---------------------------|
| IFLS1 | `bk2*` KK        | General health + ADL only — **no** depression items                  | No                        |
| IFLS2 | `b3b_kk`         | General health + serious illness + ADL — **no** depression items     | No                        |
| IFLS3 | `b3b_kk`         | 4 proto-depression items: kk04 sleep, kk05 bothered, kk06 lonely, kk07 sadness | Limited / robustness only |
| IFLS4 | `b3b_kp`         | KP module (`kp01` = "in past week did you feel", `kp02` = how often) — long format, partial CES-D | Yes — partial             |
| IFLS5 | `b3b_kp`         | **Full CES-D 10** (`kptype` = A–J = 10 items, `kp02` 1–4 frequency) | **Primary outcome**       |

IFLS5: 31,447 adults with complete 10-item CES-D, **0% missing on kp02**. Response scale: 1=Rarely (<1 day), 2=Some (1–2 days), 3=Occasionally (3–4 days), 4=Most of time (5–7 days). Standard CES-D scoring → 0–30, with cutoffs at 10 (depressive symptoms).

Bonus IFLS5 outcomes: `b3a_pna1` (subjective well-being / "yesterday" diary, including bedtime `pna05hr`/`pna5mnt` — **direct sleep-disruption channel**), `b3a_si` (life satisfaction).

**Headline plan:** IFLS5 cross-section as the primary analysis; pool IFLS4 with a "harmonized partial CES-D" as a robustness/panel exercise.

## 3. GPS situation

**GPS coordinates are NOT in the public-use IFLS files.** Confirmed by:
- Exhaustive scan of every `.dta` across all five waves: zero columns matching `lat|lon|long|gps|x_coor|y_coor`.
- IFLS5 User Guide Vol 1, p. 35: *"Module SC indicates the precise location of the household. Much of this information is suppressed in the public-use data to protect respondent confidentiality."*
- The internal field team did use GPS for QC (Vol 1, p. 33: *"comparing… locations, GPS data on locations…"*) but did not release it.

**What we have instead — administrative codes** (in `bk_sc1.dta` for households; in `bk1.dta` for CF):
- `sc01_14_14` = province code (BPS 2-digit)
- `sc02_14_14` = kabupaten/kota (district) code
- `sc03_14_14` = kecamatan (subdistrict) code
- Plus internal IFLS codes `sc05`/`sc10`/`sc12`/`sc13`/`sc14`/`sc15`
- `commid14` (community ID) ties HH to its community; 311 communities total.

**Two ways forward, in order of effort:**

| Option | What you do | Spatial precision | Effort |
|--------|-------------|-------------------|--------|
| **A — admin centroid** | Geocode each kecamatan to its centroid using BPS / geoBoundaries shapefile, then pull temperature for that point | ~5–25 km (kecamatan median) | Low. Doable today with shapefile + Open-Meteo. |
| **B — area-mean from gridded climate** | Average ERA5-Land (0.1°) or CHIRPS daily over each kecamatan polygon via GEE | Polygon-area mean, statistically defensible | Medium. Needs GEE auth (already in `solar panel/.env`). Recommended for the headline spec. |
| C — restricted GPS | Apply to RAND for the Restricted Use file (signed agreement, IRB) | EA-level (~1 km) | High. Months of paperwork. Skip unless reviewers demand it. |

**Recommendation:** Build the pipeline on **Option B (kecamatan polygon mean)** using ERA5-Land via GEE — same precision Open-Meteo gives anyway, no rate limits, and we can add humidity / heat index / nighttime min cleanly. Validate against Open-Meteo at a few representative kecamatan centroids.

## 4. Built-in shock / stressor candidates

IFLS already collects a rich set of stressors that can be used either as (a) heterogeneity cuts for the heat × baseline-stress interaction, or (b) treatment shocks in their own right.

### 4a. Within-data stress / shock variables

| Module      | Wave    | Content                                                                | Use as…                       |
|-------------|---------|------------------------------------------------------------------------|-------------------------------|
| `b2_nd1`/`nd2` | **IFLS4, IFLS5** | **Natural disaster module — past 5 years.** Type (flood/quake/eruption/fire/landslide/drought/civil-strife…), date, deaths, injuries, asset loss, house damage, displacement, aid received | Stressor; identifies disaster-affected HHs |
| `b2_bh`     | IFLS4, IFLS5 | Borrowing module — `bh04` loan turned down                            | Financial stress              |
| `b2_vu`     | IFLS4, IFLS5 | Vulnerability — livestock/asset ownership                              | Asset-poverty stressor        |
| `b2_kr`     | all       | Consumption / non-food expenditure — build PCE quintiles               | Income stressor               |
| `b1_ksr*`   | IFLS3+    | Food consumption frequency — proxy for food insecurity                 | Food-insecurity stressor      |
| `b3a_kw*`   | all       | Labor module — informality, hours, occupation                          | Outdoor / informal-work cut   |
| `b3a_tr` / `b3a_re` | IFLS4+ | Transfers in / remittances received                              | Remittance shock              |
| `b3a_si`    | IFLS4, IFLS5 | Life satisfaction (Cantril ladder)                                  | Secondary outcome             |
| `b3a_dl*`   | all       | Daily activities limitations                                           | Health-stress cut             |
| `b3b_ak*`   | all       | Acute morbidity (past 4 weeks)                                         | Recent-illness cut            |
| `b3b_eh`    | IFLS4, IFLS5 | Health expectations / time horizon                                  | Future-orientation cut        |
| `b3b_ep1`/`ep2` | IFLS4, IFLS5 | Subjective probabilities (income, weather, mortality)            | Subjective-risk cut           |

### 4b. Macro / nationwide shocks usable for sample-period framing

| Date         | Event                                                  | IFLS wave overlap            | Useful for                     |
|--------------|--------------------------------------------------------|------------------------------|--------------------------------|
| 1997-07 →    | Asian Financial Crisis (rupiah collapse)               | IFLS2 fielded during onset; IFLS2+ in 1998 was specifically designed to study it | Historical pre-period only (no CES-D yet) |
| 2004-12-26   | Indian Ocean Tsunami / Aceh earthquake                 | IFLS3 just past; IFLS4 captures recovery | Limited — IFLS sample originally **excluded Aceh** |
| 2005-10, 2008-05/12 | Subsidy cuts + BLT cash transfers              | Bridges IFLS3 → IFLS4         | Buffer / cushion shock         |
| 2006-05-27   | Yogyakarta–Bantul earthquake (M6.3, ~5,800 deaths)    | 14 months before IFLS4 onset | **`b2_nd*` should pick this up** |
| 2007–2008    | Global food-price crisis (rice spike)                  | IFLS4 fielded during peak     | Stress shock during interview window |
| 2008-09      | Global Financial Crisis                                | Tail end of IFLS4 fielding   | Light                          |
| 2009-09-30   | Padang / West Sumatra M7.6 earthquake                  | Between waves                | `b2_nd*` recall in IFLS5       |
| 2010-10/11   | Mt Merapi eruption (Yogyakarta)                        | Between waves                | `b2_nd*` recall in IFLS5       |
| 2014-11      | Jokowi fuel-subsidy cut (1 month into IFLS5 fielding) | **Within IFLS5 field period** | Pre/post-cut comparison; financial-stress channel |
| 2015-09–11   | El Niño + Indonesian peat-fire haze (PM2.5 spikes; NOAA-recorded) | **Within IFLS5 field period (last 3 months)** | **Air-quality shock × heat interaction — strong candidate** |

### 4c. Pre-specified heterogeneity menu (start here, refine in `heterogeneity_plan.md`)

Headline interaction: **CES-D = α + β·Heat + γ·Stress + δ·(Heat × Stress) + FE + ε**, where Stress is one of:

1. **Recent natural disaster** (`b2_nd1` `nd01==1` and `nd02==1` within last 5 years) — direct stress
2. **Bottom expenditure quintile** (PCE) — financial fragility
3. **Loan turned down past 12 months** (`bh04`) — credit stress
4. **Recent serious illness in HH** (`b3b_ak*`, `b3a_dl*`) — health stress
5. **Outdoor / informal occupation** (`b3a_kw*`, agriculture/construction) — exposure × stress combined
6. **Caregiver of someone with ADL limitations** (from `b3b_kk4` helper roster)
7. **Widowed or recent bereavement** (from `bk_ar1` marital status changes)
8. **Lived through 2006 Yogya quake or 2010 Merapi** (province + birth-year filter, validated via `b2_nd*`)
9. **Survey conducted during 2015 haze months** (interview month ∈ {Sep, Oct, Nov 2015}) — air pollution × heat
10. **Lower-education / low-numeracy** (from `bus_us` cognitive tests, IFLS5)

Each cut should be pre-registered before running the regression. Effects predicted to amplify under the "heat tips already-stressed people" hypothesis are 1, 2, 3, 4, 6, 9 most strongly.

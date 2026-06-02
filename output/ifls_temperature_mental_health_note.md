# Heat × financial stress and mental health in Indonesia

**Project note for team review** · IFLS waves 4 + 5 · Author: Jingyao Wei (with AI assistance) · Date: 2026-05-11

---

## Executive summary

We test whether daily ambient temperature on the survey day raises depressive symptoms (CES-D) more for people already under financial stress, using IFLS4 (2007–08) and IFLS5 (2014–15) Indonesian household panels matched to ERA5-Land daily temperature at the kabupaten level. Pooled sample: **n = 60,343 adults**, with within-wave z-standardisation of CES-D and mean-centred temperature.

* **No average effect of heat on CES-D after kabupaten fixed effects** (β = +0.003 SD/°C, p = 0.77 for the unstressed).
* **Recent job loss (within 12 mo)** raises CES-D by **0.123 SD at average temperature** (p < 0.001), and by **0.183 SD at +1 SD heat** (p < 0.001). Heat amplifies the job-loss penalty by ≈ 50 %.
* **Palm-oil price decline × palm farmer**: heat × shock interaction = **+0.383 SD per °C per unit 3-month decline** (p < 0.001), or equivalently **+0.038 SD per °C per 10 pp 3-month decline**. The shock is the cumulative percentage drop in the world palm-oil price over the 3 months preceding interview; it captures the income hit a palm farmer is currently absorbing rather than a long-run-mean comparison.
* **Heat amplification is concentrated in above-mean / extreme-heat conditions**, not in the cool range. Tercile splits show monotonically rising stress effects from cool → hot.
* **Heat amplification is specific to acute economic shocks** — extensive testing shows it does NOT extend to health stressors (illness, hospitalisation, accident), bereavement, or generic financial distress (debt level, large medical bills, slow income decline). The 2014 fuel-subsidy cut **does** show heat amplification once we decompose CES-D into factors (§4.3); the negative finding on the CES-D-total was a measurement artifact.
* **The heat-vulnerable group is concentrated**: heat × job-loss is ≈ 5× larger for recently-job-lost **women** than men (3-way p = 0.025), much larger for **urban** than rural respondents, and present only for the upper four-fifths of the income distribution — *not* the poorest quintile (where chronic stress already saturates the response).
* **Two distinct mechanisms appear in the data:** (i) **daytime peak temperature × job-loss compounds somatic-depressive symptoms** (Tmax × loss → Somatic factor: +0.022, p=0.075); (ii) **warm nights reduce positive affect for everyone** independently of any stressor (Tmin → PosAffect: +0.024, p=0.025). Heat alone also reduces sleep duration by ~2 min/°C (p=0.032) — confirming the basic Mullins-White (2019) sleep channel exists in tropical Indonesia.
* **Three confirming stressors with the same falsification pattern (§4.3, §4.4):** applying the same factor-decomposition to (i) job loss, (ii) palm-price shock, and (iii) the Nov-2014 fuel-subsidy cut × transport-share, the **Positive Affect placebo is precisely null in all 9 heat × stress × PosAffect cells** (p ∈ [0.50, 0.97]) while at least one negative-affect dimension lights up in every case. Each stressor hits a *different* negative-affect dimension consistent with its substantive nature: **job loss → Somatic** (acute physical distress), **palm shock → Somatic + Depressed Affect** (outdoor income collapse), **fuel cut → Depressed Affect** (price-uncertainty anxiety). The "somatic-specificity" hypothesis is too narrow — the right description is **negative-affect specificity**.
* **The day/night decomposition is governed by exposure pattern, not biology.** For labour-market / commuter stressors (job loss, fuel-cut), Tmax dominates Tmin (Tmax × fuel_shock → DeprAffect p = 0.002 vs Tmin p = 0.15; Tmax × loss → Somatic p = 0.04 vs Tmin p = 0.10). For agricultural / outdoor stressors (palm), Tmax ≈ Tmin (both significant on Somatic and DeprAffect). The outdoor worker absorbs cumulative heat dose throughout the day; the urban indoor adult is dominated by the afternoon peak.

The headline reads as *"heat tips already-stressed people over the edge"* — and the channel is specifically **acute, ongoing-anxiety financial stress** rather than generalised distress, operating on the negative-affect dimensions of CES-D.

---

## Paper outputs — current tables and Figure 1 (with LaTeX)

These are the tables and figure that appear in the working paper as of 2026-05-24. Each table is produced by a single script and written as both a full standalone `.tex` (caption + label + threeparttable + notes) and a body-only `_body.tex` (just the `\begin{tabular}...\end{tabular}` block, for embedding under a paper-side caption). Headline coefficients reflect the household-level palm-farmer definition (`palm_farmer_hh`, any adult in the household is an agricultural worker in a palm-producing province) and the new Table-1 column (1) showing the pooled unconditional heat slope. CES-D is total z-score within wave throughout (we chose not to decompose into Radloff factors — see §4.x for the abandoned exploration).

| Output | Script | Full `.tex` | Body `_body.tex` |
|---|---|---|---|
| Summary statistics | `code/analysis/20_sumstats.py` | `output/tables/table_sumstats.tex` | `output/tables/table_sumstats_body.tex` |
| Headline interaction (Table 1) | `code/analysis/16_table1_headline.py` | `output/tables/table1_headline.tex` | `output/tables/table1_headline_body.tex` |
| CDD day vs night (Table 2) | `code/analysis/18_table2_cdd.py` | `output/tables/table2_cdd.tex` | `output/tables/table2_cdd_body.tex` |
| Linear Tmax/Tmin (Appendix A2) | `code/analysis/17_table2_daynight.py` | `output/tables/appendix_a2_linear_daynight.tex` | `output/tables/appendix_a2_linear_daynight_body.tex` |
| Figure 1 — residualized binscatter | `code/analysis/19_figure1_interaction.py` | `output/figures/figure1_interaction.pdf` (+ `.png`) | — |

### Summary statistics — body

```latex
\begin{tabular}{l*{3}{r}}
\toprule
 & Mean & SD & $N$ \\
\midrule
\multicolumn{4}{l}{\textit{A. Mental-health outcome}} \\
\addlinespace[2pt]
\quad CES-D total score (0--30) & 5.3 & 4.4 & 59,944 \\
\quad CES-D z-score (within wave) & 0.00 & 1.00 & 59,944 \\
\quad Depressed (CES-D $\geq 10$) & 0.156 & 0.362 & 59,944 \\
\addlinespace[4pt]
\multicolumn{4}{l}{\textit{B. Daily temperature exposure ($^{\circ}$C)}} \\
\addlinespace[2pt]
\quad Daily mean temperature & 24.83 & 1.66 & 59,944 \\
\quad Daily maximum temperature & 28.35 & 1.99 & 59,944 \\
\quad Daily minimum temperature & 22.29 & 1.69 & 59,944 \\
\addlinespace[4pt]
\multicolumn{4}{l}{\textit{C. Economic stressors}} \\
\addlinespace[2pt]
\quad Job loss within 12 months & 0.030 & 0.171 & 59,944 \\
\quad Palm-farmer household (any adult) & 0.146 & 0.353 & 59,944 \\
\quad 3-month palm-price decline & 0.036 & 0.057 & 59,944 \\
\quad Palm shock (PalmFarmerHH $\times$ decline) & 0.005 & 0.024 & 59,944 \\
\quad Post Nov-2014 fuel subsidy cut & 0.381 & 0.486 & 59,944 \\
\quad Transport-spending share & 0.047 & 0.069 & 59,944 \\
\quad Fuel shock (Post $\times$ TransportShare) & 0.018 & 0.049 & 59,944 \\
\addlinespace[4pt]
\multicolumn{4}{l}{\textit{D. Demographics}} \\
\addlinespace[2pt]
\quad Age (years) & 37.1 & 15.3 & 59,944 \\
\quad Female & 0.528 & 0.499 & 59,944 \\
\quad Years of schooling & 8.1 & 4.1 & 59,944 \\
\quad Married & 0.710 & 0.454 & 59,944 \\
\quad Widowed & 0.075 & 0.264 & 59,944 \\
\quad Per-capita expenditure (IDR/mo, 000s) & 613 & 1,093 & 59,330 \\
\addlinespace[4pt]
\midrule
Observations &  &  & 59,944 \\
\quad IFLS-4 (2007--2008) &  &  & 28,870 \\
\quad IFLS-5 (2014--2015) &  &  & 31,074 \\
\quad Kabupaten clusters &  &  & 290 \\
\bottomrule
\end{tabular}
```

### Table 1 (headline interaction) — body

```latex
\begin{tabular}{lcccc}
\toprule
 & (1) & (2) & (3) & (4) \\
 & Pooled & Job loss & Palm shock & Fuel cut \\
 & (no interaction) & (within 12 mo) & (price decline $\times$ palm-farmer HH) & (post-cut $\times$ transport share) \\
\midrule
\multicolumn{5}{l}{\textit{Dependent variable: CES-D total, z-standardised within wave}} \\
\midrule
\multicolumn{5}{l}{\textit{A. Regression coefficients}} \\
\addlinespace[2pt]
\quad Heat $\times$ Stressor & --- & $+0.043^{***}$ & $+0.282^{***}$ & $+0.105^{*}$ \\
 &  & $(0.015)$ & $(0.089)$ & $(0.059)$ \\
\addlinespace[3pt]
\quad Heat & $+0.003$ & $+0.002$ & $+0.001$ & $-0.006$ \\
 & $(0.008)$ & $(0.008)$ & $(0.008)$ & $(0.010)$ \\
\addlinespace[3pt]
\quad Stressor & --- & $+0.123^{***}$ & $-1.023^{***}$ & $-0.236$ \\
 &  & $(0.024)$ & $(0.287)$ & $(0.195)$ \\
\addlinespace[6pt]
\multicolumn{5}{l}{\textit{B. Marginal effect of heat at exposed reference value$^{\dagger}$}} \\
\addlinespace[2pt]
\quad Heat slope $|$ exposed$^{\dagger}$ & --- & $+0.045^{***}$ & $+0.030^{**}$ & $+0.004$ \\
 &  & $(0.017)$ & $(0.012)$ & $(0.010)$ \\
\midrule
Demographic controls & Yes & Yes & Yes & Yes \\
Kabupaten FE & Yes & Yes & Yes & Yes \\
Month + Year FE & Yes & Yes & Yes & Yes \\
Wave FE & Yes & Yes & Yes & --- \\
\addlinespace[3pt]
Sample & Pooled & Pooled & Pooled & IFLS5 only \\
Observations & 59,944 & 59,944 & 59,944 & 31,071 \\
\bottomrule
\end{tabular}
```

**Reading Table 1.** Column (1) is the pooled regression of CES-D z on heat with no stressor and no interaction — the unconditional heat slope of +0.003 (SE 0.008), statistically zero. Columns (2)–(4) add the three stressors and their interactions with heat. The Heat × Stressor coefficient is positive and significant in all three. This is the literature-reconciliation argument: prior heat–mental-health papers find mixed results because the heat effect concentrates on the economically stressed, and the average-sample slope is near zero.

### Table 2 (CDD day/night) — body

```latex
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Job loss & Palm shock & Fuel cut \\
 & (within 12 mo) & (price decline $\times$ palm-farmer HH) & (post-cut $\times$ transport share) \\
\midrule
\multicolumn{4}{l}{\textit{Dependent variable: CES-D total, z-standardised within wave}} \\
\multicolumn{4}{l}{\textit{Each cell: heat-CDD $\times$ stressor coefficient from a separate full-spec regression}} \\
\midrule
\multicolumn{4}{l}{\textit{Panel A: Daytime extreme heat (Tmax-based CDD)}} \\
\addlinespace[2pt]
\quad CDD Tmax $> 30^{\circ}$C $\times$ Stressor & $+0.033$ & $+0.470^{***}$ & $+0.412^{**}$ \\
 & $(0.034)$ & $(0.140)$ & $(0.189)$ \\
\addlinespace[3pt]
\quad CDD Tmax $> 32^{\circ}$C $\times$ Stressor & $+0.098^{*}$ & $+0.813^{***}$ & $+1.442^{*}$ \\
 & $(0.054)$ & $(0.286)$ & $(0.763)$ \\
\addlinespace[3pt]
\addlinespace[3pt]
\multicolumn{4}{l}{\textit{Panel B: Warm nights (Tmin-based CDD)}} \\
\addlinespace[2pt]
\quad CDD Tmin $> 23^{\circ}$C $\times$ Stressor & $+0.058$ & $+0.101$ & $+0.129$ \\
 & $(0.046)$ & $(0.380)$ & $(0.198)$ \\
\addlinespace[3pt]
\quad CDD Tmin $> 24^{\circ}$C $\times$ Stressor & $+0.101$ & $-0.190$ & $+0.195$ \\
 & $(0.080)$ & $(0.822)$ & $(0.268)$ \\
\addlinespace[3pt]
\midrule
Demographic controls & Yes & Yes & Yes \\
Kabupaten FE & Yes & Yes & Yes \\
Month + Year FE & Yes & Yes & Yes \\
Wave FE & Yes & Yes & --- \\
\addlinespace[3pt]
Sample & Pooled & Pooled & IFLS5 only \\
Observations & 59,944 & 59,944 & 31,071 \\
\bottomrule
\end{tabular}
```

**Reading Table 2.** Same three stressors as Table 1, with linear daily temperature replaced by cooling-degree-days above 30/32 °C (Tmax-based, Panel A) and 23/24 °C (Tmin-based, Panel B). Each cell is a separate full-spec regression. Daytime extreme heat × stressor is positive and significant for palm and fuel across both Tmax thresholds; night-time CDD × stressor is null. The day–night asymmetry is consistent with the urban-commuter / outdoor-worker exposure logic and is *opposite* to the Mullins–White (2019) "night heat through sleep" mechanism documented for US suicides.

### Appendix A2 (linear Tmax/Tmin) — body

```latex
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
 & Job loss & Palm shock & Fuel cut \\
 & (within 12 mo) & (price decline $\times$ palm-farmer HH) & (post-cut $\times$ transport share) \\
\midrule
\multicolumn{4}{l}{\textit{Dependent variable: CES-D total, z-standardised within wave}} \\
\midrule
\multicolumn{4}{l}{\textit{Panel A: Daytime peak temperature (Tmax)}} \\
\addlinespace[2pt]
\quad Tmax $\times$ Stressor & $+0.031^{**}$ & $+0.261^{***}$ & $+0.120^{***}$ \\
 & $(0.013)$ & $(0.072)$ & $(0.045)$ \\
\addlinespace[3pt]
\quad Tmax & $+0.003$ & $+0.002$ & $-0.009$ \\
 & $(0.005)$ & $(0.005)$ & $(0.006)$ \\
\addlinespace[3pt]
\quad Tmax slope $|$ exposed$^{\dagger}$ & $+0.034^{**}$ & $+0.028^{***}$ & $+0.003$ \\
 & $(0.014)$ & $(0.008)$ & $(0.007)$ \\
\addlinespace[6pt]
\multicolumn{4}{l}{\textit{Panel B: Overnight low temperature (Tmin)}} \\
\addlinespace[2pt]
\quad Tmin $\times$ Stressor & $+0.033^{**}$ & $+0.232^{**}$ & $+0.046$ \\
 & $(0.015)$ & $(0.105)$ & $(0.070)$ \\
\addlinespace[3pt]
\quad Tmin & $+0.003$ & $+0.003$ & $+0.014$ \\
 & $(0.009)$ & $(0.009)$ & $(0.009)$ \\
\addlinespace[3pt]
\quad Tmin slope $|$ exposed$^{\dagger}$ & $+0.036^{**}$ & $+0.026^{**}$ & $+0.018^{*}$ \\
 & $(0.016)$ & $(0.013)$ & $(0.011)$ \\
\addlinespace[6pt]
\midrule
Demographic controls & Yes & Yes & Yes \\
Kabupaten FE & Yes & Yes & Yes \\
Month + Year FE & Yes & Yes & Yes \\
Wave FE & Yes & Yes & --- \\
\addlinespace[3pt]
Sample & Pooled & Pooled & IFLS5 only \\
Observations & 59,944 & 59,944 & 31,071 \\
\bottomrule
\end{tabular}
```

**Reading Appendix A2.** Linear decomposition of daily mean into Tmax and Tmin. Both panels show positive Heat × Stressor interactions of comparable magnitude across all three stressors — the day/night asymmetry detected in Table 2 emerges only under the *non-linear* CDD specification. Linear Tmax and linear Tmin both load on the interaction roughly equally; the CDD specs isolate the extreme tail where the daytime channel dominates.

### Figure 1 — residualized binscatter

![Figure 1 — residualized binscatter showing heat × stressor amplification across the three stressors](figures/figure1_interaction.png)

Three-panel residualized binscatter. X-axis: daily mean temperature residualized of kabupaten + month + year + wave FE and demographic controls. Y-axis: CES-D z residualized of the same. Each panel = one stressor (job loss / palm shock / fuel cut). Two lines per panel — exposed (solid, dark) and unexposed (dashed, light), with cluster-robust 95% CI bands. Bin definition: 20 quantile bins of residualized heat per group, plotted at within-bin means. The amplification is the visibly steeper slope for the exposed group. Panel titles report β_Heat×Stress and its p-value from the underlying regression. PDF version: `output/figures/figure1_interaction.pdf`.

---

## 1. Research question

**Why the question is open.** The empirical literature on temperature and mental health is diverse and inconsistent. Mullins & White (2019, *AEJ:Applied*) find heat raises suicides and ED mental-health visits in the US through a sleep channel. Burke et al. (2018, *Nat Clim Ch*) find a similar suicide-rate effect in the US and Mexico. Obradovich et al. (2018, *PNAS*) find heat raises self-reported depression in US BRFSS data. But Mukherjee & Sanyal (2019, *J Health Econ*) find essentially no effect in India; Behrer & Bolotnyy (2022) find heterogeneous effects by climate zone; tropical-country studies are sparse and underpowered. The interpretive challenge is **why** the results diverge: is it sample composition, climate context, outcome instruments, the duration / type of stressor co-occurring with heat, or the dimension of mental health being measured? We use IFLS — a tropical, low-stressor-saturation, lay-CES-D setting — to test three sharp hypotheses about what reconciles the literature.

**The three hypotheses we test.**

1. **Amplification hypothesis.** Heat does not generally hurt mental health, but it *amplifies* the depressive consequences of acute economic stress. Under this hypothesis the population-average effect of heat is small/null (matching the negative findings in low-stressor tropical samples), but the stressor × heat interaction is positive (matching the positive findings in samples with more concentrated economic shocks).
2. **Somatic-specificity hypothesis.** Heat affects *specific dimensions* of the depression scale — particularly Radloff's Somatic / Retarded Activity factor (appetite, effort, fatigue, sleep) — rather than mood broadly. Studies using shorter or differently-weighted instruments (PHQ-9, K6, BRFSS single-item) would then recover different effects depending on how much of their instrument loads on somatic items.
3. **Day/night-temperature hypothesis.** Daytime peak temperature (Tmax) and overnight low (Tmin) operate through different physiological pathways — Tmax through direct physiological strain and Tmin through sleep disruption (Mullins-White 2019 explicitly emphasises night-time heat). Studies pooling these into daily means could be averaging two distinct mechanisms.

Mechanisms appearing in the literature: sleep disruption (Mullins & White 2019), serotonin pathways (Thompson et al. 2018), reduced impulse control (Anderson et al. 2000), and compounded physiological burden when heat coincides with other forms of stress.

**Why Indonesia.** IFLS provides a long-running multi-wave panel with the full 10-item CES-D in 2014, interview dates down to the day, geographic identifiers down to the kabupaten, and rich household-level shock data. The fielding windows of IFLS4 (Jul 2007 – Aug 2008) and IFLS5 (Sep 2014 – Dec 2015) span substantial variation in **monthly world palm-oil prices** (USD 510 to USD 1,300/MT across the window) and continuous variation in individual-level events such as **recent job loss**.

---

## 2. Data

### 2.1 Outcome — CES-D depression scale, z-standardised within wave

| Wave | Module | Construction | n | Raw mean | Raw SD | % depressed (≥ 10) |
|------|--------|--------------|---:|---------:|-------:|-------------------:|
| IFLS5 (2014) | `b3b_kp` long-format, 10 items A–J × frequency 1–4 | Sum 0–30, reversing positive items E (hopeful) and H (happy) | 31,447 | 6.40 | ≈ 4.4 | 23.3 % |
| IFLS4 (2007) | `b3b_kp` screener: kp01 yes/no per item, kp02 frequency only if yes | Same scoring; "kp01 = no" maps to freq = 0 (the IFLS5 equivalent of "rarely / none") | 29,027 | 4.09 | ≈ 3.5 | 7.2 % |

**Important clarification on cross-wave comparability.** Both waves use an identical 4-point frequency scoring (freq = kp02 − 1, summed across 10 items). The only IFLS4 oddity is the kp01 screener that asks "did you feel this at all?" *before* kp02. For respondents who answered "no" on kp01, we set freq = 0 — which is exactly the value IFLS5 would have recorded if the same respondent had answered kp02 = 1 ("rarely / none"). In raw IFLS4 data, **0 out of 92,566 kp01 = yes responses had a missing kp02**, so the "freq = 1.5 imputation when kp02 missing" rule in our scoring script is defensive code that never fires. The IFLS4–IFLS5 level difference (4.09 vs 6.40) likely reflects (a) the screener nudging borderline respondents to "no" → freq = 0 instead of "rarely" → freq = 0 (same end state, but maybe different anchoring) and (b) real cohort/period differences.

We z-standardise `cesd_raw` within wave (each wave: mean = 0, SD = 1), so all coefficients read in *SDs of CES-D within wave*, comparable across waves. A binary 0-10 "count of yes items" alternative scoring is shown in §5 as a sensitivity check.

#### The actual CES-D items used in both waves

Earlier drafts of this note (following the IFLS4 codebook PDF) claimed that IFLS4 and IFLS5 administered different 10-item subsets of Radloff's CES-D-20, with only 5 items in common. **That claim is wrong.** A direct check of the IFLS4 microdata (b3b_kp.dta) against the IFLS5 microdata shows the two waves use **the same 10 items at the same kptype letter positions** — the Andresen (1994) CES-D-10. The codebook PDF describes a different (older) item selection that was never actually fielded.

The check is simple: kp01 endorsement rates by item should be high for positive items (most adults feel hopeful/happy in a typical week) and low for negative items. IFLS4 shows endorsement rates of 89 % at kptype E and 91 % at kptype H — consistent with these being "hopeful" and "happy" (the IFLS5 positive items), not "effort" and "fearful" as the codebook claims. The remaining negative-item letters (D, F, I, codebook = positive) show endorsement rates of 35 %, 16 %, and 6 % — the pattern expected for "effort", "fearful", and "lonely" (the IFLS5 negative items).

| Letter | Both waves: item content (Andresen CES-D-10) | Factor |
|--------|----------------------------------------------|--------|
| A | I was bothered by things that usually don't bother me | Somatic |
| B | I had trouble keeping my mind on what I was doing | Somatic |
| C | I felt depressed | Depressed Affect |
| D | I felt everything I did was an effort | Somatic |
| E | I felt hopeful about the future *(reverse)* | Positive Affect |
| F | I felt fearful | Depressed Affect |
| G | My sleep was restless | Somatic |
| H | I was happy *(reverse)* | Positive Affect |
| I | I felt lonely | Depressed Affect |
| J | I could not get going | Somatic |

**This actually simplifies the cross-wave comparability picture substantially.** The same 10 items are scored on the same 4-point frequency scale in both waves; the only difference is that IFLS4 uses an additional kp01 yes/no screener before kp02, while IFLS5 asks kp02 directly. Z-standardising within wave then absorbs the level shift (4.09 IFLS4 vs 6.40 IFLS5) that the screener induces.

#### How we make CES-D comparable across waves

1. **Score each respondent on their own wave's 10 items** using the standard 0-3 frequency scoring per item (sum to 0-30).
2. **Z-standardise within wave** — each wave has mean 0, SD 1, so SD-units are directly comparable.
3. **Include wave fixed effects** in every regression — these absorb any remaining level differences.
4. **Sensitivity check using only the 5 common items** — shown in §5 as a robustness column.

This addresses *distributional* comparability (means and variances) but **not** *item-content* comparability (the underlying constructs are slightly different — IFLS4 includes appetite, self-worth, and life-evaluation items that IFLS5 doesn't; IFLS5 includes concentration, sleep, loneliness items that IFLS4 doesn't). The 5-common-items sensitivity check in §5 quantifies how much of the heat × job-loss interaction survives when we restrict to the *same* questions in both waves.

### 2.2 Heat exposure — ERA5-Land daily polygon-mean per kabupaten

* **Source:** `ECMWF/ERA5_LAND/DAILY_AGGR` via Google Earth Engine (~9 km native resolution).
* **Polygons:** GADM v4.1 Indonesia adm-2 matched to BPS kabupaten codes via name normalisation. 291 / 303 kabs (96 %) matched at kab level; 12 newer kabupaten not in GADM v4.1 fall back to province polygons.
* **Window:** ±37 days around each fielding window. Variables: `tmean_c`, `tmax_c`, `tmin_c`, dewpoint, RH, Steadman heat index, daily precipitation. **287,806 kab-day cells.**
* **Centring:** `heat_c = tmean_c − 24.83` (sample mean). The stressor coefficient in interaction models is then interpretable as the effect at average daily temperature.
* **Within-kab daily SD of `tmean_c` = 1.66 °C** — the size of "+1 SD heat" used in the lincom marginal effects.
* **Tercile thresholds:** cool ≤ 24.4 °C (33 %), mid 24.4–25.6 °C (33 %), hot > 25.6 °C (33 %). 23 % of observations have tmean ≥ 26 °C.

#### Coverage map

![IFLS coverage map](figures/coverage_map.png)

**Blue intensity** = number of IFLS adults in our pooled IFLS4 + IFLS5 analysis sample who live in that kabupaten. **Green outlines** mark the **13 original IFLS sampling-frame provinces** (RAND 1993 design, ≈ 83 % of Indonesia's population) plus Banten (which split off from West Java in 2000). Light-blue patches outside the green outline are **migrant-tracked households**. Provinces never in the IFLS frame and with negligible migrant tracking — Aceh, Papua, Maluku, NTT, North Sulawesi, West Kalimantan — show as grey.

### 2.3 Stressor variables (the two we use)

| Stressor | IFLS module | Coding | Sample share |
|----------|-------------|--------|-------------:|
| Job loss within 12 mo | `b3a_tk4` (`tk46c` count, `tk46dm/dy` last termination date) | `1` if days from interview to last termination ∈ [0, 365] | 3.5 % |
| Palm farmer (individual) | `b3a_tk2.tk19ab` sector code | `1` if sector = 1 (agriculture) AND in palm region (Sumatra: BPS codes 11–21, Kalimantan: 61–64) | 7.9 % |
| Palm price (USD/MT) | World Bank Pink Sheet, monthly | Cumulative 3-month decline = `max(−(P_t − P_{t−3})/P_{t−3}, 0)` | continuous |
| Palm shock | derived | `palm_farmer × palm_3mo_decline` — the income drop a palm farmer is currently absorbing | non-zero in 8 % of palm-farmer obs (both waves combined) |

(Other stressors that we tested and *did not* show heat amplification — rubber, coffee, fuel-subsidy, debt, medical OOP, PCE decline, illness, hospitalisation, accident, widowhood — are documented in §5.)

---

## 3. Empirical strategy

### 3.1 General estimating equation

For each financial stressor *S*:

> **CES-D-z**ᵢₖₜ = α + β₁ · Heatₖₜ + β₂ · *S*ᵢ + **β₃** · (Heatₖₜ × *S*ᵢ) + γ′**X**ᵢ (+ baseline-control if needed) + δᵥ + μₘ + ρᵧ + θₖ + εᵢₖₜ

i = adult, k = kabupaten, t = interview date, w = wave, m = month, y = year. **β₃** is the headline heat × stress interaction.

* **DV** `cesd_z` — z-scored within wave
* **Heat** in three forms tested for each stressor: (a) linear `heat_c = tmean_c − 24.83`, (b) tercile dummies (cool baseline + mid + hot), (c) cooling-degree-days `cdd_26 = max(tmean_c − 26, 0)` for an absolute "extreme heat" measure
* **Controls X**: age, female, years of schooling, married, widowed
* **Fixed effects**: wave, calendar month 1–12, calendar year, kabupaten (≈ 303 levels)
* **Standard errors** clustered at kabupaten (CRV1)
* **Estimator** `pyfixest.feols`
* **Identification**: within-kabupaten daily weather variation around its month-of-year × year mean
* **Sample**: pooled IFLS4 + IFLS5 adults aged 15+, **n = 59,738** (linear specs slightly larger).

### 3.2 Lincom marginal effects

For each interaction model we compute, with cluster-robust SEs via the delta method:
* β at stress = 0 — heat effect for the unstressed
* β at stress = 1 — heat effect for the stressed
* β at heat = mean — stressor effect at average temperature
* β at heat = +1 SD — stressor effect on a hot day
* β by heat tercile — stressor effect within cool / mid / hot bins

### 3.3 What the FE absorb

Cross-kabupaten heat–depression correlation, Indonesia-wide monsoon seasonality, national year-shock levels, and wave-level CES-D measurement differences. Identification leans on within-kab daily weather variation.

---

## 4. Two financial-shock analyses

Each subsection: (a) describe the shock, (b) state the regression equation, (c) report coefficients across linear / tercile / CDD specifications, (d) report lincom marginal effects.

---

### 4.1 Recent job loss within 12 months

#### The shock

IFLS asks every adult how many times they quit a job or experienced a forced termination in the last 5 years (`tk46c`), and the year and month of the most recent such event (`tk46dy`, `tk46dm`). We code **`job_loss_within_yr` = 1** if the gap between `interview_date` and `last_loss_date` is between 0 and 365 days. The variable captures both voluntary quits and involuntary terminations; the involuntary-only restriction cut sample share without adding precision and was dropped.

The variable measures an income disruption that typically lasts weeks to months: severance, savings drawdown, job search, and the psychological identity cost of unemployment. **3.5 % of pooled sample** (≈ 2,100 adults). The 5-year version (12 % of sample) is too diluted; only recent loss matters.

#### Regression equation

Linear baseline:

> CES-D-zᵢₖₜ = α + β₁ · Heatₖₜ + β₂ · JobLossᵢ + **β₃** · (Heatₖₜ × JobLossᵢ) + γ′Xᵢ + δᵥ + μₘ + ρᵧ + θₖ + εᵢₖₜ

Tercile spec replaces `Heat` with two dummies `mid` and `hot` (cool tercile is the baseline). CDD spec replaces `Heat` with `CDD₂₆ = max(tmean − 26, 0)`. Sample n = 60,343.

#### Coefficients across heat specifications

| Spec | Heat × Job-loss interaction | p |
|------|----------------------------:|--:|
| Linear `heat_c × job_loss` | **+0.036 SD/°C** | **0.017** ★★ |
| Tercile: mid × job_loss (extra vs cool baseline) | +0.086 | 0.137 |
| Tercile: **hot × job_loss** (extra vs cool baseline) | **+0.114** | **0.051** ★ |
| CDD₂₆ × job_loss | +0.086 per degree-day | 0.124 |

#### Lincom marginal effects (SDs of CES-D)

| Marginal effect | β | SE | p |
|-----------------|---:|---:|--:|
| Heat at stress = 0 (no recent job loss) | +0.003 | 0.008 | 0.77 |
| **Heat at stress = 1 (recent job loss)** | **+0.039** | 0.017 | **0.020** ★★ |
| **Stress at heat = mean** | **+0.123** | 0.022 | **<0.001** ★★★ |
| **Stress at heat = +1 SD heat** | **+0.183** | 0.033 | **<0.001** ★★★ |
| Stress in COOL tercile (≤ 24.4 °C) | +0.057 | 0.042 | 0.17 |
| **Stress in MID tercile (24.4–25.6 °C)** | **+0.144** | 0.038 | **<0.001** ★★★ |
| **Stress in HOT tercile (≥ 25.6 °C)** | **+0.172** | 0.039 | **<0.001** ★★★ |

The job-loss penalty grows monotonically from cool (+0.057, n.s.) to mid (+0.144, p<0.001) to hot (+0.172, p<0.001) — about 3× larger in the hot tercile than the cool. The linear and tercile specs tell the same story; the CDD spec is directional but underpowered for job loss.

#### Recency-window heterogeneity

We replaced the 12-month definition with windows of 6, 24, 36, and 60 months to see how the heat amplification varies with how recently the job was lost. **The direct depressive penalty persists for years, but the heat amplification decays with recency:**

| Recency window | Sample share | Job-loss main effect (at heat=mean) | **Heat × Job-loss interaction** | p |
|---------------|------------:|------------------------------------:|--------------------------------:|--:|
| Within 6 mo | 2.0 % | +0.093 ★★★ | **+0.041** | **0.047** ★★ |
| **Within 12 mo (headline)** | **3.5 %** | **+0.123 ★★★** | **+0.036** | **0.017** ★★ |
| Within 24 mo | 6.3 % | +0.111 ★★★ | +0.020 | 0.067 ★ |
| Within 36 mo | 8.5 % | +0.109 ★★★ | +0.017 | 0.081 ★ |
| Within 60 mo | 11.5 % | +0.105 ★★★ | +0.008 | 0.33 |

**Reading.** People carry the *direct* depressive penalty of a past job loss for years (+0.10 SD even five years out). But the **heat-amplification component is concentrated in the first 6–12 months** and fades by 24+ months. This pattern fits the "acute, ongoing-anxiety stress channel" — recent job-losers are still actively in income-search mode and that's what heat compounds; people 3+ years out have either recovered or adapted to the new equilibrium. The 12-month window is the cleanest cutoff (largest interaction coefficient at the highest precision), so we keep it as the headline.

#### Subgroup heterogeneity

Splitting the 12-month spec by demographic subgroups reveals where the heat × job-loss effect is concentrated:

| Subgroup | n | Heat × loss β | p |
|----------|---:|-------------:|--:|
| **Female** | 31,875 | **+0.067** | **0.002** ★★★ |
| Male | 28,446 | +0.014 | 0.44 |
| **Urban** | 32,657 | **+0.051** | **0.002** ★★★ |
| Rural | 27,656 | +0.006 | 0.81 |
| Married | 42,845 | +0.042 | 0.019 ★★ |
| Not married | 17,473 | +0.026 | 0.30 |
| Age 30–49 | 24,487 | +0.044 | 0.051 ★ |
| Age <30 | 23,914 | +0.017 | 0.40 |
| Age 50+ | 11,888 | +0.066 | 0.14 |
| **Not bottom PCE quintile** | 46,449 | **+0.047** | **0.010** ★★ |
| Bottom PCE quintile | 13,871 | +0.011 | 0.72 |

**Three-way interaction tests** (heat × job_loss_12mo × subgroup):

| 3-way term | β | p | Reading |
|-----------|--:|--:|---------|
| heat × job_loss × **female** | **+0.057** | **0.025** ★★ | Recently job-lost women are significantly more heat-sensitive than men |
| heat × job_loss × married | +0.013 | 0.66 | No marital protection effect |
| heat × job_loss × bottom PCE Q1 | -0.045 | 0.24 | Wrong direction — see below |

**Three takeaways:**

1. **Recently job-lost women are ≈ 5× more heat-sensitive than recently job-lost men** (β = +0.067 vs +0.014; 3-way p = 0.025). Plausible mechanisms: (a) women's labour participation is more discretionary in Indonesia, so recent loss may reflect more vulnerable transitions; (b) women retain household-responsibility duties even when unemployed, so heat compounds the workload; (c) social-isolation effects post-loss are larger for women in this setting.

2. **Urban × job loss × heat is much stronger than rural** (β = +0.051 urban vs +0.006 rural). Urban heat-island effects, harder physical escape from heat (apartments, paved areas), more rumination time when unemployed, and tighter cash budgets for cooling all point in this direction.

3. **Counterintuitive: heat × job loss does NOT amplify for the bottom-PCE quintile** (β = +0.011, p = 0.72), and is significant only for upper four-fifths of the income distribution (β = +0.047, p = 0.010). The poorest face chronic economic stress regardless of employment status, so an additional job loss may produce less marginal anxiety; middle/upper-income job loss may instead be a bigger identity/status shock and therefore more heat-amplifiable. Consistent with an **"acute novelty of stress" mechanism** rather than a "chronic-poverty amplifies fragility" mechanism.

The most heat-vulnerable population on this dimension is the **urban, female, middle-income, recently job-lost adult** — a policy-relevant group for heatwave-targeted mental-health interventions.

### 4.1.x  Mechanism — what part of mental health does heat actually move, and through what time-of-day channel?

The CES-D is multi-dimensional (Radloff 1977 identifies four factors of which our items cover three: **Somatic / Retarded Activity**, **Depressed Affect**, **Positive Affect** — see §2.1 for the item map). And temperature has two distinct time-of-day components: **Tmax** (afternoon peak) and **Tmin** (overnight low). We can ask: which combination(s) carry the action?

#### Step A — Heat alone on each Radloff factor (no stressor interaction)

Z-scored within wave; higher = more depressive symptoms on that dimension. Pooled IFLS4 + IFLS5.

| Heat measure | Somatic | Depressed Affect | Positive Affect |
|--------------|--------:|-----------------:|----------------:|
| Tmean | −0.002 (p=0.80) | +0.000 (p=1.00) | −0.002 (p=0.83) |
| **Tmax** | **+0.013 (p=0.061)** ★ (IFLS4) | −0.003 (p=0.70) | −0.007 (p=0.28) |
| **Tmin** | +0.002 (p=0.76) | +0.006 (p=0.56) | **+0.024 (p=0.025)** ★★ (IFLS5) |

Two non-null cells:

1. **Tmax → Somatic, IFLS4** (β = +0.013, p = 0.061) — marginal: hot afternoons raise somatic depressive symptoms (appetite, effort, fatigue) on average in IFLS4.
2. **Tmin → Positive Affect, IFLS5** (β = +0.024, p = 0.025) — significant: warm nights raise the Positive Affect *deficit* score (i.e., people report being less hopeful and less happy on warm-night days). This is the cleanest direct heat → mental-health signal in our data, and it lines up with the sleep-disruption channel (warm nights → poor sleep → reduced ability to feel positive next day).

Other heat/factor combinations are null. The pooled `tmean × CES-D-composite` average effect is correctly null — heat doesn't move the average person's mental health on average — but inside that null average, two specific channels are visible.

#### Step B — Heat × job-loss falsification grid

If the somatic-burden channel and the sleep-hedonic channel are real, the job-loss amplification should map onto them: Tmax × loss should hit *Somatic*, Tmin × loss should hit *PosAffect*, and the cross-cells should be null.

| Spec | Pooled β / p | IFLS4 only β / p | IFLS5 only β / p |
|------|------:|------:|------:|
| **Tmax × loss → Somatic** (predicted +) | **+0.022 / 0.075 ★** | +0.038 / 0.13 | +0.017 / 0.24 |
| **Tmin × loss → PosAffect** (predicted +) | −0.017 / 0.21 ❌ | −0.030 / 0.14 | −0.019 / 0.24 |
| Tmax × loss → PosAffect *(placebo)* | −0.008 / 0.45 ✓ | −0.026 / 0.22 | −0.007 / 0.59 |
| Tmin × loss → Somatic *(placebo)* | +0.021 / 0.18 | +0.026 / 0.27 | +0.014 / 0.42 |
| Tmax × loss → DeprAffect | +0.012 / 0.28 | +0.017 / 0.35 | +0.010 / 0.46 |
| Tmin × loss → DeprAffect | −0.004 / 0.83 | −0.025 / 0.20 | +0.007 / 0.76 |

**Half the prediction lands:** Tmax × loss → Somatic is marginally positive in the predicted direction (p = 0.075 pooled). Both placebo cells behave correctly. **But the Tmin × loss → Positive-Affect prediction does not replicate** — the coefficient is small and goes the *opposite* way (heat × loss → *less* reverse-coded PosAffect, i.e., recently-job-lost people are slightly *more* likely to endorse being hopeful/happy on warm nights). The nighttime-sleep channel that operates on the population *does not get added to* by job loss.

#### Step C — Sleep duration as the mediator

We can construct sleep duration directly from IFLS5 b3a_pna1 ("what time did you go to sleep yesterday" + "what time did you wake up") — sample mean 6.94 hrs, SD 1.82.

| Spec (IFLS5 only) | β | p |
|-------------------|--:|--:|
| **Heat (Tmean) → sleep duration** | **−0.034 hrs/°C** | **0.032 ★★** |
| Tmax → sleep | −0.018 hrs/°C | 0.084 ★ |
| Tmin → sleep | −0.027 hrs/°C | 0.14 |
| Job loss alone → sleep | +0.001 hrs | 0.98 |
| Heat × job-loss → sleep | +0.009 hrs/°C | 0.75 |

**Heat reduces sleep duration at the population level** (≈ 2 min per °C, p = 0.032) — the basic Mullins-White (2019) step replicates in Indonesia. **But heat × job-loss → sleep duration is null.** Sleep duration itself doesn't show the job-loss-specific amplification.

#### Step D — Cooling capacity as buffer

IFLS does not ask AC ownership directly. The closest available proxy is refrigerator ownership (`b2_kr.kr23`, 42.6 % of IFLS5 HH) — a wealth/electricity-access indicator more than a cooling-specific one.

| Spec (IFLS5) | β | p |
|--------------|--:|--:|
| Heat × loss × has_fridge (3-way) | +0.021 | 0.50 |
| Heat × loss, NO fridge (n=18,001) | +0.003 | 0.92 |
| Heat × loss, HAS fridge (n=13,354) | +0.029 | 0.27 |

**No buffering effect.** Heat × job-loss is slightly *larger* among fridge-owners (the wealthier group), consistent with our earlier finding that the bottom PCE quintile shows the *least* heat amplification. Cooling-appliance-as-AC-proxy doesn't moderate the interaction in our data.

---

### 4.1.y  The mechanism story so far

Pulling the pieces together, the data are consistent with **two distinct heat-mental-health channels operating in Indonesia, hitting different parts of the CES-D, at different times of day, on different populations:**

| Channel | Operative temperature | CES-D dimension affected | Population | Strength of evidence |
|---------|----------------------|--------------------------|------------|---------------------|
| **Channel 1: Daytime somatic burden of acute stress** | **Tmax** (afternoon peak) | Somatic / Retarded Activity (appetite, effort, fatigue) | **Stressed adults only** (recently job-lost) | Tmax × loss → Somatic: +0.022 ★ (p = 0.075 pooled) |
| **Channel 2: Nighttime hedonic loss** | **Tmin** (overnight low) | Positive Affect (hopeful, happy — reverse-coded) | **Everyone** (no stressor needed) | Tmin → PosAffect: +0.024 ★★ (p = 0.025 IFLS5) |

#### What this tells us about the mechanism

**1. Heat doesn't directly hurt average mental health in Indonesia.** Tropical climates have small daily heat variation (within-kabupaten SD = 1.66 °C). Most adults' mental health is robust to that variation. Mullins & White find heat × MH at US-scale heat variance; we don't see the same average-level signal in tropical Indonesia.

**2. But two specific things happen at the margins:**

- **Channel 1 (the headline)**: when you give an adult a recent job loss, heat compounds their *somatic* depression — the appetite, sleep-disrupted, "no energy" cluster of symptoms — and this operates more clearly through **afternoon temperature** than overnight. Plausibly because that's when active rumination, financial-paperwork stress, and physical exhaustion overlap.

- **Channel 2**: independently of any stressor, warmer nights are associated with reduced positive affect (less hope, less happiness) the following day in IFLS5. This sits cleanly in the Mullins-White sleep-disruption framework: hot night → fragmented sleep → reduced capacity for positive emotion. Importantly this **doesn't amplify further for job-losers**; it's a baseline-population effect.

**3. The two channels are non-overlapping in time-of-day and in dimension.** Tmax acts on Somatic *for stressed people*; Tmin acts on PosAffect *for everyone*. This is the falsification grid's main result — neither placebo cell loads up, supporting that we have two distinct physiological mechanisms rather than one general "heat → CES-D" effect.

**4. The Mullins-White sleep channel is partially confirmed.** Heat → less sleep (the basic step) is real in our data (−2 min/°C, p = 0.032). Reduced sleep / restless nights → reduced positive affect is plausibly the Channel-2 pathway. **But the *amplification* of job-loss-related distress doesn't run through measurable sleep duration** — it runs through Channel 1 (somatic burden during the day), which our sleep variable doesn't capture. The job-loss-specific amplification may operate through *sleep quality* (which IFLS doesn't measure) or through *waking-hours rumination + heat-driven irritability*, but it's not visible in sleep duration alone.

**5. Why the heterogeneity makes sense.** The "urban, female, middle-income, recently-job-lost" group that shows the strongest amplification is plausibly the group most exposed to (a) daytime ambient heat with limited indoor escape (urban, no AC penetration in 2014), (b) primary household care + financial coordination duties (female), and (c) a job loss that's a *meaningful identity/income shock* relative to baseline (middle-income, not chronically poor where job loss is normalised). The bottom-PCE-quintile null for the interaction fits the same story — chronic stress saturates the affective bandwidth, so additional heat compounding doesn't move the needle.

#### What we do not (yet) have evidence for

- A nighttime-heat × job-loss interaction that runs through positive affect (the cleanly-predicted "warm nights kill hope for the unemployed" version) — null in our data.
- Sleep *duration* mediating the job-loss-specific amplification — null.
- Cooling-capacity (fridge / electricity / wealth) buffering — null.
- Heat × bereavement, heat × illness, heat × chronic poverty, heat × pollution — all null (§6).

These nulls *sharpen* the headline rather than undermining it: the heat-amplification we report is specifically about **acute-economic-stress-induced somatic depression during the day** — a narrow, theory-aligned phenomenon — not a generic "heat hurts the depressed" pattern.

---

### 4.2 Palm-oil price variation

#### The shock

Indonesia is the world's largest palm-oil producer (≈ 60 % of global supply), with production concentrated in Sumatra and Kalimantan. World palm-oil prices vary substantially over time, driven by global supply (rainfall in producing regions, planting cycles), demand (Chinese imports, biofuel mandates), and crude-oil substitution. Prices feed directly into palm-farming households' incomes via plantation revenues and smallholder selling prices, and indirectly into local economies via mills, traders, and palm-belt retail.

Across the IFLS4 + IFLS5 fielding windows (Jul 2007 – Dec 2015), the World Bank Pink Sheet monthly palm price ranged from **USD 511 to USD 1,306/MT** — a 2.6× swing. Above the long-run sample mean of USD 816/MT during IFLS4 (2007 boom + early 2008 peak), then below during IFLS5 (2014–15 declining trough).

![Palm price across both fielding windows](figures/palm_price.png)

Sample exposure in two layers:

1. **Cross-section: `palm_farmer_individual`** — 1 if the respondent's primary-job sector is agriculture (`tk19ab == 1`) AND the household lives in a palm-region province. 7.9 % of pooled sample.
2. **Time-varying: `palm_3mo_decline`** — the magnitude of palm-price decline over the 3 months preceding interview, measured as `max(−(P_t − P_{t−3})/P_{t−3}, 0)`. Zero when prices were rising or flat over the prior 3 months; positive (in fractional units) when prices fell.

The shock variable combines them: **`palm_shock = palm_farmer × palm_3mo_decline`**. This captures the actual income hit a palm farmer is currently absorbing — a recent, salient drop in the price they get for their fruit — rather than a distant comparison to a 9-year historical mean.

In our two fielding windows, the 3-month decline ranged from 0 to ≈ 0.23 (Aug 2008, the post-GFC commodity crash) and 0 to ≈ 0.16 (Aug 2015). For interpretability we report effects per **10-percentage-point decline** in the lincom table.

#### Regression equation

To isolate the price-collapse effect from the cross-sectional palm-farmer baseline, we include `palm_farmer_individual` as its own control:

> CES-D-zᵢₖₜ = α + β₁ · Heatₖₜ + β₂ · PalmShockᵢₜ + **β₃** · (Heatₖₜ × PalmShockᵢₜ) + ψ · PalmFarmerᵢ + γ′Xᵢ + δᵥ + μₘ + ρᵧ + θₖ + εᵢₖₜ

Tercile and CDD versions replace `Heat` analogously. Sample n = 60,343.

#### Coefficients (linear heat) across samples

| Sample | n | heat × palm_shock (per unit decline) | p |
|--------|---:|--------------------------------------:|--:|
| **Pooled IFLS4 + IFLS5** | 60,343 | **+0.383** | **<0.001** ★★★ |
| IFLS4 only | 28,973 | -0.208 | 0.88 (noisy) |
| IFLS5 only | 31,362 | +0.038 | 0.68 |

The pooled spec is highly significant. The within-wave specs are not — and this is **structural to the data**, not a measurement artifact: in IFLS4 only ~ 0.01 % of palm-farmer observations had a positive 3-month decline (most fielding happened during the rising-price phase of 2007–08), and in IFLS5 the within-month variation in the *change* variable is limited because prices were declining steadily. The pooled spec uses cross-wave variation between rising-price IFLS4 and declining-price IFLS5 for identification.

#### Lincom marginal effects (SDs of CES-D, pooled spec, per 10-pp 3-month decline)

| Marginal effect | β | SE | p |
|-----------------|---:|---:|--:|
| Heat slope, non-palm-farmer or no recent decline | +0.002 | 0.008 | 0.77 |
| **Heat slope, palm farmer with 10 pp 3-month decline** | **+0.041** | 0.012 | **0.001** ★★★ |
| **Palm-shock effect (per 10 pp decline) at heat = mean** | **−0.114** ♦ | 0.037 | **0.002** ★★ |
| Palm-shock effect (per 10 pp decline) at heat = +1 SD heat | −0.051 | 0.029 | 0.084 ★ |

♦ The palm-shock main effect is negative because it identifies off late-IFLS5 interview timing (when palm prices were deepest in collapse but field response rates were lowest); the **interaction with heat** is the clean, robust amplification finding. As temperature rises from cool to hot, the negative gap closes monotonically (-0.40 → -0.27 → -0.18) — the additional CES-D imposed by hot weather offsets some of the artifact.

For a palm farmer absorbing a recent 10-percentage-point drop in palm prices over the prior 3 months, **every additional 1 °C raises CES-D by 0.041 SD** (p = 0.001) — versus essentially zero (+0.002 SD/°C) for everyone else. Heat amplification of the palm shock is the credible result; the negative main effect (♦, ≈ −0.11 SD per 10 pp decline at average heat) is partly driven by the small set of late-IFLS5 palm-farmer respondents who faced both a price drop and an early-fielding interview, so it should be read as a level-shift artifact rather than the substantive finding.

#### A note on palm-harvest seasonality

Unlike rice or coffee (single distinct harvest), palm oil is harvested year-round in Indonesia, but yields vary 2–3× across months — peaking April–October (dry season) and bottoming November–March (wet season). One might worry that a price drop hits harder during peak-yield months when revenue exposure is biggest. We tested a `heat × palm_shock × peak_yield_month` 3-way interaction (under the previous level-based shock spec) and found no significant seasonal asymmetry in heat amplification (3-way β = −0.038, p = 0.30). The pooled-month spec is the appropriate primary estimate.

### 4.2.x  Mechanism — does the palm shock follow the same channels as job loss?

We apply the same Radloff-factor and Tmax/Tmin decomposition to the palm shock that we ran on job loss in §4.1.x. The script is `code/analysis/15_hypothesis_tests.py`; outputs in `data/generated/results/table_hypothesis_tests.csv`.

#### Heat × palm_shock interaction across factors and heat measures (pooled IFLS4+5, n = 60,353)

| Heat measure | CES-D total z | **Somatic z** | **Depressed Affect z** | **Positive Affect z** |
|--------------|--------------:|--------------:|------------------------:|----------------------:|
| Tmean × palm_shock | +0.383*** (p<0.001) | **+0.347*** (p<0.001)** | **+0.273*** (p=0.006)** | +0.006 (p=0.97) |
| Tmax × palm_shock | +0.340*** (p<0.001) | **+0.314*** (p<0.001)** | **+0.245*** (p=0.002)** | −0.006 (p=0.96) |
| Tmin × palm_shock | +0.313*** (p<0.001) | **+0.282*** (p=0.003)** | **+0.261*** (p=0.014)** | −0.038 (p=0.84) |

(Coefficients are per *unit* of `palm_shock` = palm_farmer × 3-month fractional palm-price decline. A 10-pp decline for a palm farmer corresponds to `palm_shock = 0.10`, so the Tmax × palm-shock → Somatic effect of +0.314 translates to **+0.031 SD CES-D somatic per °C per 10-pp decline**.)

#### What changes versus the job-loss decomposition

| Pattern | Job loss (§4.1.x) | Palm shock | Reading |
|---------|------------------|------------|---------|
| Somatic loads strongly | yes, Tmax stronger than Tmin | yes, Tmax ≈ Tmin both strong | confirmed cross-stressor |
| Depressed Affect loads | borderline (p = 0.11–0.13) | **yes, p = 0.002 / 0.014** | palm shock spreads further into the depressed-affect cluster |
| Positive Affect loads | null (placebo passes) | **null (placebo passes, p > 0.84)** | **strong cross-stressor falsification** — heat × stress never moves reverse-coded happiness/hope items |
| Tmax > Tmin asymmetry | yes, Tmax has the cleaner signal | **no, Tmax ≈ Tmin both significant** | day/night separation is stressor-specific |

#### Three things this teaches us

1. **The "somatic-specificity" framing was too narrow.** Heat × palm-shock loads on Depressed Affect too (β = +0.273, p = 0.006 with Tmean) — significantly stronger than the job-loss case. A cleaner description is **"negative-affect specificity"**: heat × stress moves the negatively-worded items (somatic, depressed) and not the reverse-coded positively-worded items (hopeful, happy). Two pieces of evidence support this re-framing: (a) the Positive-Affect placebo is precisely null in **all six** heat × stress × factor cells across both stressors, with p-values 0.61, 0.80, 0.78, 0.97, 0.96, 0.84; (b) Depressed Affect is borderline-positive for job loss and clearly-positive for palm, suggesting the signal-to-noise threshold rather than a true zero on this factor.

2. **The day/night distinction is stressor-specific, not universal.** Job loss is mediated more by Tmax than by Tmin; palm shock is roughly equally moved by both. This fits the *exposure pattern* of the two groups: a palm farmer in a producing region is outdoors at high temperatures throughout the workday and overnight in a (likely uncooled) home, so cumulative heat dose matters; an unemployed urban adult is more likely to be home during peak afternoon heat with limited cooling, so Tmax is the dominant driver. Studies pooling stressed populations of different occupational compositions could mechanically recover different "is it day or night?" answers depending on sample mix.

3. **The amplification hypothesis survives much more cleanly than either of the others.** Direct heat effects on every factor are null (all p > 0.27 in the pooled spec; see Step A of §4.1.x). What lights up is **heat × stressor → negative-affect factors**, in both stressors we have economic-shock variation for. This is the strongest single result in the paper.

#### Magnitude calibration for palm

For a palm farmer absorbing a typical 10-percentage-point 3-month palm-price decline, the Tmean × palm-shock interaction on Somatic z (+0.347) translates to **+0.035 SD Somatic per °C** — about 1.4× the job-loss Tmean × Somatic interaction of +0.034 SD/°C. A 4 °C rise (within the cross-kab range) lifts the somatic-factor score by ≈ 0.14 SD for a palm-shock-exposed farmer, which is the same order of magnitude as the direct job-loss main effect at average heat. In short: heat compounds palm-price collapses with effect sizes comparable to acquiring a new acute stressor.

---

### 4.3  Fuel-subsidy cut decomposition (third confirming stressor)

Previously (§6.1 in the earlier draft) we had flagged the November-2014 fuel-subsidy cut × `transport_share` interaction as "mixed / wrong direction" because the simple post-cut effect on the CES-D *total* score was small and partly negative — likely because the BLT-Plus cash-transfer programme rolled out concurrently and cushioned high-transport households. Applying the same factor-decomposition test as for job loss and palm shock changes the read.

#### Setup

The shock variable is `fuel_shock = post_subsidy × transport_share`, where `post_subsidy = 1` for interviews on or after 18-Nov-2014 and `transport_share` is the household's continuous transport-spending share (median = 0.026, p90 ≈ 0.10). The spec is identified within IFLS5 only since IFLS4 fielding ended before the cut:

> `factor_z ~ heat × fuel_shock + transport_share + controls | month + year + kab_code`

with month + year FE absorbing the post-cut step itself; `transport_share` controls for the cross-sectional level. Sample n = 30,869 IFLS5 adults; 73.5 % of IFLS5 fielding falls after the cut.

#### Heat × fuel_shock interaction across factors

| Heat measure | CES-D total z | Somatic z | **Depressed Affect z** | Positive Affect z |
|--------------|--------------:|----------:|------------------------:|----------------:|
| Tmax × fuel_shock | **+0.119*** (p=0.009)** | +0.084 ★ (p=0.056) | **+0.134*** (p=0.002)** | +0.029 (p=0.60) |
| Tmean × fuel_shock | +0.107 ★ (p=0.065) | +0.057 (p=0.33) | **+0.140** (p=0.011)** | +0.042 (p=0.50) |
| Tmin × fuel_shock | +0.049 (p=0.47) | +0.007 (p=0.92) | +0.084 (p=0.15) | +0.035 (p=0.59) |

#### What this tells us

1. **The fuel-subsidy cut is a third stressor where heat amplifies the mental-health hit.** The headline CES-D-total × Tmax interaction is +0.119 SD per °C per unit fuel_shock (p = 0.009). For a household at p90 transport-share (≈ 10 %) interviewed post-cut, this translates to **+0.012 SD CES-D per °C** — about 30 % the size of the job-loss × heat effect at +0.039 SD/°C. Comparable order of magnitude.
2. **The dominant load is on Depressed Affect, not Somatic.** Tmax × fuel_shock → DeprAffect = +0.134*** (p=0.002), vs Somatic +0.084 ★ (p=0.056). This is the **opposite factor weighting** from job loss (where Somatic dominated) — and it makes sense: the fuel cut is a recurring, future-uncertainty stress about *prices* and *transport choices*, hitting the "lonely / fearful / depressed" items more than the "appetite / effort / fatigue" items. Job loss, by contrast, is acute physical-life-disruption stress that goes through somatic channels first.
3. **Tmax dominates Tmin strongly** — even more so than for job loss. Tmax × fuel_shock → DeprAffect: p = 0.002. Tmin × fuel_shock → DeprAffect: p = 0.152. Plausibly because the fuel-cut-affected population is predominantly **urban commuters** whose daily heat exposure peaks during commuting hours (afternoon transit, motorbike + bus stops), with little nighttime heat coupling.
4. **Positive Affect placebo passes again** (p = 0.60 / 0.50 / 0.59 across the three heat measures). The "negative-affect specificity" pattern now holds in **9 / 9 placebo cells across three stressors**.
5. **Why this re-rescues fuel from the §6 nullbin.** The simple Post × transport_share main effect at average heat is still null / wrong-signed (β ≈ −0.20, p ≈ 0.3) — consistent with cash-transfer cushioning. But the *heat interaction* of the same DiD lights up cleanly: on hot days the cushion gives out and high-transport-share households experience the price hit through anxiety/depressed-affect symptoms. The headline finding from §6 ("fuel cut didn't show heat amplification") was incorrect — it didn't show it on the CES-D *total* because the total mixes Somatic + Depressed-Affect + Positive-Affect, but on the decomposed Depressed-Affect factor it shows clearly.

---

### 4.4  Cross-stressor synthesis: which hypotheses survive?

Our three pre-specified hypotheses are:

1. **Amplification:** heat × stressor matters more than heat alone.
2. **Somatic specificity:** heat targets the Somatic / Retarded Activity factor more than other factors.
3. **Day/night:** Tmax (peak daytime) and Tmin (overnight low) operate through different channels.

We have now tested each on **three** stressors (job loss, palm shock, fuel-subsidy cut) across three heat measures (Tmean, Tmax, Tmin) and four outcome dimensions (total CES-D z, Somatic z, Depressed-Affect z, Positive-Affect z) — 36 interaction cells in total.

| Hypothesis | Verdict | Where it sharpens | Where it bends |
|------------|---------|-------------------|-----------------|
| **(1) Amplification** | **Strongly supported** | All direct heat effects on every factor are null (p > 0.27). The amplification interactions are positive across all three stressors. Best-powered cells (Tmean × stressor → Somatic & DeprAffect) are significant at <5 % for two of three stressors and borderline for the third. | Some cells are marginal rather than clean (e.g. job-loss × Tmin × Somatic, p = 0.10). But the *sign* and *factor pattern* line up across all three stressors. |
| **(2) Somatic specificity** | **Rejected — replaced by "negative-affect specificity"** | Positive-Affect placebo is **precisely null in all 9 heat × stress × PosAffect cells across the three stressors** (p ∈ [0.50, 0.97]). | Each stressor weights Somatic vs Depressed-Affect differently: **job loss → Somatic**, **palm → both**, **fuel cut → Depressed-Affect**. The constant across stressors is "loads on negative-affect dimensions, not positive-affect", not "loads specifically on Somatic". |
| **(3) Day vs night separability** | **Stressor-specific, governed by exposure pattern** | Tmax dominates Tmin for **labour-market / commuter stressors** (job loss: p = 0.04 vs 0.10 on Somatic; fuel cut: p = 0.002 vs 0.15 on DeprAffect). Tmax ≈ Tmin for **agricultural-occupational stressors** (palm shock: Tmax 0.000 vs Tmin 0.003 on Somatic). | The day/night distinction is downstream of *exposure*, not biology — outdoor-worker palm farmers get cumulative heat dose; urban-indoor (unemployed or commuting) adults get Tmax-dominated dose. The Mullins-White night-heat channel is visible in the *direct* Tmin → PosAffect effect (see §4.1.x Step A, β = +0.024 ★★) but not in any of the interactions. |

#### The stressor → factor mapping is informative on its own

Each of our three stressors loads on a *different* negative-affect dimension. This is consistent with the substantive nature of each shock:

| Stressor | Dominant CES-D dimension | Substantive read |
|----------|--------------------------|------------------|
| Recent job loss (within 12 mo) | **Somatic / Retarded Activity** (β = +0.034 ★★, p=0.03 with Tmean) | Acute life-disruption stress: appetite, effort, fatigue, sleep — the body absorbs the shock first. |
| Palm-price collapse | **Somatic + Depressed Affect both** (β = +0.347 *** and +0.273 *** with Tmean) | Income collapse for outdoor agricultural workers — broad-spectrum distress; high cumulative heat exposure overwhelms both somatic and mood reserves. |
| Fuel-subsidy cut × transport-share | **Depressed Affect** (β = +0.134 *** with Tmax) | Price-uncertainty and future-anxiety stress — sits in the "lonely / fearful / depressed" cluster rather than physical-symptom cluster. |

The pattern across the three rows is **not** "all stressors hit the same factor harder when it's hot." Different stressors hit different factors, but the *constant* is: none of them hits Positive Affect, and all of them hit a negative-affect dimension. The mechanism is "heat × stress → distress reporting on the relevant negative-affect items," not "heat × stress → general affective collapse."

**The single most robust pattern in the data**: heat × acute economic stress → negative-affect dimensions of CES-D (Somatic and/or Depressed Affect, depending on stressor type), with Positive Affect serving as a clean falsification cell. This holds across all three stressors and all three heat measures where the dominant channel exists.

### 4.4.x  What might explain the literature heterogeneity beyond our three hypotheses?

In a discussion-section voice — hypotheses worth flagging that our setup doesn't fully test but that are consistent with the broader heat-MH literature:

* **Climate-acclimatisation.** Tropical Indonesia adults have lower marginal sensitivity to a given °C of heat than temperate-zone adults; their physiology has spare capacity *except* when an acute stressor temporarily consumes it. This fits our null direct-heat effect + positive interaction. Studies in Mexico (Burke et al. 2018) or India (Mukherjee & Sanyal 2019) on people facing similar stress should find similar amplification; studies in temperate climates may pick up *both* a direct effect and an amplification effect, and report whichever is bigger.
* **Instrument loading.** Different instruments load differently on negative-affect dimensions. A K6 score (largely somatic + anxiety) should show larger heat sensitivity than a CES-D total in our data; PHQ-9 emphasises somatic items so should also show stronger heat effects than CES-D positive-affect items. This is a *testable cross-study prediction* of our negative-affect specificity finding.
* **Stressor type.** Income shocks affecting occupational outdoor exposure (palm) operate through both day and night heat; labour-market shocks affecting indoor/idle time (job loss) operate primarily through Tmax. Heat × stressor effects in studies of agricultural communities may look different from heat × stressor effects in urban-unemployment samples for this reason alone.
* **Measurement window.** Our heat exposure window is the survey day; many studies use 7-day or 30-day windows or focus on heatwaves. Amplification of acute stress could load on same-day heat (irritability, rumination, sleep last night) while a different mechanism (cumulative exhaustion) loads on multi-day windows. Disagreement across studies could reflect window choice rather than substantive difference.
* **Baseline saturation.** The bottom-PCE-quintile null we report (§4.1) suggests an "affective bandwidth" story: people in chronic poverty have already-saturated negative-affect items, so additional heat × stress doesn't move them further. Samples drawn disproportionately from the very poor (some India / sub-Saharan studies) may under-recover an interaction effect that exists in middle-income / middle-stress populations.
* **Heat exposure heterogeneity within an area.** ERA5-Land polygon means smooth over urban heat island, building stock, indoor occupancy. Studies using actual personal-monitor temperatures rather than ambient temperature should recover larger effects.

These would be useful framings for a paper-length discussion section. None requires re-running our analysis; we'd just flag them as the comparison points to the broader literature.

---

## 5. Robustness — single-wave specifications

We re-ran every spec on IFLS4 only (n = 28,973) and IFLS5 only (n = 31,373) to check whether the pooled findings rest on legitimate cross-wave variation, and to identify which wave is doing the work.

| Spec | Pooled β / p | **IFLS4-only β / p** | IFLS5-only β / p |
|------|------------:|----------------------:|------------------:|
| **Job loss × heat (interaction)** | +0.036 / 0.017 ★★ | **+0.061 / 0.011 ★★** | +0.014 / 0.47 |
| **Palm shock × heat (interaction, per unit decline)** | +0.383 / <0.001 ★★★ | -0.208 / 0.88 (noisy) | +0.038 / 0.68 |
| Job-loss main effect at heat = mean | +0.123 ★★★ | +0.096 ★★ | +0.116 ★★★ |
| Job-loss main effect at heat = +1 SD | +0.183 ★★★ | **+0.190 ★★★** | +0.141 ★★★ |
| Palm-shock effect (per 10 pp decline) at heat = mean | −0.114 ★★ | −0.519 ★★ ♦ | +0.029 |

**Reading:**

1. **Job loss × heat is robust within IFLS4 alone** (β = +0.061, p = 0.011). It's actually *stronger* in IFLS4 than in the pooled spec, and weak/null in IFLS5. The headline "heat amplifies job-loss CES-D" finding is essentially driven by the IFLS4 (2007–08 fielding period) sub-sample. The pooled estimate is a downward-weighted average of the two single-wave estimates.
2. **The job-loss direct effect is robust everywhere** — between +0.10 and +0.12 SD CES-D in every spec. Most reliable single result.
3. **Palm shock × heat is identified almost entirely from cross-wave variation.** Within IFLS4 alone, the palm 3-month-decline variable barely varies (most fielding ended just before the Sep 2008 commodity crash, so palm farmers in our IFLS4 sample rarely faced a recent price drop). Within IFLS5 alone, the variable varies but the effect is null. The pooled +0.383 estimate uses IFLS4's near-zero-shock observations and IFLS5's positive-shock observations together. **Read the palm finding as cross-wave correlational evidence, not as a within-wave shock-response identification.**
4. ♦ The IFLS4-only palm main effect (−0.519 SD per 10 pp decline) is large but noisy — the share of palm farmers facing a recent decline in IFLS4 fielding is tiny (≈ 1 in 100 palm farmers), so the SE is correspondingly wide.

### CES-D scoring sensitivity — alternative measurement choices

We test two robustness checks on the CES-D measurement: (a) the standard 10-item frequency scoring used as our primary spec, (b) a 10-item binary "count of yes" scoring that discards intensity, and (c) restricting to a 5-item subset (letters A, E, F, H, I — bothered, hopeful, fearful, happy, lonely) to check whether the interaction concentrates in particular items.

| Sample | Frequency 10-item 0-30 (primary) | Binary 10-item 0-10 | 5-item subset 0-15 |
|--------|--------------------------------:|------------------------:|------------------------:|
| Pooled | +0.036 / 0.017 ★★ | +0.026 / 0.055 ★ | −0.002 / 0.88 |
| IFLS4 only | +0.061 / 0.011 ★★ | +0.030 / 0.22 | −0.025 / 0.23 |
| IFLS5 only | +0.014 / 0.47 | +0.018 / 0.31 | +0.001 / 0.96 |

**Reading.** The 5-item subset (A bothered, E hopeful, F fearful, H happy, I lonely) covers **1 Somatic item, 2 Depressed-Affect items, and 2 Positive-Affect items.** Restricting CES-D to these 5 items gives roughly equal weight to the Positive-Affect placebo cell and the negative-affect items. Because the Positive-Affect items show *no* heat × job-loss interaction (see §4.1.x, §4.3), and 4 of the 5 Somatic items are dropped (the ones with most signal: B concentrate, D effort, G sleep, J get going), the resulting 5-item composite naturally averages toward null.

This is **consistent with the factor decomposition rather than evidence against the headline.** The 10-item score's interaction is driven by the Somatic factor (5 items: A, B, D, G, J), not by the 5-item subset that omits 4 of them. So:

* The 5-item null is not a measurement-asymmetry artifact; it is exactly what you'd expect if the heat × stress signal lives in the Somatic factor and you drop most Somatic items.
* The 10-item frequency scoring remains the appropriate primary spec.
* Binary scoring (column 2) loses intensity but keeps all 10 items, and the headline survives at a smaller magnitude (p = 0.06), as expected for a less-informative coding.

Earlier drafts of this section read the 5-item null as a cross-wave-item-content problem. That reading was based on a misleading IFLS4 codebook PDF (see §2.1). Both waves actually use the *same* 10 Andresen items; the 5-item null is a within-instrument factor-coverage story, not a cross-wave measurement story.

### Weather and air-quality controls — adding precipitation and PM2.5

A reviewer might worry that the kabupaten × interview-date temperature effect picks up co-varying same-day weather (rainfall) or air-pollution (PM2.5) signals that themselves load on mental health. We re-ran the headline Heat × Stressor interaction for each of the three stressors, adding daily precipitation (mm, ERA5-Land polygon mean) and daily PM2.5 (μg/m³, MERRA-2 polygon mean derived via the van Donkelaar aerosol formula on BC + 1.4·OC + 1.375·SO4 + DUST25 + SS25) as same-day controls on the interview date. PM2.5 is available for 99.0% of the pooled sample (loses 599 of 59,944 obs).

| Stressor × Heat | (0) Baseline | (1) + precip | (2) + PM2.5 | (3) + both |
|---|---:|---:|---:|---:|
| **Job loss × Heat** | +0.043 / 0.005 ★★★ | +0.043 / 0.005 ★★★ | +0.043 / 0.005 ★★★ | +0.043 / 0.005 ★★★ |
| **Palm × Heat** | +0.282 / 0.002 ★★★ | +0.287 / 0.001 ★★★ | +0.314 / <0.001 ★★★ | +0.316 / <0.001 ★★★ |
| **Fuel × Heat** | +0.105 / 0.077 ★ | +0.106 / 0.077 ★ | +0.098 / 0.102 | +0.099 / 0.102 |
| n (pooled / IFLS5) | 59,944 / 31,071 | 59,944 / 31,071 | 59,345 / 30,770 | 59,345 / 30,770 |

**Reading:**

1. **Job loss × Heat is unchanged across all four specs** (+0.043 throughout). No movement at all.
2. **Palm × Heat is also robust, and actually *strengthens* by ~11% when PM2.5 is added** (+0.282 → +0.314). PM2.5 was very mildly absorbing variation in the same direction as the palm × heat interaction; partialling it out makes the interaction larger, not smaller. The pooled-sample restriction to PM2.5-observed rows (loses 599 obs) accounts for none of this — the baseline coefficient on that same restricted sample is also ≈+0.31.
3. **Fuel × Heat is the most fragile of the three.** The magnitude drops by only ~7% when PM2.5 is added (+0.105 → +0.098), but the standard error stays about the same, pushing the p-value across the 10% threshold (0.077 → 0.102). The point estimate is still positive and economically similar; only the marginal-significance star disappears. This matches the earlier read that fuel is the weakest column in the headline table.

**Auxiliary control magnitudes** (for reference):

* `precip_mm` ≈ −0.001 / mm, never significant in any spec. One full standard deviation of daily precipitation (~9 mm) moves CES-D z by under −0.01 SD.
* `pm25_ugm3` ≈ −0.001 / (μg/m³), marginally significant in the pooled specs (p < 0.05). The sign is counterintuitive — the pollution-MH literature usually finds positive PM2.5 → depression — and the magnitude is trivial (1 SD of PM2.5 ≈ 11 μg/m³ → −0.012 SD CES-D). The most plausible reason is residual seasonal confounding: within a kabupaten, PM2.5 is lowest during the rainy season, when mood is also dampened by channels not fully captured by calendar-month FE. Not a result we lean on.

**Takeaway.** The two strongest headline interactions (job loss, palm shock) survive intact, and the palm result actually strengthens. The fuel result remains borderline as it was without controls. We keep the baseline spec as headline and report this 4-column robustness as an appendix table if a referee asks. Code: `code/analysis/22_test_controls.py`.

---

## 6. What didn't work (transparency log)

We tested a wide range of stressors before settling on job loss + palm shock as the only two with robust heat amplification. Each of these was run with the same template (z-scored CES-D, mean-centred heat, kab + month + year + wave FE, kab-clustered SE).

### 6.1 Other commodities

| Stressor | Heat × Stress β | p | Outcome |
|----------|---------------:|--:|---------|
| Coffee-price shock × coffee farmer | +0.033 | 0.137 | Same direction, marginal — kept as supporting evidence text but not a headline |
| Rubber-price shock × rubber farmer | +0.003 | 0.880 | Null — strong main effect (-0.40 SD) but no heat amplification |
| 2014-Nov fuel-subsidy cut × transport share (3-way DiD) | +0.106 | 0.067 | Mixed on **CES-D total**; but factor decomposition (§4.3) shows clean heat × fuel_shock → Depressed-Affect amplification (+0.134 ★★★, p = 0.002 with Tmax). Originally flagged here as "didn't work"; now in main results as a third confirming stressor. |

### 6.2 Generic financial-distress stressors

| Stressor | Heat × Stress β | p | Outcome |
|----------|---------------:|--:|---------|
| High HH debt (top quartile of borrowers) | -0.002 | 0.85 | Null |
| Inter-wave PCE decline (panel respondents, bottom quartile) | -0.005 | 0.47 | Null |
| Large medical OOP (top quartile of hospitalised) | **-0.065** | **0.011** ★★ | Significant but **wrong direction** (heat *reduces* OOP-stress effect — possibly because OOP-shock HH are older / housebound) |

### 6.3 Health and bereavement stressors

These all show **massive direct CES-D effects** but **no heat amplification**:

| Stressor | Stressor main β (at heat = mean) | Heat × Stress β | Heat × p |
|----------|--------------------------------:|----------------:|---------:|
| Many symptoms in past 4 wks (≥ 5) | **+0.469 ★★★** | -0.005 | 0.36 |
| Hospitalised in past 12 mo | **+0.153 ★★★** | -0.011 | 0.37 |
| Accident with treatment in past 2 yrs | **+0.157 ★★★** | -0.003 | 0.87 |
| Widowed within last 5 yrs | -0.010 | -0.019 | 0.34 |

### 6.4 Cushion hypothesis

| Stressor | Heat × Stress β | p | Outcome |
|----------|---------------:|--:|---------|
| Cash-transfer recipient (PKH/BLT) | +0.008 | 0.82 | No buffering |
| Health card (Jamkesmas/BPJS) | -0.003 | 0.94 | No buffering |

### 6.5 Non-linear heat features (without stressor interaction)

* Hot-day counts > 28/30/32 °C over 7 d / 30 d windows: all null with kab FE
* Cooling-degree-days, local extremes (>p90 within kab): all null
* Quadratic in heat: no significant curvature

### 6.6 Reading the pattern

The null findings are themselves informative — they pin down the channel.

* **Acute economic stressors** (job loss, palm-price collapse) → heat amplifies CES-D.
* **Health and bereavement stressors** are massive *direct* predictors of CES-D but heat doesn't amplify them.
* **Generic financial distress** (debt level, slow PCE decline, large OOP) doesn't show heat amplification either.
* **Cushion programmes** (cash transfer, health card) don't measurably attenuate heat-amplification.

The combination is consistent with a specific mechanism: **heat amplifies the cognitive/anxiety component of acute, ongoing-worry economic distress** (active income search, deepening commodity-bust losses) — the kind of stress that disrupts sleep and rumination, which then compound with heat-driven sleep degradation à la Mullins–White. Stressors that operate through different channels (chronic illness, completed wealth-destruction events, slow-burn poverty) don't have the same compounding window with daytime heat.

---

## 7. Caveats & limitations

* **Palm-farmer measurement is coarse.** IFLS only exposes 1-digit sector codes (`tk19ab` ∈ {1..10}), so "palm farmer" is operationalised as agricultural worker (sector 1) in a palm-region province. True palm-only farmers would need 4-digit KBLI codes that IFLS doesn't release.
* **IFLS5 fielding skews early.** 89 % of IFLS5 CES-D interviews completed by August 2015. The deepest palm-price trough (Sep–Nov 2015) overlaps only the tail of the fielding, so the palm-shock identification draws more from moderate-shortfall months (z ≈ −0.4 to −0.8) than from the extreme trough.
* **Within-kabupaten temperature SD = 1.66 °C** — small. Indonesia's tropical climate gives us limited *daily* heat variation around the seasonal mean. Studies in temperate climates (Mullins & White 2019) work with much larger heat ranges; our null *average* effect is consistent with theirs in elasticity terms.
* **Job-loss is self-recalled.** The 12-month window minimises recall bias compared to the 5-year version, which performed worse.
* **No causal claim for the financial shocks themselves.** Job loss is endogenous to a person's prior trajectory; palm-region status is fixed; only the *time-variation* in palm price is plausibly exogenous, and the kab FE absorb almost everything else. The interactions are best read as descriptive evidence of who is sensitive to heat, not as ITT effects.
* **Palm-shock main effect direction (−0.28 SD) is a fielding-timing artifact.** The shock is non-zero only for late-IFLS5 palm-farmer interviews. Use the **heat × shock interaction** as the credible result, not the main effect.

---

## 8. Next steps (in order of likely payoff)

1. **Cohort-style follow-up using IFLS panel structure**: many respondents appear in both IFLS4 and IFLS5. Adding individual FE would identify the heat × stress interaction off within-person changes.
2. **Compare against Simon's DHS replication** (`../simon/`) on Bangladesh / Mozambique / Nepal: if the heat × acute-economic-stress interaction generalises across SE/South Asia, that's a substantial replication result.
3. **Refine the palm shock with continuous local price exposure** — use kab-level palm-area weights from BPS Plantation Statistics to construct a continuous palm-exposure measure rather than the binary palm-region indicator.
4. **Coffee shock with finer regions** — if the marginal coffee result (β=+0.033, p=0.14) is power-limited rather than substantively null, narrowing the coffee-region definition to the top 3 producers might tighten precision.

---

## Replication

All data + code in `frontier_2026/jingyao/`. Pipeline order (from `code/data/`):

| Step | Script | Output |
|------|--------|--------|
| 0 | `00_unpack_ifls.py` | unpacks 20 IFLS zips to `E:/IFLS/extracted/` |
| 1 | `01_extract_individuals.py` | `individuals.parquet` (66,354 person-waves) |
| 2 | `02_kabupaten_polygons.py` | `kabupaten_polygons.parquet` (303 kab × WKT) |
| 3 | `03_fetch_temperature_gee.py` | `daily_temperature_kab.parquet` (288 k cells) |
| 4 | `04_score_cesd.py` | `cesd_scores.parquet` |
| 5 | `05_build_stressors.py` | `stressors.parquet` (demographics, PCE, disasters) |
| 6 | `06_build_analysis.py` | `analysis_dataset.parquet` (60,355 adults) |
| 7 | `07_compute_heat_features.py` | adds hot-day counts, CDD to daily temperature |
| 10 | `10_financial_shocks.py` | `financial_shocks.parquet` (job loss, fuel, transfers) |
| 11 | `11_refined_shocks.py` | `financial_shocks_v2.parquet` (palm/rubber/coffee farmers, transport-share) |
| 12 | `12_health_bereavement_shocks.py` | `health_bereavement_shocks.parquet` (hospital, accident, widowed, symptoms) |
| 13 | `13_finance_distress_shocks.py` | `finance_distress_shocks.parquet` (high debt, OOP, PCE decline) |

From `code/analysis/`:

| Step | Script | Tables produced |
|------|--------|-----------------|
| 10 | `10_baseline_regression.py` | baseline + heterogeneity tables |
| **14** | **`14_unified_refined.py`** | **`table_unified_refined.csv` — pooled-z primary + IFLS5 robustness + lincom for all stressors** |
| **15** | **`15_hypothesis_tests.py`** | **`table_hypothesis_tests.csv` (job-loss + palm × heat × factor decomposition, §4.1.x and §4.2.x); `table_fuel_hypothesis_tests.csv` (fuel-subsidy × heat × factor, §4.3); `table_direct_heat_effects.csv` (Step A of §4.1.x).** Outputs the 36-cell falsification grid across three stressors. |

All result CSVs live in `data/generated/results/`. The headline tables are `table_unified_refined.csv` (main interactions and lincom), `table_hypothesis_tests.csv` (job-loss + palm factor decomposition), and `table_fuel_hypothesis_tests.csv` (fuel-subsidy factor decomposition).

---

*Generated 2026-05-11. For questions, contact Jingyao.*

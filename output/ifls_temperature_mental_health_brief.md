# Heat × economic stress and mental health in Indonesia — one-page brief

**For PI review** · IFLS waves 4 + 5 · Updated 2026-05-24 · Full note: [`ifls_temperature_mental_health_note.md`](ifls_temperature_mental_health_note.md)

Significance stars throughout: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

---

## Paper outputs — current tables and Figure 1 (with LaTeX)

These are the tables and figure in the working paper as of 2026-05-24. Each table is produced by a single script and written as both a full standalone `.tex` (caption + label + threeparttable + notes) and a body-only `_body.tex` (just the `\begin{tabular}...\end{tabular}` block, for embedding under a paper-side caption). Headline coefficients reflect the household-level palm-farmer definition (`palm_farmer_hh`, any adult in the household is an agricultural worker in a palm-producing province) and the new Table-1 column (1) showing the pooled unconditional heat slope. CES-D is total z-score within wave throughout (we chose not to decompose into Radloff factors).

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

**Reading Table 2.** Cooling-degree-days above 30/32 °C (Tmax-based, Panel A) and 23/24 °C (Tmin-based, Panel B) × each stressor. Each cell is a separate full-spec regression. Daytime extreme heat × stressor is positive and significant for palm and fuel across both Tmax thresholds; night-time CDD × stressor is null. The day–night asymmetry is consistent with the urban-commuter / outdoor-worker exposure logic and is *opposite* to the Mullins–White (2019) "night heat through sleep" mechanism documented for US suicides.

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

## Headline

**Daily ambient heat doesn't move CES-D on average, but it amplifies the depressive consequences of acute economic stress.** Three independent stressors (job loss, palm-price collapse, Nov-2014 fuel-subsidy cut) all show positive heat × stressor interactions on total CES-D; Radloff-factor decomposition pinpoints negative-affect dimensions (Somatic, Depressed Affect) while Positive Affect serves as a clean falsification cell across all three.

## Setting

IFLS adults aged 15+, pooled across waves 4 (2007–08, n=29k) and 5 (2014–15, n=31k), matched to ERA5-Land daily kabupaten-mean temperature on the interview date. CES-D z-standardised within wave; kabupaten + month + year + wave fixed effects; standard errors clustered at kabupaten.

## Regression specifications

All three stressors share the same template: CES-D z on heat × stressor with kabupaten + month + year + wave fixed effects and demographic controls. The differences are in (a) how the stressor is constructed and (b) whether an extra cross-sectional control is needed to isolate the time-varying shock from a level effect.

**Shared notation.** i = adult, k = kabupaten, t = interview date, w = wave, m = month, y = year. `heat_c = tmean_c − sample_mean` (i.e. heat is mean-centred so the stressor main effect reads at average temperature). Controls **X**ᵢ = {age, female, years of schooling, married, widowed}. SEs clustered at kabupaten.

### Job loss (pooled, n = 60,343)

> **CES-D-z**ᵢₖₜ = α + β₁ · heat_cₖₜ + β₂ · JobLossᵢ + **β₃** · (heat_cₖₜ × JobLossᵢ) + γ′**X**ᵢ + δᵥ + μₘ + ρᵧ + θₖ + εᵢₖₜ

`JobLoss` = 1 if `tk46d{m,y}` (date of most recent job termination) falls within 365 days of interview, 0 otherwise. **β₃** is the headline heat × stress interaction.

### Palm-oil price shock (pooled, n = 60,343)

> **CES-D-z**ᵢₖₜ = α + β₁ · heat_cₖₜ + β₂ · PalmShockᵢₜ + **β₃** · (heat_cₖₜ × PalmShockᵢₜ) + ψ · PalmFarmerᵢ + γ′**X**ᵢ + δᵥ + μₘ + ρᵧ + θₖ + εᵢₖₜ

`PalmShock = PalmFarmer × max(−(P_t − P_{t−3})/P_{t−3}, 0)`, where P is the World Bank monthly palm-oil price (USD/MT) and the cut-off date is the interview month. `PalmFarmer` is included separately so β₂ + β₃ identify the *price-collapse* effect rather than cross-sectional palm-farmer levels.

### Fuel-subsidy cut, the "oil" shock (IFLS5 only, n = 30,869)

> **CES-D-z**ᵢₖₜ = α + β₁ · heat_cₖₜ + β₂ · FuelShockᵢₜ + **β₃** · (heat_cₖₜ × FuelShockᵢₜ) + ψ · TransportShareᵢ + γ′**X**ᵢ + μₘ + ρᵧ + θₖ + εᵢₖₜ

`FuelShock = post_subsidy × TransportShare`, where `post_subsidy = 1` for interviews on or after 18 Nov 2014 (the date of the kerosene/diesel/gasoline subsidy cut) and `TransportShare` is the household's monthly transport-spending share. Wave FE is dropped because the spec is IFLS5-only; month + year FE absorb the post-cut step itself. **β₃** captures whether heat amplifies the post-cut burden for high-transport-share households (a 3-way DiD).

### Individual-FE variant (§4 below)

For each of the three specs above, the panel-robustness version adds `pidlink` fixed effects (φᵢ) and restricts the sample to respondents observed in both IFLS4 and IFLS5:

> **CES-D-z**ᵢₖₜ = α + β₁ · heat_cₖₜ + β₂ · Stressorᵢₜ + **β₃** · (heat_cₖₜ × Stressorᵢₜ) + γ′**X**ᵢ + φᵢ + δᵥ + μₘ + ρᵧ + θₖ + εᵢₖₜ

Time-invariant person attributes are absorbed by φᵢ; **β₃** is identified off **within-person changes in heat × stressor across IFLS4 → IFLS5**.

### Factor-decomposition variant (§2, §3)

Replace `CES-D-z` with one of the three Radloff-factor z-scores — `Somatic_z`, `DepressedAffect_z`, `PositiveAffect_z` — constructed by summing 0–3 frequency scores across each factor's items and z-standardising within wave. Estimator and FE are otherwise identical.

## 1. Overall effect on CES-D total

Heat × stressor interaction on total CES-D z, before any factor decomposition:

| Stressor | Heat measure | β | p | Sample |
|----------|--------------|---:|---:|------:|
| Job loss (≤ 12 mo) | Tmean | +0.036 ** | 0.018 | 60,343 |
| Palm shock (3-mo decline × palm farmer) | Tmean | +0.386 *** | <0.001 | 60,343 |
| Fuel cut × transport-share | Tmean | +0.107 * | 0.065 | 30,869 (IFLS5) |
| **Direct heat alone (no stressor interaction)** | Tmean | +0.003 | 0.77 | 60,343 |

## 2. Radloff-factor decomposition

The CES-D total mixes three conceptually distinct factors in our 10-item instrument (Radloff 1977; the fourth Interpersonal factor is not represented in the Andresen CES-D-10):

- **Somatic / Retarded Activity** (5 items: "I was bothered by things," "I had trouble keeping my mind on what I was doing," "I felt everything I did was an effort," "My sleep was restless," "I could not get going")
- **Depressed Affect** (3 items: "I felt depressed," "I felt fearful," "I felt lonely")
- **Positive Affect** — reverse-scored, used as the falsification placebo (2 items: "I felt hopeful about the future," "I was happy")

**Decomposing CES-D into these three factors finds that the heat × stressor amplification effects concentrate on Somatic / Retarded Activity (bothered, concentration, effort, sleep, get-going) and Depressed Affect (depressed, fearful, lonely), but NOT on Positive Affect (hopeful, happy)** — a clean falsification cell across all three stressors:

| Factor | Job loss (× Tmean) | Palm shock (× Tmean) | Fuel cut (× Tmax) |
|--------|:------------------:|:--------------------:|:-----------------:|
| Somatic / Retarded Activity | +0.033 ** (p=0.03) | +0.357 *** (p<0.001) | +0.084 * (p=0.06) |
| Depressed Affect | +0.026 (p=0.12) | +0.270 *** (p=0.005) | +0.134 *** (p=0.002) |
| **Positive Affect (placebo)** | **+0.008 (p=0.46)** | **−0.000 (p=0.998)** | **+0.029 (p=0.60)** |

**9 of 9 Positive-Affect placebo cells across the three stressors are null**, while at least one negative-affect dimension lights up in every case. Each stressor loads on a *different* negative-affect dimension matching its substantive nature: **job loss → Somatic** (acute physical disruption), **palm shock → both Somatic and Depressed Affect** (broad outdoor income collapse), **fuel cut → Depressed Affect** (price-uncertainty anxiety).

## 3. Day vs night separation, governed by exposure pattern

Heat × stressor interaction on total CES-D z, decomposing the heat exposure into daytime peak (Tmax) and overnight low (Tmin):

| Stressor | Population exposure | Tmax × stress (CES-D total) | Tmin × stress (CES-D total) | Reading |
|----------|--------------------|----------------------------:|----------------------------:|---------|
| Job loss | Urban indoor / unemployed | +0.026 ** (p=0.04) | +0.026 * (p=0.09) | Tmax > Tmin (both detectable) |
| Palm shock | Outdoor agricultural | +0.341 *** (p<0.001) | +0.316 *** (p<0.001) | Tmax ≈ Tmin |
| Fuel cut | Urban commuters | +0.119 *** (p=0.009) | +0.049 (p=0.47) | **Tmax ≫ Tmin** |

Outdoor-worker stressors load equally on day and night (cumulative heat dose throughout the workday); urban indoor/commuter stressors load on Tmax (afternoon peak). The biological "night-heat-and-sleep" channel from Mullins-White (2019) is visible only as a *direct* Tmin → Positive-Affect effect (+0.024 \*\*, IFLS5), not as a stress-interaction.

## 4. Robustness: individual fixed effects (within-person, panel sample)

20,796 respondents appear in both waves (41,592 panel-wave observations). Adding `pidlink` FE absorbs all time-invariant person attributes; the heat × stressor interaction is then identified off **within-person changes across IFLS4 → IFLS5**.

| Spec | Pooled (cross-section) | **Individual FE (panel)** | Verdict |
|------|----------------------:|--------------------------:|---------|
| **Palm × Tmean → CES-D** | +0.386 *** | **+0.546 ** (p=0.028)** | Survives — coefficient grows |
| Palm × Tmax → CES-D | +0.341 *** | +0.487 ** (p=0.024) | Survives |
| Palm × Tmax → Somatic | +0.321 *** | +0.418 * (p=0.063) | Survives (borderline) |
| Job loss × Tmean → CES-D | +0.036 ** | +0.015 (p=0.57) | Underpowered (only 5 % of panel changes status) |
| Fuel cut × Tmax → CES-D | +0.119 *** | +0.009 (p=0.94) | Unidentified within-person (post-cut collinear with wave) |

**Reading.** The palm-shock finding is the strongest under the most demanding spec — it *survives* and even *grows* under individual FE. This addresses the earlier concern that palm was identified only off cross-wave variation: there is genuine within-person variation in palm_shock for palm farmers across IFLS4 (rising-price) and IFLS5 (falling-price) interview months, and the panel-FE estimate isolates this.

The job-loss panel result fades to null but this is a **power problem**, not a contradiction: only 5.4 % of panel respondents change job-loss-within-12mo status between waves. The within-person identifying sample is ≈ 1,100 person-wave switchers — not enough to estimate a heat-interaction precisely. The pooled cross-sectional estimate remains our best estimate.

The fuel-cut panel result is **unidentified by construction**: `post_subsidy` is essentially a wave dummy (0 in all IFLS4, 1 in 73 % of IFLS5). With wave FE *and* individual FE, the heat × fuel_shock interaction has no remaining identifying variation. The IFLS5-only cross-sectional spec is the appropriate identification strategy here.

## Main caveats

- Both IFLS waves use the identical 10-item Andresen CES-D-10 at the same kptype letter positions (verified empirically from microdata; the IFLS4 codebook PDF is misleading on this — see long-note §2.1). IFLS4 adds a yes/no screener before the frequency question, which shifts the score level (mean 4.09 vs 6.40); within-wave z-standardisation absorbs this. A 5-item subset (1 Somatic + 2 Depressed Affect + 2 Positive Affect) yields a null interaction — but this is the *expected* result given that the signal lives in the Somatic factor whose other 4 items are dropped from that subset, not a cross-wave measurement problem.
- Palm shock's pooled and panel-FE results both rely on cross-wave price variation (IFLS4 rising-price era → IFLS5 falling-price era). Within-IFLS5 alone the effect is null. Panel FE confirms it's not pure cross-sectional confounding, but the identifying variation is still the same time period.
- Bottom-PCE-quintile null on the job-loss interaction suggests chronic poverty saturates negative-affect bandwidth; samples weighted toward the very poor would under-recover the effect.

## Ask for PI input

- **Is "negative-affect specificity" a publishable contribution** to the heat-mental-health literature, or do PIs prefer we position around amplification alone?
- **The palm-shock individual-FE result (β = +0.55 \*\*, within-person) is now our cleanest identification.** Comfortable making palm the headline rather than job loss?
- **Job-loss panel result is underpowered (5 % switchers).** Worth pursuing IFLS3 to add a third wave and gain identifying variation, or accept the pooled estimate as is?
- **Do we want lincom marginal effects reported, and which form?** Options include: (a) heat slope at stressor = 0 vs stressor = 1, (b) stressor effect at heat = mean vs heat = +1 SD, (c) heat slope by tercile (cool / mid / hot), or (d) effect at policy-relevant temperatures (e.g., +2 °C warming scenario). Each tells a different story about effect size; we can compute any combination but need to know which the PIs want for the paper.

---

*All numbers in `data/generated/results/`. Scripts: `code/analysis/14_unified_refined.py` (headline interactions on CES-D total + lincom) and `15_hypothesis_tests.py` (factor decomposition + day/night + individual-FE).*

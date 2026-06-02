"""Small pyfixest wrappers for repeated analysis-table regressions."""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from math import erfc, sqrt

import numpy as np
import pandas as pd
import pyfixest as pf

from analysis.lib.input import apply_sample, drop_singleton_clusters, require_columns

CONTROL_SETS = {
    "standard": ["age", "female", "edu_yrs", "married", "widowed"],
}

FE_SETS = {
    "pooled": "month + year + wave + kabupaten_code",
    "ifls5": "month + year + kabupaten_code",
    "within_kab_wave": "month + year + kabupaten_code + wave^kabupaten_code",
    "within_person": "pidlink + month + year + kabupaten_code",
    "within_day": "day_id + kabupaten_code",
}


def controls(name: str = "standard") -> str:
    """Expand a named control set to a formula fragment."""
    if name not in CONTROL_SETS:
        raise ValueError(f"unknown control set: {name}")
    return " + ".join(CONTROL_SETS[name])


def fixed_effects(name: str) -> str:
    """Expand a named fixed-effect set to a pyfixest FE fragment."""
    return FE_SETS.get(name, name)


def build_formula(
    *,
    outcome: str,
    rhs_terms: Sequence[str],
    controls_name: str = "standard",
    fixed_effects_name: str = "pooled",
) -> str:
    """Build a pyfixest formula from visible table-script pieces."""
    terms = [term for term in rhs_terms if term]
    control_terms = controls(controls_name)
    if control_terms:
        terms.append(control_terms)
    rhs = " + ".join(terms)
    return f"{outcome} ~ {rhs} | {fixed_effects(fixed_effects_name)}"


def run_model(
    df: pd.DataFrame,
    *,
    formula: str | None = None,
    outcome: str | None = None,
    rhs_terms: Sequence[str] | None = None,
    controls_name: str = "standard",
    fixed_effects_name: str = "pooled",
    sample: str = "pooled",
    cluster: str = "kabupaten_code",
    required_columns: Iterable[str] | None = None,
    drop_singletons: bool = True,
):
    """
    Wrapper for pyfixest regression in our analysis, with some common data prep steps.
    Apply a common sample, drop missing required columns, and fit FE OLS.
    """
    data = apply_sample(df, sample)
    if required_columns is not None:
        size = len(data)
        required = list(required_columns)
        require_columns(data, required)
        data = data.dropna(subset=required).copy()
        print(
            f"Dropped {size - len(data)} rows with missing required columns: {required}"
        )
    if drop_singletons:
        size = len(data)
        data = drop_singleton_clusters(data, cluster)
        print(f"Dropped {size - len(data)} rows in singleton clusters of {cluster}")

    if formula is None:
        if outcome is None or rhs_terms is None:
            raise ValueError("provide either formula or outcome plus rhs_terms")
        formula = build_formula(
            outcome=outcome,
            rhs_terms=rhs_terms,
            controls_name=controls_name,
            fixed_effects_name=fixed_effects_name,
        )

    return pf.feols(formula, data=data, vcov={"CRV1": cluster})


def coef_stats(model, term: str) -> dict[str, float]:
    """Return coefficient, SE, and p-value for a model term."""
    coefs = model.coef()
    return {
        "b": float(coefs.get(term, np.nan)),
        "se": float(model.se().get(term, np.nan)),
        "p": float(model.pvalue().get(term, np.nan)),
    }


def prefixed_coef_stats(model, term: str, prefix: str) -> dict[str, float]:
    """Return coefficient statistics with a table-row prefix."""
    stats = coef_stats(model, term)
    return {f"{prefix}_{key}": value for key, value in stats.items()}


def lincom(model, weights: Mapping[str, float]) -> tuple[float, float, float]:
    """Compute a linear combination using the model's clustered vcov."""
    coefs = model.coef()
    vcov = pd.DataFrame(model._vcov, index=coefs.index, columns=coefs.index)
    contrast = pd.Series(0.0, index=coefs.index)
    for term, weight in weights.items():
        if term not in contrast.index:
            return np.nan, np.nan, np.nan
        contrast[term] = weight

    estimate = float(contrast @ coefs)
    se = float(np.sqrt(contrast @ vcov @ contrast))
    t_stat = estimate / se if se > 0 else np.nan
    p_value = erfc(abs(t_stat) / sqrt(2)) if not pd.isna(t_stat) else np.nan
    return estimate, se, p_value


def interaction_name(left: str, right: str) -> str:
    """Return pyfixest's interaction-term name for two variables."""
    return f"{left}:{right}"


def extract_interaction_model(
    model,
    *,
    heat: str,
    stressor: str,
    high_stressor_value: float = 1.0,
) -> dict[str, float]:
    """Extract common Heat x Stressor table quantities from a fitted model."""
    interaction = interaction_name(heat, stressor)
    heat_high_b, heat_high_se, heat_high_p = lincom(
        model,
        {heat: 1.0, interaction: high_stressor_value},
    )
    return {
        "n": int(model._N),
        **prefixed_coef_stats(model, interaction, "inter"),
        **prefixed_coef_stats(model, heat, "heat"),
        **prefixed_coef_stats(model, stressor, "stress"),
        "heat_high_b": heat_high_b,
        "heat_high_se": heat_high_se,
        "heat_high_p": heat_high_p,
        "high_value": high_stressor_value,
    }


def run_heat_stressor_specs(
    df: pd.DataFrame,
    specs: Sequence[Mapping[str, object]],
    *,
    outcome: str,
    heat: str,
    controls_name: str = "standard",
    cluster: str = "kabupaten_code",
) -> list[dict[str, object]]:
    """Run a simple list of Heat x Stressor specifications."""
    rows: list[dict[str, object]] = []
    for spec in specs:
        stressor = str(spec["stressor"])
        extra_terms = list(spec.get("extra_terms", []))
        sample = str(spec.get("sample", "pooled"))
        fe = str(spec.get("fixed_effects", sample))
        high_value = float(spec.get("high_stressor_value", 1.0))
        rhs_terms = [f"{heat} * {stressor}", *extra_terms]
        required = [
            outcome,
            heat,
            stressor,
            *extra_terms,
            *CONTROL_SETS[controls_name],
            cluster,
            "month",
            "year",
        ]
        if sample == "pooled":
            required.append("wave")
        model = run_model(
            df,
            outcome=outcome,
            rhs_terms=rhs_terms,
            controls_name=controls_name,
            fixed_effects_name=fe,
            sample=sample,
            cluster=cluster,
            required_columns=required,
        )
        rows.append(
            {
                **dict(spec),
                "result": extract_interaction_model(
                    model,
                    heat=heat,
                    stressor=stressor,
                    high_stressor_value=high_value,
                ),
            }
        )
    return rows

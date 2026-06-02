"""Formatting helpers shared by analysis tables."""
from __future__ import annotations

import pandas as pd


def stars(p_value: float) -> str:
    """Return LaTeX significance stars for conventional p-value cutoffs."""
    if pd.isna(p_value):
        return ""
    if p_value < 0.01:
        return r"^{***}"
    if p_value < 0.05:
        return r"^{**}"
    if p_value < 0.10:
        return r"^{*}"
    return ""


def coef_cell(coef: float, se: float, p_value: float) -> tuple[str, str]:
    """Return LaTeX coefficient and standard-error cells."""
    if pd.isna(coef):
        return "", ""
    return f"${coef:+.3f}{stars(p_value)}$", f"$({se:.3f})$"


def fmt_int(value: int | float) -> str:
    """Format counts with thousands separators."""
    if pd.isna(value):
        return ""
    return f"{int(value):,}"

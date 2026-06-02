"""Shared table output helpers."""
from __future__ import annotations

from pathlib import Path
from collections.abc import Iterable, Mapping

import pandas as pd

from analysis.lib.input import PROJECT

TABLES = PROJECT / "output" / "tables"
TABLES.mkdir(parents=True, exist_ok=True)


def write_table_body(name: str, body_lines: Iterable[str], *, table_dir: Path = TABLES) -> Path:
    """Write a tabular-only LaTeX body."""
    path = table_dir / f"{name}_body.tex"
    path.write_text("\n".join(body_lines) + "\n", encoding="utf-8")
    return path


def write_full_table(name: str, lines: Iterable[str], *, table_dir: Path = TABLES) -> Path:
    """Write a full LaTeX table."""
    path = table_dir / f"{name}.tex"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_table_csv(
    name: str,
    rows: Iterable[Mapping[str, object]],
    *,
    table_dir: Path = TABLES,
) -> Path:
    """Write a machine-readable table CSV."""
    path = table_dir / f"{name}.csv"
    pd.DataFrame(rows).to_csv(path, index=False)
    return path

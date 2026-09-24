"""Check answers and report results in the same format as LeetCode."""

import os
import sys
import time
from collections import Counter
from typing import Callable

import pytest
from pyspark.sql import DataFrame

_COLOR = sys.__stdout__.isatty() and "NO_COLOR" not in os.environ
RED, GREEN, GREY, RESET = (
    ("\033[31m", "\033[32m", "\033[90m", "\033[0m") if _COLOR else ("", "", "", "")
)


def _cell(value) -> str:
    return "null" if value is None else str(value)


def format_table(columns: list[str], rows: list[tuple]) -> str:
    """Format rows as a LeetCode table: | col | col |."""
    cells = [[_cell(v) for v in row] for row in rows]
    widths = [max([len(c)] + [len(r[i]) for r in cells]) for i, c in enumerate(columns)]

    def line(values):
        return "| " + " | ".join(v.ljust(w) for v, w in zip(values, widths)) + " |"

    lines = [line(columns), line(["-" * w for w in widths])]
    lines += [line(r) for r in cells]
    return "\n".join(lines)


def _table(df: DataFrame) -> tuple[list[str], list[tuple]]:
    return df.columns, [tuple(r) for r in df.collect()]


def _indent(text: str) -> str:
    return "\n".join("  " + line for line in text.splitlines())


def check(
    request: pytest.FixtureRequest,
    inputs: dict[str, DataFrame],
    solve: Callable[[], DataFrame],
    expected: DataFrame,
) -> None:
    """Run solve() and fail the test with a LeetCode report if the answer is wrong.

    Row order is ignored. Column names must match, but column order is ignored.
    If the answer is correct, the output is kept for the summary at the end of the run.
    """
    case = request.node.callspec.id
    input_text = "\n\n".join(
        f"{GREY}{name} ={RESET}\n{_indent(format_table(*_table(df)))}"
        for name, df in inputs.items()
    )

    start = time.perf_counter()
    try:
        out_cols, out_rows = _table(solve())
    except NotImplementedError:
        pytest.skip("not implemented yet")
    except Exception as exc:  # noqa: BLE001
        message = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
        pytest.fail(
            f"\n{RED}Runtime Error{RESET}   {case}\n\n"
            f"{type(exc).__name__}: {message}\n\n"
            f"Input\n\n{input_text}\n",
            pytrace=False,
        )
    runtime_ms = (time.perf_counter() - start) * 1000

    exp_cols, exp_rows = _table(expected)
    correct = sorted(out_cols) == sorted(exp_cols)
    if correct:
        order = [out_cols.index(c) for c in exp_cols]
        reordered = [tuple(row[i] for i in order) for row in out_rows]
        correct = Counter(reordered) == Counter(exp_rows)

    if not correct:
        pytest.fail(
            f"\n{RED}Wrong Answer{RESET}   Runtime: {runtime_ms:.0f} ms   {case}\n\n"
            f"Input\n\n{input_text}\n\n"
            f"Output\n\n{_indent(format_table(out_cols, out_rows))}\n\n"
            f"Expected\n\n{GREEN}{_indent(format_table(exp_cols, exp_rows))}{RESET}\n",
            pytrace=False,
        )

    request.node.user_properties.append(
        (
            "leetcode_output",
            f"{GREEN}Accepted{RESET}   Runtime: {runtime_ms:.0f} ms   {case}\n\n"
            f"{_indent(format_table(out_cols, out_rows))}\n",
        )
    )

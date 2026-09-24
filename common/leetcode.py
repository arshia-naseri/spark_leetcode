"""Check answers and report results in the same format as LeetCode."""

import time
from collections import Counter
from typing import Callable

import pytest
from pyspark.sql import DataFrame

RED = GREEN = GREY = RESET = ""


def set_color(enabled: bool) -> None:
    """Turn the ANSI colors in the reports on or off."""
    global RED, GREEN, GREY, RESET
    RED, GREEN, GREY, RESET = (
        ("\033[31m", "\033[32m", "\033[90m", "\033[0m") if enabled else ("", "", "", "")
    )


def _cell(value) -> str:
    return "null" if value is None else str(value)


def format_table(
    columns: list[str],
    rows: list[tuple],
    marked_cols: set[int] = frozenset(),
    marked_rows: set[int] = frozenset(),
    color: str = "",
) -> str:
    """Format rows as a LeetCode table: | col | col |.

    Cells in marked_cols or marked_rows show in the given color.
    """
    cells = [[_cell(v) for v in row] for row in rows]
    widths = [max([len(c)] + [len(r[i]) for r in cells]) for i, c in enumerate(columns)]

    def line(values, row_marked=False):
        parts = []
        for i, (v, w) in enumerate(zip(values, widths)):
            text = v.ljust(w)
            if color and (row_marked or i in marked_cols):
                text = f"{color}{text}{RESET}"
            parts.append(text)
        return "| " + " | ".join(parts) + " |"

    lines = [line(columns), line(["-" * w for w in widths])]
    lines += [line(r, i in marked_rows) for i, r in enumerate(cells)]
    return "\n".join(lines)


def _table(df: DataFrame) -> tuple[list[str], list[tuple]]:
    return df.columns, [tuple(r) for r in df.collect()]


def _json_table(
    columns: list[str],
    rows: list[tuple],
    marked_cols: set[int] = frozenset(),
    marked_rows: set[int] = frozenset(),
) -> dict:
    """Return a table as JSON data. All cells are text, the same as in format_table()."""
    return {
        "columns": list(columns),
        "rows": [[_cell(v) for v in row] for row in rows],
        "marked_cols": sorted(marked_cols),
        "marked_rows": sorted(marked_rows),
    }


def _indent(text: str) -> str:
    return "\n".join("  " + line for line in text.splitlines())


def _column_diff(out_cols: list[str], exp_cols: list[str]) -> list[str]:
    """Return the column name errors. An empty list means the names match.

    Column order is ignored. Column names are case-sensitive.
    """
    out, exp = Counter(out_cols), Counter(exp_cols)
    extra = sorted((out - exp).elements())
    missing = sorted((exp - out).elements())
    lines = []
    if extra:
        lines.append(f"Extra columns: {', '.join(extra)}")
    if missing:
        lines.append(f"Missing columns: {', '.join(missing)}")
    if lines and Counter(c.lower() for c in out_cols) == Counter(c.lower() for c in exp_cols):
        lines.append("Column names differ only in upper or lower case.")
    return lines


def _unmatched_rows(
    out_cols: list[str], out_rows: list[tuple], exp_cols: list[str], exp_rows: list[tuple]
) -> tuple[set[int], set[int]]:
    """Match rows on the columns that both tables have. Row order is ignored.

    Return the indexes of the output rows and the expected rows that have no match.
    """
    common = [c for c in exp_cols if c in out_cols]
    out_idx = [out_cols.index(c) for c in common]
    exp_idx = [exp_cols.index(c) for c in common]
    available: dict[tuple, list[int]] = {}
    for i, row in enumerate(out_rows):
        available.setdefault(tuple(row[j] for j in out_idx), []).append(i)

    missing = set()
    for i, row in enumerate(exp_rows):
        matches = available.get(tuple(row[j] for j in exp_idx))
        if matches:
            matches.pop()
        else:
            missing.add(i)
    extra = {i for rows in available.values() for i in rows}
    return extra, missing


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
    input_tables = {name: _table(df) for name, df in inputs.items()}
    # The same result as data, for the web UI. conftest.py writes it with --leetcode-json.
    result: dict = {
        "case": case,
        "inputs": {name: _json_table(*table) for name, table in input_tables.items()},
    }
    request.node.user_properties.append(("leetcode_result", result))
    input_text = "\n\n".join(
        f"{GREY}{name} ={RESET}\n{_indent(format_table(*table))}"
        for name, table in input_tables.items()
    )

    start = time.perf_counter()
    try:
        out_cols, out_rows = _table(solve())
    except NotImplementedError:
        result["status"] = "skipped"
        pytest.skip("not implemented yet")
    except Exception as exc:  # noqa: BLE001
        message = str(exc).strip().splitlines()[0] if str(exc).strip() else ""
        result.update(
            status="error", error=f"{type(exc).__name__}: {message}", detail=str(exc)[:4000]
        )
        pytest.fail(
            f"\n{RED}Runtime Error{RESET}   {case}\n\n"
            f"{type(exc).__name__}: {message}\n\n"
            f"Input\n\n{input_text}\n",
            pytrace=False,
        )
    runtime_ms = (time.perf_counter() - start) * 1000
    result["runtime_ms"] = round(runtime_ms)

    exp_cols, exp_rows = _table(expected)
    reason = _column_diff(out_cols, exp_cols)
    extra_rows, missing_rows = _unmatched_rows(out_cols, out_rows, exp_cols, exp_rows)
    correct = not reason and not extra_rows and not missing_rows

    if not correct:
        # Red: output parts that are not expected. Green: expected parts that are missing.
        extra_cols = {i for i, c in enumerate(out_cols) if c not in exp_cols}
        missing_cols = {i for i, c in enumerate(exp_cols) if c not in out_cols}
        output_table = format_table(out_cols, out_rows, extra_cols, extra_rows, RED)
        expected_table = format_table(exp_cols, exp_rows, missing_cols, missing_rows, GREEN)
        result.update(
            status="wrong",
            reason=reason,
            output=_json_table(out_cols, out_rows, extra_cols, extra_rows),
            expected=_json_table(exp_cols, exp_rows, missing_cols, missing_rows),
        )
        reason_text = "".join(f"{RED}{line}{RESET}\n" for line in reason)
        pytest.fail(
            f"\n{RED}Wrong Answer{RESET}   Runtime: {runtime_ms:.0f} ms   {case}\n\n"
            f"{reason_text}{chr(10) if reason else ''}"
            f"Input\n\n{input_text}\n\n"
            f"Output\n\n{_indent(output_table)}\n\n"
            f"Expected\n\n{_indent(expected_table)}\n",
            pytrace=False,
        )

    result.update(
        status="accepted",
        output=_json_table(out_cols, out_rows),
        expected=_json_table(exp_cols, exp_rows),
    )
    request.node.user_properties.append(
        (
            "leetcode_output",
            f"{GREEN}Accepted{RESET}   Runtime: {runtime_ms:.0f} ms   {case}\n\n"
            f"{_indent(format_table(out_cols, out_rows))}\n",
        )
    )

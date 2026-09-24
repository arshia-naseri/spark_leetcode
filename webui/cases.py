"""Read the test cases of a problem without Spark.

The server shows the input and expected tables before a run. Each test_cases.py
builds its DataFrames with spark.createDataFrame(rows, schema) and gives the
input tables to check(). This module calls test_case() with a fake Spark
session and a fake check() to get the tables. Spark does not start.
"""

import importlib
import inspect
import sys
from pathlib import Path

from common.leetcode import _cell


class _FakeFrame:
    def __init__(self, rows, schema: str):
        self.columns = _ddl_columns(schema)
        self.rows = [[_cell(v) for v in row] for row in rows]

    def table(self) -> dict:
        return {"columns": self.columns, "rows": self.rows}


class _FakeSpark:
    def createDataFrame(self, rows, schema):  # noqa: N802 (same name as Spark)
        return _FakeFrame(rows, schema)


class _Captured(Exception):
    def __init__(self, inputs, expected):
        self.inputs, self.expected = inputs, expected


def _fake_check(request, inputs, run, expected):
    raise _Captured(inputs, expected)


def _ddl_columns(schema: str) -> list[str]:
    """Return the column names of a DDL string such as "a INT, b DECIMAL(10,2)"."""
    columns, depth, part = [], 0, ""
    for char in schema + ",":
        if char in "(<":
            depth += 1
        elif char in ")>":
            depth -= 1
        if char == "," and depth == 0:
            if part.strip():
                columns.append(part.split()[0].strip("`"))
            part = ""
        else:
            part += char
    return columns


def problem_module(problem: Path) -> str:
    """Return the module name of a problem folder, for example problems.easy.p0175_x."""
    return f"problems.{problem.parent.name}.{problem.name}"


def load_cases(problem: Path) -> list[dict]:
    """Return the cases of a problem: [{"inputs": {name: table}, "expected": table}]."""
    package = problem_module(problem)
    try:
        tests = importlib.import_module(f"{package}._internal.test_cases")
        params = list(inspect.signature(tests.test_case).parameters)
        case_params = params[params.index("method") + 1 :]
        tests.check = _fake_check
        cases = []
        for case in tests.CASES:
            try:
                tests.test_case(
                    spark=_FakeSpark(),
                    request=None,
                    module_name="solution",
                    method="dataframe",
                    **dict(zip(case_params, case)),
                )
            except _Captured as captured:
                cases.append(
                    {
                        "inputs": {n: f.table() for n, f in captured.inputs.items()},
                        "expected": captured.expected.table(),
                    }
                )
        return cases
    finally:
        # Forget the modules, so that the next call reads changed files again.
        for name in [m for m in sys.modules if m == package or m.startswith(f"{package}.")]:
            del sys.modules[name]

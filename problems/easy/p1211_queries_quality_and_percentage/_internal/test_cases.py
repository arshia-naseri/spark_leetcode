import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, OUTPUT_SCHEMA, QUERIES_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "queries_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, queries_rows, expected_rows):
    module = MODULES[module_name]
    queries = spark.createDataFrame(queries_rows, QUERIES_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(queries)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, queries)  # noqa: E731

    check(request, {"Queries": queries}, run, expected)

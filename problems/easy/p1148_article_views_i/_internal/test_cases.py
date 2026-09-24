import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, OUTPUT_SCHEMA, VIEWS_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "views_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, views_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    views = spark.createDataFrame(views_rows, VIEWS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(views)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, views)  # noqa: E731

    check(request, {"Views": views}, run, expected)

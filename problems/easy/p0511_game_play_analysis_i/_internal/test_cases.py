import pytest

from common.leetcode import check
from common.practice import load

from .data import ACTIVITY_SCHEMA, CASES, OUTPUT_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "activity_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, activity_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    activity = spark.createDataFrame(activity_rows, ACTIVITY_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(activity)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, activity)  # noqa: E731

    check(request, {"Activity": activity}, run, expected)

import pytest

from common.leetcode import check
from common.practice import load

from .data import ACTIVITIES_SCHEMA, CASES, OUTPUT_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "activities_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, activities_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    activities = spark.createDataFrame(activities_rows, ACTIVITIES_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(activities)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, activities)  # noqa: E731

    check(request, {"Activities": activities}, run, expected)

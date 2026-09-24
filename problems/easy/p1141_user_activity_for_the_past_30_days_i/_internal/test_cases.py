import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import ACTIVITY_SCHEMA, CASES, OUTPUT_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "activity_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, activity_rows, expected_rows):
    module = MODULES[module_name]
    activity = spark.createDataFrame(activity_rows, ACTIVITY_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(activity)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, activity)  # noqa: E731

    check(request, {"Activity": activity}, run, expected)

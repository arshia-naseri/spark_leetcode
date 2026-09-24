import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, DAILY_SALES_SCHEMA, OUTPUT_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "daily_sales_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, daily_sales_rows, expected_rows):
    module = MODULES[module_name]
    daily_sales = spark.createDataFrame(daily_sales_rows, DAILY_SALES_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(daily_sales)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, daily_sales)  # noqa: E731

    check(request, {"DailySales": daily_sales}, run, expected)

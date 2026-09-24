import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, OUTPUT_SCHEMA, PRICES_SCHEMA, UNITS_SOLD_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "prices_rows, units_sold_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, prices_rows, units_sold_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    prices = spark.createDataFrame(prices_rows, PRICES_SCHEMA)
    units_sold = spark.createDataFrame(units_sold_rows, UNITS_SOLD_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(prices, units_sold)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, prices, units_sold)  # noqa: E731

    check(request, {"Prices": prices, "UnitsSold": units_sold}, run, expected)

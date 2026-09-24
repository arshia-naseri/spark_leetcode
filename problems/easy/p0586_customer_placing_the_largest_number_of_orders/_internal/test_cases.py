import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, ORDERS_SCHEMA, OUTPUT_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "orders_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, orders_rows, expected_rows):
    module = MODULES[module_name]
    orders = spark.createDataFrame(orders_rows, ORDERS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(orders)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, orders)  # noqa: E731

    check(request, {"Orders": orders}, run, expected)

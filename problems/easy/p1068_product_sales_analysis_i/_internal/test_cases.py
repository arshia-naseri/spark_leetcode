import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, OUTPUT_SCHEMA, PRODUCT_SCHEMA, SALES_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "sales_rows, product_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, sales_rows, product_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    sales = spark.createDataFrame(sales_rows, SALES_SCHEMA)
    product = spark.createDataFrame(product_rows, PRODUCT_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(sales, product)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, sales, product)  # noqa: E731

    check(request, {"Sales": sales, "Product": product}, run, expected)

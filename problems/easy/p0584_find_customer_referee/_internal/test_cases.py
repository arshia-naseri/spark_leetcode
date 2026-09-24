import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, CUSTOMER_SCHEMA, OUTPUT_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "customer_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, customer_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    customer = spark.createDataFrame(customer_rows, CUSTOMER_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(customer)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, customer)  # noqa: E731

    check(request, {"Customer": customer}, run, expected)

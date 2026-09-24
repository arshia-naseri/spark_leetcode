import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, OUTPUT_SCHEMA, TRANSACTIONS_SCHEMA, VISITS_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "visits_rows, transactions_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, visits_rows, transactions_rows, expected_rows):
    module = MODULES[module_name]
    visits = spark.createDataFrame(visits_rows, VISITS_SCHEMA)
    transactions = spark.createDataFrame(transactions_rows, TRANSACTIONS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(visits, transactions)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, visits, transactions)  # noqa: E731

    check(request, {"Visits": visits, "Transactions": transactions}, run, expected)

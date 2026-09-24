import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, OUTPUT_SCHEMA, TRANSACTIONS_SCHEMA, USERS_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "users_rows, transactions_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, users_rows, transactions_rows, expected_rows):
    module = MODULES[module_name]
    users = spark.createDataFrame(users_rows, USERS_SCHEMA)
    transactions = spark.createDataFrame(transactions_rows, TRANSACTIONS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(users, transactions)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, users, transactions)  # noqa: E731

    check(request, {"Users": users, "Transactions": transactions}, run, expected)

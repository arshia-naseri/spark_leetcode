import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, OUTPUT_SCHEMA, REGISTER_SCHEMA, USERS_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "users_rows, register_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, users_rows, register_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    users = spark.createDataFrame(users_rows, USERS_SCHEMA)
    register = spark.createDataFrame(register_rows, REGISTER_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(users, register)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, users, register)  # noqa: E731

    check(request, {"Users": users, "Register": register}, run, expected)

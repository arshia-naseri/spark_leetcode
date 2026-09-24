import pytest

from common.leetcode import check
from common.practice import load

from .data import BONUS_SCHEMA, CASES, EMPLOYEE_SCHEMA, OUTPUT_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "employee_rows, bonus_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, employee_rows, bonus_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    employee = spark.createDataFrame(employee_rows, EMPLOYEE_SCHEMA)
    bonus = spark.createDataFrame(bonus_rows, BONUS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(employee, bonus)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, employee, bonus)  # noqa: E731

    check(request, {"Employee": employee, "Bonus": bonus}, run, expected)

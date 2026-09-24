import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, EMPLOYEES_SCHEMA, OUTPUT_SCHEMA, SALARIES_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "employees_rows, salaries_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, employees_rows, salaries_rows, expected_rows):
    module = MODULES[module_name]
    employees = spark.createDataFrame(employees_rows, EMPLOYEES_SCHEMA)
    salaries = spark.createDataFrame(salaries_rows, SALARIES_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(employees, salaries)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, employees, salaries)  # noqa: E731

    check(request, {"Employees": employees, "Salaries": salaries}, run, expected)

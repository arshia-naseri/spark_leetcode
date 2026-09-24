import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, EMPLOYEE_SCHEMA, OUTPUT_SCHEMA, PROJECT_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "project_rows, employee_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, project_rows, employee_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    project = spark.createDataFrame(project_rows, PROJECT_SCHEMA)
    employee = spark.createDataFrame(employee_rows, EMPLOYEE_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(project, employee)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, project, employee)  # noqa: E731

    check(request, {"Project": project, "Employee": employee}, run, expected)

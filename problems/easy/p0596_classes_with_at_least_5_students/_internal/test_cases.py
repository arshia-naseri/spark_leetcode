import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, COURSES_SCHEMA, OUTPUT_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "courses_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, courses_rows, expected_rows):
    module = MODULES[module_name]
    courses = spark.createDataFrame(courses_rows, COURSES_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(courses)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, courses)  # noqa: E731

    check(request, {"Courses": courses}, run, expected)

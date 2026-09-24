import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, LOGINS_SCHEMA, OUTPUT_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "logins_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, logins_rows, expected_rows):
    module = MODULES[module_name]
    logins = spark.createDataFrame(logins_rows, LOGINS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(logins)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, logins)  # noqa: E731

    check(request, {"Logins": logins}, run, expected)

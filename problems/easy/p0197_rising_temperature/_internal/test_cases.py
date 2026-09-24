import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, OUTPUT_SCHEMA, WEATHER_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "weather_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, weather_rows, expected_rows):
    module = MODULES[module_name]
    weather = spark.createDataFrame(weather_rows, WEATHER_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(weather)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, weather)  # noqa: E731

    check(request, {"Weather": weather}, run, expected)

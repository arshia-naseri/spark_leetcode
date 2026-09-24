import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import ACTOR_DIRECTOR_SCHEMA, CASES, OUTPUT_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "actor_director_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, actor_director_rows, expected_rows):
    module = MODULES[module_name]
    actor_director = spark.createDataFrame(actor_director_rows, ACTOR_DIRECTOR_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(actor_director)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, actor_director)  # noqa: E731

    check(request, {"ActorDirector": actor_director}, run, expected)

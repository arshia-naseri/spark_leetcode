import pytest

from common.leetcode import check
from common.practice import load

from .data import ADDRESS_SCHEMA, CASES, OUTPUT_SCHEMA, PERSON_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "person_rows, address_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(spark, request, module_name, method, person_rows, address_rows, expected_rows):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    person = spark.createDataFrame(person_rows, PERSON_SCHEMA)
    address = spark.createDataFrame(address_rows, ADDRESS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(person, address)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, person, address)  # noqa: E731

    check(request, {"Person": person, "Address": address}, run, expected)

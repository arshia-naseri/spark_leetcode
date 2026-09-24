import pytest

from common.leetcode import check

from .. import practice
from . import solution
from .data import CASES, COMPANY_SCHEMA, ORDERS_SCHEMA, OUTPUT_SCHEMA, SALES_PERSON_SCHEMA

MODULES = {"practice": practice, "solution": solution}


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "sales_person_rows, company_rows, orders_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(
    spark, request, module_name, method, sales_person_rows, company_rows, orders_rows, expected_rows
):
    module = MODULES[module_name]
    sales_person = spark.createDataFrame(sales_person_rows, SALES_PERSON_SCHEMA)
    company = spark.createDataFrame(company_rows, COMPANY_SCHEMA)
    orders = spark.createDataFrame(orders_rows, ORDERS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module.solve(sales_person, company, orders)  # noqa: E731
    else:
        run = lambda: module.solve_sql(spark, sales_person, company, orders)  # noqa: E731

    check(
        request,
        {"SalesPerson": sales_person, "Company": company, "Orders": orders},
        run,
        expected,
    )

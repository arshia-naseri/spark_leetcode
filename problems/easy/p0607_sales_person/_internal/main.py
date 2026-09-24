import sys

from common.practice import load
from common.spark import get_spark

from .data import (
    COMPANY_SCHEMA,
    EXAMPLE_COMPANY,
    EXAMPLE_ORDERS,
    EXAMPLE_SALES_PERSON,
    ORDERS_SCHEMA,
    SALES_PERSON_SCHEMA,
)

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    sales_person = spark.createDataFrame(EXAMPLE_SALES_PERSON, SALES_PERSON_SCHEMA)
    company = spark.createDataFrame(EXAMPLE_COMPANY, COMPANY_SCHEMA)
    orders = spark.createDataFrame(EXAMPLE_ORDERS, ORDERS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(sales_person, company, orders)),
        ("SQL", lambda: module("sql").solve_sql(spark, sales_person, company, orders)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

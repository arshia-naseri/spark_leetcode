import sys

from common.practice import load
from common.spark import get_spark

from .data import CUSTOMERS_SCHEMA, EXAMPLE_CUSTOMERS, EXAMPLE_ORDERS, ORDERS_SCHEMA

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    customers = spark.createDataFrame(EXAMPLE_CUSTOMERS, CUSTOMERS_SCHEMA)
    orders = spark.createDataFrame(EXAMPLE_ORDERS, ORDERS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(customers, orders)),
        ("SQL", lambda: module("sql").solve_sql(spark, customers, orders)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

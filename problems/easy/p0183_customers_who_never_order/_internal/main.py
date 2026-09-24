import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import CUSTOMERS_SCHEMA, EXAMPLE_CUSTOMERS, EXAMPLE_ORDERS, ORDERS_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    customers = spark.createDataFrame(EXAMPLE_CUSTOMERS, CUSTOMERS_SCHEMA)
    orders = spark.createDataFrame(EXAMPLE_ORDERS, ORDERS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(customers, orders)),
        ("SQL", lambda: module.solve_sql(spark, customers, orders)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

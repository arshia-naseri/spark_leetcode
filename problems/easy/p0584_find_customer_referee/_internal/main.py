import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import CUSTOMER_SCHEMA, EXAMPLE_CUSTOMER

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    customer = spark.createDataFrame(EXAMPLE_CUSTOMER, CUSTOMER_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(customer)),
        ("SQL", lambda: module.solve_sql(spark, customer)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

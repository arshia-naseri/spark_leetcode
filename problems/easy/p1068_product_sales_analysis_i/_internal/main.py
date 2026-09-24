import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EXAMPLE_PRODUCT, EXAMPLE_SALES, PRODUCT_SCHEMA, SALES_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    sales = spark.createDataFrame(EXAMPLE_SALES, SALES_SCHEMA)
    product = spark.createDataFrame(EXAMPLE_PRODUCT, PRODUCT_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(sales, product)),
        ("SQL", lambda: module.solve_sql(spark, sales, product)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

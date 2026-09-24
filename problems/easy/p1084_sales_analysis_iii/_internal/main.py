import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EXAMPLE_PRODUCT, EXAMPLE_SALES, PRODUCT_SCHEMA, SALES_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    product = spark.createDataFrame(EXAMPLE_PRODUCT, PRODUCT_SCHEMA)
    sales = spark.createDataFrame(EXAMPLE_SALES, SALES_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(product, sales)),
        ("SQL", lambda: module.solve_sql(spark, product, sales)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

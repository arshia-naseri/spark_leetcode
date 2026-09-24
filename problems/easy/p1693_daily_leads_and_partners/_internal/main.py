import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import DAILY_SALES_SCHEMA, EXAMPLE_DAILY_SALES

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    daily_sales = spark.createDataFrame(EXAMPLE_DAILY_SALES, DAILY_SALES_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(daily_sales)),
        ("SQL", lambda: module.solve_sql(spark, daily_sales)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

import sys

from common.practice import load
from common.spark import get_spark

from .data import DAILY_SALES_SCHEMA, EXAMPLE_DAILY_SALES

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    daily_sales = spark.createDataFrame(EXAMPLE_DAILY_SALES, DAILY_SALES_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(daily_sales)),
        ("SQL", lambda: module("sql").solve_sql(spark, daily_sales)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

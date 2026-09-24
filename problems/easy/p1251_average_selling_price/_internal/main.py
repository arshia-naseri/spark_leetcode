import sys

from common.practice import load
from common.spark import get_spark

from .data import EXAMPLE_PRICES, EXAMPLE_UNITS_SOLD, PRICES_SCHEMA, UNITS_SOLD_SCHEMA

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    prices = spark.createDataFrame(EXAMPLE_PRICES, PRICES_SCHEMA)
    units_sold = spark.createDataFrame(EXAMPLE_UNITS_SOLD, UNITS_SOLD_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(prices, units_sold)),
        ("SQL", lambda: module("sql").solve_sql(spark, prices, units_sold)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

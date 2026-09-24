import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EXAMPLE_PRICES, EXAMPLE_UNITS_SOLD, PRICES_SCHEMA, UNITS_SOLD_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    prices = spark.createDataFrame(EXAMPLE_PRICES, PRICES_SCHEMA)
    units_sold = spark.createDataFrame(EXAMPLE_UNITS_SOLD, UNITS_SOLD_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(prices, units_sold)),
        ("SQL", lambda: module.solve_sql(spark, prices, units_sold)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

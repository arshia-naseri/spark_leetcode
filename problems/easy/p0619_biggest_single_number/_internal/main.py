import sys

from common.practice import load
from common.spark import get_spark

from .data import EXAMPLE_MY_NUMBERS, MY_NUMBERS_SCHEMA

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    my_numbers = spark.createDataFrame(EXAMPLE_MY_NUMBERS, MY_NUMBERS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(my_numbers)),
        ("SQL", lambda: module("sql").solve_sql(spark, my_numbers)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

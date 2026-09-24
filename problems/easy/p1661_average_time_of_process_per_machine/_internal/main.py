import sys

from common.practice import load
from common.spark import get_spark

from .data import ACTIVITY_SCHEMA, EXAMPLE_ACTIVITY

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    activity = spark.createDataFrame(EXAMPLE_ACTIVITY, ACTIVITY_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(activity)),
        ("SQL", lambda: module("sql").solve_sql(spark, activity)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

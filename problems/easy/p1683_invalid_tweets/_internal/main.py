import sys

from common.practice import load
from common.spark import get_spark

from .data import EXAMPLE_TWEETS, TWEETS_SCHEMA

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    tweets = spark.createDataFrame(EXAMPLE_TWEETS, TWEETS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(tweets)),
        ("SQL", lambda: module("sql").solve_sql(spark, tweets)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

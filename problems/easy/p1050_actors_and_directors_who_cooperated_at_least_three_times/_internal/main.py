import sys

from common.practice import load
from common.spark import get_spark

from .data import ACTOR_DIRECTOR_SCHEMA, EXAMPLE_ACTOR_DIRECTOR

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    actor_director = spark.createDataFrame(EXAMPLE_ACTOR_DIRECTOR, ACTOR_DIRECTOR_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(actor_director)),
        ("SQL", lambda: module("sql").solve_sql(spark, actor_director)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

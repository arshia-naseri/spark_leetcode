import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import ACTIVITY_SCHEMA, EXAMPLE_ACTIVITY

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    activity = spark.createDataFrame(EXAMPLE_ACTIVITY, ACTIVITY_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(activity)),
        ("SQL", lambda: module.solve_sql(spark, activity)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

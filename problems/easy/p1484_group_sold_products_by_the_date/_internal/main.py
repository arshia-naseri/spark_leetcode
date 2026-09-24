import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import ACTIVITIES_SCHEMA, EXAMPLE_ACTIVITIES

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    activities = spark.createDataFrame(EXAMPLE_ACTIVITIES, ACTIVITIES_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(activities)),
        ("SQL", lambda: module.solve_sql(spark, activities)),
    ]:
        print(f"{name}:")
        try:
            run().show(truncate=False)
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

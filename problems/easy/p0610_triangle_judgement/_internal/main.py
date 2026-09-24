import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EXAMPLE_TRIANGLE, TRIANGLE_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    triangle = spark.createDataFrame(EXAMPLE_TRIANGLE, TRIANGLE_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(triangle)),
        ("SQL", lambda: module.solve_sql(spark, triangle)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EXAMPLE_WORLD, WORLD_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    world = spark.createDataFrame(EXAMPLE_WORLD, WORLD_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(world)),
        ("SQL", lambda: module.solve_sql(spark, world)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import ACTOR_DIRECTOR_SCHEMA, EXAMPLE_ACTOR_DIRECTOR

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    actor_director = spark.createDataFrame(EXAMPLE_ACTOR_DIRECTOR, ACTOR_DIRECTOR_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(actor_director)),
        ("SQL", lambda: module.solve_sql(spark, actor_director)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

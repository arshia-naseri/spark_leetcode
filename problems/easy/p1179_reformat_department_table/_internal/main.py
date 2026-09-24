import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import DEPARTMENT_SCHEMA, EXAMPLE_DEPARTMENT

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    department = spark.createDataFrame(EXAMPLE_DEPARTMENT, DEPARTMENT_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(department)),
        ("SQL", lambda: module.solve_sql(spark, department)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

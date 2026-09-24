import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EMPLOYEE_SCHEMA, EXAMPLE_EMPLOYEE, EXAMPLE_PROJECT, PROJECT_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    project = spark.createDataFrame(EXAMPLE_PROJECT, PROJECT_SCHEMA)
    employee = spark.createDataFrame(EXAMPLE_EMPLOYEE, EMPLOYEE_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(project, employee)),
        ("SQL", lambda: module.solve_sql(spark, project, employee)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

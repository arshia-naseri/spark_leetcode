import sys

from common.practice import load
from common.spark import get_spark

from .data import EMPLOYEE_SCHEMA, EXAMPLE_EMPLOYEE, EXAMPLE_PROJECT, PROJECT_SCHEMA

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    project = spark.createDataFrame(EXAMPLE_PROJECT, PROJECT_SCHEMA)
    employee = spark.createDataFrame(EXAMPLE_EMPLOYEE, EMPLOYEE_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(project, employee)),
        ("SQL", lambda: module("sql").solve_sql(spark, project, employee)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

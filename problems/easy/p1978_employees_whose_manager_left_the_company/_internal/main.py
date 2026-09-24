import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EMPLOYEES_SCHEMA, EXAMPLE_EMPLOYEES

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    employees = spark.createDataFrame(EXAMPLE_EMPLOYEES, EMPLOYEES_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(employees)),
        ("SQL", lambda: module.solve_sql(spark, employees)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

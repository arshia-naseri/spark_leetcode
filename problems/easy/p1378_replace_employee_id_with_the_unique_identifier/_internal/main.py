import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EMPLOYEE_UNI_SCHEMA, EMPLOYEES_SCHEMA, EXAMPLE_EMPLOYEE_UNI, EXAMPLE_EMPLOYEES

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    employees = spark.createDataFrame(EXAMPLE_EMPLOYEES, EMPLOYEES_SCHEMA)
    employee_uni = spark.createDataFrame(EXAMPLE_EMPLOYEE_UNI, EMPLOYEE_UNI_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(employees, employee_uni)),
        ("SQL", lambda: module.solve_sql(spark, employees, employee_uni)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

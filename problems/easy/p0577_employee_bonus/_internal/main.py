import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import BONUS_SCHEMA, EMPLOYEE_SCHEMA, EXAMPLE_BONUS, EXAMPLE_EMPLOYEE

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    employee = spark.createDataFrame(EXAMPLE_EMPLOYEE, EMPLOYEE_SCHEMA)
    bonus = spark.createDataFrame(EXAMPLE_BONUS, BONUS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(employee, bonus)),
        ("SQL", lambda: module.solve_sql(spark, employee, bonus)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

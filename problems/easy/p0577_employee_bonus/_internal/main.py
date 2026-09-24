import sys

from common.practice import load
from common.spark import get_spark

from .data import BONUS_SCHEMA, EMPLOYEE_SCHEMA, EXAMPLE_BONUS, EXAMPLE_EMPLOYEE

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    employee = spark.createDataFrame(EXAMPLE_EMPLOYEE, EMPLOYEE_SCHEMA)
    bonus = spark.createDataFrame(EXAMPLE_BONUS, BONUS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(employee, bonus)),
        ("SQL", lambda: module("sql").solve_sql(spark, employee, bonus)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

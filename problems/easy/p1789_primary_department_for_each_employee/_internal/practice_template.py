"""1789. Primary Department for Each Employee. Write your practice solution here.

Read question.md for the problem statement.

Employee: employee_id INT, department_id INT, primary_flag STRING
Output:   employee_id, department_id (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employee: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employee: DataFrame) -> DataFrame:
    # The table is available as the view "Employee".
    employee.createOrReplaceTempView("Employee")
    raise NotImplementedError

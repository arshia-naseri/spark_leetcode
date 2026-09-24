"""1741. Find Total Time Spent by Each Employee. Write your practice solution here.

Read question.md for the problem statement.

Employees: emp_id INT, event_day DATE, in_time INT, out_time INT
Output:    day, emp_id, total_time (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employees: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    # The table is available as the view "Employees".
    employees.createOrReplaceTempView("Employees")
    raise NotImplementedError

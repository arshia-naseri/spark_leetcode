"""181. Employees Earning More Than Their Managers. Write your practice solution here.

Read question.md for the problem statement.

Employee: id INT, name STRING, salary INT, managerId INT
Output:   Employee (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employee: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employee: DataFrame) -> DataFrame:
    # The table is available as the view "Employee".
    employee.createOrReplaceTempView("Employee")
    raise NotImplementedError

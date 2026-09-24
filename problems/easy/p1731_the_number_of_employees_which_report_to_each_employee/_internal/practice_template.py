"""1731. The Number of Employees Which Report to Each Employee. Write your practice solution here.

Read question.md for the problem statement.

Employees: employee_id INT, name STRING, reports_to INT, age INT
Output:    employee_id, name, reports_count, average_age (order by employee_id)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employees: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    # The table is available as the view "Employees".
    employees.createOrReplaceTempView("Employees")
    raise NotImplementedError

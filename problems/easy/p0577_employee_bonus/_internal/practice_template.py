"""577. Employee Bonus. Write your practice solution here.

Read question.md for the problem statement.

Employee: empId INT, name STRING, supervisor INT, salary INT
Bonus:    empId INT, bonus INT
Output:   name, bonus (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employee: DataFrame, bonus: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employee: DataFrame, bonus: DataFrame) -> DataFrame:
    # The tables are available as the views "Employee" and "Bonus".
    employee.createOrReplaceTempView("Employee")
    bonus.createOrReplaceTempView("Bonus")
    raise NotImplementedError

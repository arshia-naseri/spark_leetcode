"""1378. Replace Employee ID With The Unique Identifier. Write your practice solution here.

Read question.md for the problem statement.

Employees:   id INT, name STRING
EmployeeUNI: id INT, unique_id INT
Output:      unique_id, name (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employees: DataFrame, employee_uni: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employees: DataFrame, employee_uni: DataFrame) -> DataFrame:
    # The tables are available as the views "Employees" and "EmployeeUNI".
    employees.createOrReplaceTempView("Employees")
    employee_uni.createOrReplaceTempView("EmployeeUNI")
    raise NotImplementedError

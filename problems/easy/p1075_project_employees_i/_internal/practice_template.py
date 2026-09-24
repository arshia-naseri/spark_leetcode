"""1075. Project Employees I. Write your practice solution here.

Read question.md for the problem statement.

Project:  project_id INT, employee_id INT
Employee: employee_id INT, name STRING, experience_years INT
Output:   project_id, average_years (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(project: DataFrame, employee: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, project: DataFrame, employee: DataFrame) -> DataFrame:
    # The tables are available as the views "Project" and "Employee".
    project.createOrReplaceTempView("Project")
    employee.createOrReplaceTempView("Employee")
    raise NotImplementedError

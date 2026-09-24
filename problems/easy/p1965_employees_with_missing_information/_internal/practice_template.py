"""1965. Employees With Missing Information. Write your practice solution here.

Read question.md for the problem statement.

Employees: employee_id INT, name STRING
Salaries:  employee_id INT, salary INT
Output:    employee_id (ordered by employee_id ascending)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employees: DataFrame, salaries: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employees: DataFrame, salaries: DataFrame) -> DataFrame:
    # The tables are available as the views "Employees" and "Salaries".
    employees.createOrReplaceTempView("Employees")
    salaries.createOrReplaceTempView("Salaries")
    raise NotImplementedError

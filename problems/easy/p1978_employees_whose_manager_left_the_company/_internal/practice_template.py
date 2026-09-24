"""1978. Employees Whose Manager Left the Company. Write your practice solution here.

Read question.md for the problem statement.

Employees: employee_id INT, name STRING, manager_id INT, salary INT
Output:    employee_id (order by employee_id)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(employees: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    # The table is available as the view "Employees".
    employees.createOrReplaceTempView("Employees")
    raise NotImplementedError

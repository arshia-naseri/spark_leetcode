"""627. Swap Sex of Employees. Write your practice solution here.

Read question.md for the problem statement.

Salary: id INT, name STRING, sex STRING, salary INT
Output: id, name, sex, salary (any order). Spark DataFrames are immutable:
return the Salary table after the update as a new DataFrame.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(salary: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, salary: DataFrame) -> DataFrame:
    # The table is available as the view "Salary".
    # Spark views do not support UPDATE. Use SELECT to get the updated rows.
    salary.createOrReplaceTempView("Salary")
    raise NotImplementedError

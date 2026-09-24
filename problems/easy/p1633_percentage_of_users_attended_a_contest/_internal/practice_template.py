"""1633. Percentage of Users Attended a Contest. Write your practice solution here.

Read question.md for the problem statement.

Users:    user_id INT, user_name STRING
Register: contest_id INT, user_id INT
Output:   contest_id, percentage (percentage descending, then contest_id ascending)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(users: DataFrame, register: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, users: DataFrame, register: DataFrame) -> DataFrame:
    # The tables are available as the views "Users" and "Register".
    users.createOrReplaceTempView("Users")
    register.createOrReplaceTempView("Register")
    raise NotImplementedError

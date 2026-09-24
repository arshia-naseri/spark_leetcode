"""1517. Find Users With Valid E-Mails. Write your practice solution here.

Read question.md for the problem statement.

Users:  user_id INT, name STRING, mail STRING
Output: user_id, name, mail (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(users: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, users: DataFrame) -> DataFrame:
    # The table is available as the view "Users".
    users.createOrReplaceTempView("Users")
    raise NotImplementedError

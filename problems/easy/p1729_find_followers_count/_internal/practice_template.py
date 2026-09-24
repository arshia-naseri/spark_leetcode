"""1729. Find Followers Count. Write your practice solution here.

Read question.md for the problem statement.

Followers: user_id INT, follower_id INT
Output:    user_id, followers_count (order by user_id ascending)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(followers: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, followers: DataFrame) -> DataFrame:
    # The table is available as the view "Followers".
    followers.createOrReplaceTempView("Followers")
    raise NotImplementedError

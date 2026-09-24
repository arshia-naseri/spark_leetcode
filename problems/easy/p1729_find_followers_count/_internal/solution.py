"""1729. Find Followers Count.

https://leetcode.com/problems/find-followers-count/

For each user, return the number of followers. Order the result by
user_id in ascending order.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(followers: DataFrame) -> DataFrame:
    return (
        followers
        .groupBy("user_id")
        .agg(F.count("follower_id").alias("followers_count"))
        .orderBy("user_id")
    )


def solve_sql(spark: SparkSession, followers: DataFrame) -> DataFrame:
    followers.createOrReplaceTempView("Followers")
    return spark.sql(
        """
        SELECT user_id, COUNT(follower_id) AS followers_count
        FROM Followers
        GROUP BY user_id
        ORDER BY user_id
        """
    )

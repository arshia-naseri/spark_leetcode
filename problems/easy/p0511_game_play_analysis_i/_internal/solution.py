"""511. Game Play Analysis I.

https://leetcode.com/problems/game-play-analysis-i/

Find the first login date for each player.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(activity: DataFrame) -> DataFrame:
    return activity.groupBy("player_id").agg(F.min("event_date").alias("first_login"))


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    activity.createOrReplaceTempView("Activity")
    return spark.sql(
        """
        SELECT player_id, MIN(event_date) AS first_login
        FROM Activity
        GROUP BY player_id
        """
    )

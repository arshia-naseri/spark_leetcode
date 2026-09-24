"""1683. Invalid Tweets.

https://leetcode.com/problems/invalid-tweets/

Find the IDs of the invalid tweets. A tweet is invalid if the number of
characters in its content is strictly greater than 15.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(tweets: DataFrame) -> DataFrame:
    return tweets.filter(F.length("content") > 15).select("tweet_id")


def solve_sql(spark: SparkSession, tweets: DataFrame) -> DataFrame:
    tweets.createOrReplaceTempView("Tweets")
    return spark.sql(
        """
        SELECT tweet_id
        FROM Tweets
        WHERE LENGTH(content) > 15
        """
    )

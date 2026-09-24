"""1683. Invalid Tweets. Write your practice solution here.

Read question.md for the problem statement.

Tweets: tweet_id INT, content STRING
Output: tweet_id (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(tweets: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, tweets: DataFrame) -> DataFrame:
    # The table is available as the view "Tweets".
    tweets.createOrReplaceTempView("Tweets")
    raise NotImplementedError

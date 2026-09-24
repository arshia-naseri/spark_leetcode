"""1148. Article Views I.

https://leetcode.com/problems/article-views-i/

Find all the authors that viewed at least one of their own articles.
Sort the result by id in ascending order.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(views: DataFrame) -> DataFrame:
    return (
        views
        .filter(F.col("author_id") == F.col("viewer_id"))
        .select(F.col("author_id").alias("id"))
        .distinct()
        .orderBy("id")
    )


def solve_sql(spark: SparkSession, views: DataFrame) -> DataFrame:
    views.createOrReplaceTempView("Views")
    return spark.sql(
        """
        SELECT DISTINCT author_id AS id
        FROM Views
        WHERE author_id = viewer_id
        ORDER BY id
        """
    )

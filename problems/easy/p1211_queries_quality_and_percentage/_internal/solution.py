"""1211. Queries Quality and Percentage.

https://leetcode.com/problems/queries-quality-and-percentage/

For each query_name, find the quality (the average of rating / position)
and the poor query percentage (the percentage of rows with rating less
than 3). Round both values to 2 decimal places.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(queries: DataFrame) -> DataFrame:
    return queries.groupBy("query_name").agg(
        F.round(F.avg(F.col("rating") / F.col("position")), 2).alias("quality"),
        F.round(
            F.avg(F.when(F.col("rating") < 3, 1).otherwise(0)) * 100, 2
        ).alias("poor_query_percentage"),
    )


def solve_sql(spark: SparkSession, queries: DataFrame) -> DataFrame:
    queries.createOrReplaceTempView("Queries")
    return spark.sql(
        """
        SELECT
            query_name,
            ROUND(AVG(rating / position), 2) AS quality,
            ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2)
                AS poor_query_percentage
        FROM Queries
        GROUP BY query_name
        """
    )

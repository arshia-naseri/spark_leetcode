"""620. Not Boring Movies.

https://leetcode.com/problems/not-boring-movies/

Report the movies that have an odd-numbered ID and a description that is
not "boring". Sort the result by rating in descending order.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(cinema: DataFrame) -> DataFrame:
    return (
        cinema
        .filter((F.col("id") % 2 == 1) & (F.col("description") != "boring"))
        .orderBy(F.col("rating").desc())
    )


def solve_sql(spark: SparkSession, cinema: DataFrame) -> DataFrame:
    cinema.createOrReplaceTempView("Cinema")
    return spark.sql(
        """
        SELECT id, movie, description, rating
        FROM Cinema
        WHERE id % 2 = 1 AND description != 'boring'
        ORDER BY rating DESC
        """
    )

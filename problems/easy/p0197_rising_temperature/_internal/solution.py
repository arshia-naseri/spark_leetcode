"""197. Rising Temperature.

https://leetcode.com/problems/rising-temperature/

Find the id of each date that has a higher temperature than the day
before it (yesterday).
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(weather: DataFrame) -> DataFrame:
    today = weather.alias("t")
    yesterday = weather.alias("y")
    return (
        today
        .join(
            yesterday,
            (F.datediff(F.col("t.recordDate"), F.col("y.recordDate")) == 1)
            & (F.col("t.temperature") > F.col("y.temperature")),
        )
        .select(F.col("t.id").alias("id"))
    )


def solve_sql(spark: SparkSession, weather: DataFrame) -> DataFrame:
    weather.createOrReplaceTempView("Weather")
    return spark.sql(
        """
        SELECT t.id
        FROM Weather t
        JOIN Weather y
          ON DATEDIFF(t.recordDate, y.recordDate) = 1
         AND t.temperature > y.temperature
        """
    )

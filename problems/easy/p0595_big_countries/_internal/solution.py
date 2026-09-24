"""595. Big Countries.

https://leetcode.com/problems/big-countries/

A country is big if its area is at least 3000000 or its population is at
least 25000000. Find the name, population, and area of the big countries.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(world: DataFrame) -> DataFrame:
    return (
        world
        .filter((F.col("area") >= 3000000) | (F.col("population") >= 25000000))
        .select("name", "population", "area")
    )


def solve_sql(spark: SparkSession, world: DataFrame) -> DataFrame:
    world.createOrReplaceTempView("World")
    return spark.sql(
        """
        SELECT name, population, area
        FROM World
        WHERE area >= 3000000 OR population >= 25000000
        """
    )

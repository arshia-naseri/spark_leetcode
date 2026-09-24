"""595. Big Countries. Write your practice solution here.

Read question.md for the problem statement.

World:  name STRING, continent STRING, area INT, population INT, gdp BIGINT
Output: name, population, area (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(world: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, world: DataFrame) -> DataFrame:
    # The table is available as the view "World".
    world.createOrReplaceTempView("World")
    raise NotImplementedError

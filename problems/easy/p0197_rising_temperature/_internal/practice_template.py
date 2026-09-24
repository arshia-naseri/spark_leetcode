"""197. Rising Temperature. Write your practice solution here.

Read question.md for the problem statement.

Weather: id INT, recordDate DATE, temperature INT
Output:  id (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(weather: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, weather: DataFrame) -> DataFrame:
    # The table is available as the view "Weather".
    weather.createOrReplaceTempView("Weather")
    raise NotImplementedError

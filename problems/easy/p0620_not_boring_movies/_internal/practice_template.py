"""620. Not Boring Movies. Write your practice solution here.

Read question.md for the problem statement.

Cinema: id INT, movie STRING, description STRING, rating DOUBLE
Output: id, movie, description, rating (order by rating descending)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(cinema: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, cinema: DataFrame) -> DataFrame:
    # The table is available as the view "Cinema".
    cinema.createOrReplaceTempView("Cinema")
    raise NotImplementedError

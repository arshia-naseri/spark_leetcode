"""610. Triangle Judgement. Write your practice solution here.

Read question.md for the problem statement.

Triangle: x INT, y INT, z INT
Output:   x, y, z, triangle ("Yes" or "No") (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(triangle: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, triangle: DataFrame) -> DataFrame:
    # The table is available as the view "Triangle".
    triangle.createOrReplaceTempView("Triangle")
    raise NotImplementedError

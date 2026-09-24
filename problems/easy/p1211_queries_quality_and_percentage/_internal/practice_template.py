"""1211. Queries Quality and Percentage. Write your practice solution here.

Read question.md for the problem statement.

Queries: query_name STRING, result STRING, position INT, rating INT
Output:  query_name, quality, poor_query_percentage (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(queries: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, queries: DataFrame) -> DataFrame:
    # The table is available as the view "Queries".
    queries.createOrReplaceTempView("Queries")
    raise NotImplementedError

"""1148. Article Views I. Write your practice solution here.

Read question.md for the problem statement.

Views:  article_id INT, author_id INT, viewer_id INT, view_date DATE
Output: id (sorted by id in ascending order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(views: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, views: DataFrame) -> DataFrame:
    # The table is available as the view "Views".
    views.createOrReplaceTempView("Views")
    raise NotImplementedError

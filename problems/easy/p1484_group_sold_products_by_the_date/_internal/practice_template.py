"""1484. Group Sold Products By The Date. Write your practice solution here.

Read question.md for the problem statement.

Activities: sell_date DATE, product STRING
Output:     sell_date, num_sold, products (order by sell_date)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(activities: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, activities: DataFrame) -> DataFrame:
    # The table is available as the view "Activities".
    activities.createOrReplaceTempView("Activities")
    raise NotImplementedError

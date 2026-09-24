"""1693. Daily Leads and Partners. Write your practice solution here.

Read question.md for the problem statement.

DailySales: date_id DATE, make_name STRING, lead_id INT, partner_id INT
Output:     date_id, make_name, unique_leads, unique_partners (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(daily_sales: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, daily_sales: DataFrame) -> DataFrame:
    # The table is available as the view "DailySales".
    daily_sales.createOrReplaceTempView("DailySales")
    raise NotImplementedError

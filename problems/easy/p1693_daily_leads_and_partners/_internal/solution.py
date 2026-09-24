"""1693. Daily Leads and Partners.

https://leetcode.com/problems/daily-leads-and-partners/

For each date_id and make_name, find the number of distinct lead_id
values and distinct partner_id values.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(daily_sales: DataFrame) -> DataFrame:
    return (
        daily_sales
        .groupBy("date_id", "make_name")
        .agg(
            F.countDistinct("lead_id").alias("unique_leads"),
            F.countDistinct("partner_id").alias("unique_partners"),
        )
    )


def solve_sql(spark: SparkSession, daily_sales: DataFrame) -> DataFrame:
    daily_sales.createOrReplaceTempView("DailySales")
    return spark.sql(
        """
        SELECT
            date_id,
            make_name,
            COUNT(DISTINCT lead_id) AS unique_leads,
            COUNT(DISTINCT partner_id) AS unique_partners
        FROM DailySales
        GROUP BY date_id, make_name
        """
    )

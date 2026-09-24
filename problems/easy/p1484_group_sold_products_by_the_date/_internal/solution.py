"""1484. Group Sold Products By The Date.

https://leetcode.com/problems/group-sold-products-by-the-date/

For each date, find the number of different products sold and their names.
Sort the names lexicographically and join them with a comma. Order the
result by sell_date.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(activities: DataFrame) -> DataFrame:
    return (
        activities
        .groupBy("sell_date")
        .agg(
            F.countDistinct("product").alias("num_sold"),
            F.concat_ws(",", F.array_sort(F.collect_set("product"))).alias("products"),
        )
        .orderBy("sell_date")
    )


def solve_sql(spark: SparkSession, activities: DataFrame) -> DataFrame:
    activities.createOrReplaceTempView("Activities")
    return spark.sql(
        """
        SELECT
            sell_date,
            COUNT(DISTINCT product) AS num_sold,
            CONCAT_WS(',', ARRAY_SORT(COLLECT_SET(product))) AS products
        FROM Activities
        GROUP BY sell_date
        ORDER BY sell_date
        """
    )

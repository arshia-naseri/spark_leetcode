"""1251. Average Selling Price.

https://leetcode.com/problems/average-selling-price/

Find the average selling price for each product, rounded to 2 decimal
places. If a product has no sold units, its average selling price is 0.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(prices: DataFrame, units_sold: DataFrame) -> DataFrame:
    p = prices.alias("p")
    u = units_sold.alias("u")
    joined = p.join(
        u,
        (F.col("p.product_id") == F.col("u.product_id"))
        & F.col("u.purchase_date").between(F.col("p.start_date"), F.col("p.end_date")),
        how="left",
    )
    return (
        joined
        .groupBy(F.col("p.product_id").alias("product_id"))
        .agg(
            F.coalesce(
                F.round(F.sum(F.col("p.price") * F.col("u.units")) / F.sum("u.units"), 2),
                F.lit(0.0),
            ).alias("average_price")
        )
    )


def solve_sql(spark: SparkSession, prices: DataFrame, units_sold: DataFrame) -> DataFrame:
    prices.createOrReplaceTempView("Prices")
    units_sold.createOrReplaceTempView("UnitsSold")
    return spark.sql(
        """
        SELECT p.product_id,
               COALESCE(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0.0) AS average_price
        FROM Prices p
        LEFT JOIN UnitsSold u
          ON p.product_id = u.product_id
         AND u.purchase_date BETWEEN p.start_date AND p.end_date
        GROUP BY p.product_id
        """
    )

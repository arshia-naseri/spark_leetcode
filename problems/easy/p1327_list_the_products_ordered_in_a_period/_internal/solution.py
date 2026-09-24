"""1327. List the Products Ordered in a Period.

https://leetcode.com/problems/list-the-products-ordered-in-a-period/

Get the names of products that have at least 100 units ordered in
February 2020, and the total units.
"""

import datetime

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(products: DataFrame, orders: DataFrame) -> DataFrame:
    february = orders.filter(
        F.col("order_date").between(datetime.date(2020, 2, 1), datetime.date(2020, 2, 29))
    )
    totals = february.groupBy("product_id").agg(F.sum("unit").alias("unit"))
    return (
        totals
        .filter(F.col("unit") >= 100)
        .join(products, on="product_id")
        .select("product_name", "unit")
    )


def solve_sql(spark: SparkSession, products: DataFrame, orders: DataFrame) -> DataFrame:
    products.createOrReplaceTempView("Products")
    orders.createOrReplaceTempView("Orders")
    return spark.sql(
        """
        SELECT p.product_name, SUM(o.unit) AS unit
        FROM Orders o
        JOIN Products p ON o.product_id = p.product_id
        WHERE o.order_date BETWEEN DATE '2020-02-01' AND DATE '2020-02-29'
        GROUP BY p.product_id, p.product_name
        HAVING SUM(o.unit) >= 100
        """
    )

"""586. Customer Placing the Largest Number of Orders.

https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

Find the customer_number of the customer who has placed the largest number
of orders. If there is a tie, return all tied customers (follow-up).
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(orders: DataFrame) -> DataFrame:
    counts = orders.groupBy("customer_number").agg(F.count("*").alias("cnt"))
    top = counts.agg(F.max("cnt").alias("cnt"))
    return counts.join(top, on="cnt").select("customer_number")


def solve_sql(spark: SparkSession, orders: DataFrame) -> DataFrame:
    orders.createOrReplaceTempView("Orders")
    return spark.sql(
        """
        WITH counts AS (
            SELECT customer_number, COUNT(*) AS cnt
            FROM Orders
            GROUP BY customer_number
        )
        SELECT customer_number
        FROM counts
        WHERE cnt = (SELECT MAX(cnt) FROM counts)
        """
    )

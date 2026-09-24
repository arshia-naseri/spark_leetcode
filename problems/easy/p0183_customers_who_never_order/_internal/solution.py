"""183. Customers Who Never Order.

https://leetcode.com/problems/customers-who-never-order/

Find all customers who never order anything.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(customers: DataFrame, orders: DataFrame) -> DataFrame:
    return (
        customers.alias("c")
        .join(orders.alias("o"), F.col("c.id") == F.col("o.customerId"), how="left_anti")
        .select(F.col("c.name").alias("Customers"))
    )


def solve_sql(spark: SparkSession, customers: DataFrame, orders: DataFrame) -> DataFrame:
    customers.createOrReplaceTempView("Customers")
    orders.createOrReplaceTempView("Orders")
    return spark.sql(
        """
        SELECT c.name AS Customers
        FROM Customers c
        WHERE NOT EXISTS (
            SELECT 1 FROM Orders o WHERE o.customerId = c.id
        )
        """
    )

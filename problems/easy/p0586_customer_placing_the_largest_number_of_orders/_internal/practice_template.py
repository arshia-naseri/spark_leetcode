"""586. Customer Placing the Largest Number of Orders. Write your practice solution here.

Read question.md for the problem statement.

Orders: order_number INT, customer_number INT
Output: customer_number (any order; return all customers if there is a tie)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(orders: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, orders: DataFrame) -> DataFrame:
    # The table is available as the view "Orders".
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError

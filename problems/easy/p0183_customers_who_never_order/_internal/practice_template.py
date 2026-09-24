"""183. Customers Who Never Order. Write your practice solution here.

Read question.md for the problem statement.

Customers: id INT, name STRING
Orders:    id INT, customerId INT
Output:    Customers (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(customers: DataFrame, orders: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, customers: DataFrame, orders: DataFrame) -> DataFrame:
    # The tables are available as the views "Customers" and "Orders".
    customers.createOrReplaceTempView("Customers")
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError

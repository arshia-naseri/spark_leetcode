"""1068. Product Sales Analysis I. Write your practice solution here.

Read question.md for the problem statement.

Sales:   sale_id INT, product_id INT, year INT, quantity INT, price INT
Product: product_id INT, product_name STRING
Output:  product_name, year, price (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(sales: DataFrame, product: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, sales: DataFrame, product: DataFrame) -> DataFrame:
    # The tables are available as the views "Sales" and "Product".
    sales.createOrReplaceTempView("Sales")
    product.createOrReplaceTempView("Product")
    raise NotImplementedError

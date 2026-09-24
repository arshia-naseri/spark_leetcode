"""1084. Sales Analysis III. Write your practice solution here.

Read question.md for the problem statement.

Product: product_id INT, product_name STRING, unit_price INT
Sales:   seller_id INT, product_id INT, buyer_id INT, sale_date DATE, quantity INT, price INT
Output:  product_id, product_name (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(product: DataFrame, sales: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, product: DataFrame, sales: DataFrame) -> DataFrame:
    # The tables are available as the views "Product" and "Sales".
    product.createOrReplaceTempView("Product")
    sales.createOrReplaceTempView("Sales")
    raise NotImplementedError

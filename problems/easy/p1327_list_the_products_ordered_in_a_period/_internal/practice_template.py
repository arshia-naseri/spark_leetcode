"""1327. List the Products Ordered in a Period. Write your practice solution here.

Read question.md for the problem statement.

Products: product_id INT, product_name STRING, product_category STRING
Orders:   product_id INT, order_date DATE, unit INT
Output:   product_name, unit (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(products: DataFrame, orders: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, products: DataFrame, orders: DataFrame) -> DataFrame:
    # The tables are available as the views "Products" and "Orders".
    products.createOrReplaceTempView("Products")
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError

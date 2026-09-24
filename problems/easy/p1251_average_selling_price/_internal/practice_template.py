"""1251. Average Selling Price. Write your practice solution here.

Read question.md for the problem statement.

Prices:    product_id INT, start_date DATE, end_date DATE, price INT
UnitsSold: product_id INT, purchase_date DATE, units INT
Output:    product_id, average_price (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(prices: DataFrame, units_sold: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, prices: DataFrame, units_sold: DataFrame) -> DataFrame:
    # The tables are available as the views "Prices" and "UnitsSold".
    prices.createOrReplaceTempView("Prices")
    units_sold.createOrReplaceTempView("UnitsSold")
    raise NotImplementedError

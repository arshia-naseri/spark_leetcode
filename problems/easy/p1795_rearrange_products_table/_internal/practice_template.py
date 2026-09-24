"""1795. Rearrange Products Table. Write your practice solution here.

Read question.md for the problem statement.

Products: product_id INT, store1 INT, store2 INT, store3 INT
Output:   product_id, store, price (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(products: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, products: DataFrame) -> DataFrame:
    # The table is available as the view "Products".
    products.createOrReplaceTempView("Products")
    raise NotImplementedError

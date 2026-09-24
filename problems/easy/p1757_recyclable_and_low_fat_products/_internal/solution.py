"""1757. Recyclable and Low Fat Products.

https://leetcode.com/problems/recyclable-and-low-fat-products/

Find the ids of products that are both low fat and recyclable.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(products: DataFrame) -> DataFrame:
    return (
        products
        .where((F.col("low_fats") == "Y") & (F.col("recyclable") == "Y"))
        .select("product_id")
    )


def solve_sql(spark: SparkSession, products: DataFrame) -> DataFrame:
    products.createOrReplaceTempView("Products")
    return spark.sql(
        """
        SELECT product_id
        FROM Products
        WHERE low_fats = 'Y' AND recyclable = 'Y'
        """
    )

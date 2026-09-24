"""1068. Product Sales Analysis I.

https://leetcode.com/problems/product-sales-analysis-i/

Report the product_name, year, and price for each sale_id in the Sales table.
"""

from pyspark.sql import DataFrame, SparkSession


def solve(sales: DataFrame, product: DataFrame) -> DataFrame:
    return (
        sales
        .join(product, on="product_id", how="inner")
        .select("product_name", "year", "price")
    )


def solve_sql(spark: SparkSession, sales: DataFrame, product: DataFrame) -> DataFrame:
    sales.createOrReplaceTempView("Sales")
    product.createOrReplaceTempView("Product")
    return spark.sql(
        """
        SELECT p.product_name, s.year, s.price
        FROM Sales s
        JOIN Product p ON s.product_id = p.product_id
        """
    )

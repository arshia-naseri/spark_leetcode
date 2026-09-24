"""1795. Rearrange Products Table.

https://leetcode.com/problems/rearrange-products-table/

Rearrange the Products table so that each row has (product_id, store, price).
Do not include a row when the price in that store is null.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(products: DataFrame) -> DataFrame:
    return (
        products
        .unpivot("product_id", ["store1", "store2", "store3"], "store", "price")
        .where(F.col("price").isNotNull())
    )


def solve_sql(spark: SparkSession, products: DataFrame) -> DataFrame:
    products.createOrReplaceTempView("Products")
    return spark.sql(
        """
        SELECT product_id, 'store1' AS store, store1 AS price
        FROM Products WHERE store1 IS NOT NULL
        UNION ALL
        SELECT product_id, 'store2' AS store, store2 AS price
        FROM Products WHERE store2 IS NOT NULL
        UNION ALL
        SELECT product_id, 'store3' AS store, store3 AS price
        FROM Products WHERE store3 IS NOT NULL
        """
    )

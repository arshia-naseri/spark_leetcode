"""1084. Sales Analysis III.

https://leetcode.com/problems/sales-analysis-iii/

Report the products that were only sold in the first quarter of 2019
(from 2019-01-01 to 2019-03-31, inclusive).
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(product: DataFrame, sales: DataFrame) -> DataFrame:
    in_q1 = F.col("sale_date").between(F.lit("2019-01-01").cast("date"), F.lit("2019-03-31").cast("date"))
    sold_only_in_q1 = (
        sales
        .groupBy("product_id")
        .agg(F.min(in_q1.cast("int")).alias("all_in_q1"))
        .where(F.col("all_in_q1") == 1)
        .select("product_id")
    )
    return product.join(sold_only_in_q1, on="product_id", how="inner").select(
        "product_id", "product_name"
    )


def solve_sql(spark: SparkSession, product: DataFrame, sales: DataFrame) -> DataFrame:
    product.createOrReplaceTempView("Product")
    sales.createOrReplaceTempView("Sales")
    return spark.sql(
        """
        SELECT p.product_id, p.product_name
        FROM Product p
        JOIN Sales s ON p.product_id = s.product_id
        GROUP BY p.product_id, p.product_name
        HAVING MIN(s.sale_date) >= DATE '2019-01-01'
           AND MAX(s.sale_date) <= DATE '2019-03-31'
        """
    )

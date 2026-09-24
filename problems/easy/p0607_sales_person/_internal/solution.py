"""607. Sales Person.

https://leetcode.com/problems/sales-person/

Find the names of all the sales persons who did not have any orders
related to the company with the name "RED".
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(sales_person: DataFrame, company: DataFrame, orders: DataFrame) -> DataFrame:
    red_orders = (
        orders
        .join(company.filter(F.col("name") == "RED"), on="com_id", how="inner")
        .select("sales_id")
    )
    return (
        sales_person
        .join(red_orders, on="sales_id", how="left_anti")
        .select("name")
    )


def solve_sql(
    spark: SparkSession, sales_person: DataFrame, company: DataFrame, orders: DataFrame
) -> DataFrame:
    sales_person.createOrReplaceTempView("SalesPerson")
    company.createOrReplaceTempView("Company")
    orders.createOrReplaceTempView("Orders")
    return spark.sql(
        """
        SELECT s.name
        FROM SalesPerson s
        WHERE NOT EXISTS (
            SELECT 1
            FROM Orders o
            JOIN Company c ON o.com_id = c.com_id
            WHERE c.name = 'RED' AND o.sales_id = s.sales_id
        )
        """
    )

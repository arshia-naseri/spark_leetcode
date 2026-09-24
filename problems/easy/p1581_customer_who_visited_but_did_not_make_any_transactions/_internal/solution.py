"""1581. Customer Who Visited but Did Not Make Any Transactions.

https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

Find the IDs of the customers who visited without a transaction, and the
number of these visits for each customer.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(visits: DataFrame, transactions: DataFrame) -> DataFrame:
    return (
        visits
        .join(transactions, on="visit_id", how="left_anti")
        .groupBy("customer_id")
        .agg(F.count("*").alias("count_no_trans"))
    )


def solve_sql(spark: SparkSession, visits: DataFrame, transactions: DataFrame) -> DataFrame:
    visits.createOrReplaceTempView("Visits")
    transactions.createOrReplaceTempView("Transactions")
    return spark.sql(
        """
        SELECT v.customer_id, COUNT(*) AS count_no_trans
        FROM Visits v
        LEFT JOIN Transactions t ON v.visit_id = t.visit_id
        WHERE t.transaction_id IS NULL
        GROUP BY v.customer_id
        """
    )

"""1587. Bank Account Summary II.

https://leetcode.com/problems/bank-account-summary-ii/

Report the name and balance of users with a balance higher than 10000.
The balance of an account is the sum of the amounts of all transactions
of that account.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(users: DataFrame, transactions: DataFrame) -> DataFrame:
    return (
        users
        .join(transactions, on="account", how="inner")
        .groupBy("account", "name")
        .agg(F.sum("amount").alias("balance"))
        .where(F.col("balance") > 10000)
        .select("name", "balance")
    )


def solve_sql(spark: SparkSession, users: DataFrame, transactions: DataFrame) -> DataFrame:
    users.createOrReplaceTempView("Users")
    transactions.createOrReplaceTempView("Transactions")
    return spark.sql(
        """
        SELECT u.name, SUM(t.amount) AS balance
        FROM Users u
        JOIN Transactions t ON u.account = t.account
        GROUP BY u.account, u.name
        HAVING SUM(t.amount) > 10000
        """
    )

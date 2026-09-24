"""1587. Bank Account Summary II. Write your practice solution here.

Read question.md for the problem statement.

Users:        account INT, name STRING
Transactions: trans_id INT, account INT, amount INT, transacted_on DATE
Output:       name, balance (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(users: DataFrame, transactions: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, users: DataFrame, transactions: DataFrame) -> DataFrame:
    # The tables are available as the views "Users" and "Transactions".
    users.createOrReplaceTempView("Users")
    transactions.createOrReplaceTempView("Transactions")
    raise NotImplementedError

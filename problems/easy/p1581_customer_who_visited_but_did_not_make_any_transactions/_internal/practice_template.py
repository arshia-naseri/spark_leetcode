"""1581. Customer Who Visited but Did Not Make Any Transactions. Write your practice solution here.

Read question.md for the problem statement.

Visits:       visit_id INT, customer_id INT
Transactions: transaction_id INT, visit_id INT, amount INT
Output:       customer_id, count_no_trans (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(visits: DataFrame, transactions: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, visits: DataFrame, transactions: DataFrame) -> DataFrame:
    # The tables are available as the views "Visits" and "Transactions".
    visits.createOrReplaceTempView("Visits")
    transactions.createOrReplaceTempView("Transactions")
    raise NotImplementedError

"""584. Find Customer Referee. Write your practice solution here.

Read question.md for the problem statement.

Customer: id INT, name STRING, referee_id INT
Output:   name (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(customer: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, customer: DataFrame) -> DataFrame:
    # The table is available as the view "Customer".
    customer.createOrReplaceTempView("Customer")
    raise NotImplementedError

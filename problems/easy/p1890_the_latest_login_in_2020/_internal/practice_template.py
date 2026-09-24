"""1890. The Latest Login in 2020. Write your practice solution here.

Read question.md for the problem statement.

Logins: user_id INT, time_stamp TIMESTAMP_NTZ
Output: user_id, last_stamp (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(logins: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, logins: DataFrame) -> DataFrame:
    # The table is available as the view "Logins".
    logins.createOrReplaceTempView("Logins")
    raise NotImplementedError

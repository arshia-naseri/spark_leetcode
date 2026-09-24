"""619. Biggest Single Number. Write your practice solution here.

Read question.md for the problem statement.

MyNumbers: num INT
Output:    num (one row; null if there is no single number)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(my_numbers: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, my_numbers: DataFrame) -> DataFrame:
    # The table is available as the view "MyNumbers".
    my_numbers.createOrReplaceTempView("MyNumbers")
    raise NotImplementedError

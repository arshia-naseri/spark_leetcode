"""182. Duplicate Emails. Write your practice solution here.

Read question.md for the problem statement.

Person: id INT, email STRING
Output: Email (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(person: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, person: DataFrame) -> DataFrame:
    # The table is available as the view "Person".
    person.createOrReplaceTempView("Person")
    raise NotImplementedError

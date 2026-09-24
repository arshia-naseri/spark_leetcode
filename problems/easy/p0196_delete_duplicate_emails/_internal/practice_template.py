"""196. Delete Duplicate Emails. Write your practice solution here.

Read question.md for the problem statement.

Person: id INT, email STRING
Output: id, email (any order). Spark DataFrames are immutable: return the
Person table after the delete as a new DataFrame.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(person: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, person: DataFrame) -> DataFrame:
    # The table is available as the view "Person".
    # Spark views do not support DELETE. Use SELECT to get the rows that stay.
    person.createOrReplaceTempView("Person")
    raise NotImplementedError

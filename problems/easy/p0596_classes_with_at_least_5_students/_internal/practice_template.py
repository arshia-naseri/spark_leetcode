"""596. Classes With at Least 5 Students. Write your practice solution here.

Read question.md for the problem statement.

Courses: student STRING, class STRING
Output:  class (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(courses: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, courses: DataFrame) -> DataFrame:
    # The table is available as the view "Courses".
    courses.createOrReplaceTempView("Courses")
    raise NotImplementedError

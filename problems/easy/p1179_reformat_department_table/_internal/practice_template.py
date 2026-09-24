"""1179. Reformat Department Table. Write your practice solution here.

Read question.md for the problem statement.

Department: id INT, revenue INT, month STRING
Output:     id, Jan_Revenue, Feb_Revenue, ..., Dec_Revenue (13 columns, any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(department: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, department: DataFrame) -> DataFrame:
    # The table is available as the view "Department".
    department.createOrReplaceTempView("Department")
    raise NotImplementedError

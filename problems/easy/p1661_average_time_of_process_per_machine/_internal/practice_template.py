"""1661. Average Time of Process per Machine. Write your practice solution here.

Read question.md for the problem statement.

Activity: machine_id INT, process_id INT, activity_type STRING, timestamp DOUBLE
Output:   machine_id, processing_time (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(activity: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    # The table is available as the view "Activity".
    activity.createOrReplaceTempView("Activity")
    raise NotImplementedError

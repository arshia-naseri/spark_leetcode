"""1141. User Activity for the Past 30 Days I. Write your practice solution here.

Read question.md for the problem statement.

Activity: user_id INT, session_id INT, activity_date DATE, activity_type STRING
Output:   day, active_users (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(activity: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    # The table is available as the view "Activity".
    activity.createOrReplaceTempView("Activity")
    raise NotImplementedError

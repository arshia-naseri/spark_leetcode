"""511. Game Play Analysis I. Write your practice solution here.

Read question.md for the problem statement.

Activity: player_id INT, device_id INT, event_date DATE, games_played INT
Output:   player_id, first_login (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(activity: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    # The table is available as the view "Activity".
    activity.createOrReplaceTempView("Activity")
    raise NotImplementedError

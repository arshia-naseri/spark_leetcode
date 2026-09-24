"""1141. User Activity for the Past 30 Days I.

https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

Find the daily active user count for a period of 30 days that ends on
2019-07-27 (inclusive). A user is active on a day if the user made at
least one activity on that day.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(activity: DataFrame) -> DataFrame:
    return (
        activity
        .where(F.col("activity_date").between("2019-06-28", "2019-07-27"))
        .groupBy(F.col("activity_date").alias("day"))
        .agg(F.countDistinct("user_id").alias("active_users"))
    )


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    activity.createOrReplaceTempView("Activity")
    return spark.sql(
        """
        SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
        FROM Activity
        WHERE activity_date BETWEEN DATE '2019-06-28' AND DATE '2019-07-27'
        GROUP BY activity_date
        """
    )

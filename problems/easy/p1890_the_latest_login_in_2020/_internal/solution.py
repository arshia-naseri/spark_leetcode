"""1890. The Latest Login in 2020.

https://leetcode.com/problems/the-latest-login-in-2020/

Report the latest login in the year 2020 for each user. Do not include
the users who did not login in 2020.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(logins: DataFrame) -> DataFrame:
    return (
        logins
        .where(F.year("time_stamp") == 2020)
        .groupBy("user_id")
        .agg(F.max("time_stamp").alias("last_stamp"))
    )


def solve_sql(spark: SparkSession, logins: DataFrame) -> DataFrame:
    logins.createOrReplaceTempView("Logins")
    return spark.sql(
        """
        SELECT user_id, MAX(time_stamp) AS last_stamp
        FROM Logins
        WHERE YEAR(time_stamp) = 2020
        GROUP BY user_id
        """
    )

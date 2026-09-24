"""1633. Percentage of Users Attended a Contest.

https://leetcode.com/problems/percentage-of-users-attended-a-contest/

Find the percentage of the users that registered in each contest, rounded
to two decimals. Order by percentage descending, then by contest_id
ascending.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(users: DataFrame, register: DataFrame) -> DataFrame:
    total = users.count()
    return (
        register
        .groupBy("contest_id")
        .agg(F.round(F.count("user_id") * 100 / F.lit(total), 2).alias("percentage"))
        .orderBy(F.col("percentage").desc(), F.col("contest_id").asc())
    )


def solve_sql(spark: SparkSession, users: DataFrame, register: DataFrame) -> DataFrame:
    users.createOrReplaceTempView("Users")
    register.createOrReplaceTempView("Register")
    return spark.sql(
        """
        SELECT contest_id,
               ROUND(COUNT(user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
        FROM Register
        GROUP BY contest_id
        ORDER BY percentage DESC, contest_id ASC
        """
    )

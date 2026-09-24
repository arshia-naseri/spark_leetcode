"""1667. Fix Names in a Table.

https://leetcode.com/problems/fix-names-in-a-table/

Fix the names so that only the first character is uppercase and the rest
are lowercase. Order the result by user_id.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(users: DataFrame) -> DataFrame:
    return (
        users
        .select(
            "user_id",
            F.concat(
                F.upper(F.substring("name", 1, 1)),
                F.lower(F.expr("substring(name, 2)")),
            ).alias("name"),
        )
        .orderBy("user_id")
    )


def solve_sql(spark: SparkSession, users: DataFrame) -> DataFrame:
    users.createOrReplaceTempView("Users")
    return spark.sql(
        """
        SELECT user_id,
               CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
        FROM Users
        ORDER BY user_id
        """
    )

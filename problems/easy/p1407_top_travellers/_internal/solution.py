"""1407. Top Travellers.

https://leetcode.com/problems/top-travellers/

Report the distance traveled by each user. A user with no rides has a
distance of 0. Order by travelled_distance descending, then by name
ascending.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(users: DataFrame, rides: DataFrame) -> DataFrame:
    totals = rides.groupBy("user_id").agg(F.sum("distance").alias("total"))
    return (
        users
        .join(totals, users["id"] == totals["user_id"], how="left")
        .select(
            users["name"],
            F.coalesce(totals["total"], F.lit(0).cast("bigint")).alias("travelled_distance"),
        )
        .orderBy(F.col("travelled_distance").desc(), F.col("name").asc())
    )


def solve_sql(spark: SparkSession, users: DataFrame, rides: DataFrame) -> DataFrame:
    users.createOrReplaceTempView("Users")
    rides.createOrReplaceTempView("Rides")
    return spark.sql(
        """
        SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
        FROM Users u
        LEFT JOIN Rides r ON u.id = r.user_id
        GROUP BY u.id, u.name
        ORDER BY travelled_distance DESC, u.name ASC
        """
    )

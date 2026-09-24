"""1050. Actors and Directors Who Cooperated At Least Three Times.

https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

Find all the pairs (actor_id, director_id) where the actor cooperated with
the director at least three times.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(actor_director: DataFrame) -> DataFrame:
    return (
        actor_director
        .groupBy("actor_id", "director_id")
        .agg(F.count("*").alias("cnt"))
        .filter(F.col("cnt") >= 3)
        .select("actor_id", "director_id")
    )


def solve_sql(spark: SparkSession, actor_director: DataFrame) -> DataFrame:
    actor_director.createOrReplaceTempView("ActorDirector")
    return spark.sql(
        """
        SELECT actor_id, director_id
        FROM ActorDirector
        GROUP BY actor_id, director_id
        HAVING COUNT(*) >= 3
        """
    )

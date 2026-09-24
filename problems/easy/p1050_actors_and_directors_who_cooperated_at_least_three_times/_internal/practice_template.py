"""1050. Actors and Directors Who Cooperated At Least Three Times. Write your practice solution here.

Read question.md for the problem statement.

ActorDirector: actor_id INT, director_id INT, timestamp INT
Output:        actor_id, director_id (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(actor_director: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, actor_director: DataFrame) -> DataFrame:
    # The table is available as the view "ActorDirector".
    actor_director.createOrReplaceTempView("ActorDirector")
    raise NotImplementedError

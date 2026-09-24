from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, actor_director: DataFrame) -> DataFrame:
    # The table is available as the view "ActorDirector".
    actor_director.createOrReplaceTempView("ActorDirector")
    raise NotImplementedError

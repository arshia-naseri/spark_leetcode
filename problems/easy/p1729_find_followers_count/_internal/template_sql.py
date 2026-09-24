from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, followers: DataFrame) -> DataFrame:
    # The table is available as the view "Followers".
    followers.createOrReplaceTempView("Followers")
    raise NotImplementedError

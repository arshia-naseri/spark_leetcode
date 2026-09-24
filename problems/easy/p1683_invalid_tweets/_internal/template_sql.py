from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, tweets: DataFrame) -> DataFrame:
    # The table is available as the view "Tweets".
    tweets.createOrReplaceTempView("Tweets")
    raise NotImplementedError

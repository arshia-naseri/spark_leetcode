from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, cinema: DataFrame) -> DataFrame:
    # The table is available as the view "Cinema".
    cinema.createOrReplaceTempView("Cinema")
    raise NotImplementedError

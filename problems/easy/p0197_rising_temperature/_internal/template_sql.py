from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, weather: DataFrame) -> DataFrame:
    # The table is available as the view "Weather".
    weather.createOrReplaceTempView("Weather")
    raise NotImplementedError

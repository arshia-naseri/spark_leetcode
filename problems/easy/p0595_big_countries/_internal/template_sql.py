from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, world: DataFrame) -> DataFrame:
    # The table is available as the view "World".
    world.createOrReplaceTempView("World")
    raise NotImplementedError

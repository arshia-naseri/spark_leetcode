from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, activities: DataFrame) -> DataFrame:
    # The table is available as the view "Activities".
    activities.createOrReplaceTempView("Activities")
    raise NotImplementedError

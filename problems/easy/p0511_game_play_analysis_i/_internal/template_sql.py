from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    # The table is available as the view "Activity".
    activity.createOrReplaceTempView("Activity")
    raise NotImplementedError

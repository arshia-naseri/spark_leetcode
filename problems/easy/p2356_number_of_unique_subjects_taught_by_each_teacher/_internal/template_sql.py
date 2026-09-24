from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, teacher: DataFrame) -> DataFrame:
    # The table is available as the view "Teacher".
    teacher.createOrReplaceTempView("Teacher")
    raise NotImplementedError

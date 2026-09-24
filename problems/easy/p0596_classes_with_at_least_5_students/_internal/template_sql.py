from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, courses: DataFrame) -> DataFrame:
    # The table is available as the view "Courses".
    courses.createOrReplaceTempView("Courses")
    raise NotImplementedError

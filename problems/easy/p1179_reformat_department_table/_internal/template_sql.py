from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, department: DataFrame) -> DataFrame:
    # The table is available as the view "Department".
    department.createOrReplaceTempView("Department")
    raise NotImplementedError

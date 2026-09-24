from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, my_numbers: DataFrame) -> DataFrame:
    # The table is available as the view "MyNumbers".
    my_numbers.createOrReplaceTempView("MyNumbers")
    raise NotImplementedError

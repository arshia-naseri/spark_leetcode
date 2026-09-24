from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, person: DataFrame) -> DataFrame:
    # The table is available as the view "Person".
    person.createOrReplaceTempView("Person")
    raise NotImplementedError

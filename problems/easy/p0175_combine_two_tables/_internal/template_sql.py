from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, person: DataFrame, address: DataFrame) -> DataFrame:
    # The tables are available as the views "Person" and "Address".
    person.createOrReplaceTempView("Person")
    address.createOrReplaceTempView("Address")
    raise NotImplementedError

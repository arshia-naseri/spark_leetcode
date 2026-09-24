from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, employee: DataFrame, bonus: DataFrame) -> DataFrame:
    # The tables are available as the views "Employee" and "Bonus".
    employee.createOrReplaceTempView("Employee")
    bonus.createOrReplaceTempView("Bonus")
    raise NotImplementedError

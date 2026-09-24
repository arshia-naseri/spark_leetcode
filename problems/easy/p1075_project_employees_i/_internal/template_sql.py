from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, project: DataFrame, employee: DataFrame) -> DataFrame:
    # The tables are available as the views "Project" and "Employee".
    project.createOrReplaceTempView("Project")
    employee.createOrReplaceTempView("Employee")
    raise NotImplementedError

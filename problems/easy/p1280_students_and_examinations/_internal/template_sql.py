from pyspark.sql import DataFrame, SparkSession


def solve_sql(
    spark: SparkSession, students: DataFrame, subjects: DataFrame, examinations: DataFrame
) -> DataFrame:
    # The tables are available as the views "Students", "Subjects" and "Examinations".
    students.createOrReplaceTempView("Students")
    subjects.createOrReplaceTempView("Subjects")
    examinations.createOrReplaceTempView("Examinations")
    raise NotImplementedError

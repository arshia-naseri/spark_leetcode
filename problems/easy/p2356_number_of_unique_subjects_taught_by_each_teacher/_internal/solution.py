"""2356. Number of Unique Subjects Taught by Each Teacher.

https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

Calculate the number of unique subjects that each teacher teaches.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(teacher: DataFrame) -> DataFrame:
    return teacher.groupBy("teacher_id").agg(
        F.countDistinct("subject_id").alias("cnt")
    )


def solve_sql(spark: SparkSession, teacher: DataFrame) -> DataFrame:
    teacher.createOrReplaceTempView("Teacher")
    return spark.sql(
        """
        SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
        FROM Teacher
        GROUP BY teacher_id
        """
    )

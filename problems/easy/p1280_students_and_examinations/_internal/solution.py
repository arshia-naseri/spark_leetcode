"""1280. Students and Examinations.

https://leetcode.com/problems/students-and-examinations/

Find the number of times each student attended each exam. Include all
students and all subjects. Order by student_id and subject_name.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(students: DataFrame, subjects: DataFrame, examinations: DataFrame) -> DataFrame:
    counts = examinations.groupBy("student_id", "subject_name").agg(
        F.count("*").alias("attended_exams")
    )
    return (
        students
        .crossJoin(subjects)
        .join(counts, on=["student_id", "subject_name"], how="left")
        .select(
            "student_id",
            "student_name",
            "subject_name",
            F.coalesce(F.col("attended_exams"), F.lit(0).cast("bigint")).alias("attended_exams"),
        )
        .orderBy("student_id", "subject_name")
    )


def solve_sql(
    spark: SparkSession, students: DataFrame, subjects: DataFrame, examinations: DataFrame
) -> DataFrame:
    students.createOrReplaceTempView("Students")
    subjects.createOrReplaceTempView("Subjects")
    examinations.createOrReplaceTempView("Examinations")
    return spark.sql(
        """
        SELECT s.student_id, s.student_name, sub.subject_name,
               COUNT(e.student_id) AS attended_exams
        FROM Students s
        CROSS JOIN Subjects sub
        LEFT JOIN Examinations e
          ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
        GROUP BY s.student_id, s.student_name, sub.subject_name
        ORDER BY s.student_id, sub.subject_name
        """
    )

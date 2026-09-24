"""1280. Students and Examinations. Write your practice solution here.

Read question.md for the problem statement.

Students:     student_id INT, student_name STRING
Subjects:     subject_name STRING
Examinations: student_id INT, subject_name STRING
Output:       student_id, student_name, subject_name, attended_exams
              (order by student_id and subject_name)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(students: DataFrame, subjects: DataFrame, examinations: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(
    spark: SparkSession, students: DataFrame, subjects: DataFrame, examinations: DataFrame
) -> DataFrame:
    # The tables are available as the views "Students", "Subjects" and "Examinations".
    students.createOrReplaceTempView("Students")
    subjects.createOrReplaceTempView("Subjects")
    examinations.createOrReplaceTempView("Examinations")
    raise NotImplementedError

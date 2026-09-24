"""2356. Number of Unique Subjects Taught by Each Teacher. Write your practice solution here.

Read question.md for the problem statement.

Teacher: teacher_id INT, subject_id INT, dept_id INT
Output:  teacher_id, cnt (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(teacher: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, teacher: DataFrame) -> DataFrame:
    # The table is available as the view "Teacher".
    teacher.createOrReplaceTempView("Teacher")
    raise NotImplementedError

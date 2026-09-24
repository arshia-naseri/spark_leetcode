import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import (
    EXAMINATIONS_SCHEMA,
    EXAMPLE_EXAMINATIONS,
    EXAMPLE_STUDENTS,
    EXAMPLE_SUBJECTS,
    STUDENTS_SCHEMA,
    SUBJECTS_SCHEMA,
)

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    students = spark.createDataFrame(EXAMPLE_STUDENTS, STUDENTS_SCHEMA)
    subjects = spark.createDataFrame(EXAMPLE_SUBJECTS, SUBJECTS_SCHEMA)
    examinations = spark.createDataFrame(EXAMPLE_EXAMINATIONS, EXAMINATIONS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(students, subjects, examinations)),
        ("SQL", lambda: module.solve_sql(spark, students, subjects, examinations)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

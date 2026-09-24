import sys

from common.practice import load
from common.spark import get_spark

from .data import (
    EXAMINATIONS_SCHEMA,
    EXAMPLE_EXAMINATIONS,
    EXAMPLE_STUDENTS,
    EXAMPLE_SUBJECTS,
    STUDENTS_SCHEMA,
    SUBJECTS_SCHEMA,
)

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    students = spark.createDataFrame(EXAMPLE_STUDENTS, STUDENTS_SCHEMA)
    subjects = spark.createDataFrame(EXAMPLE_SUBJECTS, SUBJECTS_SCHEMA)
    examinations = spark.createDataFrame(EXAMPLE_EXAMINATIONS, EXAMINATIONS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(students, subjects, examinations)),
        ("SQL", lambda: module("sql").solve_sql(spark, students, subjects, examinations)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()

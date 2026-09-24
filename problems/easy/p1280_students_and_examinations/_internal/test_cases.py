import pytest

from common.leetcode import check
from common.practice import load

from .data import CASES, EXAMINATIONS_SCHEMA, OUTPUT_SCHEMA, STUDENTS_SCHEMA, SUBJECTS_SCHEMA

MODULES = ["practice", "solution"]


@pytest.mark.parametrize("method", ["dataframe", "sql"])
@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize(
    "students_rows, subjects_rows, examinations_rows, expected_rows",
    CASES,
    ids=[f"case{i}" for i in range(1, len(CASES) + 1)],
)
def test_case(
    spark,
    request,
    module_name,
    method,
    students_rows,
    subjects_rows,
    examinations_rows,
    expected_rows,
):
    # Import in run(). Then check() shows an error in the file as a Runtime Error.
    module = lambda: load(__package__, module_name, method)  # noqa: E731
    students = spark.createDataFrame(students_rows, STUDENTS_SCHEMA)
    subjects = spark.createDataFrame(subjects_rows, SUBJECTS_SCHEMA)
    examinations = spark.createDataFrame(examinations_rows, EXAMINATIONS_SCHEMA)
    expected = spark.createDataFrame(expected_rows, OUTPUT_SCHEMA)

    if method == "dataframe":
        run = lambda: module().solve(students, subjects, examinations)  # noqa: E731
    else:
        run = lambda: module().solve_sql(spark, students, subjects, examinations)  # noqa: E731

    check(
        request,
        {"Students": students, "Subjects": subjects, "Examinations": examinations},
        run,
        expected,
    )

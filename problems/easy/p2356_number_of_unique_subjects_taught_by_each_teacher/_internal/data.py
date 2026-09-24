TEACHER_SCHEMA = "teacher_id INT, subject_id INT, dept_id INT"
OUTPUT_SCHEMA = "teacher_id INT, cnt BIGINT"

EXAMPLE_TEACHER = [
    (1, 2, 3),
    (1, 2, 4),
    (1, 3, 3),
    (2, 1, 1),
    (2, 2, 1),
    (2, 3, 1),
    (2, 4, 1),
]
EXAMPLE_OUTPUT = [
    (1, 2),
    (2, 4),
]

# Each case: (teacher rows, expected output rows).
CASES = [
    (EXAMPLE_TEACHER, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One teacher teaches one subject in many departments.
    ([(7, 5, 1), (7, 5, 2), (7, 5, 3)], [(7, 1)]),
    # Two teachers teach the same subject in different departments.
    (
        [(1, 10, 1), (2, 10, 2), (2, 11, 2)],
        [(1, 1), (2, 2)],
    ),
    # One row.
    ([(3, 9, 9)], [(3, 1)]),
]

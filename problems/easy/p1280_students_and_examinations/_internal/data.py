STUDENTS_SCHEMA = "student_id INT, student_name STRING"
SUBJECTS_SCHEMA = "subject_name STRING"
EXAMINATIONS_SCHEMA = "student_id INT, subject_name STRING"
OUTPUT_SCHEMA = "student_id INT, student_name STRING, subject_name STRING, attended_exams BIGINT"

EXAMPLE_STUDENTS = [
    (1, "Alice"),
    (2, "Bob"),
    (13, "John"),
    (6, "Alex"),
]
EXAMPLE_SUBJECTS = [
    ("Math",),
    ("Physics",),
    ("Programming",),
]
EXAMPLE_EXAMINATIONS = [
    (1, "Math"),
    (1, "Physics"),
    (1, "Programming"),
    (2, "Programming"),
    (1, "Physics"),
    (1, "Math"),
    (13, "Math"),
    (13, "Programming"),
    (13, "Physics"),
    (2, "Math"),
    (1, "Math"),
]
EXAMPLE_OUTPUT = [
    (1, "Alice", "Math", 3),
    (1, "Alice", "Physics", 2),
    (1, "Alice", "Programming", 1),
    (2, "Bob", "Math", 1),
    (2, "Bob", "Physics", 0),
    (2, "Bob", "Programming", 1),
    (6, "Alex", "Math", 0),
    (6, "Alex", "Physics", 0),
    (6, "Alex", "Programming", 0),
    (13, "John", "Math", 1),
    (13, "John", "Physics", 1),
    (13, "John", "Programming", 1),
]

# Each case: (students rows, subjects rows, examinations rows, expected output rows).
CASES = [
    (EXAMPLE_STUDENTS, EXAMPLE_SUBJECTS, EXAMPLE_EXAMINATIONS, EXAMPLE_OUTPUT),
    # No exams: each student and subject pair has 0.
    (
        [(1, "Alice"), (2, "Bob")],
        [("Math",), ("Physics",)],
        [],
        [
            (1, "Alice", "Math", 0),
            (1, "Alice", "Physics", 0),
            (2, "Bob", "Math", 0),
            (2, "Bob", "Physics", 0),
        ],
    ),
    # No students: empty result.
    ([], EXAMPLE_SUBJECTS, EXAMPLE_EXAMINATIONS, []),
    # No subjects: empty result.
    (EXAMPLE_STUDENTS, [], EXAMPLE_EXAMINATIONS, []),
    # Exams for an unknown student or an unknown subject are not counted.
    (
        [(1, "Alice")],
        [("Math",)],
        [(1, "Math"), (99, "Math"), (1, "Art")],
        [(1, "Alice", "Math", 1)],
    ),
    # Two students with the same name: group by student_id, not by name.
    (
        [(1, "Sam"), (2, "Sam")],
        [("Math",)],
        [(2, "Math"), (2, "Math")],
        [(1, "Sam", "Math", 0), (2, "Sam", "Math", 2)],
    ),
]

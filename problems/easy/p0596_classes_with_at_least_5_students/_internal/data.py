COURSES_SCHEMA = "student STRING, class STRING"
OUTPUT_SCHEMA = "class STRING"

EXAMPLE_COURSES = [
    ("A", "Math"),
    ("B", "English"),
    ("C", "Math"),
    ("D", "Biology"),
    ("E", "Math"),
    ("F", "Computer"),
    ("G", "Math"),
    ("H", "Math"),
    ("I", "Math"),
]
EXAMPLE_OUTPUT = [
    ("Math",),
]

# Each case: (courses rows, expected output rows).
CASES = [
    (EXAMPLE_COURSES, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No class has five students.
    (
        [("A", "Math"), ("B", "Math"), ("C", "Math"), ("D", "Math"), ("E", "Art")],
        [],
    ),
    # Exactly five students is enough. Four students is not enough.
    (
        [
            ("A", "Math"), ("B", "Math"), ("C", "Math"), ("D", "Math"), ("E", "Math"),
            ("A", "Art"), ("B", "Art"), ("C", "Art"), ("D", "Art"),
        ],
        [("Math",)],
    ),
    # Two classes have five or more students. One student is in many classes.
    (
        [
            ("A", "Math"), ("B", "Math"), ("C", "Math"), ("D", "Math"), ("E", "Math"),
            ("A", "Art"), ("B", "Art"), ("C", "Art"), ("D", "Art"), ("E", "Art"),
            ("F", "Art"), ("A", "Music"),
        ],
        [("Math",), ("Art",)],
    ),
]

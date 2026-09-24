PERSON_SCHEMA = "id INT, email STRING"
OUTPUT_SCHEMA = "Email STRING"

EXAMPLE_PERSON = [
    (1, "a@b.com"),
    (2, "c@d.com"),
    (3, "a@b.com"),
]
EXAMPLE_OUTPUT = [
    ("a@b.com",),
]

# Each case: (person rows, expected output rows).
CASES = [
    (EXAMPLE_PERSON, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No duplicates.
    ([(1, "a@b.com"), (2, "c@d.com")], []),
    # One email three times: show it one time only.
    ([(1, "x@y.com"), (2, "x@y.com"), (3, "x@y.com")], [("x@y.com",)]),
    # Two different duplicate emails and one unique email.
    (
        [(1, "a@b.com"), (2, "c@d.com"), (3, "a@b.com"), (4, "c@d.com"), (5, "e@f.com")],
        [("a@b.com",), ("c@d.com",)],
    ),
]

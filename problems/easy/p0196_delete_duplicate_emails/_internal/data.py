PERSON_SCHEMA = "id INT, email STRING"
OUTPUT_SCHEMA = "id INT, email STRING"

EXAMPLE_PERSON = [
    (1, "john@example.com"),
    (2, "bob@example.com"),
    (3, "john@example.com"),
]
EXAMPLE_OUTPUT = [
    (1, "john@example.com"),
    (2, "bob@example.com"),
]

# Each case: (person rows, expected output rows).
CASES = [
    (EXAMPLE_PERSON, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No duplicates: all rows stay.
    (
        [(1, "a@x.com"), (2, "b@x.com"), (3, "c@x.com")],
        [(1, "a@x.com"), (2, "b@x.com"), (3, "c@x.com")],
    ),
    # All rows have the same email: only the smallest id stays.
    (
        [(7, "a@x.com"), (4, "a@x.com"), (9, "a@x.com")],
        [(4, "a@x.com")],
    ),
    # Smallest id is not the first row. Many duplicate groups.
    (
        [
            (5, "a@x.com"),
            (2, "a@x.com"),
            (8, "b@x.com"),
            (3, "b@x.com"),
            (6, "b@x.com"),
            (1, "c@x.com"),
        ],
        [(2, "a@x.com"), (3, "b@x.com"), (1, "c@x.com")],
    ),
]

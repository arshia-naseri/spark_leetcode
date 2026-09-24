USERS_SCHEMA = "user_id INT, name STRING"
OUTPUT_SCHEMA = "user_id INT, name STRING"

EXAMPLE_USERS = [
    (1, "aLice"),
    (2, "bOB"),
]
EXAMPLE_OUTPUT = [
    (1, "Alice"),
    (2, "Bob"),
]

# Each case: (users rows, expected output rows).
CASES = [
    (EXAMPLE_USERS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One-character names, names that are already correct, all uppercase, all lowercase.
    (
        [(1, "a"), (2, "B"), (3, "Carol"), (4, "DAVE"), (5, "eve")],
        [(1, "A"), (2, "B"), (3, "Carol"), (4, "Dave"), (5, "Eve")],
    ),
    # Duplicate names with different case.
    (
        [(1, "sAM"), (2, "SAM"), (3, "sam")],
        [(1, "Sam"), (2, "Sam"), (3, "Sam")],
    ),
    # Null name stays null.
    (
        [(1, None), (2, "jOHN")],
        [(1, None), (2, "John")],
    ),
]

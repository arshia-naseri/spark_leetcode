USERS_SCHEMA = "user_id INT, user_name STRING"
REGISTER_SCHEMA = "contest_id INT, user_id INT"
OUTPUT_SCHEMA = "contest_id INT, percentage DOUBLE"

EXAMPLE_USERS = [
    (6, "Alice"),
    (2, "Bob"),
    (7, "Alex"),
]
EXAMPLE_REGISTER = [
    (215, 6),
    (209, 2),
    (208, 2),
    (210, 6),
    (208, 6),
    (209, 7),
    (209, 6),
    (215, 7),
    (208, 7),
    (210, 2),
    (207, 2),
    (210, 7),
]
EXAMPLE_OUTPUT = [
    (208, 100.0),
    (209, 100.0),
    (210, 100.0),
    (215, 66.67),
    (207, 33.33),
]

# Each case: (users rows, register rows, expected output rows).
CASES = [
    (EXAMPLE_USERS, EXAMPLE_REGISTER, EXAMPLE_OUTPUT),
    # No registrations: no contests in the output.
    (EXAMPLE_USERS, [], []),
    # One user: each contest is 100 percent.
    ([(1, "Ann")], [(10, 1), (11, 1)], [(10, 100.0), (11, 100.0)]),
    # Six users: 1/6 = 16.67 and 5/6 = 83.33 (round half up).
    (
        [(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E"), (6, "F")],
        [(1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)],
        [(2, 83.33), (1, 16.67)],
    ),
    # Seven users, some users not in a contest: 1/7 = 14.29, 2/7 = 28.57.
    (
        [(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E"), (6, "F"), (7, "G")],
        [(5, 1), (3, 2), (3, 3)],
        [(3, 28.57), (5, 14.29)],
    ),
]

USERS_SCHEMA = "id INT, name STRING"
RIDES_SCHEMA = "id INT, user_id INT, distance INT"
OUTPUT_SCHEMA = "name STRING, travelled_distance BIGINT"

EXAMPLE_USERS = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Alex"),
    (4, "Donald"),
    (7, "Lee"),
    (13, "Jonathan"),
    (19, "Elvis"),
]
EXAMPLE_RIDES = [
    (1, 1, 120),
    (2, 2, 317),
    (3, 3, 222),
    (4, 7, 100),
    (5, 13, 312),
    (6, 19, 50),
    (7, 7, 120),
    (8, 19, 400),
    (9, 7, 230),
]
EXAMPLE_OUTPUT = [
    ("Elvis", 450),
    ("Lee", 450),
    ("Bob", 317),
    ("Jonathan", 312),
    ("Alex", 222),
    ("Alice", 120),
    ("Donald", 0),
]

# Each case: (users rows, rides rows, expected output rows).
CASES = [
    (EXAMPLE_USERS, EXAMPLE_RIDES, EXAMPLE_OUTPUT),
    # No rides: each user traveled 0.
    (
        [(1, "Alice"), (2, "Bob")],
        [],
        [("Alice", 0), ("Bob", 0)],
    ),
    # No users: empty result.
    ([], EXAMPLE_RIDES, []),
    # Two users with the same name: group by id, not by name.
    (
        [(1, "Sam"), (2, "Sam"), (3, "Ann")],
        [(1, 1, 10), (2, 2, 20), (3, 1, 5)],
        [("Sam", 20), ("Sam", 15), ("Ann", 0)],
    ),
    # Rides of a user_id that is not in Users are not in the result.
    (
        [(1, "Alice")],
        [(1, 1, 100), (2, 99, 500)],
        [("Alice", 100)],
    ),
]

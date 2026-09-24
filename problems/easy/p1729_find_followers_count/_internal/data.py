FOLLOWERS_SCHEMA = "user_id INT, follower_id INT"
OUTPUT_SCHEMA = "user_id INT, followers_count BIGINT"

EXAMPLE_FOLLOWERS = [
    (0, 1),
    (1, 0),
    (2, 0),
    (2, 1),
]
EXAMPLE_OUTPUT = [
    (0, 1),
    (1, 1),
    (2, 2),
]

# Each case: (followers rows, expected output rows).
CASES = [
    (EXAMPLE_FOLLOWERS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One user with many followers. Followers that have no followers do not show.
    ([(5, 1), (5, 2), (5, 3), (5, 4)], [(5, 4)]),
    # Each user has one follower. The users are not in ID order.
    ([(9, 1), (3, 1), (7, 2)], [(3, 1), (7, 1), (9, 1)]),
]

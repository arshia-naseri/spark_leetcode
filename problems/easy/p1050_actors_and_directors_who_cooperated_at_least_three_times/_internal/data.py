ACTOR_DIRECTOR_SCHEMA = "actor_id INT, director_id INT, timestamp INT"
OUTPUT_SCHEMA = "actor_id INT, director_id INT"

EXAMPLE_ACTOR_DIRECTOR = [
    (1, 1, 0),
    (1, 1, 1),
    (1, 1, 2),
    (1, 2, 3),
    (1, 2, 4),
    (2, 1, 5),
    (2, 1, 6),
]
EXAMPLE_OUTPUT = [
    (1, 1),
]

# Each case: (actor_director rows, expected output rows).
CASES = [
    (EXAMPLE_ACTOR_DIRECTOR, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No pair cooperated three times.
    ([(1, 1, 0), (1, 1, 1), (2, 2, 2), (2, 2, 3)], []),
    # Many pairs qualify. One pair has more than three rows.
    (
        [
            (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4),
            (3, 4, 5), (3, 4, 6), (3, 4, 7),
            (5, 6, 8), (5, 6, 9),
        ],
        [(1, 1), (3, 4)],
    ),
    # Swapped ids are different pairs: (1, 2) and (2, 1) have 2 rows each.
    ([(1, 2, 0), (1, 2, 1), (2, 1, 2), (2, 1, 3)], []),
]

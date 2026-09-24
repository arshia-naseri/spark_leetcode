CINEMA_SCHEMA = "id INT, movie STRING, description STRING, rating DOUBLE"
OUTPUT_SCHEMA = "id INT, movie STRING, description STRING, rating DOUBLE"

EXAMPLE_CINEMA = [
    (1, "War", "great 3D", 8.9),
    (2, "Science", "fiction", 8.5),
    (3, "irish", "boring", 6.2),
    (4, "Ice song", "Fantacy", 8.6),
    (5, "House card", "Interesting", 9.1),
]
EXAMPLE_OUTPUT = [
    (5, "House card", "Interesting", 9.1),
    (1, "War", "great 3D", 8.9),
]

# Each case: (cinema rows, expected output rows).
CASES = [
    (EXAMPLE_CINEMA, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # Only even IDs: no match.
    (
        [(2, "A", "fun", 7.0), (4, "B", "great", 8.0)],
        [],
    ),
    # All odd IDs are boring: no match.
    (
        [(1, "A", "boring", 7.0), (3, "B", "boring", 8.0), (4, "C", "fun", 9.0)],
        [],
    ),
    # Same rating for two movies (tie).
    (
        [(1, "A", "fun", 7.5), (3, "B", "great", 7.5), (5, "C", "boring", 7.5)],
        [(1, "A", "fun", 7.5), (3, "B", "great", 7.5)],
    ),
    # Description contains "boring" but is not equal to "boring".
    (
        [(1, "A", "not boring", 6.0), (3, "B", "boring", 5.0), (7, "C", "boringly", 4.0)],
        [(1, "A", "not boring", 6.0), (7, "C", "boringly", 4.0)],
    ),
]

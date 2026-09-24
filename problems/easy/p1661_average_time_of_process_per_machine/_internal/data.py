ACTIVITY_SCHEMA = "machine_id INT, process_id INT, activity_type STRING, timestamp DOUBLE"
OUTPUT_SCHEMA = "machine_id INT, processing_time DOUBLE"

EXAMPLE_ACTIVITY = [
    (0, 0, "start", 0.712),
    (0, 0, "end", 1.520),
    (0, 1, "start", 3.140),
    (0, 1, "end", 4.120),
    (1, 0, "start", 0.550),
    (1, 0, "end", 1.550),
    (1, 1, "start", 0.430),
    (1, 1, "end", 1.420),
    (2, 0, "start", 4.100),
    (2, 0, "end", 4.512),
    (2, 1, "start", 2.500),
    (2, 1, "end", 5.000),
]
EXAMPLE_OUTPUT = [
    (0, 0.894),
    (1, 0.995),
    (2, 1.456),
]

# Each case: (activity rows, expected output rows).
CASES = [
    (EXAMPLE_ACTIVITY, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One process with start equal to end: the time is 0.
    ([(5, 0, "start", 2.0), (5, 0, "end", 2.0)], [(5, 0.0)]),
    # The "end" rows come before the "start" rows.
    # Machine 1: (1 + 1 + 2) / 3 = 1.3333... -> 1.333.
    # Machine 2: (0.5 + 0.25) / 2 = 0.375.
    (
        [
            (1, 0, "end", 1.0),
            (1, 0, "start", 0.0),
            (1, 1, "end", 2.0),
            (1, 1, "start", 1.0),
            (1, 2, "end", 4.0),
            (1, 2, "start", 2.0),
            (2, 7, "end", 3.5),
            (2, 7, "start", 3.0),
            (2, 8, "end", 1.25),
            (2, 8, "start", 1.0),
        ],
        [(1, 1.333), (2, 0.375)],
    ),
]

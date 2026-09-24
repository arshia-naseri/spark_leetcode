from datetime import datetime as dt

# DATETIME in MySQL has no time zone. TIMESTAMP_NTZ also has no time zone,
# so Spark does not move the values to UTC.
LOGINS_SCHEMA = "user_id INT, time_stamp TIMESTAMP_NTZ"
OUTPUT_SCHEMA = "user_id INT, last_stamp TIMESTAMP_NTZ"

EXAMPLE_LOGINS = [
    (6, dt(2020, 6, 30, 15, 6, 7)),
    (6, dt(2021, 4, 21, 14, 6, 6)),
    (6, dt(2019, 3, 7, 0, 18, 15)),
    (8, dt(2020, 2, 1, 5, 10, 53)),
    (8, dt(2020, 12, 30, 0, 46, 50)),
    (2, dt(2020, 1, 16, 2, 49, 50)),
    (2, dt(2019, 8, 25, 7, 59, 8)),
    (14, dt(2019, 7, 14, 9, 0, 0)),
    (14, dt(2021, 1, 6, 11, 59, 59)),
]
EXAMPLE_OUTPUT = [
    (6, dt(2020, 6, 30, 15, 6, 7)),
    (8, dt(2020, 12, 30, 0, 46, 50)),
    (2, dt(2020, 1, 16, 2, 49, 50)),
]

# Each case: (logins rows, expected output rows).
CASES = [
    (EXAMPLE_LOGINS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No login in 2020.
    (
        [(1, dt(2019, 5, 1, 10, 0, 0)), (2, dt(2021, 3, 1, 10, 0, 0))],
        [],
    ),
    # Year boundaries: first and last second of 2020 are in 2020.
    # The second before and the second after 2020 are not.
    (
        [
            (1, dt(2020, 1, 1, 0, 0, 0)),
            (1, dt(2019, 12, 31, 23, 59, 59)),
            (2, dt(2020, 12, 31, 23, 59, 59)),
            (2, dt(2021, 1, 1, 0, 0, 0)),
            (3, dt(2019, 12, 31, 23, 59, 59)),
            (3, dt(2021, 1, 1, 0, 0, 0)),
        ],
        [
            (1, dt(2020, 1, 1, 0, 0, 0)),
            (2, dt(2020, 12, 31, 23, 59, 59)),
        ],
    ),
    # Many logins in 2020 on the same day: keep the latest time.
    (
        [
            (5, dt(2020, 7, 4, 8, 0, 0)),
            (5, dt(2020, 7, 4, 23, 0, 1)),
            (5, dt(2020, 7, 4, 12, 30, 0)),
        ],
        [(5, dt(2020, 7, 4, 23, 0, 1))],
    ),
]

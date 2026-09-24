from datetime import date

ACTIVITY_SCHEMA = "player_id INT, device_id INT, event_date DATE, games_played INT"
OUTPUT_SCHEMA = "player_id INT, first_login DATE"

EXAMPLE_ACTIVITY = [
    (1, 2, date(2016, 3, 1), 5),
    (1, 2, date(2016, 5, 2), 6),
    (2, 3, date(2017, 6, 25), 1),
    (3, 1, date(2016, 3, 2), 0),
    (3, 4, date(2018, 7, 3), 5),
]
EXAMPLE_OUTPUT = [
    (1, date(2016, 3, 1)),
    (2, date(2017, 6, 25)),
    (3, date(2016, 3, 2)),
]

# Each case: (activity rows, expected output rows).
CASES = [
    (EXAMPLE_ACTIVITY, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One player. The rows are not in date order. The earliest date is not the first row.
    (
        [
            (7, 1, date(2020, 5, 10), 3),
            (7, 2, date(2019, 12, 31), 0),
            (7, 1, date(2020, 1, 1), 8),
        ],
        [(7, date(2019, 12, 31))],
    ),
    # Different players log in on the same date. Each player gets one row.
    (
        [
            (1, 1, date(2021, 1, 1), 2),
            (2, 1, date(2021, 1, 1), 4),
            (2, 2, date(2021, 1, 2), 1),
        ],
        [(1, date(2021, 1, 1)), (2, date(2021, 1, 1))],
    ),
]

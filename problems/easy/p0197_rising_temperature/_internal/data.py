from datetime import date

WEATHER_SCHEMA = "id INT, recordDate DATE, temperature INT"
OUTPUT_SCHEMA = "id INT"

EXAMPLE_WEATHER = [
    (1, date(2015, 1, 1), 10),
    (2, date(2015, 1, 2), 25),
    (3, date(2015, 1, 3), 20),
    (4, date(2015, 1, 4), 30),
]
EXAMPLE_OUTPUT = [(2,), (4,)]

# Each case: (weather rows, expected output rows).
CASES = [
    (EXAMPLE_WEATHER, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One row: no previous day.
    ([(1, date(2015, 1, 1), 10)], []),
    # A gap of two days is not "yesterday".
    ([(1, date(2015, 1, 1), 10), (2, date(2015, 1, 3), 20)], []),
    # Equal temperature is not higher.
    ([(1, date(2015, 1, 1), 10), (2, date(2015, 1, 2), 10)], []),
    # The id order is not the date order. Leap day and month boundary.
    (
        [
            (5, date(2020, 2, 29), 5),
            (1, date(2020, 3, 1), 7),
            (3, date(2020, 2, 28), 9),
        ],
        [(1,)],
    ),
    # Year boundary and negative temperatures.
    ([(10, date(2019, 12, 31), -5), (11, date(2020, 1, 1), 0)], [(11,)]),
]

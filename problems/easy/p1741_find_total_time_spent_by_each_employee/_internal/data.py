from datetime import date

EMPLOYEES_SCHEMA = "emp_id INT, event_day DATE, in_time INT, out_time INT"
OUTPUT_SCHEMA = "day DATE, emp_id INT, total_time BIGINT"

EXAMPLE_EMPLOYEES = [
    (1, date(2020, 11, 28), 4, 32),
    (1, date(2020, 11, 28), 55, 200),
    (1, date(2020, 12, 3), 1, 42),
    (2, date(2020, 11, 28), 3, 33),
    (2, date(2020, 12, 9), 47, 74),
]
EXAMPLE_OUTPUT = [
    (date(2020, 11, 28), 1, 173),
    (date(2020, 11, 28), 2, 30),
    (date(2020, 12, 3), 1, 41),
    (date(2020, 12, 9), 2, 27),
]

# Each case: (employees rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEES, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One event only.
    ([(7, date(2021, 1, 1), 1, 1440)], [(date(2021, 1, 1), 7, 1439)]),
    # Three events on the same day for one employee.
    (
        [
            (3, date(2021, 5, 5), 10, 20),
            (3, date(2021, 5, 5), 30, 45),
            (3, date(2021, 5, 5), 100, 101),
        ],
        [(date(2021, 5, 5), 3, 26)],
    ),
    # Same in_time on different days: do not merge the days.
    (
        [
            (4, date(2021, 6, 1), 5, 10),
            (4, date(2021, 6, 2), 5, 10),
        ],
        [(date(2021, 6, 1), 4, 5), (date(2021, 6, 2), 4, 5)],
    ),
]

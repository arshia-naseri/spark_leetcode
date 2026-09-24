from datetime import date

ACTIVITY_SCHEMA = "user_id INT, session_id INT, activity_date DATE, activity_type STRING"
OUTPUT_SCHEMA = "day DATE, active_users BIGINT"

EXAMPLE_ACTIVITY = [
    (1, 1, date(2019, 7, 20), "open_session"),
    (1, 1, date(2019, 7, 20), "scroll_down"),
    (1, 1, date(2019, 7, 20), "end_session"),
    (2, 4, date(2019, 7, 20), "open_session"),
    (2, 4, date(2019, 7, 21), "send_message"),
    (2, 4, date(2019, 7, 21), "end_session"),
    (3, 2, date(2019, 7, 21), "open_session"),
    (3, 2, date(2019, 7, 21), "send_message"),
    (3, 2, date(2019, 7, 21), "end_session"),
    (4, 3, date(2019, 6, 25), "open_session"),
    (4, 3, date(2019, 6, 25), "end_session"),
]
EXAMPLE_OUTPUT = [
    (date(2019, 7, 20), 2),
    (date(2019, 7, 21), 2),
]

# Each case: (activity rows, expected output rows).
CASES = [
    (EXAMPLE_ACTIVITY, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No activity in the period.
    (
        [
            (1, 1, date(2019, 6, 1), "open_session"),
            (2, 2, date(2019, 8, 1), "open_session"),
        ],
        [],
    ),
    # Period limits: 2019-06-28 and 2019-07-27 are in the period.
    # 2019-06-27 and 2019-07-28 are not in the period.
    (
        [
            (1, 1, date(2019, 6, 27), "open_session"),
            (2, 2, date(2019, 6, 28), "open_session"),
            (3, 3, date(2019, 7, 27), "scroll_down"),
            (4, 4, date(2019, 7, 28), "end_session"),
        ],
        [(date(2019, 6, 28), 1), (date(2019, 7, 27), 1)],
    ),
    # Duplicate rows and one user with two sessions on the same day count as one user.
    (
        [
            (1, 1, date(2019, 7, 1), "open_session"),
            (1, 1, date(2019, 7, 1), "open_session"),
            (1, 2, date(2019, 7, 1), "send_message"),
            (2, 3, date(2019, 7, 1), "end_session"),
        ],
        [(date(2019, 7, 1), 2)],
    ),
]

from datetime import date

VIEWS_SCHEMA = "article_id INT, author_id INT, viewer_id INT, view_date DATE"
OUTPUT_SCHEMA = "id INT"

EXAMPLE_VIEWS = [
    (1, 3, 5, date(2019, 8, 1)),
    (1, 3, 6, date(2019, 8, 2)),
    (2, 7, 7, date(2019, 8, 1)),
    (2, 7, 6, date(2019, 8, 2)),
    (4, 7, 1, date(2019, 7, 22)),
    (3, 4, 4, date(2019, 7, 21)),
    (3, 4, 4, date(2019, 7, 21)),
]
EXAMPLE_OUTPUT = [(4,), (7,)]

# Each case: (views rows, expected output rows).
CASES = [
    (EXAMPLE_VIEWS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No author views an own article.
    (
        [(1, 3, 5, date(2019, 8, 1)), (2, 5, 3, date(2019, 8, 2))],
        [],
    ),
    # One author views two own articles on different dates: show the id one time.
    (
        [
            (1, 2, 2, date(2019, 8, 1)),
            (5, 2, 2, date(2019, 8, 3)),
            (6, 9, 1, date(2019, 8, 3)),
        ],
        [(2,)],
    ),
    # Null viewer_id is not equal to author_id.
    (
        [(1, 3, None, date(2019, 8, 1)), (2, 8, 8, date(2019, 8, 2))],
        [(8,)],
    ),
]

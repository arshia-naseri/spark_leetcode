from datetime import date

DAILY_SALES_SCHEMA = "date_id DATE, make_name STRING, lead_id INT, partner_id INT"
OUTPUT_SCHEMA = "date_id DATE, make_name STRING, unique_leads BIGINT, unique_partners BIGINT"

D7 = date(2020, 12, 7)
D8 = date(2020, 12, 8)

EXAMPLE_DAILY_SALES = [
    (D8, "toyota", 0, 1),
    (D8, "toyota", 1, 0),
    (D8, "toyota", 1, 2),
    (D7, "toyota", 0, 2),
    (D7, "toyota", 0, 1),
    (D8, "honda", 1, 2),
    (D8, "honda", 2, 1),
    (D7, "honda", 0, 1),
    (D7, "honda", 1, 2),
    (D7, "honda", 2, 1),
]
EXAMPLE_OUTPUT = [
    (D8, "toyota", 2, 3),
    (D7, "toyota", 1, 2),
    (D8, "honda", 2, 2),
    (D7, "honda", 3, 2),
]

# Each case: (daily_sales rows, expected output rows).
CASES = [
    (EXAMPLE_DAILY_SALES, EXAMPLE_OUTPUT),
    # Empty table: no groups.
    ([], []),
    # Full duplicate rows: each value counts one time.
    (
        [(D7, "bmw", 5, 6), (D7, "bmw", 5, 6), (D7, "bmw", 5, 6)],
        [(D7, "bmw", 1, 1)],
    ),
    # Same make on different dates and different makes on the same date are separate groups.
    (
        [(D7, "audi", 1, 1), (D8, "audi", 2, 2), (D8, "audi", 3, 2), (D7, "kia", 1, 1)],
        [(D7, "audi", 1, 1), (D8, "audi", 2, 1), (D7, "kia", 1, 1)],
    ),
    # Same ID value used as lead and partner: the two counts are independent.
    (
        [(D8, "ford", 1, 1), (D8, "ford", 1, 2), (D8, "ford", 2, 1)],
        [(D8, "ford", 2, 2)],
    ),
    # Null IDs: COUNT(DISTINCT) does not count nulls.
    (
        [(D7, "fiat", None, 1), (D7, "fiat", 1, None), (D7, "fiat", 1, 1)],
        [(D7, "fiat", 1, 1)],
    ),
]

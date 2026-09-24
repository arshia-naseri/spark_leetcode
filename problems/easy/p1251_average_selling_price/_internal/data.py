from datetime import date

PRICES_SCHEMA = "product_id INT, start_date DATE, end_date DATE, price INT"
UNITS_SOLD_SCHEMA = "product_id INT, purchase_date DATE, units INT"
OUTPUT_SCHEMA = "product_id INT, average_price DOUBLE"

EXAMPLE_PRICES = [
    (1, date(2019, 2, 17), date(2019, 2, 28), 5),
    (1, date(2019, 3, 1), date(2019, 3, 22), 20),
    (2, date(2019, 2, 1), date(2019, 2, 20), 15),
    (2, date(2019, 2, 21), date(2019, 3, 31), 30),
]
EXAMPLE_UNITS_SOLD = [
    (1, date(2019, 2, 25), 100),
    (1, date(2019, 3, 1), 15),
    (2, date(2019, 2, 10), 200),
    (2, date(2019, 3, 22), 30),
]
EXAMPLE_OUTPUT = [
    (1, 6.96),
    (2, 16.96),
]

# Each case: (prices rows, units_sold rows, expected output rows).
CASES = [
    (EXAMPLE_PRICES, EXAMPLE_UNITS_SOLD, EXAMPLE_OUTPUT),
    # No sales at all: each product gets 0.
    (EXAMPLE_PRICES, [], [(1, 0.0), (2, 0.0)]),
    # No prices: empty result.
    ([], EXAMPLE_UNITS_SOLD, []),
    # One product has sales, one product has no sales.
    (
        [
            (1, date(2019, 1, 1), date(2019, 1, 31), 10),
            (3, date(2019, 1, 1), date(2019, 1, 31), 7),
        ],
        [(1, date(2019, 1, 15), 4)],
        [(1, 10.0), (3, 0.0)],
    ),
    # Sales on the start date and on the end date of a period count.
    # (1 * 10 + 2 * 40) / 3 = 30.00
    (
        [
            (1, date(2019, 1, 1), date(2019, 1, 10), 10),
            (1, date(2019, 1, 11), date(2019, 1, 20), 40),
        ],
        [(1, date(2019, 1, 10), 1), (1, date(2019, 1, 11), 2)],
        [(1, 30.0)],
    ),
    # Duplicate sale rows count two times. (1 + 2 + 2) / 3 = 1.67
    (
        [
            (1, date(2019, 1, 1), date(2019, 1, 31), 1),
            (1, date(2019, 2, 1), date(2019, 2, 28), 2),
        ],
        [
            (1, date(2019, 1, 5), 1),
            (1, date(2019, 2, 5), 1),
            (1, date(2019, 2, 5), 1),
        ],
        [(1, 1.67)],
    ),
    # A sale out of all price periods and a sale of an unknown product
    # do not count.
    (
        [
            (1, date(2019, 1, 1), date(2019, 1, 31), 10),
            (2, date(2019, 1, 1), date(2019, 1, 31), 20),
        ],
        [
            (1, date(2019, 3, 1), 5),
            (2, date(2019, 1, 10), 3),
            (9, date(2019, 1, 5), 3),
        ],
        [(1, 0.0), (2, 20.0)],
    ),
]

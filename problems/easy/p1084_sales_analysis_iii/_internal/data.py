from datetime import date

PRODUCT_SCHEMA = "product_id INT, product_name STRING, unit_price INT"
SALES_SCHEMA = (
    "seller_id INT, product_id INT, buyer_id INT, sale_date DATE, quantity INT, price INT"
)
OUTPUT_SCHEMA = "product_id INT, product_name STRING"

EXAMPLE_PRODUCT = [
    (1, "S8", 1000),
    (2, "G4", 800),
    (3, "iPhone", 1400),
]
EXAMPLE_SALES = [
    (1, 1, 1, date(2019, 1, 21), 2, 2000),
    (1, 2, 2, date(2019, 2, 17), 1, 800),
    (2, 2, 3, date(2019, 6, 2), 1, 800),
    (3, 3, 4, date(2019, 5, 13), 2, 2800),
]
EXAMPLE_OUTPUT = [
    (1, "S8"),
]

# Each case: (product rows, sales rows, expected output rows).
CASES = [
    (EXAMPLE_PRODUCT, EXAMPLE_SALES, EXAMPLE_OUTPUT),
    # No sales: no product was sold, so no product is in the result.
    (EXAMPLE_PRODUCT, [], []),
    # Boundary dates: 2019-01-01 and 2019-03-31 are in the range.
    # 2018-12-31 and 2019-04-01 are not in the range.
    (
        [(1, "A", 10), (2, "B", 20), (3, "C", 30), (4, "D", 40)],
        [
            (1, 1, 1, date(2019, 1, 1), 1, 10),
            (1, 2, 1, date(2019, 3, 31), 1, 20),
            (1, 3, 1, date(2018, 12, 31), 1, 30),
            (1, 4, 1, date(2019, 4, 1), 1, 40),
        ],
        [(1, "A"), (2, "B")],
    ),
    # Duplicate sale rows give one result row. A product with no sales is not
    # in the result. A sale in the first quarter of a different year removes
    # the product.
    (
        [(1, "A", 10), (2, "B", 20), (3, "C", 30)],
        [
            (1, 1, 1, date(2019, 2, 1), 1, 10),
            (1, 1, 1, date(2019, 2, 1), 1, 10),
            (2, 3, 2, date(2019, 2, 1), 1, 30),
            (2, 3, 2, date(2020, 2, 1), 1, 30),
        ],
        [(1, "A")],
    ),
]

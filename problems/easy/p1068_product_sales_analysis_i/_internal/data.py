SALES_SCHEMA = "sale_id INT, product_id INT, year INT, quantity INT, price INT"
PRODUCT_SCHEMA = "product_id INT, product_name STRING"
OUTPUT_SCHEMA = "product_name STRING, year INT, price INT"

EXAMPLE_SALES = [
    (1, 100, 2008, 10, 5000),
    (2, 100, 2009, 12, 5000),
    (7, 200, 2011, 15, 9000),
]
EXAMPLE_PRODUCT = [
    (100, "Nokia"),
    (200, "Apple"),
    (300, "Samsung"),
]
EXAMPLE_OUTPUT = [
    ("Nokia", 2008, 5000),
    ("Nokia", 2009, 5000),
    ("Apple", 2011, 9000),
]

# Each case: (sales rows, product rows, expected output rows).
CASES = [
    (EXAMPLE_SALES, EXAMPLE_PRODUCT, EXAMPLE_OUTPUT),
    # No sales: the output is empty.
    ([], EXAMPLE_PRODUCT, []),
    # Products with no sales do not show in the output.
    (
        [(5, 300, 2020, 1, 800)],
        EXAMPLE_PRODUCT,
        [("Samsung", 2020, 800)],
    ),
    # Same sale_id in two years, and two sales with equal output rows.
    # Each sale gives one row, so duplicate rows stay.
    (
        [
            (1, 100, 2008, 10, 5000),
            (1, 100, 2009, 3, 4500),
            (2, 100, 2008, 7, 5000),
        ],
        [(100, "Nokia")],
        [
            ("Nokia", 2008, 5000),
            ("Nokia", 2009, 4500),
            ("Nokia", 2008, 5000),
        ],
    ),
]

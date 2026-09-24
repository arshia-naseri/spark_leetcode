import datetime

PRODUCTS_SCHEMA = "product_id INT, product_name STRING, product_category STRING"
ORDERS_SCHEMA = "product_id INT, order_date DATE, unit INT"
OUTPUT_SCHEMA = "product_name STRING, unit BIGINT"

D = datetime.date

EXAMPLE_PRODUCTS = [
    (1, "Leetcode Solutions", "Book"),
    (2, "Jewels of Stringology", "Book"),
    (3, "HP", "Laptop"),
    (4, "Lenovo", "Laptop"),
    (5, "Leetcode Kit", "T-shirt"),
]
EXAMPLE_ORDERS = [
    (1, D(2020, 2, 5), 60),
    (1, D(2020, 2, 10), 70),
    (2, D(2020, 1, 18), 30),
    (2, D(2020, 2, 11), 80),
    (3, D(2020, 2, 17), 2),
    (3, D(2020, 2, 24), 3),
    (4, D(2020, 3, 1), 20),
    (4, D(2020, 3, 4), 30),
    (4, D(2020, 3, 4), 60),
    (5, D(2020, 2, 25), 50),
    (5, D(2020, 2, 27), 50),
    (5, D(2020, 3, 1), 50),
]
EXAMPLE_OUTPUT = [
    ("Leetcode Solutions", 130),
    ("Leetcode Kit", 100),
]

# Each case: (products rows, orders rows, expected output rows).
CASES = [
    (EXAMPLE_PRODUCTS, EXAMPLE_ORDERS, EXAMPLE_OUTPUT),
    # No orders.
    (EXAMPLE_PRODUCTS, [], []),
    # No products and no orders.
    ([], [], []),
    # Date limits: Feb 1 and Feb 29 count. Jan 31 and Mar 1 do not count.
    (
        [(1, "A", "X"), (2, "B", "X"), (3, "C", "X")],
        [
            (1, D(2020, 2, 1), 50),
            (1, D(2020, 2, 29), 50),
            (2, D(2020, 1, 31), 100),
            (2, D(2020, 2, 15), 99),
            (3, D(2020, 3, 1), 200),
        ],
        [("A", 100)],
    ),
    # February of other years does not count.
    (
        [(1, "A", "X"), (2, "B", "X")],
        [
            (1, D(2019, 2, 10), 500),
            (1, D(2021, 2, 10), 500),
            (2, D(2020, 2, 10), 100),
        ],
        [("B", 100)],
    ),
    # Duplicate order rows all count.
    (
        [(1, "A", "X")],
        [(1, D(2020, 2, 3), 50), (1, D(2020, 2, 3), 50)],
        [("A", 100)],
    ),
    # Total is 99: under the limit, so no result.
    (
        [(1, "A", "X")],
        [(1, D(2020, 2, 3), 49), (1, D(2020, 2, 4), 50)],
        [],
    ),
]

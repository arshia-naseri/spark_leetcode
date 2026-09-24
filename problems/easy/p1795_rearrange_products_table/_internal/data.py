PRODUCTS_SCHEMA = "product_id INT, store1 INT, store2 INT, store3 INT"
OUTPUT_SCHEMA = "product_id INT, store STRING, price INT"

EXAMPLE_PRODUCTS = [
    (0, 95, 100, 105),
    (1, 70, None, 80),
]
EXAMPLE_OUTPUT = [
    (0, "store1", 95),
    (0, "store2", 100),
    (0, "store3", 105),
    (1, "store1", 70),
    (1, "store3", 80),
]

# Each case: (products rows, expected output rows).
CASES = [
    (EXAMPLE_PRODUCTS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # Product with no store: no rows for it.
    ([(1, None, None, None), (2, None, 5, None)], [(2, "store2", 5)]),
    # Same price in all stores, and price 0 is not null.
    (
        [(3, 10, 10, 10), (4, 0, None, None)],
        [(3, "store1", 10), (3, "store2", 10), (3, "store3", 10), (4, "store1", 0)],
    ),
]

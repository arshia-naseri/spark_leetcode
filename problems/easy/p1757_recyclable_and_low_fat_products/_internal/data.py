PRODUCTS_SCHEMA = "product_id INT, low_fats STRING, recyclable STRING"
OUTPUT_SCHEMA = "product_id INT"

EXAMPLE_PRODUCTS = [
    (0, "Y", "N"),
    (1, "Y", "Y"),
    (2, "N", "Y"),
    (3, "Y", "Y"),
    (4, "N", "N"),
]
EXAMPLE_OUTPUT = [(1,), (3,)]

# Each case: (products rows, expected output rows).
CASES = [
    (EXAMPLE_PRODUCTS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No product is both low fat and recyclable.
    ([(1, "Y", "N"), (2, "N", "Y"), (3, "N", "N")], []),
    # All products are both low fat and recyclable.
    ([(5, "Y", "Y"), (6, "Y", "Y")], [(5,), (6,)]),
]

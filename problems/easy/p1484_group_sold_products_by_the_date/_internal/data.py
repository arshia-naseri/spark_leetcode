from datetime import date

ACTIVITIES_SCHEMA = "sell_date DATE, product STRING"
OUTPUT_SCHEMA = "sell_date DATE, num_sold BIGINT, products STRING"

EXAMPLE_ACTIVITIES = [
    (date(2020, 5, 30), "Headphone"),
    (date(2020, 6, 1), "Pencil"),
    (date(2020, 6, 2), "Mask"),
    (date(2020, 5, 30), "Basketball"),
    (date(2020, 6, 1), "Bible"),
    (date(2020, 6, 2), "Mask"),
    (date(2020, 5, 30), "T-Shirt"),
]
EXAMPLE_OUTPUT = [
    (date(2020, 5, 30), 3, "Basketball,Headphone,T-Shirt"),
    (date(2020, 6, 1), 2, "Bible,Pencil"),
    (date(2020, 6, 2), 1, "Mask"),
]

# Each case: (activities rows, expected output rows).
CASES = [
    (EXAMPLE_ACTIVITIES, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One row.
    ([(date(2021, 1, 1), "Pen")], [(date(2021, 1, 1), 1, "Pen")]),
    # Many duplicates on one date. Count and list each product one time.
    (
        [
            (date(2021, 1, 1), "Pen"),
            (date(2021, 1, 1), "Pen"),
            (date(2021, 1, 1), "Pen"),
            (date(2021, 1, 1), "Apple"),
            (date(2021, 1, 1), "Apple"),
        ],
        [(date(2021, 1, 1), 2, "Apple,Pen")],
    ),
    # Same product on different dates. Each date has its own row.
    (
        [
            (date(2021, 1, 3), "Pen"),
            (date(2021, 1, 1), "Pen"),
            (date(2021, 1, 2), "Pen"),
            (date(2021, 1, 2), "Cup"),
        ],
        [
            (date(2021, 1, 1), 1, "Pen"),
            (date(2021, 1, 2), 2, "Cup,Pen"),
            (date(2021, 1, 3), 1, "Pen"),
        ],
    ),
    # Rows in reverse order. The names must be sorted.
    (
        [
            (date(2021, 2, 1), "Zebra"),
            (date(2021, 2, 1), "Mango"),
            (date(2021, 2, 1), "Banana"),
            (date(2021, 2, 1), "Apple"),
        ],
        [(date(2021, 2, 1), 4, "Apple,Banana,Mango,Zebra")],
    ),
]

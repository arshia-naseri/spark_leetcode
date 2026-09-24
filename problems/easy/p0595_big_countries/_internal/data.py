WORLD_SCHEMA = "name STRING, continent STRING, area INT, population INT, gdp BIGINT"
OUTPUT_SCHEMA = "name STRING, population INT, area INT"

EXAMPLE_WORLD = [
    ("Afghanistan", "Asia", 652230, 25500100, 20343000000),
    ("Albania", "Europe", 28748, 2831741, 12960000000),
    ("Algeria", "Africa", 2381741, 37100000, 188681000000),
    ("Andorra", "Europe", 468, 78115, 3712000000),
    ("Angola", "Africa", 1246700, 20609294, 100990000000),
]
EXAMPLE_OUTPUT = [
    ("Afghanistan", 25500100, 652230),
    ("Algeria", 37100000, 2381741),
]

# Each case: (world rows, expected output rows).
CASES = [
    (EXAMPLE_WORLD, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No big countries.
    (
        [
            ("Albania", "Europe", 28748, 2831741, 12960000000),
            ("Andorra", "Europe", 468, 78115, 3712000000),
        ],
        [],
    ),
    # Values at the limits are big. Values one below the limits are not big.
    (
        [
            ("A", "Asia", 3000000, 1, 1),
            ("B", "Asia", 1, 25000000, 1),
            ("C", "Asia", 2999999, 24999999, 1),
            ("D", "Asia", 3000000, 25000000, 1),
        ],
        [("A", 1, 3000000), ("B", 25000000, 1), ("D", 25000000, 3000000)],
    ),
    # Null values: one condition is true, so the country is big.
    # No condition is true, so the country is not big.
    (
        [
            ("E", "Asia", None, 30000000, 1),
            ("F", "Asia", 4000000, None, 1),
            ("G", "Asia", None, None, 1),
            ("H", "Asia", None, 100, 1),
        ],
        [("E", 30000000, None), ("F", None, 4000000)],
    ),
]

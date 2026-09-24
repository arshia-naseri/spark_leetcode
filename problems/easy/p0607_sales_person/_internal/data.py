from datetime import date

SALES_PERSON_SCHEMA = "sales_id INT, name STRING, salary INT, commission_rate INT, hire_date DATE"
COMPANY_SCHEMA = "com_id INT, name STRING, city STRING"
ORDERS_SCHEMA = "order_id INT, order_date DATE, com_id INT, sales_id INT, amount INT"
OUTPUT_SCHEMA = "name STRING"

EXAMPLE_SALES_PERSON = [
    (1, "John", 100000, 6, date(2006, 4, 1)),
    (2, "Amy", 12000, 5, date(2010, 5, 1)),
    (3, "Mark", 65000, 12, date(2008, 12, 25)),
    (4, "Pam", 25000, 25, date(2005, 1, 1)),
    (5, "Alex", 5000, 10, date(2007, 2, 3)),
]
EXAMPLE_COMPANY = [
    (1, "RED", "Boston"),
    (2, "ORANGE", "New York"),
    (3, "YELLOW", "Boston"),
    (4, "GREEN", "Austin"),
]
EXAMPLE_ORDERS = [
    (1, date(2014, 1, 1), 3, 4, 10000),
    (2, date(2014, 2, 1), 4, 5, 5000),
    (3, date(2014, 3, 1), 1, 1, 50000),
    (4, date(2014, 4, 1), 1, 4, 25000),
]
EXAMPLE_OUTPUT = [("Amy",), ("Mark",), ("Alex",)]

ALL_NAMES = [("John",), ("Amy",), ("Mark",), ("Pam",), ("Alex",)]

# Each case: (sales person rows, company rows, orders rows, expected output rows).
CASES = [
    (EXAMPLE_SALES_PERSON, EXAMPLE_COMPANY, EXAMPLE_ORDERS, EXAMPLE_OUTPUT),
    # No orders: all sales persons are in the output.
    (EXAMPLE_SALES_PERSON, EXAMPLE_COMPANY, [], ALL_NAMES),
    # No sales persons: empty output.
    ([], EXAMPLE_COMPANY, EXAMPLE_ORDERS, []),
    # No company with the name "RED": all sales persons are in the output.
    (
        EXAMPLE_SALES_PERSON,
        [(2, "ORANGE", "New York"), (3, "YELLOW", "Boston"), (4, "GREEN", "Austin")],
        EXAMPLE_ORDERS,
        ALL_NAMES,
    ),
    # An order to "RED" with a null sales_id. It does not remove any sales
    # person (a NOT IN subquery gives no rows here).
    (
        EXAMPLE_SALES_PERSON,
        EXAMPLE_COMPANY,
        EXAMPLE_ORDERS + [(5, date(2014, 5, 1), 1, None, 100)],
        EXAMPLE_OUTPUT,
    ),
    # Two sales persons with the same name, no "RED" orders: both rows stay.
    # One sales person with many other orders: only one row.
    # Two companies with the name "RED": orders to both count.
    (
        [
            (1, "Amy", 1000, 1, date(2010, 1, 1)),
            (2, "Amy", 2000, 2, date(2011, 1, 1)),
            (3, "Bob", 3000, 3, date(2012, 1, 1)),
            (4, "Cat", 4000, 4, date(2013, 1, 1)),
        ],
        [(1, "RED", "Boston"), (2, "BLUE", "Austin"), (3, "RED", "Dallas")],
        [
            (1, date(2014, 1, 1), 2, 1, 10),
            (2, date(2014, 1, 2), 2, 1, 20),
            (3, date(2014, 1, 3), 1, 3, 30),
            (4, date(2014, 1, 4), 3, 4, 40),
            (5, date(2014, 1, 5), 3, 4, 50),
        ],
        [("Amy",), ("Amy",)],
    ),
]

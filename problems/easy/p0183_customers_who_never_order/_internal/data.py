CUSTOMERS_SCHEMA = "id INT, name STRING"
ORDERS_SCHEMA = "id INT, customerId INT"
OUTPUT_SCHEMA = "Customers STRING"

EXAMPLE_CUSTOMERS = [
    (1, "Joe"),
    (2, "Henry"),
    (3, "Sam"),
    (4, "Max"),
]
EXAMPLE_ORDERS = [
    (1, 3),
    (2, 1),
]
EXAMPLE_OUTPUT = [
    ("Henry",),
    ("Max",),
]

# Each case: (customers rows, orders rows, expected output rows).
CASES = [
    (EXAMPLE_CUSTOMERS, EXAMPLE_ORDERS, EXAMPLE_OUTPUT),
    # No orders: all customers are in the output.
    (
        EXAMPLE_CUSTOMERS,
        [],
        [("Joe",), ("Henry",), ("Sam",), ("Max",)],
    ),
    # No customers: the output is empty.
    ([], EXAMPLE_ORDERS, []),
    # All customers have orders: the output is empty.
    (
        [(1, "Joe"), (2, "Henry")],
        [(1, 1), (2, 2), (3, 1)],
        [],
    ),
    # Order with a null customerId: NOT IN on a null gives no rows, but
    # the correct output keeps the customers without orders.
    (
        EXAMPLE_CUSTOMERS,
        [(1, 3), (2, None)],
        [("Joe",), ("Henry",), ("Max",)],
    ),
    # Two customers with the same name: each one is in the output alone.
    (
        [(1, "Joe"), (2, "Joe"), (3, "Joe")],
        [(1, 2)],
        [("Joe",), ("Joe",)],
    ),
    # Order for a customerId that is not in Customers.
    (
        [(1, "Joe"), (2, "Henry")],
        [(1, 99)],
        [("Joe",), ("Henry",)],
    ),
]

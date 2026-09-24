ORDERS_SCHEMA = "order_number INT, customer_number INT"
OUTPUT_SCHEMA = "customer_number INT"

EXAMPLE_ORDERS = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 3),
]
EXAMPLE_OUTPUT = [
    (3,),
]

# Each case: (orders rows, expected output rows).
CASES = [
    (EXAMPLE_ORDERS, EXAMPLE_OUTPUT),
    # Empty table: no customers.
    ([], []),
    # One order only.
    ([(1, 7)], [(7,)]),
    # One customer has all orders.
    ([(1, 5), (2, 5), (3, 5)], [(5,)]),
    # The top customer is not the first or the last customer number.
    (
        [(1, 1), (2, 2), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4)],
        [(2,)],
    ),
    # Follow-up: a tie for the largest number of orders. Return all tied customers.
    (
        [(1, 1), (2, 1), (3, 2), (4, 2), (5, 3)],
        [(1,), (2,)],
    ),
]

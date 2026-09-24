PATIENTS_SCHEMA = "patient_id INT, patient_name STRING, conditions STRING"
OUTPUT_SCHEMA = "patient_id INT, patient_name STRING, conditions STRING"

EXAMPLE_PATIENTS = [
    (1, "Daniel", "YFEV COUGH"),
    (2, "Alice", ""),
    (3, "Bob", "DIAB100 MYOP"),
    (4, "George", "ACNE DIAB100"),
    (5, "Alain", "DIAB201"),
]
EXAMPLE_OUTPUT = [
    (3, "Bob", "DIAB100 MYOP"),
    (4, "George", "ACNE DIAB100"),
]

# Each case: (patients rows, expected output rows).
CASES = [
    (EXAMPLE_PATIENTS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No matches.
    ([(1, "Ann", "COUGH"), (2, "Ben", "DIAB201 FLU")], []),
    # "DIAB1" is inside a code but not at its start: no match.
    ([(1, "Ann", "SADIAB100"), (2, "Ben", "ACNE XDIAB1")], []),
    # Null conditions: no match.
    ([(1, "Ann", None), (2, "Ben", "DIAB1")], [(2, "Ben", "DIAB1")]),
    # Code in the middle of the list, and two DIAB1 codes in one row.
    (
        [(1, "Ann", "ACNE DIAB105 FLU"), (2, "Ben", "DIAB100 DIAB101")],
        [(1, "Ann", "ACNE DIAB105 FLU"), (2, "Ben", "DIAB100 DIAB101")],
    ),
]

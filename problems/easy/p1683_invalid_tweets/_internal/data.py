TWEETS_SCHEMA = "tweet_id INT, content STRING"
OUTPUT_SCHEMA = "tweet_id INT"

EXAMPLE_TWEETS = [
    (1, "Let us Code"),
    (2, "More than fifteen chars are here!"),
]
EXAMPLE_OUTPUT = [
    (2,),
]

# Each case: (tweets rows, expected output rows).
CASES = [
    (EXAMPLE_TWEETS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No invalid tweets.
    ([(1, "Hi"), (2, "Hello world")], []),
    # Boundary: 15 characters is valid, 16 characters is invalid.
    ([(1, "abcdefghijklmno"), (2, "abcdefghijklmnop")], [(2,)]),
    # Spaces and "!" count as characters.
    ([(1, "a b c d e f g h!"), (2, "!!!!!!!!!!!!!!!")], [(1,)]),
    # All tweets are invalid.
    (
        [(1, "This tweet is too long"), (2, "This one is long too!")],
        [(1,), (2,)],
    ),
    # Empty content and null content are not invalid.
    ([(1, ""), (2, None), (3, "Sixteen chars!!!")], [(3,)]),
]

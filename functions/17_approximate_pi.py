# Assignment
# Write a function that approximates π with the alternating series `4 * (1 - 1/3
# + 1/5 - 1/7 + ...)`. Its argument is the number of terms, including the first
# `1/1` term. Reject non-positive term counts and display an approximation for a
# reasonably large count.
#
# Solution

# Let the caller choose how many terms to include. Each call builds its own sum
# from the start, then returns the approximation for that term count.
def approximate_pi(term_count: int) -> float:
    """Approximate pi using term_count terms of the Gregory–Leibniz series."""
    # Check the type explicitly: the int hint documents the expected input but
    # does not enforce it. The loop's range needs an integer count.
    if type(term_count) is not int:
        raise TypeError("term_count must be an integer")
    # Require at least the first term. Stop with an error if the count is zero
    # or negative, since those values are outside this function's contract.
    if term_count <= 0:
        raise ValueError("term_count must be positive")

    # Begin with an empty sum and a positive sign for the first term, 1/1.
    # total stores the accumulated terms; sign controls whether to add or subtract.
    total = 0.0
    sign = 1

    # range supplies indices 0 through term_count - 1, giving exactly the
    # requested number of terms, including the initial 1/1 term.
    for index in range(term_count):
        # 2 * index + 1 generates 1, 3, 5, ... . With the current sign, the
        # first passes add 1/1, then -1/3, then 1/5 to the running total.
        total += sign / (2 * index + 1)
        # Negating sign changes 1 to -1 or -1 to 1 for the next iteration.
        # The for loop advances the index automatically and ends after all terms.
        sign = -sign

    # The series sums to pi/4, so multiply the completed partial sum by 4.
    # Using finitely many terms gives an approximation; the series converges
    # slowly, which is why the example below uses many terms.
    return 4 * total


# The underscore in 10_000 only makes the integer easier to read: it is 10000.
# Call the function first, then format its result to five decimal places.
# Formatting changes the displayed text; accuracy depends on the calculated sum.
print(f"Approximation of pi (10,000 terms): {approximate_pi(10_000):.5f}")

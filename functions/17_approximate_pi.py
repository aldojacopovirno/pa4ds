# Assignment
# Write a function that approximates π with the alternating series `4 * (1 - 1/3
# + 1/5 - 1/7 + ...)`. Its argument is the number of terms, including the first
# `1/1` term. Reject non-positive term counts and display an approximation for a
# reasonably large count.
#
# Solution

# Odd denominators and alternating signs create the series terms.
def approximate_pi(term_count: int) -> float:
    """Approximate pi using term_count terms of the Gregory–Leibniz series."""
    if type(term_count) is not int:
        raise TypeError("term_count must be an integer")
    if term_count <= 0:
        raise ValueError("term_count must be positive")

    total = 0.0
    sign = 1

    for index in range(term_count):
        # Odd denominators (1, 3, 5, ...) with alternating + and - signs.
        total += sign / (2 * index + 1)
        sign = -sign

    return 4 * total


print(f"Approximation of pi (10,000 terms): {approximate_pi(10_000):.5f}")

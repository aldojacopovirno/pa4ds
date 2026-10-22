# Assignment
# Implement a factorial function for non-negative integers, with `0! = 1`. Then
# use it to calculate the binomial coefficient `n choose k`, requiring `0 <= k
# <= n`; return an integer result and display one example.
#
# Solution

# The factorial loop multiplies every integer from one through n.
def factorial(number: int) -> int:
    """Return n! for a non-negative integer n."""
    if type(number) is not int:
        raise TypeError("number must be an integer.")
    if number < 0:
        raise ValueError("number must be non-negative.")

    product = 1
    for factor in range(1, number + 1):
        product *= factor
    return product


def binomial_coefficient(n: int, k: int) -> int:
    """Return the number of ways to choose k items from n items."""
    if type(n) is not int or type(k) is not int:
        raise TypeError("n and k must be integers.")
    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n.")

    return factorial(n) // (factorial(k) * factorial(n - k))


print(binomial_coefficient(10, 0))

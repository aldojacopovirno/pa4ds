# Assignment
# Implement a factorial function for non-negative integers, with `0! = 1`. Then
# use it to calculate the binomial coefficient `n choose k`, requiring `0 <= k
# <= n`; return an integer result and display one example.
#
# Solution

# Define factorial separately so the binomial calculation can reuse it three
# times with different arguments. The int hints describe the expected types;
# the checks inside the function enforce the restrictions when it is called.
def factorial(number: int) -> int:
    """Return n! for a non-negative integer n."""
    # Require the exact int type before using number in range. This also rejects
    # Boolean values, which Python otherwise accepts in many integer operations.
    if type(number) is not int:
        raise TypeError("number must be an integer.")
    # Factorial is defined here only for non-negative integers. Reject a negative
    # input before an empty range could silently leave the product at 1.
    if number < 0:
        raise ValueError("number must be non-negative.")

    # Start at 1, the value that leaves multiplication unchanged. For number == 0,
    # the loop has no iterations, so this starting value also implements 0! = 1.
    product = 1

    # range excludes its upper limit, so number + 1 includes the final factor.
    # Each pass multiplies the running product by the next integer, building
    # 1, then 1*2, then 1*2*3, and so on until all factors have been used.
    for factor in range(1, number + 1):
        product *= factor

    # Return after the entire loop so the caller receives the complete factorial.
    return product


# Use n for the available items and k for how many to choose. The result counts
# selections where choosing the same items in a different order counts once.
def binomial_coefficient(n: int, k: int) -> int:
    """Return the number of ways to choose k items from n items."""
    # Both values must be integers. or makes this condition True if either
    # type check fails, so the function stops before using invalid values.
    if type(n) is not int or type(k) is not int:
        raise TypeError("n and k must be integers.")
    # The number chosen must lie between 0 and n, inclusive. These checks also
    # keep all three factorial arguments, including n - k, non-negative.
    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n.")

    # Apply n! / (k! * (n-k)!). The denominator removes the orderings within
    # the chosen group and the unchosen group from the n! arrangements.
    # // performs integer division. This ratio is a whole number for valid n, k,
    # so it gives the exact integer result without converting to a float.
    return factorial(n) // (factorial(k) * factorial(n - k))


# There is exactly one way to choose no items: the empty selection. Passing
# n = 10 and k = 0 therefore returns 1, which print displays.
print(binomial_coefficient(10, 0))

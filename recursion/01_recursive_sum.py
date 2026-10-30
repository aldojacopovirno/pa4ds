# Assignment
# Write a recursive function that adds every integer from `n` down to `0` when
# `n` is non-negative, and from `n` up to `0` when `n` is negative. For
# example, the sum from `-5` through `0` is `-15`, and from `5` through `0` is
# `15`. Demonstrate both signs.
#
# Solution

# n is the current term in the running total. Each call adds n to the sum of
# the integers between the next value toward zero and 0. The int hints document
# the expected types; they do not check values at runtime.
def recursive_sum(n: int) -> int:

    # Base case: at 0 there is no further integer to include. Returning 0 lets
    # the caller finish its addition without changing the accumulated sum.
    if n == 0:
        return 0
    # For negative n, the next integer toward zero is n + 1 (e.g. -5 then -4).
    # Include n now and recurse on a value closer to the base case.
    elif n < 0:
        return n + recursive_sum(n + 1)
    # For positive n, move toward zero with n - 1 and add the current term.
    else:
        return n + recursive_sum(n - 1)


# Each call moves n one step closer to 0, so every chain of calls eventually
# reaches the base case and stops.
print(f"recursive_sum(-5) = {recursive_sum(-5)}")
print(f"recursive_sum(5) = {recursive_sum(5)}")

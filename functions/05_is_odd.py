# Assignment
# Write an `is_odd` function by calling the `is_even` function and reversing its
# Boolean result. Keep the evenness check in the same file so this program can
# run on its own, then show the result for a sample integer.
#
# Solution

# Keep the evenness helper here so this file can call it on its own.
# number is a parameter for the integer supplied by each call. The int hint
# documents this expectation; this version has no runtime type check.
def is_even(number: int) -> bool:
    """Return whether number is divisible by 2."""
    # An integer is even when division by 2 leaves no remainder. The comparison
    # produces a Boolean that return sends back to the caller.
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """Use the evenness check and invert its Boolean result."""
    # Pass our parameter to is_even as its argument. not reverses the returned
    # Boolean: an even integer gives False here, and an odd integer gives True.
    # Reusing the helper keeps the divisibility rule in a single place.
    return not is_even(number)


# input() returns text; int() converts it to an integer before we call is_odd.
# This conversion belongs to the calling code, not to either helper function.
number = int(input("Integer: "))

# The outer call runs is_odd, which calls is_even, then returns its reversed
# result. Insert that final Boolean into a labelled message for the user.
print(f"Is odd: {is_odd(number)}")

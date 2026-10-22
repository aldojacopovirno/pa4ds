# Assignment
# Write an `is_odd` function by calling the `is_even` function and reversing its
# Boolean result. Keep the evenness check in the same file so this program can
# run on its own, then show the result for a sample integer.
#
# Solution

# The oddness check reuses and reverses the evenness result.
def is_even(number: int) -> bool:
    """Return whether number is divisible by 2."""
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """Use the evenness check and invert its Boolean result."""
    return not is_even(number)


number = int(input("Integer: "))
print(f"Is odd: {is_odd(number)}")

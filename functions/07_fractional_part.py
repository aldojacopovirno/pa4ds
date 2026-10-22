# Assignment
# Write `get_fraction` to return the digits after the decimal point of a
# floating-point number as a value between 0 and 1. For this exercise, use the
# non-negative fractional part, so both `3.75` and `-3.75` produce `0.75`. Read
# a number and display the function result.
#
# Solution

# Put the calculation in a function so it can be reused for different numbers.
# The float hints describe the expected input and result; they do not check types.
def get_fraction(number: float) -> float:
    """Return the non-negative digits after the decimal point."""
    # First use abs to remove the sign: -3.75 becomes 3.75. Then % 1 takes the
    # remainder after removing all whole units, leaving 0.75 in this example.
    # The order matters: -3.75 % 1 alone would give 0.25 under Python's rule
    # for a positive divisor. For a finite input, this result is at least 0
    # and less than 1; a whole number has fractional part 0.
    return abs(number) % 1


# input returns text, so convert it with float before passing it to the function.
number = float(input("Number: "))

# Evaluate the function call inside the braces and insert its returned value
# into the f-string. The label explains which part of the number is displayed.
print(f"Fractional part: {get_fraction(number)}")

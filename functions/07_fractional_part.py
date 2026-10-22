# Assignment
# Write `get_fraction` to return the digits after the decimal point of a
# floating-point number as a value between 0 and 1. For this exercise, use the
# non-negative fractional part, so both `3.75` and `-3.75` produce `0.75`. Read
# a number and display the function result.
#
# Solution

# The remainder after division by one gives the decimal part.
def get_fraction(number: float) -> float:
    """Return the non-negative digits after the decimal point."""
    # Taking abs first makes -3.75 have fractional part 0.75 as well.
    return abs(number) % 1


number = float(input("Number: "))
print(f"Fractional part: {get_fraction(number)}")

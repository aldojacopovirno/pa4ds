# Assignment
# Write a function named `is_even` that accepts an integer and returns `True`
# when the number is divisible by 2, otherwise `False`. Demonstrate the function
# with at least one even and one odd value.
#
# Solution

# A remainder of zero means the number is divisible by two.
def is_even(number: int) -> bool:
    """Return whether an integer is even; reject other input types."""
    if type(number) is not int:
        raise TypeError("number must be an integer")
    return number % 2 == 0


print(f"Is 2 even? {is_even(2)}")
print(f"Is 3 even? {is_even(3)}")

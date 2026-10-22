# Assignment
# Write a function named `is_even` that accepts an integer and returns `True`
# when the number is divisible by 2, otherwise `False`. Demonstrate the function
# with at least one even and one odd value.
#
# Solution

# Define the check once so calls can reuse it with different integers.
# number is the input parameter; -> bool describes the expected result type.
def is_even(number: int) -> bool:
    """Return whether an integer is even; reject other input types."""
    # The int hint does not enforce a type at runtime, so check before using %.
    # Require the exact int type: this also rejects True and False, whose type
    # is bool even though Python allows them in many integer operations.
    if type(number) is not int:
        # Stop this call with an error instead of calculating on an invalid type.
        raise TypeError("number must be an integer")

    # % gives the remainder of division. An integer is even exactly when its
    # remainder on division by 2 is zero, including for zero and negative values.
    # == already produces True or False, so return it without an extra if.
    return number % 2 == 0


# Each call passes an argument to number and inserts the returned Boolean into
# the message. These two examples show both possible outcomes of the check.
print(f"Is 2 even? {is_even(2)}")
print(f"Is 3 even? {is_even(3)}")

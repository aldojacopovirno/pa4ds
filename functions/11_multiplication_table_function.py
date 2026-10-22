# Assignment
# Define a function that accepts a number and prints its multiplication table
# for multipliers 1 through 10. Call the function once with a sample value. Keep
# the repeated printing inside the function so it can be reused with another
# number.
#
# Solution

# Define the repeated work once so each call can supply a different number.
# Defining the function does not run its body: number receives a value when
# the function is called. The float hint describes the expected numeric input.
# -> None says that the function displays rows instead of returning a useful
# result for another calculation; it implicitly returns None when it finishes.
def print_multiplication_table(number: float) -> None:
    """Print the multiplication table from 1 through 10."""
    # range(1, 11) supplies 1 through 10 because the upper limit is excluded.
    # for assigns each multiplier in turn and stops when the range is exhausted.
    for multiplier in range(1, 11):
        # Multiply the current multiplier by the supplied number and insert
        # both factors and their product into one row of the table.
        print(f"{multiplier} * {number} = {multiplier * number}")


# This call runs the body with 10 as number. Another argument would reuse the
# same loop to print a different multiplication table.
print_multiplication_table(10)

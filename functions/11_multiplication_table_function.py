# Assignment
# Define a function that accepts a number and prints its multiplication table
# for multipliers 1 through 10. Call the function once with a sample value. Keep
# the repeated printing inside the function so it can be reused with another
# number.
#
# Solution

# The loop supplies each multiplier to the same reusable function.
def print_multiplication_table(number: float) -> None:
    """Print the multiplication table from 1 through 10."""
    for multiplier in range(1, 11):
        print(f"{multiplier} * {number} = {multiplier * number}")


print_multiplication_table(10)

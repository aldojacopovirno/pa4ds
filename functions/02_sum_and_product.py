# Assignment
# Ask the user for two numbers. Write one function that returns their sum and
# another that returns their product. Call both functions and display the two
# results with clear labels.
#
# Solution

# The functions return values, while the main program handles display.
def summation(first_number: float, second_number: float) -> float:
    """Return the sum of two numbers."""
    return first_number + second_number


def multiplication(first_number: float, second_number: float) -> float:
    """Return the product of two numbers."""
    return first_number * second_number


first_number = float(input("First number: "))
second_number = float(input("Second number: "))

print(f"Sum: {summation(first_number, second_number):.2f}")
print(f"Product: {multiplication(first_number, second_number):.2f}")

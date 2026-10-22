# Assignment
# Ask the user for two numbers. Write one function that returns their sum and
# another that returns their product. Call both functions and display the two
# results with clear labels.
#
# Solution

# def defines a reusable operation; the indented body runs when we call it.
# first_number and second_number are parameters: names for the values received
# by a call. The hints describe the expected inputs and result, without checking
# their types at runtime.
def summation(first_number: float, second_number: float) -> float:
    """Return the sum of two numbers."""
    # return sends the calculated value to the caller and ends this call.
    # Returning instead of printing lets the caller use the sum elsewhere.
    return first_number + second_number


# Give multiplication its own function so either calculation can be reused
# independently with a different pair of numbers.
def multiplication(first_number: float, second_number: float) -> float:
    """Return the product of two numbers."""
    # Multiply the two values received by this call and return their product.
    return first_number * second_number


# input() returns text. Convert it to float so the functions receive numbers,
# including numbers with decimal parts, and can perform numeric arithmetic.
first_number = float(input("First number: "))
second_number = float(input("Second number: "))

# The values inside these calls are arguments. Each call gives its two values
# to the function's parameters, then its returned result enters the f-string.
# Keep display here so the calculation functions need no console interaction.
# :.2f displays two decimal places; it does not round the function's return value.
print(f"Sum: {summation(first_number, second_number):.2f}")
print(f"Product: {multiplication(first_number, second_number):.2f}")

# Assignment
# Write a small program that deliberately attempts to divide a number by zero so
# that Python raises `ZeroDivisionError`. Catch that specific exception and
# display its type and message. This exercise is about recognizing how Python
# reports an invalid arithmetic operation.
#
# Solution

# An average per day would divide the total number of pizzas by the day count.
# Use zero days deliberately: there is no valid average with this denominator.
pizzas_eaten = 100
days = 0

# Put the operation that may fail inside try. Indentation makes the division
# part of that block, so Python can transfer control to a matching except block.
try:
    # / attempts the division, but a zero denominator raises ZeroDivisionError.
    # The calculation fails before = can store a value in average_pizzas.
    average_pizzas = pizzas_eaten / days
# Catch this specific exception so we can explain this failure to the user.
# The words "as error" give us a variable holding the exception object.
except ZeroDivisionError as error:
    # type(error).__name__ gives the error's class name, e.g. ZeroDivisionError.
    # The second pair of braces inserts its message, explaining what went wrong.
    print(f"{type(error).__name__}: {error}")

# Assignment
# Write a small program that deliberately attempts to divide a number by zero so
# that Python raises `ZeroDivisionError`. Catch that specific exception and
# display its type and message. This exercise is about recognizing how Python
# reports an invalid arithmetic operation.
#
# Solution

# The except block handles the exact error raised by dividing by zero.
pizzas_eaten = 100
days = 0

try:
    average_pizzas = pizzas_eaten / days
except ZeroDivisionError as error:
    print(f"{type(error).__name__}: {error}")

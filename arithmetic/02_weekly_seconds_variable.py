# Assignment
# Repeat the weekly-seconds calculation, but store the result in a variable
# before displaying it. Use the same unit conversions as in the previous
# exercise. The goal is to make the intermediate value available for later use,
# not only to print it immediately.
#
# Solution

# Use * to multiply the unit conversions: 60 * 60 gives seconds per hour,
# multiplying by 24 gives seconds per day, and multiplying by 7 gives a week.
# Python calculates the right-hand expression first. The = then stores that
# result under seconds_in_week, so later statements can use it without repeating
# the calculation. A descriptive name also tells us which quantity was stored.
seconds_in_week = 60 * 60 * 24 * 7

# The f prefix lets {seconds_in_week} insert the variable's value into the text.
# print() displays that text; the label gives the number a meaning and a unit.
print(f"Seconds in a week: {seconds_in_week}")

# Assignment
# Generate one random integer from 1 through 10, including both endpoints, and
# display it. Use the standard library’s random-number generator rather than
# choosing a fixed value.
#
# Solution

# Import random() from the standard library so we can generate a value instead
# of choosing a fixed number ourselves.
from random import random

# random() produces a pseudo-random float x with 0 <= x < 1. Multiplying by
# 10 gives a value from 0 up to, but excluding, 10. Because this value is
# nonnegative, int() removes its fractional part and leaves an integer 0 to 9.
# Add 1 to shift these integers to 1 through 10, including both endpoints.
# For example, a generated value of 0.73 becomes int(7.3) + 1, which is 8.
random_number = int(random() * 10) + 1

# Display the resulting integer; later draws may produce the same number.
print(f"Random number generated: {random_number}")

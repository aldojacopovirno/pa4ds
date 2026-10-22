# Assignment
# Generate one random integer from 1 through 10, including both endpoints, and
# display it. Use the standard library’s random-number generator rather than
# choosing a fixed value.
#
# Solution

from random import random

# Scaling a random value below one and shifting it gives the range 1 to 10.
random_number = int(random() * 10) + 1

print(f"Random number generated: {random_number}")

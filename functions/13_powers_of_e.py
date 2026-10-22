# Assignment
# Display a small table of the exponential function `e**x` for the integer
# exponents -1, 0, 1, 2, and 3. Show both the exponent and its value, aligning
# the columns so the table is easy to compare.
#
# Solution

from math import exp

# Each pass evaluates the exponential function for one exponent.
print("=== Powers of Euler's Number ===")
print(f"{'Exponent':>8} {'Value':>10}")

for exponent in range(-1, 4):
    value = exp(exponent)
    print(f"{exponent:>8} {value:>10.5f}")

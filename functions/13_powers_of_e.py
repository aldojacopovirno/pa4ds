# Assignment
# Display a small table of the exponential function `e**x` for the integer
# exponents -1, 0, 1, 2, and 3. Show both the exponent and its value, aligning
# the columns so the table is easy to compare.
#
# Solution

# Import exp from math to calculate e**x, where e is Euler's number
# (approximately 2.71828), without entering an approximation of e ourselves.
from math import exp

print("=== Powers of Euler's Number ===")
# >8 and >10 right-align the headings in fields at least eight and ten
# characters wide, matching the widths used for the values below.
print(f"{'Exponent':>8} {'Value':>10}")

# range(-1, 4) supplies -1, 0, 1, 2, and 3 because its upper limit is excluded.
# for advances through these exponents automatically and stops after 3.
for exponent in range(-1, 4):
    # exp(exponent) computes e**exponent. A negative exponent gives a reciprocal
    # (e**-1 = 1/e), zero gives 1, and positive integers give repeated products.
    value = exp(exponent)
    # Align the exponent and value with their headings. .5f shows five digits
    # after the decimal point, rounding only the displayed value.
    print(f"{exponent:>8} {value:>10.5f}")

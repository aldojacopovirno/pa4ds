# Assignment
# Ask for the two perpendicular side lengths of a right triangle. Use the
# Pythagorean theorem, `c = sqrt(a² + b²)`, to calculate the hypotenuse and
# display it to two decimal places.
#
# Solution

from math import sqrt

# The square-root formula combines the two perpendicular side lengths.
print("==== Pythagorean Theorem ====")
side_a = float(input("Enter the first side length: "))
side_b = float(input("Enter the second side length: "))

hypotenuse = sqrt(side_a**2 + side_b**2)
print(f"Hypotenuse length: {hypotenuse:.2f}")

# Assignment
# Ask for the two perpendicular side lengths of a right triangle. Use the
# Pythagorean theorem, `c = sqrt(a² + b²)`, to calculate the hypotenuse and
# display it to two decimal places.
#
# Solution

# Import sqrt to take the square root after adding the squared side lengths.
from math import sqrt

# The formula assumes a right triangle and two valid perpendicular side lengths.
print("==== Pythagorean Theorem ====")

# input returns text. Convert each answer with float so decimal lengths can be
# used in the calculation; these prompts ask for the sides forming the right angle.
side_a = float(input("Enter the first side length: "))
side_b = float(input("Enter the second side length: "))

# The Pythagorean theorem says c**2 = a**2 + b**2. Use ** 2 to square each
# length, add the squares, then take sqrt to obtain the hypotenuse length c.
hypotenuse = sqrt(side_a**2 + side_b**2)

# Insert the result into the f-string. :.2f displays exactly two decimal places,
# rounding the displayed number without changing the value in hypotenuse.
print(f"Hypotenuse length: {hypotenuse:.2f}")

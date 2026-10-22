# Assignment
# Calculate the area of a circle with radius 3. Use π = 3.14159 and the formula
# `area = π × radius²`. Display the radius and the area, rounding the result to
# two decimal places.
#
# Solution

# Use the given approximation of pi and the distance from the centre of the
# circle to its edge. These are the two values needed for the area formula.
pi = 3.14159
radius = 3

# In Python, ** means exponentiation: radius**2 is radius multiplied by itself.
# Python evaluates ** before *, so this expression squares 3 to get 9 and then
# multiplies by pi. If the radius is in centimetres, the area is in square
# centimetres.
surface_area = pi * radius**2

# Insert the radius and the calculated area into the sentence with f-strings.
# The format :.2f displays the area rounded to two digits after the decimal
# point; it changes the displayed text, not the value stored in surface_area.
# Inside print's parentheses, the two adjacent strings join into one sentence.
# The space at the end of the first string keeps the words separated.
print(
    f"The surface area of a circle with radius {radius} "
    f"is {surface_area:.2f}"
)

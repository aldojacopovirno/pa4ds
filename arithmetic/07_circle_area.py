# Assignment
# Calculate the area of a circle with radius 3. Use π = 3.14159 and the formula
# `area = π × radius²`. Display the radius and the area, rounding the result to
# two decimal places.
#
# Solution

# Square the radius before multiplying by pi.
pi = 3.14159
radius = 3

surface_area = pi * radius**2
print(
    f"The surface area of a circle with radius {radius} "
    f"is {surface_area:.2f}"
)

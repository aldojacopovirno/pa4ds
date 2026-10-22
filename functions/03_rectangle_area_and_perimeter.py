# Assignment
# Ask the user for the width and height of a rectangle. Calculate its perimeter
# as twice the sum of its side lengths and its area as width times height.
# Require positive side lengths, then display both results to two decimal
# places.
#
# Solution

# Define each formula separately so a caller can reuse either calculation.
# width and height are parameters; a call supplies the actual side lengths.
def rectangle_perimeter(width: float, height: float) -> float:
    """Return the perimeter of a rectangle."""
    # A rectangle has two sides of each length: width + height + width + height
    # equals 2 * (width + height). Return the distance around its boundary.
    return 2 * (width + height)


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    # Width times height measures the surface covered by the rectangle.
    # Return the result so the caller decides how to use or display it.
    return width * height


# Convert the entered text to numbers so side lengths can have decimal parts.
# Both lengths must use the same unit for the formulas to make sense.
width = float(input("Width: "))
height = float(input("Height: "))

# Each comparison produces a Boolean. or makes this condition true when either
# side is zero or negative, which would not give the required rectangle.
# The calling code checks this requirement before calling either function;
# the functions themselves apply their formulas without checking the lengths.
if width <= 0 or height <= 0:
    # Raising the error stops this run before invalid lengths reach the output.
    raise ValueError("Side lengths must be positive.")

# Call each function with the validated lengths and display its returned value.
# :.2f shows two decimal places. The perimeter uses the input length unit;
# the area uses its square, e.g. metres and square metres for inputs in metres.
print(f"Perimeter: {rectangle_perimeter(width, height):.2f}")
print(f"Area: {rectangle_area(width, height):.2f}")

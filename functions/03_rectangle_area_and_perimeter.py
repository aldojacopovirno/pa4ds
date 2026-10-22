# Assignment
# Ask the user for the width and height of a rectangle. Calculate its perimeter
# as twice the sum of its side lengths and its area as width times height.
# Require positive side lengths, then display both results to two decimal
# places.
#
# Solution

# Keeping the formulas in separate functions makes each result reusable.
def rectangle_perimeter(width: float, height: float) -> float:
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


width = float(input("Width: "))
height = float(input("Height: "))

if width <= 0 or height <= 0:
    raise ValueError("Side lengths must be positive.")

print(f"Perimeter: {rectangle_perimeter(width, height):.2f}")
print(f"Area: {rectangle_area(width, height):.2f}")

# Assignment
# Write a function for the equation `a*x**2 + b*x + c = 0`, assuming `a` is not
# zero. Use the discriminant to decide whether there are no real roots, one
# repeated real root, or two real roots. Return the roots as a tuple, with an
# empty tuple when there are no real solutions.
#
# Solution

# The discriminant determines how many real roots the equation has.
def quadratic_equation_solver(a: float, b: float, c: float) -> tuple:
    """Return the real roots of a*x**2 + b*x + c = 0."""
    from math import sqrt

    if a == 0:
        raise ValueError("The coefficient a must be non-zero.")

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return ()
    if discriminant == 0:
        return (-b / (2 * a),)

    return (
        (-b - sqrt(discriminant)) / (2 * a),
        (-b + sqrt(discriminant)) / (2 * a),
    )


print(quadratic_equation_solver(1, -5, 6))

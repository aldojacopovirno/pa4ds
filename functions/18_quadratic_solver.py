# Assignment
# Write a function for `a*x**2 + b*x + c = 0` where `a` is non-zero. Return a
# three-item tuple containing the number of real roots followed by the roots;
# use `None` for root positions that do not exist. Show an example with two real
# roots.
#
# Solution

# The discriminant separates the zero-root, one-root, and two-root cases.
def quadratic_equation_solver(a: float, b: float, c: float) -> tuple:
    """Return (root_count, first_root, second_root) for a quadratic."""
    from math import sqrt

    if a == 0:
        raise ValueError("The coefficient a must be non-zero.")

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return 0, None, None
    if discriminant == 0:
        return 1, -b / (2 * a), None

    first_root = (-b - sqrt(discriminant)) / (2 * a)
    second_root = (-b + sqrt(discriminant)) / (2 * a)
    return 2, first_root, second_root


print(quadratic_equation_solver(1, -5, 6))

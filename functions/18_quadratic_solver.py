# Assignment
# Write a function for `a*x**2 + b*x + c = 0` where `a` is non-zero. Return a
# three-item tuple containing the number of real roots followed by the roots;
# use `None` for root positions that do not exist. Show an example with two real
# roots.
#
# Solution

# Supply the coefficients as parameters so one function can solve different
# quadratic equations. Every branch returns three values in the same order:
# the number of real roots, the first root, and the second root.
def quadratic_equation_solver(a: float, b: float, c: float) -> tuple:
    """Return (root_count, first_root, second_root) for a quadratic."""
    # Import the square-root operation needed for the two-root formula below.
    from math import sqrt

    # == compares values. If a is zero, the equation is no longer quadratic,
    # and the formula would divide by zero. Stop this call before calculating.
    if a == 0:
        raise ValueError("The coefficient a must be non-zero.")

    # **2 squares b. The sign of b*b - 4*a*c tells us how many real roots
    # are possible, because this value appears under the square root.
    discriminant = b**2 - 4 * a * c

    # A negative discriminant has no real square root, so return a count of zero.
    # Commas group these values into a tuple; None marks each missing root.
    # return ends the call immediately, avoiding a square root of a negative value.
    if discriminant < 0:
        return 0, None, None

    # If the computed discriminant is exactly zero, the plus and minus forms
    # coincide. Return the repeated root once and mark the unused position None.
    # The parentheses make 2 * a the whole divisor in -b / (2 * a).
    if discriminant == 0:
        return 1, -b / (2 * a), None

    # A negative or zero discriminant would already have returned, so the
    # remaining case has two distinct real roots. Subtract the square root for
    # one and add it for the other, using the same nonzero denominator in both.
    first_root = (-b - sqrt(discriminant)) / (2 * a)
    second_root = (-b + sqrt(discriminant)) / (2 * a)

    # Package both calculated roots with their count so the caller can interpret
    # the same three tuple positions regardless of which case was selected.
    return 2, first_root, second_root


# Match the arguments to a, b, c: x**2 - 5*x + 6 = 0 has discriminant 1.
# Its roots are 2 and 3, so this call returns (2, 2.0, 3.0) for print to display.
print(quadratic_equation_solver(1, -5, 6))

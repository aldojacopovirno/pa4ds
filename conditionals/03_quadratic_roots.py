# Assignment
# Write a function for the equation `a*x**2 + b*x + c = 0`, assuming `a` is not
# zero. Use the discriminant to decide whether there are no real roots, one
# repeated real root, or two real roots. Return the roots as a tuple, with an
# empty tuple when there are no real solutions.
#
# Solution

# Pass the three coefficients to a function so the same calculation can be used
# for different equations. The return value groups the real roots in a tuple.
# The type hints describe the expected inputs and output; they do not check
# or convert the arguments when the function is called.
def quadratic_equation_solver(a: float, b: float, c: float) -> tuple:
    """Return the real roots of a*x**2 + b*x + c = 0."""
    # Import the square-root function used in the quadratic formula. We will
    # call it only after checking that its argument is positive.
    from math import sqrt

    # == compares two values and produces True or False. If a is zero, the
    # equation is no longer quadratic, and the formula would divide by 2 * 0.
    # Raise an error to stop this call before attempting that calculation.
    if a == 0:
        raise ValueError("The coefficient a must be non-zero.")

    # The quadratic formula is (-b +/- sqrt(discriminant)) / (2 * a).
    # Calculate b squared minus 4*a*c once: its sign tells us which kind of
    # result is possible, so we can choose a branch before taking a square root.
    discriminant = b**2 - 4 * a * c

    # A negative number has no real square root, so there are no real roots.
    # Return an empty tuple to represent that result. return ends the function
    # call immediately, so none of the calculations below run in this case.
    if discriminant < 0:
        return ()

    # We reach this check only if the discriminant was not negative.
    # If it is exactly zero, adding or subtracting its square root gives the
    # same root, -b / (2 * a), so return that value only once.
    # The comma makes a one-item tuple; parentheses alone would just group
    # the number. In the formula, parentheses keep all of 2 * a in the divisor.
    if discriminant == 0:
        return (-b / (2 * a),)

    # A negative or zero discriminant would already have ended this call, so
    # the remaining case is a positive discriminant. Subtract its square root
    # for one root and add it for the other. The comma groups the two results
    # into the returned tuple.
    return (
        (-b - sqrt(discriminant)) / (2 * a),
        (-b + sqrt(discriminant)) / (2 * a),
    )


# Match the arguments to a, b, c: this call solves x**2 - 5*x + 6 = 0.
# Its discriminant is 25 - 24 = 1, so the function returns (2.0, 3.0).
# Python finishes the function call before print displays the returned tuple.
print(quadratic_equation_solver(1, -5, 6))

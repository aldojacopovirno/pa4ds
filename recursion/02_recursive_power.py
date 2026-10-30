# Assignment
# Write a recursive function that raises an integer base `x` to a non-negative
# integer exponent `y`, using the definition `x**0 = 1` and `x**y = x * x**(y - 1)`
# for larger `y`. Demonstrate a positive base and a negative base with an odd
# exponent.
#
# Solution

# x is the base and y is the exponent. Each recursive step reduces y by one,
# matching the definition x**y = x * x**(y - 1) until y reaches 0.
def recursive_power(x: int, y: int) -> int:

    # Base case: any base (including negative) raised to the zeroth power is 1.
    if y == 0:
        return 1

    else:
        # Decrement y in this call's local variable before recursing. The next
        # call therefore computes x**(y - 1); multiplying by x completes x**y.
        y -= 1
        return x * recursive_power(x, y)


# 2**2 is 4. (-3)**3 is -27 because an odd number of negative factors stays negative.
print(f"recursive_power(2, 2) = {recursive_power(2, 2)}")
print(f"recursive_power(-3, 3) = {recursive_power(-3, 3)}")

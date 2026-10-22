# Assignment
# Write a recursive function for the Fibonacci sequence using `F(0) = 0`, `F(1)
# = 1`, and `F(n) = F(n - 1) + F(n - 2)` for larger `n`. Reject negative inputs
# and demonstrate the function on a few small values.
#
# Solution

# The cases n equals zero and n equals one stop the recursive calls.
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for number in range(5):
    print(f"Fibonacci({number}) = {fibonacci(number)}")

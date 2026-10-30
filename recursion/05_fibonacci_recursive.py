# Assignment
# Write a recursive function for the Fibonacci sequence using `F(0) = 0`, `F(1)
# = 1`, and `F(n) = F(n - 1) + F(n - 2)` for larger `n`. Reject negative inputs
# and demonstrate the function on a few small values.
#
# Solution

# n is the index of the requested Fibonacci number: F(0), F(1), F(2), etc.
# The function expects a non-negative integer. The int hints document the input
# and return types; they do not check types when the function runs.
def fibonacci(n: int) -> int:
    # n < 0 is a Boolean condition. If it is True, stop with an error because
    # this exercise defines the sequence only for non-negative indices.
    if n < 0:
        raise ValueError("n must be non-negative")

    # These are the base cases: their answers are already known, so return
    # immediately without making more calls. Every valid chain of calls ends
    # at one of these cases.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # For n >= 2, split the calculation into two smaller problems. Both
        # n - 1 and n - 2 move closer to a base case, so recursion can stop.
        # Python first calculates F(n - 1), then F(n - 2). This call waits for
        # both results, adds them, and returns the sum to whoever called it.
        # For example, F(3) needs F(2) + F(1); F(2) needs F(1) + F(0).
        # The base cases return 1 and 0, giving F(2) = 1 and then F(3) = 2.
        # F(1) is calculated twice here. This simple recursive method repeats
        # such work because it does not save results for later calls.
        return fibonacci(n - 1) + fibonacci(n - 2)


# range(5) produces indices 0 through 4; its upper limit is excluded. Each
# iteration calls the function with one index and prints its returned value.
# The displayed Fibonacci values are 0, 1, 1, 2, and 3, respectively.
for number in range(5):
    print(f"Fibonacci({number}) = {fibonacci(number)}")

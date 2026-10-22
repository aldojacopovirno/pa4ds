# Assignment
# Extend the recursive Fibonacci calculation so it prints when a call starts and
# when it returns a value. Indent each message according to the call depth, then
# trace a small input so the nested calls are visible.
#
# Solution

# Increasing depth on each call makes the recursive tree visible in the output.
def fibonacci_with_depth(n: int, depth: int = 0) -> int:
    print(f"{' ' * depth}fib({n}) called")

    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_with_depth(n - 1, depth + 1)
        result += fibonacci_with_depth(n - 2, depth + 1)

    print(f"{' ' * depth}fib({n}) returning {result}")
    return result

fibonacci_with_depth(5)

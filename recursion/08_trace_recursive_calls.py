# Assignment
# Extend the recursive Fibonacci calculation so it prints when a call starts and
# when it returns a value. Indent each message according to the call depth, then
# trace a small input so the nested calls are visible.
#
# Solution

# n selects F(n), and depth records how many levels below the first call we are.
# depth defaults to 0, so a caller can start the trace by supplying only n.
# n is expected to be a non-negative integer; int hints describe the expected
# types but do not enforce them when the function runs.
def fibonacci_with_depth(n: int, depth: int = 0) -> int:
    # Multiplying a string by depth repeats it that many times. ' ' * depth
    # therefore adds depth spaces before the message, showing how calls nest.
    # Print on entry, before any check, so even a rejected call appears.
    print(f"{' ' * depth}fib({n}) called")

    # Reject negative indices before starting any smaller calculations.
    # Raising the error stops this call, so it does not print a return message.
    if n < 0:
        raise ValueError("n must be non-negative")

    # Base cases need no further calls. Store the known value in result rather
    # than returning here, so they also reach the shared return message below.
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        # First calculate F(n - 1). This call pauses until that entire smaller
        # calculation finishes, then stores its returned value in result.
        # Each call has its own local result; nested calls do not overwrite it.
        # depth + 1 places the new call one level deeper in the trace.
        result = fibonacci_with_depth(n - 1, depth + 1)

        # Only after the first branch returns, calculate F(n - 2) and add its
        # result to F(n - 1). Both direct child calls receive the same depth + 1
        # because they are at the same level, even though they run in order.
        # Smaller indices eventually reach 0 or 1 and stop making calls.
        result += fibonacci_with_depth(n - 2, depth + 1)

    # Print after any child calls have finished. Using this call's own depth
    # aligns its return message with its entry message, making the pair visible.
    print(f"{' ' * depth}fib({n}) returning {result}")
    # Pass the completed value back to the waiting caller so it can continue.
    return result


# Supplying only 5 uses the default depth of 0. The trace shows the nested
# calls and ends with "fib(5) returning 5"; the function also returns 5.
fibonacci_with_depth(5)

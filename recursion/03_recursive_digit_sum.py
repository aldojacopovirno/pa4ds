# Assignment
# Write and test a recursive function to find the sum of digits of a given
# positive number. Hint: divide by `10` and use the modulo operator to separate
# the last digit from the remaining value. Demonstrate on a multi-digit example.
#
# Solution

# n is a positive integer. The function returns the sum of its decimal digits
# by peeling off the ones place with n % 10 and recursing on n // 10.
def recursive_digit_sum(n: int) -> int:

    # Base case: a one-digit number is its own digit sum.
    if n < 10:
        return n

    # n % 10 is the last digit; n // 10 drops that digit from the value.
    # Adding them combines the last digit with the sum of the remaining digits.
    return (n % 10) + recursive_digit_sum(n // 10)


# 1 + 2 + 3 + 4 + 5 is 15. A single-digit input returns itself without recursing.
print(f"recursive_digit_sum(12345) = {recursive_digit_sum(12345)}")
print(f"recursive_digit_sum(9) = {recursive_digit_sum(9)}")

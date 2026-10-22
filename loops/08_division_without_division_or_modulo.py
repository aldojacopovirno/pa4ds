# Assignment
# Read non-negative integers `A` and `B`. Without using `/` or `%`, compute the
# integer quotient and remainder by repeatedly subtracting `B` from `A`. Handle
# `B = 0` explicitly and display both results when division is defined.
#
# Solution

# Every subtraction contributes one quotient unit until the remainder is smaller.
dividend = int(input("A (non-negative integer): "))
divisor = int(input("B (positive integer): "))

if dividend < 0 or divisor < 0:
    print("Use non-negative integers only.")
elif divisor == 0:
    print("Cannot divide by zero.")
else:
    remainder = dividend
    quotient = 0

    # Each subtraction removes one group of divisor from the dividend.
    while remainder >= divisor:
        remainder -= divisor
        quotient += 1

    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")

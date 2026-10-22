# Assignment
# Read non-negative integers `A` and `B`. Without using `/` or `%`, compute the
# integer quotient and remainder by repeatedly subtracting `B` from `A`. Handle
# `B = 0` explicitly and display both results when division is defined.
#
# Solution

# Read the amount to divide (A) and the size of each group (B). input returns
# text, so int converts each entry to an integer for comparisons and subtraction.
dividend = int(input("A (non-negative integer): "))
divisor = int(input("B (positive integer): "))

# Each comparison gives True or False. With or, this condition is True if
# either input is negative, which is outside the exercise's allowed inputs.
# if/elif/else chooses only the first matching branch, so an invalid input
# receives a message and does not enter the division calculation below.
if dividend < 0 or divisor < 0:
    print("Use non-negative integers only.")
# We reach elif only when neither input is negative. Check zero separately:
# division by zero is undefined, and subtracting zero would never make progress.
elif divisor == 0:
    print("Cannot divide by zero.")
else:
    # Here the dividend is non-negative and the divisor is positive. Keep the
    # ungrouped amount in remainder; initially none of the dividend is grouped.
    # Start quotient at zero because we have not removed any complete groups.
    remainder = dividend
    quotient = 0

    # Continue while a whole group still fits in the remaining amount. >= also
    # includes an exact fit, which must count as a group and leave zero over.
    # while checks this Boolean condition before each repetition.
    while remainder >= divisor:
        # Remove one group and count it: -= subtracts from the current value,
        # and += adds to it. A positive divisor makes remainder smaller each
        # time; the condition ensures that it never becomes negative.
        remainder -= divisor
        quotient += 1

    # The loop stops when 0 <= remainder < divisor: no complete group fits.
    # Throughout the loop, A = quotient * B + remainder, because each group
    # removed from remainder is added to the count. For A = 17 and B = 5,
    # remainder goes 17 -> 12 -> 7 -> 2, giving quotient 3: 17 = 3 * 5 + 2.
    # If A is smaller than B (including A = 0), the loop runs zero times:
    # quotient stays zero and the whole dividend remains as the remainder.
    # Print both values with labels to distinguish groups from leftover units.
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")

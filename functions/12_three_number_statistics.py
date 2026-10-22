# Assignment
# Read three numeric values and report the largest value, the smallest value,
# and their arithmetic mean. Use clear labels and round the displayed results to
# two decimal places.
#
# Solution

# Keep the entered values together so all three calculations use the same data.
numbers = []

# range(1, 4) supplies positions 1, 2, and 3; the excluded upper limit makes
# the loop ask for exactly three values and labels the prompts from one.
for position in range(1, 4):
    # input() returns text. Convert it to float to accept decimal values and
    # make the later calculations numeric.
    number = float(input(f"Enter number {position}: "))
    # append adds the new value to the end without replacing earlier entries.
    # The list therefore contains all three numbers when the loop finishes.
    numbers.append(number)

# max and min compare the actual inputs, so the results also work when all
# values are negative or all are positive.
largest = max(numbers)
smallest = min(numbers)
# An arithmetic mean is the total divided by the number of values. sum adds
# the collected numbers, and len is three after the three successful inputs,
# so the denominator is nonzero.
average = sum(numbers) / len(numbers)

# The labels identify each result. :.2f displays two digits after the decimal
# point, rounding the output without changing the stored calculation results.
print(
    f"Largest: {largest:.2f}, smallest: {smallest:.2f}, "
    f"average: {average:.2f}"
)

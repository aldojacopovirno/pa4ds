# Assignment
# Read three numeric values and report the largest value, the smallest value,
# and their arithmetic mean. Use clear labels and round the displayed results to
# two decimal places.
#
# Solution

# The built-in min, max, and sum functions summarize the collected values.
numbers = []

for position in range(1, 4):
    number = float(input(f"Enter number {position}: "))
    numbers.append(number)

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print(
    f"Largest: {largest:.2f}, smallest: {smallest:.2f}, "
    f"average: {average:.2f}"
)

# Assignment
# Read a sequence of integers and select a value only when it is even, divisible
# by 3, and greater than the value immediately before it. The first value has no
# predecessor and cannot be selected. Display the selected values’ sum and mean,
# explaining the empty-selection case.
#
# Solution

# Start at index one because the first value has no predecessor.
count = int(input("How many integers? "))
if count < 0:
    raise ValueError("The count must be non-negative.")

numbers = []
for position in range(1, count + 1):
    numbers.append(int(input(f"Integer {position}: ")))

selected_numbers = []
# Index 0 has no predecessor, so it cannot satisfy the full condition.
for index in range(1, len(numbers)):
    number = numbers[index]
    previous_number = numbers[index - 1]

    if number % 2 == 0 and number % 3 == 0 and number > previous_number:
        selected_numbers.append(number)

print(f"Sum: {sum(selected_numbers)}")
if len(selected_numbers) == 0:
    print("Mean is undefined: no values meet all conditions.")
else:
    print(f"Mean: {sum(selected_numbers) / len(selected_numbers)}")

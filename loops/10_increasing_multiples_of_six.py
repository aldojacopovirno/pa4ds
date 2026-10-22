# Assignment
# Read a sequence of integers and examine each value after the first. Select
# values that are greater than their immediate predecessor and divisible by both
# 2 and 3. Report the sum and mean of the selected values; explain when no value
# qualifies.
#
# Solution

# Compare each candidate with its immediate predecessor before selecting it.
count = int(input("How many integers? "))
if count < 0:
    raise ValueError("The count must be non-negative.")

sequence = []
for position in range(1, count + 1):
    sequence.append(int(input(f"Integer {position}: ")))

selected_sum = 0
selected_count = 0

# The first value has no previous value, so comparisons start at index 1.
for index in range(1, len(sequence)):
    number = sequence[index]
    previous_number = sequence[index - 1]

    if number % 2 == 0 and number % 3 == 0 and number > previous_number:
        selected_sum += number
        selected_count += 1

print(f"Sum of selected values: {selected_sum}")
if selected_count == 0:
    print("Mean is undefined because no values meet all conditions.")
else:
    print(f"Mean of selected values: {selected_sum / selected_count}")

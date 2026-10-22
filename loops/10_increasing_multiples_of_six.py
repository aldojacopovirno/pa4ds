# Assignment
# Read a sequence of integers and examine each value after the first. Select
# values that are greater than their immediate predecessor and divisible by both
# 2 and 3. Report the sum and mean of the selected values; explain when no value
# qualifies.
#
# Solution

# Read the sequence length first so the input loop knows how many values to ask
# for. Convert the text to an integer before using it in range.
count = int(input("How many integers? "))

# A sequence cannot have a negative number of values. Zero is allowed: it
# produces an empty sequence, handled by the final selected_count check.
if count < 0:
    raise ValueError("The count must be non-negative.")

# Start with no stored values. range excludes count + 1, giving prompt numbers
# from 1 through count; each append adds one converted integer to the list.
sequence = []
for position in range(1, count + 1):
    sequence.append(int(input(f"Integer {position}: ")))

# Track both the sum and how many values contribute. The sum alone cannot tell
# us whether any values were selected, and the mean needs their count.
selected_sum = 0
selected_count = 0

# List indices start at 0. Begin at 1 so index - 1 refers to an actual preceding
# value, and stop before len(sequence) to keep index inside the list.
# With fewer than two values, the range is empty and the loop has no iterations.
for index in range(1, len(sequence)):
    # Compare with the immediate neighbour in the original sequence, even
    # when that neighbour failed the selection test.
    number = sequence[index]
    previous_number = sequence[index - 1]

    # Each comparison produces True or False. and requires all three conditions:
    # no remainder after division by 2, no remainder after division by 3, and a
    # strict increase over the previous value. The first two mean a multiple of 6.
    # E.g. in [8, 12, 6], 12 qualifies, but 6 fails the increase test.
    if number % 2 == 0 and number % 3 == 0 and number > previous_number:
        # Add a qualifying value to the running total and count that contribution.
        # If the condition is False, neither accumulator changes. The for loop
        # then advances to the next index, regardless of the condition's result.
        selected_sum += number
        selected_count += 1

# Print only after every candidate has been checked, so the sum is complete.
print(f"Sum of selected values: {selected_sum}")

# Check the selected count, not the sequence length: a non-empty sequence may
# have no qualifying values. Avoid division by zero when that count is zero.
if selected_count == 0:
    print("Mean is undefined because no values meet all conditions.")
else:
    # Divide by the number of selected values, since only they contributed
    # to selected_sum. Dividing by count would also include rejected values.
    print(f"Mean of selected values: {selected_sum / selected_count}")

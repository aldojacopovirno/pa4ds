# Assignment
# Read exactly ten integers into a list. Find the smallest and largest values
# and count how many are divisible by 3. Scan the stored values and print the
# three results with clear labels.
#
# Solution

# Store each entered integer so we can examine the same ten values in later
# loops. input() returns text; int() converts it before append adds it to the list.
numbers = []

# range excludes its upper limit, so 1 through 10 supplies ten input labels.
# position numbers the prompts; append places each value at the end of the list.
for position in range(1, 11):
    numbers.append(int(input(f"Integer {position}: ")))

# Use the first value as both starting candidates, since we know the list is
# non-empty. Starting from 0 could give a result that never appeared in the
# input, e.g. a maximum of 0 when every entered number is negative.
minimum = numbers[0]
maximum = numbers[0]

# Keep a separate count for divisibility; no values have been checked for it yet.
divisible_by_three_count = 0

# The slice [1:] contains every value after the first, which already supplied
# the starting minimum and maximum. for visits each of these values once and
# stops when the slice is exhausted.
for number in numbers[1:]:
    # Replace the smallest value seen so far only if this value is smaller.
    # Otherwise keep the current minimum for the next comparison.
    if number < minimum:
        minimum = number

    # Maintain the largest value in the same way. These comparisons leave us
    # with the minimum and maximum of all the values examined so far.
    if number > maximum:
        maximum = number

# This pass visits the full list, including the first value, so every entered
# number is considered for the divisibility count.
for number in numbers:
    # % gives the remainder. A remainder of zero means the number is divisible
    # by 3, so count it once; a nonzero remainder leaves the count unchanged.
    if number % 3 == 0:
        divisible_by_three_count += 1

# Display the results after both scans have finished. The labels distinguish
# the two numeric values from the count; f-string braces insert each result.
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Multiples of 3: {divisible_by_three_count}")

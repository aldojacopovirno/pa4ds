# Assignment
# Read exactly ten integers into a list. Find the smallest and largest values
# and count how many are divisible by 3. Scan the stored values and print the
# three results with clear labels.
#
# Solution

# Initialize the minimum and maximum from real data before comparing later values.
numbers = []
for position in range(1, 11):
    numbers.append(int(input(f"Integer {position}: ")))

minimum = numbers[0]
maximum = numbers[0]
divisible_by_three_count = 0

# Start extrema at a real value, then compare every remaining value once.
for number in numbers[1:]:
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number

for number in numbers:
    if number % 3 == 0:
        divisible_by_three_count += 1

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Multiples of 3: {divisible_by_three_count}")

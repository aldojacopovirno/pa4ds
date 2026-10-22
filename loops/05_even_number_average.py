# Assignment
# Ask how many integers are in a sequence, read them one by one, and calculate
# the sum and mean of only the even values. If the sequence contains no even
# values, display the sum as zero and state that the mean is undefined.
#
# Solution

# continue skips odd values so only evens update the sum and count.
count = int(input("How many integers? "))
if count < 0:
    raise ValueError("The count must be non-negative.")

sequence = []
for position in range(1, count + 1):
    sequence.append(int(input(f"Integer {position}: ")))

even_sum = 0
even_count = 0
for number in sequence:
    if number % 2 != 0:
        continue
    even_sum += number
    even_count += 1

print(f"Sum of even values: {even_sum}")
if even_count == 0:
    print("Mean is undefined because there are no even values.")
else:
    print(f"Mean of even values: {even_sum / even_count}")

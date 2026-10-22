# Assignment
# Read a sequence of integers and keep the even values. Report their sum,
# arithmetic mean, minimum, and maximum. If there are no even values, still
# report a sum of zero and explain that the mean and extrema are undefined.
#
# Solution

# The empty-list check prevents undefined mean and extrema calculations.
count = int(input("How many integers? "))
if count < 0:
    raise ValueError("The count must be non-negative.")

numbers = []
for position in range(1, count + 1):
    numbers.append(int(input(f"Integer {position}: ")))

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(f"Sum: {sum(even_numbers)}")
if len(even_numbers) == 0:
    print("Mean, minimum, and maximum are undefined: no even values.")
else:
    mean = sum(even_numbers) / len(even_numbers)
    print(f"Mean: {mean}")
    print(f"Minimum: {min(even_numbers)}")
    print(f"Maximum: {max(even_numbers)}")

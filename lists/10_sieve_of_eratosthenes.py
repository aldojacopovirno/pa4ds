# Assignment
# Use a list to find and print every prime number from 2 through 100. Start with
# the candidate numbers, then mark multiples of each prime as composite so they
# are skipped later.
#
# Solution

# Zero marks composites so they are skipped in later passes.
numbers = list(range(1, 101))
numbers[0] = 0

for i in range(len(numbers)):
    prime = numbers[i]

    if prime == 0:
        continue

    for multiple in range(2 * prime, 101, prime):
        numbers[multiple - 1] = 0

for number in numbers:

    if number != 0:
        print(number)

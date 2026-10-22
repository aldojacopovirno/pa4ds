# Assignment
# Write a function that scans a list from left to right for a target value.
# Return the index of its first occurrence; if the value is not present, return
# `-1`. Demonstrate both an existing and a missing target.
#
# Solution

# Returning immediately preserves the index of the first match.
def find_index(target: int, sequence: list) -> int:

    for i in range(len(sequence)):
        if sequence[i] == target:
            return i
    return -1

target = 5

first_sequence = [1, 2, 3, 4, 5]
second_sequence = [1, 2, 3, 4, 6]

print(f"First sequence: target found at index {find_index(target, first_sequence)}")
print(f"Second sequence: target found at index {find_index(target, second_sequence)}")

# Assignment
# Write a function that compares two tuples lexicographically. Examine
# corresponding elements from left to right and decide as soon as they differ;
# if all shared positions match, the shorter tuple comes first. Demonstrate the
# function with numeric tuples.
#
# Solution

# Return at the first differing pair; only compare lengths when all shared items match.
def is_tuple_less(first_tuple: tuple, second_tuple: tuple) -> bool:

    for i in range(min(len(first_tuple), len(second_tuple))):
        if first_tuple[i] < second_tuple[i]:
            return True
        if first_tuple[i] > second_tuple[i]:
            return False
    return len(first_tuple) < len(second_tuple)

print(is_tuple_less((3, 4, 28, 9), (4, 9, 9, 5)))

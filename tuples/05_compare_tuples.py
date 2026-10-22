# Assignment
# Write a function that compares two tuples lexicographically. Examine
# corresponding elements from left to right and decide as soon as they differ;
# if all shared positions match, the shorter tuple comes first. Demonstrate the
# function with numeric tuples.
#
# Solution

# Lexicographic order compares corresponding positions from left to right,
# like words in a dictionary. The first unequal pair decides which tuple is less.
# This exercise assumes the elements have a consistent less/equal/greater
# ordering, as the integers below do. The hints document tuple inputs and a
# Boolean result; they do not check the types of the elements.
def is_tuple_less(first_tuple: tuple, second_tuple: tuple) -> bool:

    # min selects the shorter length, so every index from range is valid in
    # both tuples. Compare these shared positions before considering lengths.
    # If either tuple is empty, there are no shared positions and no iterations.
    for i in range(min(len(first_tuple), len(second_tuple))):
        # If the first value is smaller at this position, the first tuple comes
        # first. return True ends the call immediately: later positions cannot
        # change a decision made at the first differing pair.
        if first_tuple[i] < second_tuple[i]:
            return True

        # If the first value is larger, the first tuple comes after the second,
        # so return False. Otherwise the values at this position are equal
        # under the assumed ordering, and the loop advances to the next pair.
        if first_tuple[i] > second_tuple[i]:
            return False

    # Reaching this line means all shared positions matched. The shorter tuple
    # comes first: e.g. (3, 4) is less than (3, 4, 5). Equal lengths now mean
    # equal tuples, for which the strict comparison returns False.
    # The same rule makes () less than a non-empty tuple and () < () False.
    return len(first_tuple) < len(second_tuple)

# The first comparison is 3 < 4, so the function returns True immediately.
# print displays that returned Boolean after the function call finishes.
print(is_tuple_less((3, 4, 28, 9), (4, 9, 9, 5)))

# Assignment
# Write a recursive function that returns a new list with the same elements as
# the input, in reverse order. Do not modify the original list. Demonstrate on a
# short sample list.
#
# Solution

# collection is the suffix not yet placed into the reversed result. Each call
# takes the last element of the current suffix and prepends the reversal of
# everything before it. collection[:-1] removes one element from the end, so
# recursion eventually reaches an empty list.
def recursive_revert(collection: list) -> list:

    # Base case: reversing an empty list yields a new empty list.
    if len(collection) == 0:
        return []
    else:
        # [collection[-1]] is a one-element list; + concatenates lists in order.
        return [collection[-1]] + recursive_revert(collection[:-1])


collection = [1, 2, 3, 4, 5]

# The original list is unchanged; the function returns a new reversed list.
print(f"recursive_revert({collection}) = {recursive_revert(collection)}")

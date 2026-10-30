# Assignment
# Write a recursive function that returns the sum of all integers in a list.
# Use an empty list as the base case. Demonstrate on a short sample list.
#
# Solution

# collection is the list suffix still to be summed. Each call either sees an
# empty list (nothing left to add) or adds the first element to the sum of the
# rest. Slicing collection[1:] shortens the list by one item toward the base case.
def recursive_list_sum(collection: list) -> int:

    # Base case: the sum of no elements is 0.
    if len(collection) == 0:
        return 0
    else:
        # Head plus recursive sum of the tail; the tail shrinks until it is empty.
        return collection[0] + recursive_list_sum(collection[1:])


collection = [1, 2, 3, 4, 5]

# 1 + 2 + 3 + 4 + 5 is 15.
print(f"recursive_list_sum({collection}) = {recursive_list_sum(collection)}")

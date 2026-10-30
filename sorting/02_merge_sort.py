# Assignment
# Implement merge sort for a list of floating-point values. Split the list in
# half recursively, sort each half, then merge the two sorted halves. Time the
# sort on the same reproducible random sample size as the selection-sort
# exercise and report elapsed time without printing every value.
#
# Solution

from random import random, seed
from time import perf_counter

SEED = 21
SAMPLE_SIZE = 1000

seed(SEED)


# collection is split in half until trivial pieces are merged back in order.
# Unlike selection sort, merge sort builds new lists during merging rather than
# sorting entirely in place.
def merge_sort(collection: list[float]) -> list[float]:

    # Base case: zero or one element is already sorted; return a new list slice.
    if len(collection) <= 1:
        return collection
    else:
        mid = len(collection) // 2
        # Slices create smaller subproblems; each half is sorted before merging.
        left = merge_sort(collection[:mid])
        right = merge_sort(collection[mid:])

    return merge(left, right)


def merge(left: list[float], right: list[float]) -> list[float]:
    # merged holds the combined sorted output; i and j index the two inputs.
    merged: list[float] = []
    i = 0
    j = 0

    # Take the smaller front element from either list until one list is exhausted.
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # At most one of these extends adds remaining elements; the other adds nothing.
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


collection = [random() for _ in range(SAMPLE_SIZE)]

start = perf_counter()
sorted_collection = merge_sort(collection)
elapsed = perf_counter() - start

is_sorted = all(
    sorted_collection[i] <= sorted_collection[i + 1]
    for i in range(len(sorted_collection) - 1)
)

print(f"Sample size: {len(sorted_collection)}")
print(f"Sorted ascending: {is_sorted}")
print(f"Elapsed time: {elapsed:.6f} s")

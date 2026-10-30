# Assignment
# Implement selection sort for a list of floating-point values. Each pass places
# the smallest remaining element at the front of the unsorted suffix. Time the
# sort on a reproducible random sample and report how long it took without
# printing every sorted value.
#
# Solution

from random import random, seed
from time import perf_counter

# Fixed seed so repeated runs use the same pseudo-random sequence.
SEED = 21
SAMPLE_SIZE = 1000

seed(SEED)


# collection is sorted in place by repeatedly swapping the minimum of the
# suffix into position i. Returns the same list object after sorting.
def selection_sort(collection: list[float]) -> list[float]:

    if len(collection) == 0:
        return []

    # i marks the start of the unsorted suffix; everything before i is final.
    for i in range(len(collection)):
        min_index = i

        # Scan the suffix for a value smaller than the current minimum.
        for j in range(i + 1, len(collection)):
            if collection[j] < collection[min_index]:
                min_index = j

        # Swap the smallest suffix element into position i.
        collection[i], collection[min_index] = (
            collection[min_index],
            collection[i],
        )

    return collection


collection = [random() for _ in range(SAMPLE_SIZE)]

start = perf_counter()
selection_sort(collection)
elapsed = perf_counter() - start

# Confirm order without dumping all SAMPLE_SIZE values to the terminal.
is_sorted = all(
    collection[i] <= collection[i + 1] for i in range(len(collection) - 1)
)

print(f"Sample size: {len(collection)}")
print(f"Sorted ascending: {is_sorted}")
print(f"Elapsed time: {elapsed:.6f} s")

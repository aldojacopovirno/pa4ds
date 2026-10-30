# Assignment
# Implement iterative binary search on a sorted list of floating-point values.
# Return the index of the target if it is present; otherwise return `-1`. Build a
# sorted random sample, search for a value known to be in the list, and report
# the index and search time.
#
# Solution

from random import random, seed
from time import perf_counter

SEED = 21
SAMPLE_SIZE = 1000

seed(SEED)


# collection must be sorted in ascending order before calling this function.
# left and right bound the active search interval; each step halves the interval
# by comparing element to the middle value.
def binary_search(collection: list[float], element: float) -> int:
    left = 0
    right = len(collection) - 1

    while left <= right:
        mid = (left + right) // 2

        if collection[mid] == element:
            return mid
        elif element < collection[mid]:
            # Target lies in the left half, excluding mid.
            right = mid - 1
        else:
            # Target lies in the right half, excluding mid.
            left = mid + 1

    return -1


collection = [random() for _ in range(SAMPLE_SIZE)]
collection.sort()

# Pick a value guaranteed to exist so the demo shows a successful search.
element = collection[SAMPLE_SIZE // 2]

start = perf_counter()
index = binary_search(collection, element)
elapsed = perf_counter() - start

print(f"Index: {index}")
print(f"Value at index matches target: {collection[index] == element}")
print(f"Elapsed time: {elapsed:.9f} s")

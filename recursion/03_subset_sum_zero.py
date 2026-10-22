# Assignment
# Given a list of integers, recursively search for a non-empty subset whose
# values add to zero. Return one such subset if it exists; otherwise report that
# there is no solution. Do not treat the empty subset as a solution.
#
# Solution

# Each call branches into including or skipping the current value.
def subset_sum(numbers, index, selected, total):

    if len(selected) > 0 and total == 0:
        return selected
    if index == len(numbers):
        return None

    result = subset_sum(numbers, index + 1,
                        selected + [numbers[index]], total + numbers[index])
    if result is not None:
        return result

    return subset_sum(numbers, index + 1, selected, total)

numbers = [1, 4, -3, -5, 7]
result = subset_sum(numbers, 0, [], 0)
if result is None:
    print('No solution.')
else:
    print(result)

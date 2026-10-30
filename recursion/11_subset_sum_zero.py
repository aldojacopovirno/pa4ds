# Assignment
# Given a list of integers, recursively search for a non-empty subset whose
# values add to zero. Return one such subset if it exists; otherwise report that
# there is no solution. Do not treat the empty subset as a solution.
#
# Solution

# Each call decides whether to use one more value. Keep the search state in
# the parameters: numbers holds the candidates, index is the next undecided
# position, selected holds the values chosen so far, and total is their sum.
# The starting call below supplies a consistent state: index 0, no choices,
# and a total of 0.
def subset_sum(numbers, index, selected, total):

    # Both conditions must be True: the chosen values must be non-empty and
    # their sum must be zero. This prevents the initial empty selection from
    # being accepted just because its total is already 0.
    # Return immediately when successful, even if more candidates remain.
    # Check success before exhaustion so a solution using the last value counts.
    if len(selected) > 0 and total == 0:
        return selected

    # Reaching the end without passing the success check means this branch
    # failed. There is no next value to choose, so return None before indexing
    # numbers[index], which would be outside the list here.
    if index == len(numbers):
        return None

    # A nonzero partial sum can still reach zero: later candidates may be
    # positive or negative. Continue exploring when neither base case applies.
    # First try including the current value. Move to index + 1 because its
    # inclusion has now been decided, and add it to both selected and total.
    # + creates a new list, keeping this call's selection available unchanged
    # if we need to try the other choice later.
    # This call waits for the deeper search to return a solution list or None.
    result = subset_sum(numbers, index + 1,
                        selected + [numbers[index]], total + numbers[index])

    # Pass a found solution back through the waiting calls. Returning here
    # ends this call, so a successful include branch needs no further search.
    if result is not None:
        return result

    # If including the value failed, try skipping it. Advance the index while
    # keeping selected and total unchanged; all deeper additions still create
    # new lists. Return this branch's result, whether it is a solution or None.
    # Both branches increase index by one, reducing the undecided part until
    # a base case is reached. Trying both choices covers every possible subset
    # when no earlier solution has already ended the search.
    return subset_sum(numbers, index + 1, selected, total)

# Start before the first value, with an empty selection and its sum of zero.
# The include-first search finds [1, 4, -5], whose values sum to zero. Returning
# at the first success gives one solution and leaves the remaining choices unexplored.
numbers = [1, 4, -3, -5, 7]
result = subset_sum(numbers, 0, [], 0)

# Use the failure marker to choose the output: None means every branch failed;
# otherwise result contains the chosen values and can be printed as a list.
if result is None:
    print('No solution.')
else:
    print(result)

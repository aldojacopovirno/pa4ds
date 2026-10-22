# Assignment
# Search the supplied tuple for a target value and print its index. If the value
# is absent, report that fact without trying to access an invalid tuple
# position.
#
# Solution

# A tuple can hold different types together: these items include strings and
# integers. Each item has a zero-based index, regardless of its type.
pizzas = ('margherita', 5, 6, 'marinara', 4)

# Search for the integer 6; a string such as '6' would be a different value.
target = 6

# in gives a Boolean: True if an item equals target, and False if none does.
# Search by index only when this check guarantees that a match exists.
if target in pizzas:
    # Begin with index 0 so we examine items in order from the start.
    i = 0

    # Keep searching while the current item differs from the target. As soon as
    # they are equal, the condition becomes False and i is the first match's index.
    while pizzas[i] != target:
        # Advance to the next item after each mismatch. The membership check
        # guarantees a match before the end, so this search stays within bounds.
        i += 1

    # Print after the loop because i now identifies the target. The reported
    # index starts at 0, so index 2 refers to the tuple's third item.
    print(f'The index of number {target} is {i}.')

else:
    # A missing target enters this branch and never starts the indexed search.
    print(f'Number {target} is not in the tuple.')

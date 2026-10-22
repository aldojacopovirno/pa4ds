# Assignment
# Start with the tuple `("a", 2, "c", 4, "e")` and remove the value 2. Since
# tuples are immutable, create a new tuple from the parts before and after the
# removed item, then display it.
#
# Solution

# Tuples are immutable: we cannot delete an item inside an existing tuple.
# We will build a new tuple from the items that should remain instead.
items = ("a", 2, "c", 4, "e")
item_to_remove = 2

# Membership produces a Boolean. Only look up the index when the value exists,
# because index() would raise ValueError if the value were missing.
if item_to_remove in items:
    # index() returns the first matching index, so repeated values would have
    # only their first occurrence removed by the slices below.
    item_index = items.index(item_to_remove)

    # [:item_index] keeps the items before the match: a slice excludes its end.
    # [item_index + 1:] starts after the match and continues to the end.
    # + joins these slices into a new tuple, leaving out the matched item.
    # Reassigning items makes the name refer to that new tuple; it does not
    # change the original tuple. Removing the first or last item is safe too:
    # the corresponding slice is simply an empty tuple.
    items = items[:item_index] + items[item_index + 1:]

# Display the replacement, or the unchanged tuple if the value was absent and
# the if block was skipped.
print(items)

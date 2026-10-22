# Assignment
# Start with the tuple `("a", 2, "c", 4, "e")` and remove the value 2. Since
# tuples are immutable, create a new tuple from the parts before and after the
# removed item, then display it.
#
# Solution

# Slicing around the target creates a replacement tuple.
items = ("a", 2, "c", 4, "e")
item_to_remove = 2

if item_to_remove in items:
    item_index = items.index(item_to_remove)
    # Tuples cannot be changed in place, so join the slices around the item.
    items = items[:item_index] + items[item_index + 1:]

print(items)

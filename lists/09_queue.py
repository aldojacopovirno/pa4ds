# Assignment
# Implement a first-in, first-out queue using a list. Let the user add an item,
# remove the oldest item with `?`, or finish with Enter. If a removal is
# requested while the queue is empty, print a helpful message instead of
# failing.
#
# Solution

# Appending adds at the back; pop at index zero removes the oldest item.
queue = []

while True:
    item = input("Item, ? to remove the first item, Enter to quit: ")

    if item == "":
        break
    if item == "?":
        if len(queue) == 0:
            print("The queue is empty.")
        else:
            print(f"Removed: {queue.pop(0)}")
    else:
        queue.append(item)

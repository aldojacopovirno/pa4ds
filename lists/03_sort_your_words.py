# Assignment
# Read strings from the user until an empty line is entered. Store each
# non-empty string, sort the collected values alphabetically, and print them one
# per line. Pressing Enter on an empty line should finish input without adding
# an empty item.
#
# Solution

# An empty line is a sentinel that ends input without entering the list.
items = []

while True:
    item = input("Type something (press Enter to finish): ")
    if item == "":
        break
    items.append(item)

for item in sorted(items):
    print(item)

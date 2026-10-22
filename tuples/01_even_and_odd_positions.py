# Assignment
# Read a line of text and convert it to a tuple of characters. Print the
# characters at zero-based even indices first, then print those at odd indices.
# Preserve the order within each group.
#
# Solution

# Modulo two separates zero-based even indexes from odd indexes.
text = input('Type something:')

characters_tuple = tuple(text)

print('==== Characters at Even Indices ====')

for i in range(len(characters_tuple)):

    if i % 2 == 0:
        print(characters_tuple[i])

print('==== Characters at Odd Indices ====')

for i in range(len(characters_tuple)):

    if i % 2 != 0:
        print(characters_tuple[i])

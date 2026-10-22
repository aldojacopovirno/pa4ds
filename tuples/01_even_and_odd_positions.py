# Assignment
# Read a line of text and convert it to a tuple of characters. Print the
# characters at zero-based even indices first, then print those at odd indices.
# Preserve the order within each group.
#
# Solution

# Keep the answer as text: we need to inspect each character in its input order.
text = input('Type something:')

# tuple(text) places each character in a separate position, preserving its order.
# A tuple is immutable, but we can still read its characters using their indices.
characters_tuple = tuple(text)

# Even and odd describe the indices, not the characters stored at those indices.
print('==== Characters at Even Indices ====')

# Python indices start at 0. range stops before its end, so these indices run
# from 0 to len(characters_tuple) - 1 without going beyond the tuple.
# With empty input, the length is 0 and this loop runs zero times.
for i in range(len(characters_tuple)):
    # % gives the remainder after division. An index with remainder 0 when
    # divided by 2 is even, so == creates the Boolean condition for this group.
    if i % 2 == 0:
        # Read the character at the accepted index. Increasing i preserves the
        # original order of the characters within the even-index group.
        print(characters_tuple[i])

print('==== Characters at Odd Indices ====')

# Scan the indices again so all even-index characters appear before any odd-index
# characters. This second loop also keeps the original order within its group.
for i in range(len(characters_tuple)):
    # != produces True when the remainder differs from 0, selecting odd indices.
    # Even indices produce False and skip the indented print statement.
    if i % 2 != 0:
        print(characters_tuple[i])

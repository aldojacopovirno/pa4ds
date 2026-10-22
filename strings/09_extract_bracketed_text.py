# Assignment
# Given a string containing square-bracket pairs, locate each opening bracket
# and its matching closing bracket, then print the text between them. Continue
# searching after each closing bracket and stop safely if no further complete
# pair exists.
#
# Solution

# Scan separate, non-nested bracket pairs by taking the first closing bracket
# after each opening bracket. Start searching at index 0 to include all the text.
text = "The [quick] brown [fox] jumps."
start = 0

# The number of pairs is not known in advance. Repeat until a search reports
# that no further complete pair exists, then use break to leave the loop.
while True:
    # find searches from start, including that position, and returns the index
    # in the full string. It returns -1 when no opening bracket is found.
    opening_index = text.find("[", start)
    # Stop before treating the "not found" marker as a bracket position.
    if opening_index == -1:
        break

    # Begin just after the opening bracket to look for the end of this pair.
    # If no closing bracket follows, stop: this opening bracket has no complete
    # pair to extract, so it should not produce a partial result.
    closing_index = text.find("]", opening_index + 1)
    if closing_index == -1:
        break

    # A slice includes its start and excludes its end. Start one character after
    # [ and end at ], so only the enclosed text is printed: quick, then fox here.
    # Empty brackets [] give an empty slice, which print displays as a blank line.
    print(text[opening_index + 1:closing_index])

    # Move past the closing bracket before repeating. start strictly increases,
    # so each pair is handled once and this finite string is eventually exhausted.
    start = closing_index + 1

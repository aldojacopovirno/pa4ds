# Assignment
# Compare two strings character by character. Whenever the same character occurs
# at the same zero-based index in both strings, print that character and index.
# Stop safely at the end of the shorter string; use `The Holy Grail` and `Life
# of Brian` as an example.
#
# Solution

# Keep the spaces and letter case: each character contributes a position,
# and uppercase and lowercase versions count as different characters.
first_text = 'The Holy Grail'
second_text = 'Life of Brian'

# range produces every valid index of first_text, starting at 0. The for loop
# visits all of those indices, even if second_text has already ended.
for i in range(len(first_text)):
    # First check that i is also valid in second_text. and evaluates its second
    # condition only when the first is True, so an index past the end never
    # reaches second_text[i]. This is called short-circuit evaluation.
    # Then compare characters at the same index; a match at another position
    # does not count. and requires both conditions to be True before printing.
    if i < len(second_text) and first_text[i] == second_text[i]:
        # Report each match immediately. A space can also match because it is
        # a character in both strings, just like a letter.
        print(f'The character {first_text[i]} is in both strings at index {i}.')

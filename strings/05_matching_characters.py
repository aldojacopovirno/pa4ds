# Assignment
# Compare two strings character by character. Whenever the same character occurs
# at the same zero-based index in both strings, print that character and index.
# Stop safely at the end of the shorter string; use `The Holy Grail` and `Life
# of Brian` as an example.
#
# Solution

# The shorter length is the stopping point that keeps both indexes valid.
first_text = 'The Holy Grail'
second_text = 'Life of Brian'

for i in range(len(first_text)):

    if i < len(second_text) and first_text[i] == second_text[i]:
        print(f'The character {first_text[i]} is in both strings at index {i}.')

# Assignment
# Solve the previous word-frequency problem again, but read woodchuck_twister.txt
# one line at a time instead of loading it all at once. The result must be the
# same: each distinct word and its frequency, sorted alphabetically.
#
# Solution

from pathlib import Path

FILENAME = Path(__file__).parent / 'woodchuck_twister.txt'

word_counts: dict[str, int] = {}

with open(FILENAME) as file:
    while True:
        line = file.readline()

        # Only one line is in memory at a time; an empty string ends the file.
        if line == '':
            break

        # Clean each line separately: a word never continues onto the next line here.
        cleaned_line = ''
        for character in line.lower():
            if character.isalpha():
                cleaned_line += character
            else:
                cleaned_line += ' '

        # The dictionary keeps the totals across all the lines read so far.
        for word in cleaned_line.split():
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

for word in sorted(word_counts):
    print(f"{word}, {word_counts[word]}")

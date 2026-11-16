# Assignment
# Read at most the first five lines of nonsense_verse.txt and count how many of
# them contain the word "zorbly", ignoring letter case. Stop earlier if the file
# has fewer than five lines, and print the count with a clear label.
#
# Solution

from pathlib import Path

FILENAME = Path(__file__).parent / 'nonsense_verse.txt'
SEARCH_WORD = 'zorbly'
MAX_LINES = 5

lines_read = 0
matching_lines = 0

with open(FILENAME) as file:
    # Each pass reads one line, so lines_read moves toward MAX_LINES.
    while lines_read < MAX_LINES:
        # Lowercase the line so "Zorbly" and "zorbly" are the same word.
        line = file.readline().lower()

        # An empty string means the file ended before MAX_LINES lines were read.
        if line == '':
            break

        # Count the line once, even if the word occurs several times in it.
        if SEARCH_WORD in line:
            matching_lines += 1
        lines_read += 1

print(f"Lines containing '{SEARCH_WORD}' in the first {lines_read} lines: {matching_lines}")

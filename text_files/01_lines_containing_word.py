# Assignment
# Read the text file rose_speech.txt line by line and display every line that
# contains the word "name". Print each line as it appears in the file, without
# adding extra blank lines.
#
# Solution

from pathlib import Path

# Build the path from the script's own folder, so the exercise works when it is
# run from the repository root. The file is an auxiliary file stored beside it.
FILENAME = Path(__file__).parent / 'rose_speech.txt'
SEARCH_WORD = 'name'

# with closes the file automatically, even if an error occurs.
with open(FILENAME) as file:
    while True:
        # readline returns one line, including its newline character.
        # At the end of the file it returns an empty string.
        line = file.readline()

        # An empty string is the stopping condition: no lines are left.
        if line == '':
            break

        if SEARCH_WORD in line:
            # The line already ends with a newline, so print must not add another.
            print(line, end='')

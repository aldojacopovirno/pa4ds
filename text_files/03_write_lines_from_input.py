# Assignment
# Ask the user for lines of text until an empty line is entered. Write each
# line to the file typed_lines.tmp, then read the whole file back and display
# its content.
#
# Solution

from pathlib import Path

FILENAME = Path(__file__).parent / 'typed_lines.tmp'

# Mode "w" creates the file, or empties it if it already exists.
with open(FILENAME, 'w') as file:
    while True:
        text = input("Please enter a line of text (empty line to stop): ")

        # The empty line is the stopping condition for the loop.
        if text == '':
            break

        # input removes the newline, so we write it back to keep one line per entry.
        file.write(text + '\n')

# Reopen the file for reading: the content is now complete on disk.
with open(FILENAME) as file:
    content = file.read()

print("File content:")
print(content)

# Assignment
# Copy the content of rose_speech.txt into a new file called rose_copy.tmp, then
# open the new file, read it, and display its content to confirm the copy.
#
# Solution

from pathlib import Path

FOLDER = Path(__file__).parent
SOURCE_FILENAME = FOLDER / 'rose_speech.txt'
COPY_FILENAME = FOLDER / 'rose_copy.tmp'

with open(SOURCE_FILENAME) as source_file:
    with open(COPY_FILENAME, 'w') as copy_file:
        # readlines returns a list of lines, each one with its newline character.
        lines = source_file.readlines()
        # writelines writes every item of the list as it is, so nothing is added.
        copy_file.writelines(lines)

# Read the copy, not the original, to check what was really written.
with open(COPY_FILENAME) as copy_file:
    print(copy_file.read())

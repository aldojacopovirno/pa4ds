# Assignment
# Read rose_speech.txt and write a new file, rose_reversed.tmp, in which the
# characters of each line are in reverse order. The lines keep their original
# order. Then read the new file and display it.
#
# Solution

from pathlib import Path

FOLDER = Path(__file__).parent
SOURCE_FILENAME = FOLDER / 'rose_speech.txt'
REVERSED_FILENAME = FOLDER / 'rose_reversed.tmp'

with open(SOURCE_FILENAME) as source_file:
    with open(REVERSED_FILENAME, 'w') as reversed_file:
        for line in source_file:
            # Remove the newline first: reversed, it would start the line instead.
            text = line.rstrip('\n')

            # The slice [::-1] walks the string backwards, from the last character.
            reversed_file.write(text[::-1] + '\n')

with open(REVERSED_FILENAME) as reversed_file:
    print(reversed_file.read())

# Assignment
# Read woodchuck_twister.txt line by line and write a copy, woodchuck_no_vowels.tmp,
# from which every vowel (uppercase or lowercase) has been removed. Print how
# many characters were read and written, then display the new file.
#
# Solution

from pathlib import Path

FOLDER = Path(__file__).parent
SOURCE_FILENAME = FOLDER / 'woodchuck_twister.txt'
OUTPUT_FILENAME = FOLDER / 'woodchuck_no_vowels.tmp'
VOWELS = 'aeiouAEIOU'

# maketrans with a third argument builds a table that deletes those characters.
table = str.maketrans('', '', VOWELS)

characters_read = 0
characters_written = 0

with open(SOURCE_FILENAME) as source_file:
    with open(OUTPUT_FILENAME, 'w') as output_file:
        while True:
            line = source_file.readline()
            if line == '':
                break

            # translate applies the table: vowels disappear, all else is unchanged.
            new_line = line.translate(table)
            output_file.write(new_line)

            # Newlines are counted too, because they are characters of the file.
            characters_read += len(line)
            characters_written += len(new_line)

print(f"Characters read: {characters_read}")
print(f"Characters written: {characters_written}")

with open(OUTPUT_FILENAME) as output_file:
    print(output_file.read())

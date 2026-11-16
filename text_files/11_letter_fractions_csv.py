# Assignment
# For each of the files rose_speech.txt, nonsense_verse.txt and woodchuck_twister.txt,
# compute the fraction of letters a-z that each letter represents, ignoring
# letter case and every other character. Write a CSV file letter_fractions.csv
# with one row per letter: the quoted letter followed by its three fractions
# with five decimals. Then display the CSV file.
#
# Solution

from pathlib import Path

FOLDER = Path(__file__).parent
FILENAMES = [
    FOLDER / 'rose_speech.txt',
    FOLDER / 'nonsense_verse.txt',
    FOLDER / 'woodchuck_twister.txt',
]
OUTPUT_FILENAME = FOLDER / 'letter_fractions.csv'


def count_letters(filename: Path) -> tuple[dict[str, int], int]:
    """Return how many times each letter a-z occurs and the total of those letters."""
    # Every letter starts at zero, so letters absent from the file still get a row.
    letter_counts = {chr(code): 0 for code in range(ord('a'), ord('z') + 1)}
    total_letters = 0

    with open(filename) as file:
        for character in file.read().lower():
            # Digits, spaces and punctuation are not keys, so they are skipped.
            if character in letter_counts:
                letter_counts[character] += 1
                total_letters += 1

    return letter_counts, total_letters


def write_csv(counts_list: list[dict[str, int]], totals_list: list[int], filename: Path) -> None:
    """Write one row per letter: "letter",fraction_file_1,fraction_file_2,..."""
    with open(filename, 'w') as csv_file:
        for letter in sorted(counts_list[0]):
            fractions = []
            for i in range(len(counts_list)):
                # A file without letters would divide by zero, so use 0 instead.
                if totals_list[i] > 0:
                    fraction = counts_list[i][letter] / totals_list[i]
                else:
                    fraction = 0
                fractions.append(f"{fraction:.5f}")
            csv_file.write(f'"{letter}",' + ','.join(fractions) + '\n')


counts_list: list[dict[str, int]] = []
totals_list: list[int] = []

for filename in FILENAMES:
    letter_counts, total_letters = count_letters(filename)
    counts_list.append(letter_counts)
    totals_list.append(total_letters)

write_csv(counts_list, totals_list, OUTPUT_FILENAME)

with open(OUTPUT_FILENAME) as csv_file:
    print(csv_file.read())

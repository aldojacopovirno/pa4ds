# Assignment
# Find the words that appear in all three files rose_speech.txt, nonsense_verse.txt
# and woodchuck_twister.txt. Ignore letter case and words shorter than two
# letters. Print the common words in alphabetical order and how many there are.
#
# Solution

from pathlib import Path

FOLDER = Path(__file__).parent
FILENAMES = [
    FOLDER / 'rose_speech.txt',
    FOLDER / 'nonsense_verse.txt',
    FOLDER / 'woodchuck_twister.txt',
]
MIN_WORD_LENGTH = 2


def get_words(filename: Path) -> set[str]:
    """Return the set of distinct lowercase words of at least two letters."""
    words = set()
    current_word = ''

    with open(filename) as file:
        for character in file.read().lower():
            if character.isalpha():
                # The word is still going on: keep adding letters.
                current_word += character
            else:
                # A non-letter ends the word; short words are discarded.
                if len(current_word) >= MIN_WORD_LENGTH:
                    words.add(current_word)
                current_word = ''

    # The file may end with a letter, so the last word is still waiting.
    if len(current_word) >= MIN_WORD_LENGTH:
        words.add(current_word)

    return words


# Start from the first file's words, then keep only those found in each other file.
common_words = get_words(FILENAMES[0])
for filename in FILENAMES[1:]:
    # & is the set intersection: elements that belong to both sets.
    common_words = common_words & get_words(filename)

print("Common words:", sorted(common_words))
print("Number of common words:", len(common_words))

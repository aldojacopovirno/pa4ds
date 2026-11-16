# Assignment
# Read the whole of woodchuck_twister.txt at once and count the occurrences of
# each word, ignoring letter case and treating every non-letter character as a
# separator. Print each distinct word and its frequency, sorted alphabetically.
#
# Solution

from pathlib import Path

FILENAME = Path(__file__).parent / 'woodchuck_twister.txt'

# read returns the entire file as a single string.
with open(FILENAME) as file:
    text = file.read().lower()

# Replace every non-letter with a space, so "chuck," and "chuck" become the same word.
cleaned_text = ''
for character in text:
    if character.isalpha():
        cleaned_text += character
    else:
        cleaned_text += ' '

# split() without arguments ignores runs of spaces and never returns empty words.
words = cleaned_text.split()

word_counts: dict[str, int] = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word in sorted(word_counts):
    print(f"{word}, {word_counts[word]}")

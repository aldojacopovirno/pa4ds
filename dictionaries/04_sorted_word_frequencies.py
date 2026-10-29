# Assignment
# Count the occurrences of each word in a text passage, ignoring letter case and
# replacing all punctuation and non-alphabetic characters with spaces. Print each
# distinct word and its frequency, sorted alphabetically by word.
#
# Solution

# A sample text passage containing punctuation and varied letter casing.
text = (
    'How much wood would a woodchuck chuck If a woodchuck could chuck wood? He would '
    'chuck, he would, as much as he could, And chuck as much as a woodchuck would If a '
    'woodchuck could chuck wood.'
)

# Convert all characters to lowercase so word matching is case-insensitive.
text = text.lower()

# Build a translation mapping that replaces every non-alphabetic character with a space.
replacements: dict[str, str] = {}
for character in text:
    if not character.isalpha():
        replacements[character] = ' '

# str.maketrans creates a translation table from the character mapping dictionary.
translation_table = str.maketrans(replacements)
cleaned_text = text.translate(translation_table)

# A dictionary to accumulate word frequencies.
word_counts: dict[str, int] = {}

# split() without arguments splits by runs of whitespace, ignoring empty strings.
for word in cleaned_text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Extract keys and sort them alphabetically.
sorted_words = sorted(word_counts.keys())

# Display each word with its corresponding occurrence count.
for word in sorted_words:
    print(f"{word}, {word_counts[word]}")

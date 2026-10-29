# Assignment
# Count the frequency of each word in a given list of strings using a
# dictionary. Each unique word serves as a key mapped to its occurrence count.
# Display the resulting dictionary of word counts.
#
# Solution

# A sample list of fruit names with repeating items to count.
words = [
    'apple', 'cherry', 'mango', 'apple', 'apple', 'durian', 'apple', 'apple',
    'banana', 'durian', 'apple', 'apple', 'apple', 'apple', 'banana', 'apple',
    'cherry', 'durian', 'apple', 'banana', 'apple',
]

# A dictionary maps unique keys to values; here, each word maps to its count.
word_counts: dict[str, int] = {}

# Iterate over each word in the list to update its frequency.
for word in words:
    # in checks whether the word already exists as a key in the dictionary.
    if word in word_counts:
        # Increment the existing count by 1 for recurring words.
        word_counts[word] += 1
    else:
        # The first time a word appears, initialize its count to 1.
        word_counts[word] = 1

# Display the dictionary of counted frequencies.
print(word_counts)

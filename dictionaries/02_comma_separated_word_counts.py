# Assignment
# Count the occurrences of each word in a comma-separated string. Strip leading
# and trailing whitespace from each item before counting so that extra spaces do
# not create distinct keys. Store the counts in a dictionary and display it.
#
# Solution

# A sample comma-separated string with inconsistent spacing around words.
text = (
    'apple ,durian ,banana ,durian ,apple ,cherry ,cherry ,mango, apple ,apple ,cherry '
    ',durian ,banana ,apple ,apple ,apple , apple ,banana ,apple'
)

# A dictionary maps unique keys to values; here each word maps to its count.
word_counts: dict[str, int] = {}

# split(',') partitions the string at each comma into individual word tokens.
for raw_word in text.split(','):
    # strip() removes leading and trailing whitespace to standardize keys.
    word = raw_word.strip()

    # Check if the cleaned word has already been observed in the dictionary.
    if word in word_counts:
        # Increment the existing count by 1 for recurring words.
        word_counts[word] += 1
    else:
        # The first time a word appears, initialize its count to 1.
        word_counts[word] = 1

# Display the dictionary of counted frequencies.
print(word_counts)

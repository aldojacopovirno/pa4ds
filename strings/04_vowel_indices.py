# Assignment
# Read a line of text and print the index of each vowel it contains. Treat
# uppercase and lowercase vowels alike, but report the original zero-based index
# in the string for every occurrence.
#
# Solution

# Convert the answer to lowercase so one set of vowels can match both cases.
# The indices below refer to this converted string. They match the original
# indices for ASCII text; some Unicode lowercase conversions add characters.
text = input('Type something:').lower()

# Use in to check whether a character is one of these five English vowels.
vowels = 'aeiou'

# Start at zero because Python numbers the first character with index 0.
i = 0

# Check the length before reading text[i]: the last valid index is len(text) - 1.
# An empty answer has length 0, so the condition is False on the first check
# and the loop runs zero times.
while i < len(text):
    # Membership produces a Boolean: True for a vowel and False otherwise.
    # Only vowels enter this block; consonants, spaces, and punctuation skip it.
    if text[i] in vowels:
        # upper() changes the displayed vowel without changing text or i.
        # Print inside the loop so every occurrence gets its own index.
        print(f'The vowel {text[i].upper()} has {i} as index.')

    # Advance after every character, including a non-vowel. Keeping this step
    # outside the if ensures that the loop reaches the end instead of getting
    # stuck on the first character that is not a vowel.
    i += 1

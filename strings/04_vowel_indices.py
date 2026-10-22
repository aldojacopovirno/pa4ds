# Assignment
# Read a line of text and print the index of each vowel it contains. Treat
# uppercase and lowercase vowels alike, but report the original zero-based index
# in the string for every occurrence.
#
# Solution

# The index increases on every pass, including when the character is not a vowel.
text = input('Type something:').lower()
vowels = 'aeiou'
i = 0

while i < len(text):

    if text[i] in vowels:
        print(f'The vowel {text[i].upper()} has {i} as index.')

    i += 1

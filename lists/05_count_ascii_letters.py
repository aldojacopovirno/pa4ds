# Assignment
# Count how many times each lowercase English letter appears in a string. Ignore
# spaces, punctuation, and other non-letter characters. Use a 26-element list
# where position 0 counts `a`, position 1 counts `b`, and so on, then display
# the counts.
#
# Solution

# Subtracting the code for a maps each lowercase letter to index 0 through 25.
text = 'Hello World!'
text = text.lower()
letter_counts = [0] * 26

for character in text:

    if 'a' <= character <= 'z':
        index = ord(character) - ord('a')
        letter_counts[index] += 1

print(letter_counts)

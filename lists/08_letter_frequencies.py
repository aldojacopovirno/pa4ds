# Assignment
# Count the occurrences of lowercase English letters in a sample string,
# ignoring spaces and punctuation. Print only letters that occur, ordered from
# highest frequency to lowest frequency, with each count beside its letter.
#
# Solution

from string import ascii_lowercase

# Count each alphabet letter before sorting the non-zero results.
text = 'Hello World!'

text = text.lower()
letters = []

for letter in ascii_lowercase:
    count = 0
    for character in text:
        if letter == character:
            count += 1
    if count > 0:
        letters.append((count, letter))

letters.sort(reverse=True)

for count, letter in letters:
    print(letter, count)

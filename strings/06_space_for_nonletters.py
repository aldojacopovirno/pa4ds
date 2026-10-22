# Assignment
# Write a function that returns a new string with the same length as the input.
# Keep English letters unchanged and replace every other character, including
# digits and punctuation, with a space. Demonstrate it on `ph@t l00t`.
#
# Solution

# Append one output character per input character to preserve positions.
def only_letters(text: str) -> str:

    cleaned = ''

    for character in text:

        if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):
            cleaned += character

        else:
            cleaned += ' '

    return cleaned

print(only_letters("ph@t l00t"))

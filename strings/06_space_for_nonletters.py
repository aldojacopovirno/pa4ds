# Assignment
# Write a function that returns a new string with the same length as the input.
# Keep English letters unchanged and replace every other character, including
# digits and punctuation, with a space. Demonstrate it on `ph@t l00t`.
#
# Solution

# Put the cleaning steps in a function so they can be reused with other text.
# The str hints describe the expected argument and result; they do not convert
# values or check their types at runtime.
def only_letters(text: str) -> str:
    # Start with an empty result and build it in the same order as the input.
    cleaned = ''

    # Visit every input character from left to right. The loop ends after the
    # last character; with empty text it runs zero times.
    for character in text:
        # Each chained comparison checks a range of ASCII letters. or makes
        # the condition True for either lowercase a-z or uppercase A-Z.
        # Digits, punctuation, spaces, and accented letters fail both checks.
        if ('a' <= character <= 'z') or ('A' <= character <= 'Z'):
            # Keep an accepted letter with its original case. Strings cannot
            # be changed in place: += joins the text and stores a new string.
            cleaned += character

        else:
            # Replace the rejected character with exactly one space. Both
            # branches add one character, so positions and length are preserved.
            cleaned += ' '

    # Return after the full scan so the caller receives the complete result.
    # Empty input returns the initial empty string, which also has length 0.
    return cleaned


# Pass the sample to the function, then print the returned string. Here @ and
# each 0 become spaces, while the existing space remains a space.
print(only_letters("ph@t l00t"))

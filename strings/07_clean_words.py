# Assignment
# Write a function that lowercases a string and treats every non-letter as a
# word separator. Print each resulting word on its own line. For `I’m sorry,
# sir.`, the output should contain `i`, `m`, `sorry`, and `sir`.
#
# Solution

# Put the steps in a function so different sentences can use the same rules.
# -> None describes a function that prints its results; reaching the end
# implicitly returns None to the caller.
def print_cleaned_words(text: str) -> None:

    # Store a lowercase version so uppercase and lowercase letters can use
    # the same a-to-z check below.
    text = text.lower()

    # Start with an empty result and build the prepared text from left to right.
    cleaned = ''

    # Visit every character once. The loop ends after the last character.
    for character in text:

        # The chained comparison is True for lowercase English letters a to z.
        # Keep those letters in the result, preserving their order.
        if 'a' <= character <= 'z':
            cleaned += character

        else:
            # Treat every other character as a separator, including apostrophes
            # and accented letters outside a-z. For example, "I'm" becomes "i m",
            # preserving a boundary between the two pieces.
            cleaned += ' '

    # Process the completed text after the character loop. With no argument,
    # split() groups consecutive whitespace and returns only non-empty words.
    # Visit those words in order and print each on its own line.
    for word in cleaned.split():
        print(word)

# This call supplies the sentence as text. The apostrophe, comma, and full stop
# become separators, so the function prints i, m, sorry, and sir on separate lines.
print_cleaned_words("I'm sorry, sir.")

# Assignment
# Write a function that lowercases a string and treats every non-letter as a
# word separator. Print each resulting word on its own line. For `I’m sorry,
# sir.`, the output should contain `i`, `m`, `sorry`, and `sir`.
#
# Solution

# Replacing separators with spaces lets split collect only non-empty words.
def print_cleaned_words(text: str) -> None:

    text = text.lower()

    cleaned = ''

    for character in text:

        if 'a' <= character <= 'z':
            cleaned += character

        else:
            cleaned += ' '

    for word in cleaned.split():
        print(word)

print_cleaned_words("I'm sorry, sir.")

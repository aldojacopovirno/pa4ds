# Assignment
# Write a function that translates one English word by moving its first letter
# to the end and appending `ay`, e.g. `Python` becomes `ythonpay`.
# Accept letters only, handle uppercase input consistently, and report an empty
# or invalid word clearly.
#
# Solution

# Receive one word as a parameter so the same validation and translation can
# be reused. The str hints document a text argument and a text return value.
def pig_latin_converter(text: str) -> str:

    # Normalize the word to lowercase before checking it, so uppercase input
    # can use the same a-to-z rule and the translation has a consistent case.
    text = text.lower()

    # An empty string has no first character. Return a clear error message now,
    # before the later text[0] lookup could raise an indexing error.
    if text == '':
        return 'Invalid word'

    # Validate every character of the prepared word before constructing a result.
    # A valid word completes the loop; the first invalid character ends the call.
    for character in text:

        # The comparison checks the lowercase English range. not reverses it,
        # making this condition True for a space, digit, or other character.
        if not ('a' <= character <= 'z'):
            return 'Invalid word'

    # All characters have passed the check, and the word is non-empty.
    # [1:] takes everything after the first character; [0] retrieves that first
    # character. + joins the suffix, moved character, and 'ay' into a new string.
    # For "python", this builds "ython" + "p" + "ay", giving "ythonpay".
    # A one-letter word also works: its [1:] slice is simply empty.
    return text[1:] + text[0] + 'ay'

# Keep the input as text and pass it to the function. Insert the returned
# translation or error message into the f-string before displaying it.
text = input('Type an English word:')
print(f'Pig Latin translation: {pig_latin_converter(text)}')

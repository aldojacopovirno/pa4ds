# Assignment
# Write a function that translates one English word by moving its first letter
# to the end and appending `ay`, e.g. `Python` becomes `ythonpay`.
# Accept letters only, handle uppercase input consistently, and report an empty
# or invalid word clearly.
#
# Solution

# Validate every character before slicing the first letter to the end.
def pig_latin_converter(text: str) -> str:

    text = text.lower()
    if text == '':
        return 'Invalid word'

    for character in text:

        if not ('a' <= character <= 'z'):
            return 'Invalid word'

    return text[1:] + text[0] + 'ay'

text = input('Type an English word:')
print(f'Pig Latin translation: {pig_latin_converter(text)}')

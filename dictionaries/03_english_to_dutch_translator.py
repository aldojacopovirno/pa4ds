# Assignment
# Translate an English sentence into Dutch using a bilingual dictionary. Convert
# each word to lowercase before looking it up; if a word is absent from the
# dictionary, retain the original word unchanged. Combine the translated words
# into a single sentence and print the result.
#
# Solution

# A bilingual dictionary mapping lowercase English words to Dutch equivalents.
english_dutch: dict[str, str] = {
    'last': 'laatst',
    'week': 'week',
    'the': 'de',
    'royal': 'koninklijk',
    'festival': 'feest',
    'hall': 'hal',
    'saw': 'zaag',
    'first': 'eerst',
    'performance': 'optreden',
    'of': 'van',
    'a': 'een',
    'new': 'nieuw',
    'symphony': 'symphonie',
    'by': 'bij',
    'one': 'een',
    'world': 'wereld',
    'leading': 'leidend',
    'modern': 'modern',
    'composer': 'componist',
    'composers': 'componisten',
    'two': 'twee',
    'shed': 'schuur',
    'sheds': 'schuren',
}

# The sample English sentence to translate.
sentence = (
    "Last week The Royal Festival Hall saw the first performance of a new "
    "symphony by one of the world ' s leading modern composers , "
    'Arthur "Two-Sheds" Jackson .'
)

# Convert to lowercase so dictionary lookups match case-insensitively,
# and split at whitespace boundaries into a list of word tokens.
words = sentence.lower().split()
translated_words: list[str] = []

# Translate each word using the dictionary, keeping unmapped words as-is.
for word in words:
    # in checks key membership in english_dutch.
    if word in english_dutch:
        # If the translation exists, append the Dutch equivalent.
        translated_words.append(english_dutch[word])
    else:
        # If the word is not in the dictionary, retain the original word.
        translated_words.append(word)

# Reassemble the list of translated words into a single sentence.
translated_sentence = ' '.join(translated_words)
print(translated_sentence)

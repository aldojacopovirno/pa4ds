# Assignment
# Read a line of text and count how many different vowels it contains. Treat
# uppercase and lowercase letters as the same, and count each vowel type at most
# once, i.e. a word containing many `a` characters still contributes one `a` to
# the result. Display the count from a function.
#
# Solution

# Membership checks count each vowel type once, even if it repeats.
def count_distinct_vowels(text: str) -> int:
    """Count vowel types present, not their total number of occurrences."""
    text = text.lower()
    vowel_count = 0

    for vowel in "aeiou":
        if vowel in text:
            vowel_count += 1

    return vowel_count


text = input("Type some text: ")
print(f"Distinct vowels: {count_distinct_vowels(text)}")

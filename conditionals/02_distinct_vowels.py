# Assignment
# Read a line of text and count how many different vowels it contains. Treat
# uppercase and lowercase letters as the same, and count each vowel type at most
# once, i.e. a word containing many `a` characters still contributes one `a` to
# the result. Display the count from a function.
#
# Solution

# Define a function that accepts text and returns a count when we call it.
# The hints str and -> int describe the expected input and returned result;
# they document the function contract without checking values at runtime.
def count_distinct_vowels(text: str) -> int:
    """Count vowel types present, not their total number of occurrences."""
    # Convert letters to lowercase so, e.g., A and a match the same vowel.
    # lower() returns a new string, so store that string for the checks below.
    text = text.lower()

    # Start from zero because we have not found any vowel types yet.
    # The loop will increase this counter only when it finds a new vowel type.
    vowel_count = 0

    # Visit the five vowel types once each, in order: a, e, i, o, then u.
    # On each pass, vowel receives the next character. The loop stops after u.
    for vowel in "aeiou":
        # Membership with in produces a Boolean: True if this vowel occurs
        # anywhere in text, otherwise False. Run the block only when it is True.
        if vowel in text:
            # += 1 adds one to the current count and stores the new total.
            # Check each vowel once, so repeated occurrences cannot add more:
            # e.g. "banana" has three a characters but contributes just one.
            vowel_count += 1

    # After all five checks, return the total to the caller. This line is
    # outside the loop so we finish checking every vowel before returning.
    return vowel_count


# Keep the input as a string: the function needs characters to search through.
text = input("Type some text: ")

# Pass the entered text to the function. The returned count replaces the
# expression in braces, and the label explains that we counted vowel types.
print(f"Distinct vowels: {count_distinct_vowels(text)}")

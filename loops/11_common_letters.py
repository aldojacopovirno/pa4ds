# Assignment
# Read two non-empty words and compare them without distinguishing uppercase
# from lowercase. Print the letters the words share, in the order they first
# appear in the first word, and print each shared letter only once.
#
# Solution

# Put the comparison in a function so it can work with two supplied words.
# The str hints describe text arguments and a text result; they do not convert
# the arguments. We prepare the case of both words before calling the function.
def common_letters(first_word: str, second_word: str) -> str:
    """Return shared letters once, in the order of their first appearance."""
    # Begin with no matches. Keep accepted characters in result so it also
    # records which characters have already been included.
    result = ""

    # Visit the first word from left to right. This preserves the order in
    # which shared characters first appear; the loop stops at the word's end.
    for letter in first_word:
        # in checks whether the second word contains this character. not in
        # checks that we have not already included it. and requires both checks
        # to be True, so a shared character is accepted only the first time.
        if letter in second_word and letter not in result:
            # For strings, += joins the character to the current result and
            # stores the new string. Repeated or unshared characters skip this.
            result += letter

    # Return after scanning the whole word, rather than after the first match.
    # E.g. "banana" and "ananas" produce "an", even though a and n repeat.
    return result


# input() supplies text. strip() removes whitespace at the edges, and lower()
# makes uppercase and lowercase versions match during the later comparison.
# Whitespace-only input becomes an empty string after strip().
first_word = input("Enter a word: ").strip().lower()
second_word = input("Enter another word: ").strip().lower()

# Each equality check is Boolean. or keeps the loop running if either word is
# empty, so we can compare only after both words contain text.
while first_word == "" or second_word == "":
    print("Both words must be non-empty. Please try again.")
    # Read and prepare both words again so the next condition check uses the
    # new answers. The loop ends when neither answer is empty; without these
    # assignments, an invalid pair would keep the condition True forever.
    first_word = input("Enter a word: ").strip().lower()
    second_word = input("Enter another word: ").strip().lower()

# Pass the prepared words to the function, then display the returned string.
# If the words share no characters, the result is empty and print shows a blank line.
print(common_letters(first_word, second_word))

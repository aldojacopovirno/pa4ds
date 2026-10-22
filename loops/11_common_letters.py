# Assignment
# Read two non-empty words and compare them without distinguishing uppercase
# from lowercase. Print the letters the words share, in the order they first
# appear in the first word, and print each shared letter only once.
#
# Solution

# The result string prevents a shared character from being printed twice.
def common_letters(first_word: str, second_word: str) -> str:
    """Return shared letters once, in the order of their first appearance."""
    result = ""
    for letter in first_word:
        if letter in second_word and letter not in result:
            result += letter
    return result


first_word = input("Enter a word: ").strip().lower()
second_word = input("Enter another word: ").strip().lower()

while first_word == "" or second_word == "":
    print("Both words must be non-empty. Please try again.")
    first_word = input("Enter a word: ").strip().lower()
    second_word = input("Enter another word: ").strip().lower()

print(common_letters(first_word, second_word))

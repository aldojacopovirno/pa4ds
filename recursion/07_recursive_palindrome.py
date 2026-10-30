# Assignment
# Write a recursive function that checks whether a string is a palindrome,
# comparing characters without regard to case. An empty string counts as a
# palindrome. Demonstrate one matching and one non-matching word.
#
# Solution

# characters is the substring still under test. Compare the first and last
# characters; if they match, recurse on characters[1:-1], which removes both
# ends and shortens the string until it is empty or a mismatch is found.
def recursive_palindrome(characters: str) -> bool:

    # Normalise case once per call so 'A' and 'a' compare equal at the ends.
    characters = characters.lower()

    # Base case: an empty string reads the same forward and backward.
    if len(characters) == 0:
        return True
    # Mismatch at the outermost pair means the full string is not a palindrome.
    elif characters[0] != characters[-1]:
        return False
    else:
        # Inner substring must also be a palindrome for the whole string to be one.
        return recursive_palindrome(characters[1:-1])


print(f"recursive_palindrome('anna') = {recursive_palindrome('anna')}")
print(f"recursive_palindrome('pizza') = {recursive_palindrome('pizza')}")

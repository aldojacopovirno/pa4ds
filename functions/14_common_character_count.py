# Assignment
# Write a function that returns the number of distinct characters shared by two
# strings. Repeated characters count only once, and uppercase and lowercase
# remain different characters. Demonstrate it with strings that contain
# duplicates.
#
# Solution

# A set removes duplicates before the shared characters are counted.
def count_common_characters(first: str, second: str) -> int:
    """Count distinct shared characters, distinguishing upper/lower case."""
    # Sets remove duplicates; their intersection contains shared characters.
    return len(set(first) & set(second))


print(
    "Distinct shared characters in 'bee' and 'peer': "
    f"{count_common_characters('bee', 'peer')}"
)

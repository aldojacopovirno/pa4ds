# Assignment
# Write a function that returns the number of distinct characters shared by two
# strings. Repeated characters count only once, and uppercase and lowercase
# remain different characters. Demonstrate it with strings that contain
# duplicates.
#
# Solution

# Put the comparison in a function so the same steps can be reused for any
# pair of strings. Each call supplies first and second and receives an integer.
def count_common_characters(first: str, second: str) -> int:
    """Count distinct shared characters, distinguishing upper/lower case."""
    # Convert each string to a set so repeated occurrences count only once.
    # & takes the intersection: only characters present in both sets remain.
    # len counts these distinct shared characters, and return sends that count
    # to the caller. No case conversion occurs, so 'E' and 'e' remain different.
    return len(set(first) & set(second))


# 'bee' becomes {'b', 'e'} and 'peer' becomes {'p', 'e', 'r'} as sets.
# Only 'e' is shared, so the function returns 1 despite its repeated occurrences.
# Insert that returned count into the message before printing it.
print(
    "Distinct shared characters in 'bee' and 'peer': "
    f"{count_common_characters('bee', 'peer')}"
)

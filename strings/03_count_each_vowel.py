# Assignment
# Use the sample sentence `Hello World!` and count each vowel separately.
# Display the count for A, E, I, O, and U; reset the counter for each vowel so
# one vowel’s count does not include earlier results.
#
# Solution

# Reset the count at the start of each vowel’s pass.
text = "Hello World!"
lowercase_text = text.lower()
vowels = "aeiou"

for vowel in vowels:
    vowel_count = 0
    for character in lowercase_text:
        if character == vowel:
            vowel_count += 1
    print(f"In {text!r} there are {vowel_count} {vowel.upper()} characters.")

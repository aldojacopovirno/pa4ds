# Assignment
# Use the sample sentence `Hello World!` and count each vowel separately.
# Display the count for A, E, I, O, and U; reset the counter for each vowel so
# one vowel’s count does not include earlier results.
#
# Solution

# Keep the original sentence for the output, and make a lowercase copy for
# comparisons. This lets uppercase and lowercase letters count as the same vowel.
text = "Hello World!"
lowercase_text = text.lower()

# These are the five vowels to count. Their order also sets the output order.
vowels = "aeiou"

# The outer loop chooses one vowel at a time and ends after all five are counted.
for vowel in vowels:
    # Start a new count for this vowel. Resetting inside the outer loop keeps
    # counts separate: the count for 'e', for example, starts again at zero.
    vowel_count = 0

    # Scan the entire lowercase sentence for the current vowel. This inner loop
    # starts from the first character again each time the outer loop advances.
    for character in lowercase_text:
        # == produces a Boolean: True when this character is the current vowel,
        # and False otherwise. Only a match should increase this vowel's count.
        if character == vowel:
            # Add one for each matching occurrence, including repeated vowels.
            vowel_count += 1

    # Print after the inner loop finishes, while still inside the outer loop:
    # this gives one completed result per vowel, including a count of zero.
    # !r shows the original text with quotes; upper() capitalizes the vowel
    # only for display, so the comparisons above still use lowercase letters.
    print(f"In {text!r} there are {vowel_count} {vowel.upper()} characters.")

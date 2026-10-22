# Assignment
# Read a line of text and display its length. Count every character, including
# spaces and punctuation, and make the output label clear.
#
# Solution

# Read the answer as text: input returns a string, even if the user types digits.
# We need the characters themselves, so there is no conversion to a number.
user_text = input("Enter a string: ")

# Use len to count every character in the string, including spaces and
# punctuation. An empty answer gives an empty string, whose length is zero.
text_length = len(user_text)

# Include a label so the number is clearly understood as a character count.
print(f"String length: {text_length}")

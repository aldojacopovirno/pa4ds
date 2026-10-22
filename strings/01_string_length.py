# Assignment
# Read a line of text and display its length. Count every character, including
# spaces and punctuation, and make the output label clear.
#
# Solution

# len counts spaces and punctuation as characters too.
user_text = input("Enter a string: ")

text_length = len(user_text)
print(f"String length: {text_length}")

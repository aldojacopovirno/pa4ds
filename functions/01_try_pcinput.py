# Assignment
# Use the external `pcinput` helper module to read four values from the user: an
# integer, a floating-point number, a string, and one English letter. Display
# all four returned values. The helper should keep asking when a numeric value
# or letter is invalid.
#
# Solution

import pcinput

# Keep the returned values so they can be used after reading the input.
# Each input helper converts or checks the value before returning it.
integer_value = pcinput.getInteger("Type an integer: ")
float_value = pcinput.getFloat("Type a float: ")
string_value = pcinput.getString("Type a string: ")
letter_value = pcinput.getLetter("Type a letter: ")

print(
    f"Integer: {integer_value}, float: {float_value}, "
    f"string: {string_value!r}, letter: {letter_value}"
)

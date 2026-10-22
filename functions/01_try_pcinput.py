# Assignment
# Use the external `pcinput` helper module to read four values from the user: an
# integer, a floating-point number, a string, and one English letter. Display
# all four returned values. The helper should keep asking when a numeric value
# or letter is invalid.
#
# Solution

# Import makes the external module available by the name pcinput. This helper
# is not included in the repository, so it must be provided separately.
import pcinput

# The dot selects a function from the module; parentheses call that function.
# The prompt is an argument: a value passed to the function for this call.
# As required by the assignment, getInteger keeps asking for a valid integer,
# then returns it. Save that result so we can display it after the other calls.
integer_value = pcinput.getInteger("Type an integer: ")

# Request a floating-point number with the matching helper. Its contract also
# requires another attempt when the numeric input is invalid.
float_value = pcinput.getFloat("Type a float: ")

# Use the text helper for the string: this value does not need to be numeric.
string_value = pcinput.getString("Type a string: ")

# Request one English letter. The assignment requires this helper to repeat
# the request when the user enters an invalid letter.
letter_value = pcinput.getLetter("Type a letter: ")

# An f-string inserts the saved results into readable output. The !r conversion
# shows the string's representation, including quotes and escaped characters,
# so an empty string or a special character is easier to recognise.
# The two neighbouring f-strings form one message passed to print().
print(
    f"Integer: {integer_value}, float: {float_value}, "
    f"string: {string_value!r}, letter: {letter_value}"
)

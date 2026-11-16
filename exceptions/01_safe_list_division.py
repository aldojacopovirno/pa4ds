# Assignment
# Given a list that contains integers, a zero and a string, ask the user for an
# index and display the result of dividing 100 by the element at that position.
# Handle each possible error with its own message: an index outside the list,
# an input that is not an integer, a division by zero, and an element that is
# not a number.
#
# Solution

# The list is built to trigger errors: 0 cannot divide 100, and "103" is a string.
numbers = [100, 101, 0, "103", 104]

# Code that may fail goes in the try block; if an error occurs, Python skips the
# rest of the block and looks for an except clause matching the error type.
try:
    # int raises ValueError when the text is not a valid integer, e.g. "abc".
    index = int(input("Give an index: "))

    # numbers[index] raises IndexError if the index is out of range, then
    # 100 / element raises ZeroDivisionError for 0 and TypeError for a string.
    print(f"100 / {numbers[index]} = {100 / numbers[index]}")
except IndexError as error:
    # The "as" name keeps the error object; its args hold Python's own message.
    print("IndexError: The index is out of range.", error.args)
except ValueError as error:
    print("ValueError: The input is not a valid integer.", error.args)
except ZeroDivisionError as error:
    print("ZeroDivisionError: The number at the given index is zero.", error.args)
except TypeError as error:
    print("TypeError: The element at the given index is not a number.", error.args)

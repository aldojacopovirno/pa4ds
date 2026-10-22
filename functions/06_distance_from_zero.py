# Assignment
# Define `distance_from_zero` with one argument. If the argument is an integer
# or a floating-point number, return its absolute value; for any other type,
# return the string `Nope`. Show one numeric example and one unsupported-type
# example.
#
# Solution

# Define the calculation once so different arguments can use the same rules.
def distance_from_zero(value):
    """Return an int/float's absolute value, or Nope for other types."""
    # type(value) gives the argument's exact type. The tuple lists the two
    # supported types, and not in produces True when neither type matches.
    # This exact check also excludes bool, even though bool is a subclass of int.
    if type(value) not in (int, float):
        # Return early for an unsupported type, such as str, so abs is only
        # reached for an int or float. return also ends this function call.
        return "Nope"

    # Distance from zero has no negative sign: abs(-12) and abs(12) both give 12.
    # Return the result to the caller, which can print it or use it elsewhere.
    return abs(value)


# Each call passes its argument into value. print displays the returned result:
# the numeric example gives 12, while the text example follows the Nope branch.
print(distance_from_zero(-12))
print(distance_from_zero("twelve"))

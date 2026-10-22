# Assignment
# Define `distance_from_zero` with one argument. If the argument is an integer
# or a floating-point number, return its absolute value; for any other type,
# return the string `Nope`. Show one numeric example and one unsupported-type
# example.
#
# Solution

# Check the supported types before calling abs.
def distance_from_zero(value):
    """Return an int/float's absolute value, or Nope for other types."""
    if type(value) not in (int, float):
        return "Nope"
    return abs(value)


print(distance_from_zero(-12))
print(distance_from_zero("twelve"))

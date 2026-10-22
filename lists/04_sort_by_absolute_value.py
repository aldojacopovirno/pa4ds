# Assignment
# Sort the supplied integer list by increasing absolute value. The displayed
# values should retain their original signs, e.g. a negative number
# remains negative after sorting by magnitude.
#
# Solution

# The sort key compares magnitudes but keeps each original signed value.
numbers = [5, -4, 3, 4, -5]
numbers.sort(key=abs)
print(numbers)

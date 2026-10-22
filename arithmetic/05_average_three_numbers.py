# Assignment
# Start with three numeric values and calculate their arithmetic mean. Add the
# values, divide by three, and print the result with a label. Keep the
# calculation visible so it is easy to check by hand.
#
# Solution

# Store the three values separately so each one can be used in the calculation.
# The numbers below are the data for this example; the same formula works for
# other numeric values.
first_number = 1
second_number = 2
third_number = 3

# To find the mean, add the values and divide the total by how many values we have.
# Parentheses make Python calculate the whole sum before dividing by 3.
# Without them, only third_number would be divided, because / comes before +.
# Here, (1 + 2 + 3) / 3 gives 2.0. With integer inputs, / returns a float
# (a floating-point number), even when the division has no remainder.
average = (first_number + second_number + third_number) / 3

# In an f-string, Python replaces {average} with its calculated value.
# The label explains what the number means when someone reads the output.
print(f"Average: {average}")

# Assignment
# Create two variables with different values, display them, then exchange their
# values and display them again. After the exchange, each variable should
# contain the value that originally belonged to the other variable.
#
# Solution

# Start with different values so we can see whether the exchange worked.
a = 17
b = 23

# Show the starting values before changing them. Each pair of braces in the
# f-string inserts the value currently associated with that variable name.
print(f"Before: a = {a}, b = {b}")

# Evaluate the right side first: b, a produces the old values 23, 17.
# Python then assigns them to the names on the left in the same order:
# a receives 23 and b receives 17. This is called multiple assignment.
# Two separate statements, a = b followed by b = a, would lose the old value
# of a: after the first statement, both names would already have the value 23.
a, b = b, a

# Read the variables again after the exchange so the two output lines can be
# compared: each variable should now contain the other's starting value.
print(f"After:  a = {a}, b = {b}")

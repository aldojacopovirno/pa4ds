# Assignment
# Create two variables with different values, display them, then exchange their
# values and display them again. After the exchange, each variable should
# contain the value that originally belonged to the other variable.
#
# Solution

# Multiple assignment reads both old values before replacing either name.
a = 17
b = 23

print(f"Before: a = {a}, b = {b}")

a, b = b, a

print(f"After:  a = {a}, b = {b}")

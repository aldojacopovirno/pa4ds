# Assignment
# Break an amount of 289 cents into the fewest whole units of dollars, quarters,
# dimes, nickels, and pennies. Start with the largest denomination, record how
# many fit, then continue with the cents left over. Print the count of each
# denomination.
#
# Solution

# Work in whole cents so we can count coins without using decimal amounts.
amount = 289

# Describe the invalid cases with two Boolean checks: the value is not an
# integer, or it is below zero. The if block runs if either check is True.
# If amount is not an integer, the first check is already True, so Python
# skips amount < 0. This avoids comparing a value such as a string with 0.
if not isinstance(amount, int) or amount < 0:
    raise ValueError("amount must be a non-negative integer")

# Start with the largest denomination. For these denominations, taking as
# many of each as fit, from largest to smallest, gives the fewest pieces.
# divmod(value, size) returns two integers: value // size counts whole pieces,
# and value % size gives the cents left over. Assign both results at once.
# Here, 289 = 2 * 100 + 89, so keep 2 dollars and pass 89 cents to the next step.
dollars, remainder = divmod(amount, 100)

# Use only the remainder: the dollars have already covered part of the amount.
# Three quarters use 75 of the 89 cents, leaving 14 cents still to cover.
quarters, remainder = divmod(remainder, 25)

# Reassign remainder after each step so the next step uses the new balance.
# One dime uses 10 of the 14 cents, leaving 4 cents.
dimes, remainder = divmod(remainder, 10)

# Four cents cannot cover a nickel, so the count is 0. Since a penny is worth
# 1 cent, the last remainder is also the number of pennies: no extra division
# is needed, and we can store that remainder directly in pennies.
nickels, pennies = divmod(remainder, 5)

# Print each count with its denomination so the result is easy to interpret.
# The braces in each f-string insert the value stored in that variable.
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")

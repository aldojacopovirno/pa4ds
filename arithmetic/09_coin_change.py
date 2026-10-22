# Assignment
# Break an amount of 289 cents into the fewest whole units of dollars, quarters,
# dimes, nickels, and pennies. Start with the largest denomination, record how
# many fit, then continue with the cents left over. Print the count of each
# denomination.
#
# Solution

# Each divmod call returns a denomination count and the cents left over.
amount = 289

if not isinstance(amount, int) or amount < 0:
    raise ValueError("amount must be a non-negative integer")

dollars, remainder = divmod(amount, 100)
quarters, remainder = divmod(remainder, 25)
dimes, remainder = divmod(remainder, 10)
nickels, pennies = divmod(remainder, 5)

print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")

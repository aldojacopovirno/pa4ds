# Assignment
# A book has a cover price of €24.95 and a bookstore receives a 40% discount.
# Shipping costs €3.00 for the first copy and €0.75 for every additional copy.
# Calculate the total wholesale cost of 60 copies, keeping the book cost and
# shipping cost separate before adding them.
#
# Solution

# Use Decimal for money so decimal amounts can be represented exactly.
# Build each Decimal from a string: converting a float could carry over its
# small binary rounding error before the calculation even begins.
from decimal import Decimal

# Keep the order size separate from the prices so we can reuse it for both
# the book cost and the shipping cost.
copies = 60
cover_price = Decimal("24.95")

# Write 40% as 0.40 because a percentage is a fraction out of 100.
discount_rate = Decimal("0.40")

# The first copy has a different shipping charge, so keep the two rates
# separate instead of charging the same amount for every copy.
first_copy_shipping = Decimal("3.00")
additional_copy_shipping = Decimal("0.75")

# The comparison produces True or False. If the order has zero copies or
# fewer, stop with an error before using a formula that assumes a first copy.
if copies <= 0:
    raise ValueError("copies must be positive")

# Subtract the discount fraction from 1 to find the fraction we still pay:
# 1 - 0.40 = 0.60. Multiply the cover price by this remaining fraction.
discounted_price = cover_price * (Decimal("1") - discount_rate)

# The discounted price is for one book; multiply by the number of copies
# to obtain the cost of all the books, before adding any shipping charges.
books_total = copies * discounted_price

# Charge the first copy once, then charge the lower rate for copies - 1
# additional copies. For 60 books, that means 1 first copy and 59 others.
shipping_total = (
    first_copy_shipping
    + (copies - 1) * additional_copy_shipping
)

# Add the two subtotals only after each has been calculated with its own rule.
wholesale_total = books_total + shipping_total

# Insert the total into an f-string. The :.2f format displays two decimal
# places, as expected for a price in euros.
print(f"Wholesale cost: €{wholesale_total:.2f}")

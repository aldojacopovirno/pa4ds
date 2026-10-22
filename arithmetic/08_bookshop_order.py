# Assignment
# A book has a cover price of €24.95 and a bookstore receives a 40% discount.
# Shipping costs €3.00 for the first copy and €0.75 for every additional copy.
# Calculate the total wholesale cost of 60 copies, keeping the book cost and
# shipping cost separate before adding them.
#
# Solution

from decimal import Decimal

# Calculate book and shipping costs separately, then combine them.
copies = 60
cover_price = Decimal("24.95")
discount_rate = Decimal("0.40")
first_copy_shipping = Decimal("3.00")
additional_copy_shipping = Decimal("0.75")

if copies <= 0:
    raise ValueError("copies must be positive")

discounted_price = cover_price * (Decimal("1") - discount_rate)
books_total = copies * discounted_price
shipping_total = (
    first_copy_shipping
    + (copies - 1) * additional_copy_shipping
)
wholesale_total = books_total + shipping_total

print(f"Wholesale cost: €{wholesale_total:.2f}")

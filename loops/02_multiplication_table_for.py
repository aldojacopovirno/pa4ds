# Assignment
# Read an integer and print its products with 1, 2, ..., 10. Use a `for` loop
# and show one multiplication per line, with the product aligned for easy
# reading.
#
# Solution

# The range end is exclusive, so 11 is needed to include multiplier 10.
number = int(input("Type an integer: "))
print("===== Multiplication Table (for loop) =====")

for multiplier in range(1, 11):
    product = multiplier * number
    print(f"{multiplier} x {number} = {product:>5}")

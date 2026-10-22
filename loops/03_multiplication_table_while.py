# Assignment
# Read an integer and print its products with 1 through 10. Use a `while` loop,
# initialize the counter before the loop, increase it on every pass, and stop
# after the tenth product.
#
# Solution

# The counter begins at one and increases until it passes ten.
number = int(input("Type an integer: "))
print("===== Multiplication Table (while loop) =====")

multiplier = 1
while multiplier <= 10:
    product = multiplier * number
    print(f"{multiplier} x {number} = {product:>5}")
    multiplier += 1

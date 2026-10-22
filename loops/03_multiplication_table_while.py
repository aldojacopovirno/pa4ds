# Assignment
# Read an integer and print its products with 1 through 10. Use a `while` loop,
# initialize the counter before the loop, increase it on every pass, and stop
# after the tenth product.
#
# Solution

# input() returns text. Convert it to int so multiplication uses the entered
# numeric value instead of repeating its characters.
number = int(input("Type an integer: "))
print("===== Multiplication Table (while loop) =====")

# Start at 1 to include the first product. A while loop needs us to create
# and update this counter explicitly; it does not take values from a range.
multiplier = 1

# <= produces True or False. while checks this Boolean condition before every
# pass: run the indented body while the multiplier is at most 10, then stop.
while multiplier <= 10:
    # Use the current multiplier to calculate and display one row. These
    # indented instructions belong to the loop and repeat on each pass.
    product = multiplier * number
    # The f-string inserts each value into its braces. :>5 right-aligns the
    # product in at least five character positions so the results line up.
    print(f"{multiplier} x {number} = {product:>5}")

    # += 1 replaces the counter with its current value plus one. This makes
    # progress toward stopping: after printing 10 times the number, it becomes
    # 11 and the next condition is False. Without this update it would stay 1.
    multiplier += 1

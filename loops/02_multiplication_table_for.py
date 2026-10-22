# Assignment
# Read an integer and print its products with 1, 2, ..., 10. Use a `for` loop
# and show one multiplication per line, with the product aligned for easy
# reading.
#
# Solution

# input() returns text. Convert it to int so we can multiply the entered number
# numerically instead of repeating a string.
number = int(input("Type an integer: "))
print("===== Multiplication Table (for loop) =====")

# range(1, 11) supplies 1 through 10 because its upper limit is excluded.
# for assigns each value to multiplier in turn and advances automatically;
# after 10, the range is exhausted and the loop ends.
for multiplier in range(1, 11):
    # Both indented instructions run for every multiplier. Recalculate the
    # product using the current value so each pass creates the next table row.
    product = multiplier * number
    # An f-string inserts the values inside braces into the displayed row.
    # :>5 right-aligns the product in a field at least five characters wide,
    # adding spaces on the left so products line up; longer values still fit.
    print(f"{multiplier} x {number} = {product:>5}")

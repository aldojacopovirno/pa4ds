# Assignment
# Write a function that accepts two tuples and prints every ordered pair made by
# choosing one element from the first tuple and one from the second. Use nested
# loops and demonstrate the function with a tuple of names and a tuple of
# prices.
#
# Solution

# Define the pairing process once so other tuples can reuse it. Each call
# supplies the two tuples as arguments to first_tuple and second_tuple.
# -> None documents that the function prints pairs; when it finishes, its
# return value is implicitly None. The hints do not check types at runtime.
def print_pairs(first_tuple: tuple, second_tuple: tuple) -> None:

    # Visit each valid index of the first tuple, from 0 to its length minus 1.
    # On each pass, keep this first element fixed while the inner loop runs.
    for i in range(len(first_tuple)):

        # For every new i, start j at 0 again and visit the entire second tuple.
        # This gives each first element a turn with every second element.
        for j in range(len(second_tuple)):

            # The comma groups the two selected values into an ordered pair:
            # its first position comes from first_tuple, its second from
            # second_tuple. Build and display one pair on each inner pass.
            pair = (first_tuple[i], second_tuple[j])
            print(pair)

# The four names and four prices produce 4 * 4 = 16 pairs. For example, the
# first name is printed with 5, then 4, then 6, then 7 before moving to the
# next name. In general, the pair count is the product of the tuple lengths;
# if either tuple is empty, no inner body runs and there are no pairs to print.
pizzas = ('margherita', 'marinara', 'capricciosa', 'diavolo')
prices = (5, 4, 6, 7)

# Defining the function above prepared the instructions; this call runs them
# using pizzas as first_tuple and prices as second_tuple.
print_pairs(pizzas, prices)

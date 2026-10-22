# Assignment
# Write a function that accepts two tuples and prints every ordered pair made by
# choosing one element from the first tuple and one from the second. Use nested
# loops and demonstrate the function with a tuple of names and a tuple of
# prices.
#
# Solution

# The nested loops combine each first-tuple value with every second-tuple value.
def print_pairs(first_tuple: tuple, second_tuple: tuple) -> None:

    for i in range(len(first_tuple)):

        for j in range(len(second_tuple)):

            pair = (first_tuple[i], second_tuple[j])
            print(pair)

pizzas = ('margherita', 'marinara', 'capricciosa', 'diavolo')
prices = (5, 4, 6, 7)
print_pairs(pizzas, prices)

# Assignment
# Search the supplied tuple for a target value and print its index. If the value
# is absent, report that fact without trying to access an invalid tuple
# position.
#
# Solution

# Check membership before searching so a missing value cannot overrun the tuple.
pizzas = ('margherita', 5, 6, 'marinara', 4)

target = 6

if target in pizzas:
    i = 0

    while pizzas[i] != target:
        i += 1
    print(f'The index of number {target} is {i}.')

else:
    print(f'Number {target} is not in the tuple.')

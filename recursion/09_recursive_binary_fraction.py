# Assignment
# Write recursive helpers that convert the fractional part of a number in `[0, 1)`
# to a fixed-length binary expansion after the radix point. For `0`, return `'0'`.
# Otherwise prefix `'0.'` and append three binary digits obtained by repeatedly
# doubling the fraction and recording `1` when the value reaches at least `1`.
# Demonstrate on `0.357`, which should yield `'0.010'`.
#
# Solution

# number holds the remaining fractional value; digits is how many binary places
# are still required after the radix point. Each step doubles the fraction: a
# result of at least 1 contributes bit 1 and continues with the part above 1
# subtracted; otherwise the bit is 0 and doubling continues on the same value.
def recursive_binary_fraction(number: float, digits: int) -> str:

    # Base case: no more bits to append after the point.
    if digits == 0:
        return ''

    number *= 2

    if number >= 1:
        # One whole unit appeared in the doubled value; record 1 and recurse on
        # the fractional part left after removing that whole.
        return '1' + recursive_binary_fraction(number - 1, digits - 1)
    # Doubled value still below 1; record 0 and recurse with digits reduced.
    return '0' + recursive_binary_fraction(number, digits - 1)


def recursive_binary(number: float) -> str:

    # Inputs with no fractional part need no radix expansion.
    if number == 0:
        return '0'
    # This exercise fixes three bits after the point for demonstration values.
    return '0.' + recursive_binary_fraction(number, 3)


print(f"recursive_binary(0.357) = {recursive_binary(0.357)!r}")

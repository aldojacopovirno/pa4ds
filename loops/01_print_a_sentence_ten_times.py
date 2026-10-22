# Assignment
# Print the exact sentence `I am writing ten times this string!` ten times. Use
# a `for` loop whose counter is not needed inside the loop body.
#
# Solution

# The underscore shows that the loop counter is intentionally unused.
sentence = "I am writing ten times this string!"

for _ in range(10):
    print(sentence)

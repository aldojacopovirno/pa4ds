# Assignment
# Print the exact sentence `I am writing ten times this string!` ten times. Use
# a `for` loop whose counter is not needed inside the loop body.
#
# Solution

# Store the sentence once so every repetition prints exactly the same text.
sentence = "I am writing ten times this string!"

# range(10) provides the ten integers from 0 to 9: the upper limit is excluded.
# for takes one value on each pass. We call it _ because the value is unused;
# we need ten repetitions, not the numbers themselves.
for _ in range(10):
    # Indentation makes this instruction part of the loop body, so it runs
    # once per value. After the tenth value, the loop has no more work and ends.
    print(sentence)

# Assignment
# Generate the Fibonacci sequence beginning with 1, 1. Each new term is the sum
# of the previous two. Print every term that is at most 1000, and stop before
# printing the first term that exceeds 1000.
#
# Solution

# Start with the two given terms: we need two values before we can form a sum.
# They are separate terms even though both have the same value.
sequence = [1, 1]
# Python positions start at zero, so these print the first and second terms.
print(sequence[0])
print(sequence[1])

# True stays true, so the loop repeats until break explicitly ends it below.
while True:
    # Negative indexes count from the end: -1 is the latest term and -2 is
    # the one before it. Their sum is the next Fibonacci term to consider.
    next_number = sequence[-1] + sequence[-2]
    # > allows a term equal to 1000 and rejects only terms above the limit.
    # Test before appending or printing so an oversized term is never included.
    if next_number > 1000:
        # Exit the whole loop once the first term beyond the limit is found.
        break

    # Store the accepted term at the end, making it available for the next sum.
    # The positive terms grow after the initial 1, 1, so repeated sums
    # eventually exceed 1000 and reach the break instead of repeating forever.
    sequence.append(next_number)
    # Print each accepted term once, then repeat with the updated sequence.
    print(next_number)

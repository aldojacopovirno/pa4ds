# Assignment
# Generate the Fibonacci sequence beginning with 1, 1. Each new term is the sum
# of the previous two. Print every term that is at most 1000, and stop before
# printing the first term that exceeds 1000.
#
# Solution

# Compute the next term from the previous two and break before it exceeds the limit.
sequence = [1, 1]
print(sequence[0])
print(sequence[1])

while True:
    next_number = sequence[-1] + sequence[-2]
    if next_number > 1000:
        break
    sequence.append(next_number)
    print(next_number)

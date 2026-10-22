# Assignment
# Ask how many integers are in a sequence, read them one by one, and calculate
# the sum and mean of only the even values. If the sequence contains no even
# values, display the sum as zero and state that the mean is undefined.
#
# Solution

# Read how many integers to collect and convert the input text to an integer.
# A negative count cannot describe a sequence length; zero is allowed and
# produces an empty sequence, which the output checks below can handle.
count = int(input("How many integers? "))
if count < 0:
    raise ValueError("The count must be non-negative.")

# Collect the values first so the next loop can examine the complete sequence.
sequence = []
# range excludes its upper limit, so count + 1 gives positions 1 through count.
# Each iteration asks for one value; after count iterations, the range is
# exhausted and the loop ends. For count == 0, it has no positions to visit.
for position in range(1, count + 1):
    # Convert each answer to an integer and append it to the end of sequence.
    # The displayed position helps the user keep track of how many remain.
    sequence.append(int(input(f"Integer {position}: ")))

# Keep two separate totals: the sum of even values and how many were selected.
# Both start at zero because no values have been processed yet.
even_sum = 0
even_count = 0
# Visit each stored integer once. The loop ends after the last stored value.
for number in sequence:
    # % gives the remainder of division. An even integer has remainder zero
    # when divided by 2, so != 0 produces True exactly for an odd integer.
    if number % 2 != 0:
        # Skip the rest of this iteration for an odd value. continue does not
        # end the loop: processing resumes with the next number, if one exists.
        continue

    # Only even values reach these lines. Add the value to the sum, but add
    # just one to the count because we have selected one more integer.
    even_sum += number
    even_count += 1

# The sum remains zero if there were no even values, so it is always printable.
print(f"Sum of even values: {even_sum}")
# A mean needs a nonzero count. Check for no even values before dividing;
# reaching else guarantees even_count > 0, since it only grows from zero.
if even_count == 0:
    print("Mean is undefined because there are no even values.")
else:
    # Divide the selected values' sum by their count, not by the input count:
    # odd values contribute to neither part of this mean.
    print(f"Mean of even values: {even_sum / even_count}")

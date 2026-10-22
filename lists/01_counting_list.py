# Assignment
# Read a non-negative integer `n` and create a list containing the integers from
# 1 through `n`, in order. If `n` is zero, the result is an empty list. Display
# the completed list.
#
# Solution

# range stops before its upper bound, so count plus one includes n.
count = int(input("How many positive integers? "))
if count < 0:
    raise ValueError("The count must be non-negative.")

numbers = []
for number in range(1, count + 1):
    numbers.append(number)

print(numbers)

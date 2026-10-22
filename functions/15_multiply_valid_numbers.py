# Assignment
# Keep asking for two integers until both are positive, below 1000, and neither
# divides evenly by the other. Once both values satisfy every condition, display
# their product and stop asking for input.
#
# Solution

# The range checks run before modulo tests, so zero never reaches a divisor.
def allowed_numbers(first_number: int, second_number: int) -> bool:
    """Check the range and the condition that neither divides the other."""
    return (
        0 < first_number < 1000
        and 0 < second_number < 1000
        and first_number % second_number != 0
        and second_number % first_number != 0
    )


while True:
    first_number = int(input("First positive integer below 1000: "))
    second_number = int(input("Second positive integer below 1000: "))

    if allowed_numbers(first_number, second_number):
        break
    print("Both numbers must be in range and neither may divide the other.")

print(f"Product: {first_number * second_number}")

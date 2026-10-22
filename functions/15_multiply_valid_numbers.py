# Assignment
# Keep asking for two integers until both are positive, below 1000, and neither
# divides evenly by the other. Once both values satisfy every condition, display
# their product and stop asking for input.
#
# Solution

# Put all the acceptance rules in one function so each entered pair is checked
# in the same way. The int and bool hints document the inputs and result;
# converting the keyboard input to integers happens in the calling code below.
def allowed_numbers(first_number: int, second_number: int) -> bool:
    """Check the range and the condition that neither divides the other."""
    # Each comparison produces a Boolean. and requires every rule to be True,
    # and stops evaluating as soon as one is False. Checking the ranges first
    # guarantees both divisors are positive before either modulo is attempted.
    return (
        # Strict inequalities accept integers 1 through 999, excluding both
        # zero and 1000. Each value must pass its own range check.
        0 < first_number < 1000
        and 0 < second_number < 1000
        # A nonzero remainder means the second number does not divide the first.
        # Check the reverse direction too, since the rule applies both ways.
        and first_number % second_number != 0
        and second_number % first_number != 0
    )


# We do not know how many pairs will be needed, so keep asking until an explicit
# break. Each pass reads a fresh pair; int converts the text for the numeric tests.
while True:
    first_number = int(input("First positive integer below 1000: "))
    second_number = int(input("Second positive integer below 1000: "))

    # Call the function with this pair and use its returned Boolean as the
    # condition. For example, 6 and 9 pass, while 3 and 9 fail because 9 % 3 is 0.
    if allowed_numbers(first_number, second_number):
        # End the loop as soon as all rules hold, keeping the accepted values
        # available for the multiplication after the loop.
        break
    # This line runs only for a rejected pair, because an accepted pair breaks
    # out before reaching it. The loop then asks for both numbers again.
    print("Both numbers must be in range and neither may divide the other.")

# Reaching this point means the pair passed the checks. Multiply once and
# insert the result into the labelled output using the f-string's braces.
print(f"Product: {first_number * second_number}")

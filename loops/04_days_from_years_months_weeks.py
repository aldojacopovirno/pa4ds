# Assignment
# Write a function that converts a number of years, months, and weeks into days
# and returns the total. For this exercise, assume a year has 365 days, a month
# has 30 days, and a week has 7 days. Ask for the three non-negative values and
# display the returned total.
#
# Solution

# Define a function so the conversion can be reused with different inputs.
# Each parameter receives a value when the function is called. The int hints
# describe the expected inputs and result; they do not check values at runtime.
def calculate_total_days(years: int, months: int, weeks: int) -> int:
    """Convert units to days using the exercise's fixed-length convention."""
    # Use the fixed lengths required by the exercise. Real calendar months
    # and years can have different lengths, so these values are assumptions.
    days_per_year = 365
    days_per_month = 30
    days_per_week = 7

    # Multiply each quantity by its days per unit, then add the three results.
    # All terms now use days, so their sum represents one total duration.
    # return sends that total back to the caller and ends this function call.
    return (
        years * days_per_year
        + months * days_per_month
        + weeks * days_per_week
    )


# Convert the text returned by input() to integers so the quantities can be
# multiplied by the number of days in each unit.
years = int(input("Years: "))
months = int(input("Months: "))
weeks = int(input("Weeks: "))

# Each comparison gives True or False. or makes the whole condition True
# when at least one quantity is negative; raise then stops the calculation.
# Zero is allowed because a duration need not contain every kind of unit.
if years < 0 or months < 0 or weeks < 0:
    raise ValueError("Use non-negative values.")

# Pass the three valid quantities to the function. Its returned total replaces
# the expression in braces, and the output label gives the result's unit.
print(f"Total days: {calculate_total_days(years, months, weeks)}")

# Assignment
# Write a function that converts a number of years, months, and weeks into days
# and returns the total. For this exercise, assume a year has 365 days, a month
# has 30 days, and a week has 7 days. Ask for the three non-negative values and
# display the returned total.
#
# Solution

# The constants make the exercise’s fixed unit assumptions explicit.
def calculate_total_days(years: int, months: int, weeks: int) -> int:
    """Convert units to days using the exercise's fixed-length convention."""
    days_per_year = 365
    days_per_month = 30
    days_per_week = 7

    return (
        years * days_per_year
        + months * days_per_month
        + weeks * days_per_week
    )


years = int(input("Years: "))
months = int(input("Months: "))
weeks = int(input("Weeks: "))

if years < 0 or months < 0 or weeks < 0:
    raise ValueError("Use non-negative values.")

print(f"Total days: {calculate_total_days(years, months, weeks)}")

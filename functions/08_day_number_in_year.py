# Assignment
# Write a function that receives a calendar year, month, and day, then returns
# that date’s position within the year: January 1 is day 1. Use a standard date
# object so leap years are handled correctly, and demonstrate the function with
# February 29 in a leap year.
#
# Solution

# Import date from Python's datetime module to use calendar rules directly.
from datetime import date


# Receive the three parts of a date as separate arguments. The int hints describe
# the expected values; the date constructor below checks the calendar date.
def day_of_year(year: int, month: int, day: int) -> int:

    # Build a date from the arguments. It accounts for different month lengths
    # and leap years; an invalid date such as February 29, 2023 raises ValueError.
    # timetuple() provides calendar fields, including tm_yday: the position
    # within the year, counted from 1 for January 1. Return that field.
    return date(year, month, day).timetuple().tm_yday


# Pass the year, month, and day in that order. Since 2024 is a leap year,
# February 29 is valid and follows January's 31 days plus 29 February days:
# the returned position is 60. Insert that result into the displayed sentence.
print(f"Day of year for February 29, 2024: {day_of_year(2024, 2, 29)}")

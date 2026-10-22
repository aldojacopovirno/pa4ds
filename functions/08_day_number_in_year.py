# Assignment
# Write a function that receives a calendar year, month, and day, then returns
# that date’s position within the year: January 1 is day 1. Use a standard date
# object so leap years are handled correctly, and demonstrate the function with
# February 29 in a leap year.
#
# Solution

from datetime import date


# The date object accounts for leap days and validates the calendar date.
def day_of_year(year: int, month: int, day: int) -> int:

    return date(year, month, day).timetuple().tm_yday


print(f"Day of year for February 29, 2024: {day_of_year(2024, 2, 29)}")

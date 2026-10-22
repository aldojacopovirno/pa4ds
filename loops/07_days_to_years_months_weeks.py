# Assignment
# Read a non-negative number of days and convert it into whole years, months,
# weeks, and leftover days. Use 365 days per year, 30 days per month, and 7 days
# per week; subtract larger units before smaller ones and display all four
# parts.
#
# Solution

# Subtract whole years first, then months, weeks, and remaining days.
def convert_days(days: int) -> tuple[int, int, int, int]:
    """Return years, months, weeks, and remaining days (365/30/7 units)."""
    years = 0
    months = 0
    weeks = 0

    # Subtract the largest unit first, then continue with smaller units.
    while days >= 365:
        days -= 365
        years += 1

    while days >= 30:
        days -= 30
        months += 1

    while days >= 7:
        days -= 7
        weeks += 1

    return years, months, weeks, days


days = int(input("Days: "))
if days < 0:
    raise ValueError("Days must be non-negative.")

years, months, weeks, remaining_days = convert_days(days)
print(
    f"{years} years, {months} months, {weeks} weeks, "
    f"{remaining_days} days remaining"
)

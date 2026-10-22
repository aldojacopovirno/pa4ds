# Assignment
# Read a non-negative number of days and convert it into whole years, months,
# weeks, and leftover days. Use 365 days per year, 30 days per month, and 7 days
# per week; subtract larger units before smaller ones and display all four
# parts.
#
# Solution

# Put the conversion in a function so it can be reused for different inputs.
# The caller must provide a non-negative integer; the input code below checks
# its sign. The hints describe the integer input and four integer outputs,
# without checking their types at runtime.
# Here years, months, and weeks are fixed units of 365, 30, and 7 days. These
# exercise conventions do not describe the different lengths of calendar months.
def convert_days(days: int) -> tuple[int, int, int, int]:
    """Return years, months, weeks, and remaining days (365/30/7 units)."""
    # Start each counter at zero because we have not removed any whole units
    # yet. As we count units, days will hold the part still to be converted.
    years = 0
    months = 0
    weeks = 0

    # Check whether at least one whole year remains. >= includes exactly 365
    # days: that amount must become one year rather than leftover smaller units.
    # while checks this Boolean condition again after every repetition.
    while days >= 365:
        # Remove one whole year from the remaining days and record that year.
        # -= 365 means days = days - 365; += 1 adds one to the counter.
        # Subtracting a positive amount moves days toward the stopping point.
        days -= 365
        years += 1

    # The first loop stops when fewer than 365 days remain. Now remove whole
    # months from this remainder, so days already counted as years are not
    # counted again. Each repetition removes 30 days and counts one month.
    while days >= 30:
        days -= 30
        months += 1

    # Fewer than 30 days remain after counting months. Remove whole weeks until
    # fewer than 7 days remain. Each subtraction decreases days, so this loop
    # also finishes; the condition prevents subtracting more days than we have.
    while days >= 7:
        days -= 7
        weeks += 1

    # No whole week fits now, so days is the leftover amount from 0 through 6.
    # The commas group the four values into a tuple in this specific order.
    # Together they account for the input: years*365 + months*30 + weeks*7 + days.
    return years, months, weeks, days


# input returns text; int converts a whole-number entry before we compare it
# with zero or use it in subtraction. Text such as "two" cannot be converted.
days = int(input("Days: "))
# Reject a negative amount before calling the conversion function, because the
# conversion describes a duration made from non-negative numbers of units.
if days < 0:
    raise ValueError("Days must be non-negative.")

# Unpack the returned tuple: each variable receives the value in the matching
# position. For example, 400 days produces 1 year, 1 month, 0 weeks, and 5 days.
years, months, weeks, remaining_days = convert_days(days)
# Show all four parts with their units so the user can interpret the result.
# The adjacent f-strings form one message; braces insert the calculated values.
print(
    f"{years} years, {months} months, {weeks} weeks, "
    f"{remaining_days} days remaining"
)

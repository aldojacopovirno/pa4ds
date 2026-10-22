# Assignment
# Write a program that calculates how many seconds are in one week. Use the
# relationships 60 seconds per minute, 60 minutes per hour, 24 hours per day,
# and 7 days per week. Display the final number with a clear label.
#
# Solution

# To convert a week into seconds, count the smaller units inside each larger one.
# Keep each conversion factor separate so its name shows which units it connects.
# Uppercase names indicate values that we intend to keep fixed in this program.
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_WEEK = 7

# Multiply with * to build the conversion one step at a time. Python evaluates
# the expression on the right of = before storing its result in seconds_in_week.
# The parentheses let this single expression continue across several lines.
seconds_in_week = (
    SECONDS_PER_MINUTE
    # There are 60 minutes in each hour: 60 * 60 gives 3,600 seconds per hour.
    * MINUTES_PER_HOUR
    # Count those seconds for all 24 hours to get the seconds in one day.
    * HOURS_PER_DAY
    # Count seven full days to reach the total for one week.
    * DAYS_PER_WEEK
)

# In an f-string, {seconds_in_week} inserts the stored number into the text.
# The label tells the reader what the number measures.
print(f"Seconds in a week: {seconds_in_week}")

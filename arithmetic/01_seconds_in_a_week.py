# Assignment
# Write a program that calculates how many seconds are in one week. Use the
# relationships 60 seconds per minute, 60 minutes per hour, 24 hours per day,
# and 7 days per week. Display the final number with a clear label.
#
# Solution

# Multiplying named conversion factors keeps each unit change visible.
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_WEEK = 7

seconds_in_week = (
    SECONDS_PER_MINUTE
    * MINUTES_PER_HOUR
    * HOURS_PER_DAY
    * DAYS_PER_WEEK
)

print(f"Seconds in a week: {seconds_in_week}")

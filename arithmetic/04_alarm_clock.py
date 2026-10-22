# Assignment
# A 24-hour clock shows 14:00. An alarm is set to ring 535 hours later.
# Calculate the hour at which it will ring and display it in `HH:00` form. Use
# modulo 24 to wrap the elapsed time around the clock; the minutes remain zero.
#
# Solution

# A clock repeats after every 24 hours, so complete days do not change its hour.
# Keep the starting hour and the elapsed hours separate before combining them.
current_hour = 14
hours_until_alarm = 535

# First add the elapsed hours to the starting hour: 14 + 535 = 549.
# Then % 24 keeps the remainder after removing complete 24-hour days.
# Since 549 = 22 * 24 + 21, the remaining hour is 21, within the range 0 to 23.
# The parentheses make the addition happen before the modulo operation.
alarm_hour = (current_hour + hours_until_alarm) % 24

# In the f-string, :02d prints the integer hour with at least two digits,
# adding a leading zero when needed, e.g. 7 becomes 07. The literal :00 supplies
# the minutes, which stay zero because the delay contains only whole hours.
print(f"Alarm time: {alarm_hour:02d}:00")

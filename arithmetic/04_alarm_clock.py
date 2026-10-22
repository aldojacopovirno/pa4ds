# Assignment
# A 24-hour clock shows 14:00. An alarm is set to ring 535 hours later.
# Calculate the hour at which it will ring and display it in `HH:00` form. Use
# modulo 24 to wrap the elapsed time around the clock; the minutes remain zero.
#
# Solution

# Modulo 24 wraps the elapsed hour back into a 24-hour clock.
current_hour = 14
hours_until_alarm = 535

alarm_hour = (current_hour + hours_until_alarm) % 24
print(f"Alarm time: {alarm_hour:02d}:00")

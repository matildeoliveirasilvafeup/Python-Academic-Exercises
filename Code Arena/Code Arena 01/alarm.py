hour = int(input())
minute = int(input())
if hour > 24 or hour + 6 >= 24:
	alarm_hours = 6 - (24 - hour)
else: alarm_hours = hour + 6

if minute + 51 >= 60:
	difference_minutes = 60 - minute
	alarm_minutes = 51 - difference_minutes
	alarm_hours += 1
else: alarm_minutes = minute + 51
print(f"{alarm_hours:02d}:{alarm_minutes:02d}")

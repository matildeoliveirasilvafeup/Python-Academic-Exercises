def time_diff(time1, time2):
	(hour1, minute1) = time1
	(hour2, minute2) = time2
	if hour1 > hour2:
		difference_hour = hour1 - hour2
		if minute1 > minute2:
			difference_minute = minute1 - minute2
		else:
			difference_minute = minute2 - minute1
	else:
		difference_hour = hour2 - hour1
		if minute1 > minute2:
			difference_minute = minute1 - minute2
		else:
			difference_minute = minute2 - minute1
	return (difference_hour, difference_minute)
print(time_diff((14, 30), (17, 45)))
print(time_diff((10, 25), (10, 20)))
print(time_diff((19,30), (17, 00)))
print(time_diff((10, 45), (10, 45)))

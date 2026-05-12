def time_diff(time1, time2):
	(hour1,minute1) = time1
	(hour2,minute2) = time2
	min_diff = abs(minute1 - minute2)
	hour_diff = abs(hour1 - hour2)
	if (hour1 < hour2 and minute1 > minute2) or (hour1 > hour2 and minute1 < minute2):
		return hour_diff - 1, 60 - min_diff
	return hour_diff, min_diff

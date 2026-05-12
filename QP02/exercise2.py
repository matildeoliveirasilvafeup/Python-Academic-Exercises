hour = int(input())
minutes = int(input())
if hour <= 0 or hour > 24:
	print("INVALID DATE FORMAT")
elif minutes < 0 or minutes >= 60:
	print("INVALID DATE FORMAT")
else:
	if hour > 12: #pm
			hours_in_minutes = hour - 12
			if minutes == 0:
				print(f"{hours_in_minutes} pm")
			elif minutes < 10:
				print(f"{hours_in_minutes}:0{minutes} pm")
			else:
				print(f"{hours_in_minutes}:{minutes} pm")
	elif hour == 12:
		print("12 pm")
	else:#am
				hours_in_minutes = hour + 12
				if minutes == 0:
					print(f"{hours_in_minutes} am")
				elif minutes < 10:
						print(f"{hours_in_minutes}:0{minutes} am")
				else:
						print(f"{hours_in_minutes}:{minutes} am")


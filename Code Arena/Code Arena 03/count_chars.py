def count_chars(a,b):
	res = 0
	for char in a:
		if char == b:
			res += 1
	return res if res > 0 else -1



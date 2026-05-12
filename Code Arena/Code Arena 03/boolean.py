def validate(grade):
	res = isinstance(grade,(int, float)) and 0 <= grade <= 100
	return res

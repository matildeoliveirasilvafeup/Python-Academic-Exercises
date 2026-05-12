def sum_all_functions(atuple):
	total = 0
	current = 0 #comeca com 0
	for function in atuple:
		current = function(current)
		total += current
	return total

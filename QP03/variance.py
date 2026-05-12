def avg_numbers(number):
	soma = 0
	for i in range(1, number +1):
		soma += i
	average = soma / number
	return average
def var_numbers(number, precision=2): #DIZ DEFAULT 2
	average_media = avg_numbers(number)
	difference = 0
	for i in range(1, number + 1):
		difference += (i - average_media) ** 2
	variance = difference / number
	return round(variance,precision)


import math
def approx_euler(n):
	res = 0
	for i in range(n):
		sum = i + 1
		res += sum / math.factorial(i)
	res *= (1/2)
	return round(res,10)

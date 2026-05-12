def check_amicable(number1,number2):
	sum_1 = 0
	sum_2 = 0
	for i in range(1,number1):
		if number1 % i == 0:
			sum_1 += i
	for i in range(1,number2):
		if number2 % i == 0:
			sum_2 += i
	if number1 == number2:
		res = f"same number: {number2}"
	elif sum_1 == number2 and sum_2 == number1:
		res = f"{number1} and {number2} form an amicable pair"

	elif sum_1 != number2:
		res = f"sum of divisors of {number1} is not {number2}"

	return res

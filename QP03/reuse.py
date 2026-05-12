def calc_triangular (number):
	triangular = 0
	for x in range(1, number +1):
		triangular += x
	return triangular

def factorial(number):
	product = 1 #COMO É MULTIPLICAÇÃO COMECAR POR 1!
	for i in range(1, number + 1):
		product = product * i
	return product

def reuse(number):
	sum = 0
	for i in range(1, number +1):
		if i % 2 != 0:
			sum += calc_triangular(i)
		else:
			sum += factorial(i)
	return sum

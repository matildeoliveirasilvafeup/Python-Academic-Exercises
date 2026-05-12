import math
k = 50
um_sobre_pi = 0
for i in range(0, k):
	numerador = math.factorial(4 * i) * (1103 + 26390 * i)
	denominador = math.factorial(i) ** 4 * ((396) ** (4 * i))
	fracao = numerador / denominador
	um_sobre_pi += ( fracao * ( (2 * math.sqrt(2) / 9801)))
	pi = 1 / um_sobre_pi
print(round(pi, 8))

def is_perfect(n):
	soma = 0
	for i in range(1,n): #NAO ESQUECER A DIVIDIR POR 0 TEM QUE COMECAR EM 1
		if (n % i == 0):
			soma += i
	if (soma == n):
		return True
	else:
		return False

n = int(input())
if n < 1 or n > 10:
	print ("Input error")
else:
	for i in range(n, 0, -1): #numero de linhas
		for j in range(i, 0, -1): #numeros em cada linha
			print(j, end = " ") #sequencia de cada linha

		print() #cada linha




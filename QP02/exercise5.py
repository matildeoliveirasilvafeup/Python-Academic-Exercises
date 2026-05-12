n1 = str(input())
n2 = str(input())

resultado = []

for i, j in zip(n1[::-1],n2[::-1]): #percorre n1 e n2 ao mmo tempo
	resultado.append(i)
	resultado.append(j)

resultado_em_string = "".join(resultado)
print(int(resultado_em_string))

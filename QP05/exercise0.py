def flatten(lst):
	resultado = []
	for i in lst:
		if isinstance(i,list): #se for uma lista o i
			for j in i:
				resultado.append(j)
		else:
			resultado.append(i)
	return resultado

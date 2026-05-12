def remove_consecutive_duplicates(astr):
	resultado = astr[0]
	tamanho_da_string = len(astr)
	for i in range (1,tamanho_da_string):
		if astr[i] != astr[i - 1]:
			resultado += astr[i]
	return resultado

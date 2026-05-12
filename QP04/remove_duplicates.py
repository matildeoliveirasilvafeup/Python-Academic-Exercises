"""def remove_consecutive_duplicates(str):
	resultado = ""
	for letter in str:
		if letter not in resultado:
			resultado += letter
	return resultado"""

def remove_consecutive_duplicates(str):
	resultado = str[0] #adiciona o primeiro caracter ao resultado
	for letter in str:
		if letter != resultado[-1]: #resultado[-1] é o ultimo caracter
			resultado += letter
	return resultado



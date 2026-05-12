def remove_leading(ip):
	separar = ip.split('.')
	novos_numeros = [str(int(separa)) for separa in separar]
	#o int serve para remover os 0's a esquerda e o str porque vai se retornar uma string
	return '.'.join(novos_numeros)



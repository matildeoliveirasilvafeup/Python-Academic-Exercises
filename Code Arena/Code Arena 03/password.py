def strong(password):
	tamanho = len(password)
	tem_maiuscula = False
	tem_minuscula = False
	tem_numero = False
	tem_simbolo = False
	if tamanho < 8:
		return False
	for i in password:
		if i.isupper():
			tem_maiuscula = True
		elif i.islower():
			tem_minuscula = True
		elif i.isdigit():
			tem_numero = True
		else:
			tem_simbolo = True

	return tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo

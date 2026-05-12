def longest(s):
	words = s.split()
	maior = 0
	for word in words:
		tamanho = len(word)
		if tamanho > maior:
			maior = tamanho
	return maior

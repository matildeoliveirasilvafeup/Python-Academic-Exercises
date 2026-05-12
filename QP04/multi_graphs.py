def multi(g):
	res = {}
	for a,b in g:
		if (a,b) in res:
			res[(a,b)] += 1 #contador passa a ser 2, ou seja, {('A','B'): 2}
		else:
			res[(a,b)] = 1
			#contador é 1 porque ainda nao havia esta aresta, ou seja, {('A','B'): 1}
	return tuple((a,c,b) for (a,b), c in res.items())
#aqui (a,b) é a chaves e o c é o valor
#cada item é a (chave,valor) onde chave ('A','B') e valor = 2

def triplet(tup):
	#cada elemento de tup NÃO é uma sequencia de 3 elementos
	#por isso nao podemos fazer for a,b,c in tup
	#temos que fazer com RANGE
	tamanho = len(tup)
	for a in range(tamanho):
		for b in range(a +1, tamanho):
			for c in range(b+1, tamanho):
				if tup[a] + tup[b] + tup[c] == 0:
					return (tup[a],tup[b],tup[c])
	return ()


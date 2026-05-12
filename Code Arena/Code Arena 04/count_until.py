def count_until(tup):
	for n_elementos, element in enumerate(tup): #n_elementos da a posicao do sitio da tupla, que é o nº de elementos que apareceram antes
		if isinstance(element, tuple):
			return n_elementos
	return -1

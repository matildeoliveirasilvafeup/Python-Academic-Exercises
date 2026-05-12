def local_minima(alist):
	resultado = []
	for i in range(len(alist)-2):
		slice_tres = alist[i:i+3] #para incluir o 3º elemento
		minimo = min(slice_tres)
		if slice_tres.count(minimo) == 1:
			resultado.append(minimo)
	return resultado

#slice.tres.count(minimo) vê quantas vezes aparece o minimo na slice_tres,
#sendo o slice.tres a sequencia de cada 3 elementos

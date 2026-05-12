def unique_owner(cars):
	lista = []
	for placa in cars:
		if len(cars[placa][1]) == 1:
			lista.append(placa)
	return lista

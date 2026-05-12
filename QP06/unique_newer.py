
def unique_owner_newer(cars, year):
	lista = []
	for placa in cars:
		if len(cars[placa][1]) == 1 and cars[placa][3] >= year:
			lista.append(placa)

	return lista

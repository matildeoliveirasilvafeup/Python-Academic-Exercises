def unique_owner(cars):
	lista = []
	for placa in cars:
		if len(cars[placa][1]) == 1:
			lista.append(placa)
	return lista

def unique_owner_cities_acc(cars):
	cities = set()
	for placa in unique_owner(cars):
		for accident in cars[placa][2]:
			city = accident.split('-',1)[1] #divide em antes e depois do hifen apenas 1 vez, e pega no elemento do nome da cidade (indice 1)
			cities.add(city)
	return cities

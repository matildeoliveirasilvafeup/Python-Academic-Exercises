def owner_to_cars(cars):
	new_dictionary = {}
	for matricula, (value, owners, accidents, year) in cars.items():
		for person in owners:
			if person not in new_dictionary:
				new_dictionary [person] = [] #ficar com key o nome da pessoa e como valor a lista de matriculas associada a cada pessoa
			new_dictionary[person]. append(matricula)
	#ordenar agr os nomes por ordem alfabetica
	for person in new_dictionary:
		new_dictionary[person].sort()
	return new_dictionary




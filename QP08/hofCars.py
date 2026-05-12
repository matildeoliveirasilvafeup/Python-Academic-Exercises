def select_cars(cars, condition) :
	return dict(filter(lambda e: condition(e[1]) , cars.items()))


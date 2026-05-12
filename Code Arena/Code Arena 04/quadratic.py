def solver(a, b, c):
	conta_positiva = ((-1) * b + (b ** 2 - 4 * a * c) **  (1 / 2)) / (2 * a)
	conta_negativa =  ((-1) * b - (b ** 2 - 4 * a * c) **  (1 / 2)) / (2 * a)
	if conta_negativa < conta_positiva:
		return (conta_negativa, conta_positiva)
	else:
		return (conta_positiva,conta_negativa)



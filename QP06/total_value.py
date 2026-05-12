def total_value(cars):
	resultado = 0
	for placa in cars:
		resultado += cars[placa][0] #devolve o valor da placa, sendo a placa a key
	return resultado


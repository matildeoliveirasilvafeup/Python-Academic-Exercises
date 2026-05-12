"""def  overtime_employees(employees):
	lista = []
	for employee_id, hours_worked in employees:
		if hours_worked > 40:
			lista.append(employee_id)
	return lista"""

def overtime_employees(employees):
	return list(map(lambda e : e[0],filter(lambda e: e[1] > 40 ,employees)))

#LIST COMPREHENSION
# return [nome for nome, horas in employees if horas > 40]

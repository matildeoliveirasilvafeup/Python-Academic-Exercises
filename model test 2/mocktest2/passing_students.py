def passing(students):
	passed = filter (lambda x : x[1] >= 9.5, students)
	return list(map(lambda x : x[0], passed))
 #return [id for id, grade in students if grade >= 9.5]
 #da return dos id's para cada id, grade em students

"""def passing(students) :
	lista_retorno = []
	for id, grade in students:
		if grade >= 9.5:
			lista_retorno.append(id)
	return lista_retorno"""

print(passing([("up103", 7.4), ("up022", 14.5), ("up190", 10.5)]))
print(passing([("up003", 7.4), ("up022", 4.5)]))
print(passing([("up033", 13.4), ("up022", 6.5), ("up142", 16.5), ("up019", 17.5)]))
print(passing([]))

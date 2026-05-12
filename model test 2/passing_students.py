"""
Não se pode usar for, só em compreheensions

def passing(students):
	resultado = []
	for i in students:
			if i[1] >= 9.5:
				resultado.append(i[0])
	return resultado

"""

def passing(students):
	return [student[0] for student in students if student[1] >= 9.5]

def passing_students(students, passing_grade):
	passing = filter(lambda e: (e['mt1'] + e['mt2']) / 2 >= passing_grade, students)
	return list(map(lambda e : e['name'], passing))

#OU
#return [e['name'] for e in students if (e['mt1'] + e['mt2']) / 2 > = passing_grade]

def find_highest_paid_employee(database):
	if database == ():
		return ()
	highest_paid = database[0]

	for (id,name,department,salary) in database:
		(hpaidid,hpaidname, hpaiddepartment,hpaidsalary) = highest_paid
		if salary > hpaidsalary:
			highest_paid = (id,name,department,salary)
	return highest_paid



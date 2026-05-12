def count_duplicates(lst):
	resultado = []
	count = 1
	for i in range(1,len(lst)):
		if lst[i] == lst[i - 1]:
			count += 1
		else:
			resultado.append(count)
			count = 1
	resultado.append(count)
	return resultado

print(count_duplicates([1, 1, 1, 2, 2, 3]))
print(count_duplicates([0, 0, 0, 0]))
print(count_duplicates([5, 5, 6, 6, 7, 7, 7, 8]))
print(count_duplicates([1, 2, 3]))

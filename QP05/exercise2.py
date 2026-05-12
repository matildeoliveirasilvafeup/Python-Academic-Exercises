"""def merge_sorted_lists(lst1, lst2):
	lista = []
	for i in lst1:
		lista.append(i)
	for j in lst2:
		lista.append(j)
	return sorted(lista)""" #NAO SE PODE USAR SORT


def merge_sorted_lists(lst1, lst2):
	i = 0
	j = 0
	resultado = []
	while i < len(lst1) and j < len(lst2):
		if lst1[i] <= lst2[j]:
			resultado.append(lst1[i])
			i += 1
		else:
			resultado.append(lst2[j])
			j += 1

	while i < len(lst1): #se ainda há elementos em lst1
		resultado.append(lst1[i])
		i += 1

	while j < len(lst2):
		resultado.append(lst2[j]) #se ainda há elementos em lst2
		j += 1

	return resultado



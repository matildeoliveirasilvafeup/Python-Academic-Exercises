def differences(alist):
	pairs = zip(alist, alist[1:]) #pairs
	difference = map(lambda par : par[1] - par[0], pairs)
	return list(difference)
print(differences([1, 2, 3, 4]))
print(differences([4, 3, 2, 1]))
print(differences([1, 2, 2, 1, 3, 5, 9]))
print(differences([5, 15]))

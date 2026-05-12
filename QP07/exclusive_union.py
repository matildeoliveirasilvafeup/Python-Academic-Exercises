def x_union(list1, list2):
	l1 = filter(lambda p: p[0] not in map(lambda p: p[0], list2), list1 )
	l2 = filter(lambda p: p[0] not in map(lambda p: p[0], list1), list2)
	return list(l1) + list(l2)

def local_minima(alist):
	triplets = zip(alist, alist[1:], alist[2:])
	filtered = filter(lambda triplet: triplet.count(min(triplet)) == 1, triplets)
	return list(map(lambda triplet: min(triplet), filtered))
print(local_minima([10, 3, 3, 14, 5, 7, 4]))

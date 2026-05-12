def variance(alist):
	n = len(alist)
	avg = sum(alist) / n
	sigma = sum(map(lambda e: (e - avg)** 2  , alist)) / n
	return round(sigma,3)
print(variance([1, 2, 3, 4, 5, 6]))

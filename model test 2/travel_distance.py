def total_distance(dist, cities):
	total = 0
	if len(cities) < 2:
		return 0
	for i in range(len(cities) - 1):
		c1, c2 = cities[i], cities[i + 1]
		if (c1,c2) in dist:
			total += dist[(c1,c2)]
		elif (c2,c1) in dist:
			total += dist[(c2,c1)]
		else:
			return -1

		return total

from functools import reduce
def bounding_box(pts):
	x_min = reduce (lambda x,y : x if x <= y else y, map(lambda p : p[0], pts))
	y_min = reduce (lambda x,y : y if x <= y else x, map(lambda p : p[0], pts))
	x_max = reduce (lambda x,y : x if x <= y else y, map(lambda p : p[1], pts))
	y_max = reduce (lambda x,y : x if x <= y else x, map(lambda p : p[1],pts ))
	return (x_min, y_min, x_max, y_max)

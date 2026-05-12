def bounded_mult(v, s, b):
	(x,y) = v
	(width,height) = b
	conta1 = (s * x) % width
	conta2 = (s * y) % height
	if x > width or y > height:
		return None
	else:
		return (conta1,conta2)

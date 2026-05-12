def deriv(f):
	h = 0.001
	def derived(x):
		result = (f(x + h) - f(x)) / h
		return round(result,3)
	return derived

def discard_middle(s):
	tamanho = len(s)
	res = ""
	if tamanho <= 3:
		res = ""
	else:
			primeiros_dois = s[0] + s[1]
			ultimos_dois = s[-2] + s[-1]
			res += primeiros_dois + ultimos_dois
	return res

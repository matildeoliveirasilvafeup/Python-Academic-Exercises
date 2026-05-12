def academy_awards(alist):
	resultado = []
	for category, winning_movie in alist:
		resultado.append(winning_movie)
	return max(resultado, key = resultado.count )



romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
        }
def roman_to_integer(astring):
	total = 0
	i = 0
	"""Então porquê o while em vez de for?
Porque às vezes avançamos 1 posição
e outras vezes avançamos 2 posições (no caso de subtração)."""
	while i < len(astring): #Enquanto i estiver dentro da string, continuamos
		curr = romans[astring[i]] #astring[1] de 'XV' por exemplo é V
		if i + 1 < len(astring):
			next_val = romans[astring[i + 1]]
		else:
			next_val = 0
		if curr < next_val:
			total += next_val - curr
			i += 2
		else:
			total += curr
			i += 1
	return total

def remove_duplicates_jump(text,jump):
	if not text: #se a string é vazia
		return "" #retorna string vazia
	res = text[0]
	for char in range(1,len(text)):
		if text[char] != text[char -1]:
			res += text[char]
	return res[0::jump] # pega índices 0, jump, 2*jump,


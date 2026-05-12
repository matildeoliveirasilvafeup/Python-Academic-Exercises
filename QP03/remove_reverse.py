def rm_letter_rev(ch, s):
	string_a_retornar = ""
	for i in s:
		if i != ch:
			string_a_retornar += i #para somar a string

	return string_a_retornar[::-1]

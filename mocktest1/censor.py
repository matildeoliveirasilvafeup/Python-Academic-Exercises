def remove_word(text,word,next):
	res = ""
	for palavra in range(len(text)):
		if text[palavra + 1] != next:
			res += text[palavra]
		else:
			remove_word(word)
	return res
print(remove_word("HeLloHello HeL10!", "Hello", "!") )
print(remove_word("HeLlo!Hell0! Hello!", "Hell", "o") )

print(remove_word("Hello! Hello !! Hello!", "Hello", "L") )

print(remove_word("Hello-world! Hello-world?", "Hello", "-"))

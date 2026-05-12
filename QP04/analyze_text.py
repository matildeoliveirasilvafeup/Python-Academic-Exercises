def analyze_text(text, keyword):
	words = text.split() #['Olá,', 'isto', 'é', 'um', 'exemplo']
	numero_words = len(words)
	keyword_count = 0
	censurada = []
	for word in words:
		if word == keyword:
			keyword_count += 1
			word = "*" * len(word)
	return f"Words: {numero_words}; Keyword count: {keyword_count}; Censored: {text}"


print(analyze_text("This is a simple test sentence.", "simple"))

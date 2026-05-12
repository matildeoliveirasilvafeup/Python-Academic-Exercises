def mastermind(guesses, codes):
	correct = 0
	incorrect = 0
	for i in range(len(guesses)):
		if guesses[i] in codes:
			if guesses[i] == codes[i]:
				correct += 1
			else:
				incorrect += 1
	return (correct, incorrect)


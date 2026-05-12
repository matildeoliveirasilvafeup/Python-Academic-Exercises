num = int(input())
if len(str(num)) == 1:
	print("Looping number")
else:
	numero_percorrivel = str(num)
	looping = True
	for i in range(len(numero_percorrivel) - 1):
		actual = int(numero_percorrivel[i])
		proximo = int(numero_percorrivel[i + 1])
		if proximo == actual + 1:
			continue
		elif int(numero_percorrivel[i]) == 9 and int(numero_percorrivel[i + 1]) == 0:
			continue
		else:
			looping = False
			break
	if looping:
		print("Looping number")
	else:
		print("Not a looping number")

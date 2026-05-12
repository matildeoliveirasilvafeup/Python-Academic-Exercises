num = int(input())
percorrer_numero = str(num)
decimal = 0
expoente = 0
for i in percorrer_numero:
	if int(i) >= 8:
		print("Not a valid number.")
		exit()
for i in reversed(percorrer_numero):
		decimal += int(i) * (8 ** expoente) #NOTA: AQUI QUEREMOS A POSICAO DO EXPOENTE
		expoente += 1 #posição do dígito, não o valor do dígito.

print(decimal)


num = int(input())
for i in range(num):
	if (num % 2 != 0): #se num for impar
		if i == int(num / 2):
			print("#" * int(num/2) + "0" + "#"* int(num/2))
		else:
			print("#" * num)
	else:
		if i == int(num /2) - 1:
			print("#" * int((num / 2) - 1) + "00" + "#"* int((num/2) - 1))
		elif i == (num /2):
			print("#" * int((num / 2) - 1) + "00" + "#"* int((num/2) - 1))
		else:
			print("#" * num)


	#print("#" * num)




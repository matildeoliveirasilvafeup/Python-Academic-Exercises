num = int(input())
if num == 0 or num >= 10 : #igual a 0
	for i in range(1,11):
		multiplication = num * i
		print(f"{num} x {i} = {multiplication}")

else:
	for i in range(1,num):
		multiplication = num * i
		print(f"{num} x {i} = {multiplication}")
	expoente = num ** 2
	print(f"{num} ^ 2 = {expoente}")


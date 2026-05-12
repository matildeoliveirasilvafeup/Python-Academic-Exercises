lower = int(input())
upper = int(input())
num_em_string = " "
for i in range(lower, upper + 1):
	if i > 1:
		primo = True
		for j in range(2, int( i ** 0.5) + 1):
			if i % j == 0:
				primo = False
				break
		if primo:
			num_em_string += str(i) + " "
print(f"Prime numbers between {lower} and {upper} are:{num_em_string}")





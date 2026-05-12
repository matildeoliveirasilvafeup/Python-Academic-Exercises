n = int(input())
for i in range(1,n + 1):
	res = " " * (n - i) + i * "#" + "  " + "#" * i
	print(res)

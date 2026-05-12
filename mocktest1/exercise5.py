def addition(x,y):
	sum = x + y
	sum_str = str(sum)
	carry = 0
	res = []
	for char in reversed(sum_str):
		digit = int(char)
		total = digit + carry
		carry = total // 10
		res.append (f"new digit {char} with carry {carry}")

	if carry > 0:
		res.append(f"new digit {carry} from carry")
	return "\n".join(res) + f"\n{sum}"

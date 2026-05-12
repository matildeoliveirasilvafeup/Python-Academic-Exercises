mt1 = int(input())
mt2 = int(input())
mt3 = int(input())
if mt1< 0 or mt1 > 20 or mt2 < 0 or mt2 > 20 or mt3 < 0 or mt3 > 20:
	print("Input error")
elif mt1 < 10 or mt2 < 10 or mt3 < 10:
	print("RFF")
else:
	average = (mt1 * 0.4) + (mt2 * 0.4) + (mt3 * 0.2)
	print(int(average + 0.5))

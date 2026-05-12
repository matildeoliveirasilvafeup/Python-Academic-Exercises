from functools import reduce
def dec2int(alist):
	#convert list of digits to integer
	return int(reduce(lambda acumulador, x:  acumulador * 10 + x, alist,0 ))

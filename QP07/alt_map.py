def alt_map(f, g, lst):
	return list(map(lambda t: f(t[1]) if t[0] % 2 == 0
				 else g(t[1]), enumerate(lst) ))
# [(0,0), (1,1), (2,2), (3,3), (4,4)] -> com enumerate
# posicao 0 , valor 0
#posicao 1 , valor 1
print(alt_map(lambda x: x + 10, lambda x: x + 100, [0, 1, 2, 3, 4]))
print(alt_map(lambda x: x * 2, lambda x: x * 3, [1, 2, 3, 4, 5, 6]))
print(alt_map(str, lambda x: f"<{x}>", [1, 2, 3, 4]))
print(alt_map(lambda x: x ** 2, lambda x: x ** 3, [2, 3, 4]))

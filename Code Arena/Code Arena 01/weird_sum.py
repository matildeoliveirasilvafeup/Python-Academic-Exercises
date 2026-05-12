a = int(input())
b = int(input())
difference_even = (a - b) % 2 == 0 #True se a diferenca é par
soma = a + b
prod = a * b
resultado = soma * (1 + difference_even) + prod * (not difference_even)
"""Se diferença é par → resultado = soma * 2 + 0
Se diferença é ímpar → resultado = soma * 1 + produto
"""
print(resultado)

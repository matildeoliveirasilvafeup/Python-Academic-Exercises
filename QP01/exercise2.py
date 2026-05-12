number = int(input())
milhares = number // 1000
centenas = number // 100 - milhares * 10
dezenas = number // 10 - (milhares * 100 + centenas * 10)
unidades = number % 10
milhares_out = milhares * 1000
centenas_out = centenas * 100
dezenas_out = dezenas * 10
print(milhares_out)
print(centenas_out)
print(dezenas_out)
print(unidades)

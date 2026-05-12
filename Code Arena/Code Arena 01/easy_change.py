price = int(input())
amount_received = int(input())
resultado = ""
difference = amount_received - price
notas_50 = difference // 50
difference = difference % 50
notas_20 = difference // 20
difference = difference % 20
notas_10 = difference // 10
difference = difference % 10
notas_5 = difference // 5
difference = difference % 5
print(f"{notas_50} {notas_20} {notas_10} {notas_5}")

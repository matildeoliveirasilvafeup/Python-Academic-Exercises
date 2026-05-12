distance = int(input())
litres = float(input())
price = float(input())
cada_100_litros = distance / 100
total_price = cada_100_litros * price * litres
print(round(total_price,2))

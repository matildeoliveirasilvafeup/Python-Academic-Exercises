num = int(input()) # 766
numero_a_retornar = 0
while num > 0:
	last_digit = num % 10 # 6
	numero_a_retornar = numero_a_retornar * 10 + last_digit #6
	num = num // 10
print(numero_a_retornar)

"""
COM FOR
num = int(input())  # número original
rev = 0
temp = num          # variável temporária para não perder o número original

# Descobrir quantos dígitos tem o número
num_digits = 0
t = temp
for _ in range(100):  # usamos um limite grande, vai quebrar com break
    if t == 0:
        break
    t = t // 10
    num_digits += 1

# Inverter o número usando for
for _ in range(num_digits):
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print(rev)
"""

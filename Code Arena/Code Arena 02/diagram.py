# Entrada
L = int(input())
S = int(input())

R = L

while True:
    if R > S:
        # swap triplo
        L, R, S = R, S, L

    if S > R:
        # atualizar R
        R = R - S

    if R == 0:
        # swap triplo final
        L, R, S = R, S, L
        break  # sair do loop

print(S)

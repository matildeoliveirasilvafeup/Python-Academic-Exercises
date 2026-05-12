def mastermind(g1, g2, g3, c1, c2, c3):
    guess = [g1, g2, g3]
    key = [c1, c2, c3]
    resultado = 0

    # 1) Pontos exactos
    guess_rest = []
    key_rest = []

    for i in range(3):
        if guess[i] == key[i]:     # exacto
            resultado += 3
        else:
            guess_rest.append(guess[i])
            key_rest.append(key[i])

    # 2) Pontos por cor correta mas posição errada
    for g in guess_rest:
        if g in key_rest:
            resultado += 1
            key_rest.remove(g)   # impede dupla contagem

    return resultado


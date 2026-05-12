def change(amount):
    dinheiro = [200, 100, 50, 20, 10, 5, 2, 1]
    resultado = []
    for i in dinheiro:            # i é a moeda
        while amount >= i:        # não dinheiro[i]
            amount -= i
            resultado.append(i)
    return resultado

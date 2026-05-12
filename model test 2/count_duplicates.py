def count_duplicates(lst):
    if len(lst) == 0:
        return []

    resultado = []
    count = 1

    # i é ÍNDICE: 1, 2, 3, 4, 5 (não 1, 1, 1, 2, 2, 3)
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:  # Agora posso usar lst[i] porque i é índice!
            count += 1
        else:
            resultado.append(count)
            count = 1

    resultado.append(count)
    return resultado

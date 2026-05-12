def mask_data(data, n_characters, position):
    if n_characters == 0:  # caso especial
        return data

    maskedstring = ''
    resultado = ''

    if position == 'begin':
        for i in range(n_characters):
            maskedstring += '*'
        resultado = maskedstring + data[n_characters:]
    elif position == "end":
        for i in range(n_characters):
            maskedstring += '*'
        resultado = data[:len(data) - n_characters] + maskedstring
    else:
        resultado = data  # posição inválida

    return resultado

def shopping(alist, stock):
    total_gasto = 0
    quantidade_retorno = 0
    missing = {}

    for item, quantidade in alist.items():
        if item in stock:
            available_quantity, price = stock[item]

            if available_quantity > quantidade:
                quantidade_retorno += 0
                total_gasto += price * quantidade

            else:
                quantidade_retorno = quantidade - available_quantity
                total_gasto += price * (quantidade - quantidade_retorno)  # o que se compra de facto

        else:
            quantidade_retorno = quantidade
            total_gasto += 0

        if quantidade_retorno > 0:
            missing[item] = quantidade_retorno

    return total_gasto, missing

# Use to test in VS Code
def normalize(answer):
    """Auxiliary function to be used in the tests."""
    (quant,adict) = answer
    return (quant, sorted(adict.items()))

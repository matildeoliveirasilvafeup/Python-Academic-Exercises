def check_amicable(number1, number2):
    if number1 == number2:
        return f"same number: {number1}"

    somador = 0
    resultado = 0
    for i in range(1, number1):
        if number1 % i == 0:
            somador += i
    for j in range(1, number2):
        if number2 % j == 0:
            resultado += j

    if somador == number2 and resultado == number1:
        return f"{number1} and {number2} form an amicable pair"
    else:
        return f"sum of divisors of {number1} is not {number2}"


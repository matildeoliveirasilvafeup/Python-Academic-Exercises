
def adigits(a,b,c):
    # Verifica e imprime os valores em ordem
    if (a <= b and a <= c):
        if (b <= c):
            return(int(str(a)+ str(b) + str(c)))
        else:
            return(f"{a}{c}{b}")
    elif (b <= a and b <= c):
        if (a <= c):
            return(f"{b}{a}{c}")
        else:
            return(f"{b}{c}{a}")
    else:
        if (c <= a and c <= b):
            if (a < b):
                return(f"{c}{a}{b}")
            else:
                return(f"{c}{b}{a}")


import math
a = int(input())
b = int(input())
c = int(input())

quadratic_form1 = ((-1) * b + (b ** 2 - (4 * a * c)) ** (1/2)) / (2 * a)
quadratic_form2 =  ((-1) * b - (b ** 2 - (4 * a * c)) ** (1/2)) / (2 * a)
print(f"The solutions are {round(quadratic_form1,2)} and {round(quadratic_form2,2)}")

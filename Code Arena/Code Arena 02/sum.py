num = int(input())
string = str(num) #Transformar o número em algo percorrível — uma sequência (como uma string
sum = 0
for i in string: #percorre cada caractere da string
	sum += int(i) #para fazer contas, converter para int
print(sum)

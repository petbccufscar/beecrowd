# Problema 1075 - Beecrowd - Iniciante - Nível 2

# Entrada do valor inteiro N
n = int(input())

# Para que se obtenha resto 2 a partir do número N
# é só começar do 2 e ir somando o valor N até que 
# o valor seja maior que 10000.
for i in range(2,10001,n):
    print(i)
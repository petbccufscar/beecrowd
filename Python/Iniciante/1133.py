# Problema 1133 - Beecrowd - Iniciante - Nível 3

# Recebendo valores de entrada.
num1 = int(input())
num2 = int(input())

# Verificando que num1 é menor que num2.
if num1 > num2:
    num1, num2 = num2, num1

# Loop for para varrer todos os valores entre num1 e num2.
for i in range(num1 + 1, num2):
    if i % 5 == 2 or i % 5 == 3:
        print(i)

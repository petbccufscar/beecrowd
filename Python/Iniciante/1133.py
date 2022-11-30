# Problema 1135 - Beecrowd - Iniciante - Nível 3

# Entrada dos valores.
x = int(input())
y = int(input())

# Verificando o número maior.
if x > y:
    x, y = y, x

# Loop para varrer todos os números entre x e y e saída esperada.
for i in range(x + 1, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)

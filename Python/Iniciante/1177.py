# Problema 1177 - URI - Iniciante - Nível 1

# Leitura do valor de 't'
t = int(input())

# Construção da lista
n = [i%t for i in range(1000)]

# Impressão dos valores
for i, j in enumerate(n):
    print(f'N[{i}] = {j}')
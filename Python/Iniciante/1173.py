# Problema 1173 - URI - Iniciante - Nível 1

# Leitura do valor inicial
v = int(input())

# Construção da lista
n = [v*2**i for i in range(10)]

# Impressão dos valores
for i, j in enumerate(n):
    print(f'N[{i}] = {j}')
# Problema 1175 - Beecrowd - Iniciante - Nível 2

# Recebe a entrada
N = []

# Transforma a entrada em uma lista para armazenar cada número
for a in range (20):
    N.append(int(input()))

# Inverte os números que estão armazenados
N = N[::-1]

# Imprime o resultado
for (i, dado) in enumerate(N):
    print(f'N[{i}] = {dado}') 

# Problema 1040 - Beecrowd - Iniciante - Nível 2

# Efetua a leitura dos números a serem ordenados
numeros = list(map(int, input().split()))

# Copia a lista não ordenada
auxNumeros = list(numeros)

# Ordena a lista
numeros.sort()

# Imprime a lista ordenada
for n in numeros:
    print(n)

# Imprime linha em branco
print()

# Imprime a lista antes da ordenação
for n in auxNumeros:
    print(n)

# Problema 1040 - URI - Iniciante - Nível 2

# Efetua a leitura dos números a serem ordenados
numeros = [int(i) for i in input().split()]

# Copia a lista não ordenada
auxNumeros = list(numeros)

# Ordenação simples da lista de números
# iterando pela lista para cada elemento na lista
for i in range(len(numeros)):
    for j in range(i, len(numeros)):
        # Verifica se um elemento antecessor é maior que o sucessor
        if numeros[i] > numeros[j]:
            # Variável auxiliar para trocar os valores de posição
            aux = numeros[i]

            numeros[i] = numeros[j]
            numeros[j] = aux

# Imprime a lista ordenada
for i in range(len(numeros)):
    print(numeros[i])

# Imprime linha em branco
print()

# Imprime a lista antes da ordenação
for i in range(len(auxNumeros)):
    print(auxNumeros[i])

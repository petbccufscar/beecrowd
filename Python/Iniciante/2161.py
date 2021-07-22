# Problema 2161 - URI - Iniciante - Nível 1

# Lê a entrada
repeticoes = int(input())

# Inicia a variável soma com 0
soma = 0.0

# Laço de repetição
for i in range(repeticoes):
    # calculo da fração
    soma = 1.0/(soma+6.0)

# Acrescenta 3 à fração
soma += 3

# Imprime o resultado
print(f'{soma:.10f}')
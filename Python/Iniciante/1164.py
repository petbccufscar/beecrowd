# Problema 1164 - Beecrowd - Iniciante - Nível 2

# Leitura do número de casos de teste
N = int(input())

# Loop para verificar os casos de teste
for _ in range(N):
    # Leitura de um valor inteiro a ser julgado 
    X = int(input())
    
    # Soma dos divisores
    soma = 0
    
    # Cálculo da soma dos divisores
    for i in range(1, X):
        if X % i == 0:
            soma += i
    
    # Verificando se X é perfeito, ou não
    if soma == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')

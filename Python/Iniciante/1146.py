# Problema 1146 - Beecrowd - Iniciante - Nível 3

# Executamos o loop até a condição de saída
while True:
    # O input do usuário vem como string, temos que transformar em inteiro
    # para manipulação no for loop abaixo
    X = int(input())
    
    # Essa é a condição de saída, como diz o enunciado 
    # "O último número no arquivo de entrada é 0."
    # Note que saindo da função aqui impedimos que seja impresso qualquer
    # coisa após o 0
    if (X == 0):
        break
    
    # Para cada número de 1 até X, imprimimos ele, com um espaço no final
    # Note que o X não é impresso por esse loop, o range retorna 1, 2, ..., X-1;
    for i in range(1, X):
        print(i, end=" ")
    
    # Como queremos que a última impressão não tenha espaço após o número,
    # podemos dar um print sozinho após o for loop
    print(X, end="")
    # E um print para iniciar a próxima linha
    print() 
# Problema 2862 - URI - Iniciante - Nível 1

# Lê a quantidade de valores
n = int(input())

for i in range(n):
    # Lê o número e verifica se é maior que 8000
    # Se for maior que 8000, ele imprime "Mais de 8000!"
    # Caso contrário, imprimirá "Inseto!"
    print('Mais de 8000!' if int(input()) > 8000 else "Inseto!")
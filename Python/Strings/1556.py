# Problema 1556 - Beecrowd - String - Nível 8

# Remove elementos repetidos de uma lista
def removeRepetida(l):
    return list(dict.fromkeys(l))

# input: palavra a ser calculada
def palavrasPossiveis(n):

    # Caso base onde não tem nada em n
    if n == None or len(n) == 0:
        return []
    
    # A lista começa com a letra inicial da palavra dada
    l = [n[0]]

    # Ele calcula as palavras possiveis para o restante da palavra
    recursao = palavrasPossiveis(n[1:])

    # Dobra a lista com as palavras com e sem a letra inicial
    for i in recursao:
        # Adiciona a versão com e sem a letra inicial
        l.append(i)
        l.append(n[0] + i)

    # Remove as palavras repetidas da lista e retorna
    return removeRepetida(l)


# Leitura até o fim do arquivo
while True:
    try:
        # Lê a palavra dada
        palavra = input()

        # Calcula a lista de palavras e ordena
        resultado = palavrasPossiveis(palavra)
        resultado.sort()

        # Percorre a lista de palavras para imprimir
        for i in resultado:
            print(i)

        # Imprime uma linha
        print()

    # Caso chegue no fim do arquivo (EOF), o loop para
    except EOFError:
        break

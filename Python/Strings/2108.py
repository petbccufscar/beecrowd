# Problema 2108 - Beecrowd - String - Nível 4

# Iniciando a palavra mais grande
biggest = ""

while True:
    # Pegando a linha das palavras
    linha = input()
    
    # Caso de parada
    if linha == '0': 
        break

    # É uma lista de palavras
    listaDePalavras = linha.split(' ')

    # Percorre a lista de palavras
    for idx in range(len(listaDePalavras)):
        # Pega a palavra atual
        palavra = listaDePalavras[idx]

        # Caso seja a última palavra, ele não printa '-'
        if idx == len(listaDePalavras) -1:
            print(f'{len(palavra)}')
        # Caso contrário, ele printa '-'
        else:
            print(f'{len(palavra)}-',end="")

        # Verifica e atualiza a maior palavra
        if len(palavra) >= len(biggest):
            biggest = palavra

# Imprime a maior palavra
print(f'\nThe biggest word: {biggest}')
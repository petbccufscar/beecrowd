#Problema 1332 - Beecrowd - String - Nível 2

# Leitura do número de palavras
num_palavras = int(input())

for i in range(num_palavras):
    # Leitura da linha que contém a palavra
    linha = input()
    # Tamanho da linha lida
    tamanho = len(linha)
    # Contador da posição que será usado para navegar na string lida
    pos = 0
    # Dicionário de erros para cada número escrito por extenso
    erros = {"one": 0, "two": 0, "three": 0}

    # Lista com chavesdo dicionário
    chaves = list(erros.keys())

    # While que conta quantidade de letras erradas para "one"
    while pos < 3:
        if linha[pos] != chaves[0][pos]:
            erros["one"] += 1
        pos += 1
    pos = 0

    # While que conta quantidade de letras erradas para "two"
    while pos < 3:
        if linha[pos] != chaves[1][pos]:
            erros["two"] += 1
        pos += 1
    pos = 0

    # While que conta quantidade de letras erradas para "three"
    while pos < 5 and pos < tamanho:
        if linha[pos] != chaves[2][pos]:
            erros["three"] += 1
        pos += 1

    # Verifica se tamanho é igual a três
    if tamanho == 3:
        # Verifica se há no máximo um erro para "one"
        if erros["one"] <= 1:
            print(1)
        # Verifica se há no máximo um erro para "two"
        elif erros["two"] <= 1:
            print(2)
    # Verifica se tamanho é igual a 5 e se a quantidade de erros para "three"
    # é no máximo 1 
    elif tamanho == 5 and erros["three"] <= 1:
        print(3)

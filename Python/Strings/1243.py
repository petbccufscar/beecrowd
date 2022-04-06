# Problema 1243 - Beecrowd - Strings - Nível 7

while True:
    try:
        enunciado = input()
        total = 0
        nPalavras = 0

        # Cálculo do total de palavras
        # e do total de letras nas palavras
        for palavra in enunciado.split(' '):
            if palavra.isalpha():
                total += len(palavra)
                nPalavras += 1
            elif palavra[0:-1].isalpha() and palavra[-1] == '.':
                total += len(palavra) - 1
                nPalavras += 1

        # Verifica se a quantidade palavras não é nula
        if nPalavras:
            media = int(total/nPalavras)
        else:
            media = 0

        # Imprime a dificuldade
        if media >= 6:
            print(1000)
        elif media >= 4:
            print(500)
        else:
            print(250)
    except EOFError:
        break

# Problema 2484 - Beecrowd - Strings - Nível 4

while True:
    try:
        palavra = input()

        for i in range(len(palavra)):
            # Imprime espaços com base na
            # quantidade de letras já impressas
            print(i*' ', end='')

            # Impressão letra a letra, espaçadas entre si
            for j in range(len(palavra) - (i + 1)):
                print(palavra[j], end=' ')
            # Impressão da última letra isolada, já que
            # nela deve ser impressa uma nova linha
            print(palavra[-(i + 1)])
        print()
    except EOFError:
        break

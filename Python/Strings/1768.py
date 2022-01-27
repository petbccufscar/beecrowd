# Problema 1768 - Beecrowd - Strings - Nível 1

while True:
    try:
        tamanho = int(input())
        espacos = int((tamanho - 1)/2)

        # Reajuste da quantidade de espaços necessários
        # no início de cada linha, impressão da linha
        while espacos >= 0:
            print(' '*espacos, end='')
            print('*'*(tamanho - 2*espacos))
            espacos -= 1
        espacos = int((tamanho - 1)/2)
        # Impressão da base
        for i in range(2):
            print(' '*espacos, end='')
            print('*'*(tamanho - 2*espacos))
            espacos -= 1
        print()
    except EOFError:
        break

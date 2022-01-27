# Problema 2694 - Beecrowd - Strings - Nível 1

import itertools

n = int(input())

for i in range(n):
    instancia = input()

    # Separa a ocorrência de sequências de letras de
    # outros caracteres que, no exercício, são números
    instancia = [''.join(j) for k, j in\
            itertools.groupby(instancia, str.isalpha)]
    soma = 0

    # Considera as strings formadas por números,
    # já que elas estão agrupadas, e soma o valor
    # dessa string convertida para inteiro
    for i in instancia:
        if not(i.isalpha()):
            soma += int(i)
    print(soma)

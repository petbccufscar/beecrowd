# Problema 1632 - Beecrowd - Strings - Nível 4

n = int(input())

for i in range(n):
    senha = input()
    combinacoes = 1

    # Cálculo das possíveis combinações,
    # sem alterar a ordem das letras
    for i in senha:
        # Se é uma dessas letras, existem 3 possibilidades:
        # maiúsculas, minúsculas, e um número
        if i.lower() in ('a', 'e', 'i', 'o', 's'):
            combinacoes *= 3
        else:
            combinacoes *= 2

    print(combinacoes)

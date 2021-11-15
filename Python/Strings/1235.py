# Problema 1235 - Beecrowd - Strings - Nível 3

# Inicialmente, recebemos o valor da quantidade de casos
casos = int(input())

# Em cada caso:
for _ in range(casos):
    # Recebemos a string de entrada
    frase = input()

    # Guardamos a metade da quantidade de caracteres da string
    quant = int(len(frase)/2)

    # A primeira metade da string recebe os valores da metade da string
    # até seu inicio, de forma invertida
    metadeA = frase[quant-1::-1]

    # A segunda metade da string recebe os valores do final da string
    # até a sua metade, de forma invertida
    metadeB = frase[len(frase):quant-1:-1]

    # A impressão do resultado na tela é feita
    print(f'{metadeA}{metadeB}')
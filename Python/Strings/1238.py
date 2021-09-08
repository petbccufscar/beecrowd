# Problema 1238 - URI - Strings - Nível 3

#biblioteca importada para facilitar o loop em paralelo
import itertools as it

# Inicialmente, recebos o valor da quantidade de casos
casos = int(input())

# Em cada caso:
for _ in range(casos):
    # Recebemos a string de entrada e a separamos em novas duas
    frase = list(input().split())
    # Resetamos a string resultado, deixando-a vazia
    resultado = ""

    # Iniciamos dois loops simultaneos, onde só se encerra quando
    # o loop mais longo terminar
    for x, y in it.zip_longest(frase[0], frase[1]):
        # Caso a primeira palavra termine, os elementos recebidos serão do tipo "None",
        # logo, não serão concatenados na string final
        if type(x) == str:
            resultado += x
        # Caso a segunda palavra termine, os elementos recebidos serão do tipo "None",
        # logo, não serão concatenados na string final
        if type(y) == str:
            resultado += y

    # A impressão do resultado na tela é feita
    print(f'{resultado}')
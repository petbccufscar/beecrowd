# Problema 1238 - URI - Strings - Nível 3

# Biblioteca importada para facilitar o loop em paralelo
import itertools as it

# Inicialmente, recebemos o valor da quantidade de casos
casos = int(input())

# Em cada caso:
for _ in range(casos):
    # Recebemos a string de entrada e a separamos em novas duas
    fraseA, fraseB = input().split(' ')
    # Resetamos a string resultado, deixando-a vazia
    resultado = ""

    # Iniciamos dois loops simultâneos, onde só se encerra quando
    # o loop mais longo terminar
    for x, y in it.zip_longest(fraseA, fraseB, fillvalue=''):
        # Caso a primeira palavra termine, os elementos recebidos serão strings vazias
        resultado += (x + y)

    # A impressão do resultado na tela é feita
    print(resultado)
# Problema 1367 - Beecrowd - Strings - Nível 3

from collections import defaultdict

while True:
    # Leitura do tamanho da imagem
    n, m = map(int, input().split())

    if n == m == 0:
        break

    linhas = []

    # Leitura da imagem
    for _ in range(n):
        linhas.append(input())

    # Leitura do tamanho final da imagem
    a, b = map(int, input().split())

    # Vamos converter o tamanho em um escalar
    a //= n
    b //= m

    # Para cada linha da imagem original
    for linha in linhas:
        # Vamo printar 'a' linhas
        for _ in range(a):
            # Para cada caractere da linha original
            for c in linha:
                # Vamo printar 'b' caracteres
                for _ in range(b):
                    print(c, end='')
            print()
    print()

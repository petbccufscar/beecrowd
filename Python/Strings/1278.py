# Problema 1278 - Beecrowd - Strings - Nível 1

primeiro = True

while True:
    n = int(input())

    if n == 0:
        break

    if primeiro:
        primeiro = False
    else:
      print()

    frases = []

    for i in range(n):
        frase = input()
        frase = ' '.join(frase.split())
        frases.append(frase)

    maiorTamanho = max(len(f) for f in frases)

    for frase in frases:
        print(frase.rjust(maiorTamanho))

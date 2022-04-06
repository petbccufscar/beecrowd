# Problema 2356 - Beecrowd - Strings - Nível 3

while True:
    try:
        D = input()
        S = input()

        # Verifica se o trecho está presente no DNA
        if S in D:
            print("Resistente")
        else:
            print("Nao resistente")
    except EOFError:
        break

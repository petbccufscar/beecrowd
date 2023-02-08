# Problema 2691- Beecrowd - Strings - Nível 3

# Quantas vezes o programa será testado - N, o primeiro input
for _ in range(int(input())):

    # Para cada teste, separamos os fatores da multiplicação pelo 'x'
    # E convertemos para números inteiros com o map (Já que .split devolve uma lista)
    # Colocamos os dois números em X e Y
    X, Y = map(int, input().split('x'))

    # Se X for igual a Y não precisamos imprimir para X e para Y
    if X == Y:
        for i in range(5,11):
            print(f"{X} x {i} = {X*i}")
    else:
        for i in range(5,11):
            print(f"{X} x {i} = {X*i} && {Y} x {i} = {Y*i}")

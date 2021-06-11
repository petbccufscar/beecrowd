# Problema 1115 - URI - Iniciante - Nível 1

while True:
    x, y = map(int, input().split(' '))
    # se os sinais forem iguais e
    if x*y > 0:
        # se ambos forem positivos, a resposta será o primeiro quadrante
        # senão, a resposta será o terceiro quadrante
        print("primeiro" if x > 0 else "terceiro")
    # se os sinais forem diferentes e
    elif x*y < 0:
        # se o x for positivo, a resposta será o quarto quadrante
        # senão, a resposta será o segundo quadrante
        print("quarto" if x > 0 else "segundo")
    # se algum for nulo, o programa termina
    else:
        break

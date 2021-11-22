# Problema 1115 - Beecrowd - Iniciante - Nível 1

while True:
    x, y = map(int, input().split(' '))
    # Se os sinais forem iguais e
    if x*y > 0:
        # Se ambos forem positivos, a resposta será o primeiro quadrante
        # Senão, a resposta será o terceiro quadrante
        print("primeiro" if x > 0 else "terceiro")
    # se os sinais forem diferentes e
    elif x*y < 0:
        # Se o x for positivo, a resposta será o quarto quadrante
        # Senão, a resposta será o segundo quadrante
        print("quarto" if x > 0 else "segundo")
    # Se algum for nulo, o programa termina
    else:
        break

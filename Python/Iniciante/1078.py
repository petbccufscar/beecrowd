# Problema 1079 - URI - Iniciante - Nível 1

# Recebemos o valor de entrada, já utilizando a função int para convertê-lo, já que em python todo input retorna uma string
N = int(input())

# Em seguida, criamos um loop for de 1 a 11 (para multiplicador assumir valores de 1 a 10)
for multiplicador in range(1, 11):
    # Para cada iteração, exibimos a mensagem como solicitado, montado uma tabuada do valor de entrada
    print(f'{multiplicador} x {N} = {multiplicador * N}')
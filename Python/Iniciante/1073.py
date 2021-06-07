# Problema 1073 - URI - Iniciante - Nível 1

# Recebemos o valor de entrada, já utilizando a função int para convertê-lo, já que em python todo input retorna uma string
N = int(input())

# Em seguida, criamos um loop for de 2 (primeiro par) a N+1 (para englobar também o valor N como solicitado pelo problema) e passo 2
# Que nos garante que em todas iterações, a variável par será efetivamente par
for par in range(2, N + 1, 2):
    # Com isso, atribuimos o resultado de "par ** 2" a variável quadrado
    quadrado = par**2
    print(f'{par}^2 = {quadrado}')
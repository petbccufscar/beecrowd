# Problema 1933 - URI - Iniciante - Nível 1

# Entrada dos valores A e B
a, b = map(int, input().split(" "))

# Se A é igual B, imprime o valor da variável A
if(a == b):
    print(int(a))
# Se forem diferentes, soma-se o valor de A com o valor de B
# com o valor da diferença entre eles. Então, é dividido por 2
# Isso garante que seja impresso sempre o maior valor entre A e B.
else:
    # abs() apresenta o valor em módulo, ou seja, sem sinal.
    print(int((a + b + abs(a - b)) / 2))

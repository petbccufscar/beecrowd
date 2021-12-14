# Problema 1074 - Beecrowd - Iniciante - Nível 2

# Inicialmente, recebemos a quantidade de casos de testes.
testes = int(input())

# A cada teste, recebemos um novo número.
for i in range(testes):
    numero = int(input())
    # Se o numero recebido for 0
    if numero == 0:
        print('NULL')
    # Se o numero não for 0, par ou ímpar, é impresso o começo da resposta sem quebra de linha.
    elif numero % 2 == 0:
        print('EVEN', end=" ")
    else:
        print('ODD', end=" ")
    
    # Se o numero for positivo ou negativo. Caso seja 0, não entra nesta condição.
    if numero > 0:
        print('POSITIVE')
    elif numero < 0:
        print('NEGATIVE')
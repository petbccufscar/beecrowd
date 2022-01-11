# Problema 1074 - Beecrowd - Iniciante - Nível 2

# Inicialmente, recebemos a quantidade de casos de testes.
testes = int(input())

# A cada teste, recebemos um novo número.
for i in range(testes):
    numero = int(input())
    # Se o numero recebido for 0
    if numero == 0:
        resposta = "NULL"
    # Se o numero não for 0, par ou ímpar, coloca em uma variável, para o próximo teste.
    elif numero % 2 == 0:
        resposta = "EVEN "
    else:
        resposta = "ODD "    
    # Se o numero for positivo ou negativo. Caso seja 0, não entra nesta condição.
    if numero > 0:
        resposta += "POSITIVE"
    elif numero < 0:
        resposta += "NEGATIVE"
    print(resposta)
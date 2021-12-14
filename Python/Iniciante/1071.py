# Problema 1071 - Beecrowd - Iniciante - Nível 2

# Inicialmente, lemos os dois valores recebidos.
valorA = int(input())
valorB = int(input())

# Iniciamos a resposta com 0.
resposta = 0

if valorA < valorB:
    # Se A for menor que B, percorremos normalmente, ignorando o último elemento caso ele seja ímpar também
    for i in range(valorA, valorB - 1):
        # Se for ímpar, somamos a resposta.
        if i % 2 != 0:
            resposta += i
else:
    # Se A for maior que B, percorremos ela inversamente, ignorando o primeiro elemento, caso seja ímpar
    for i in range(valorA - 1, valorB, -1):
        # Se for ímpar, somamos a resposta.
        if i % 2 != 0:
            resposta += i   

print(resposta)
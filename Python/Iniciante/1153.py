# Problema 1153 - Beecrowd - Iniciante - Nível 1

# Começamos recebendo o input necessários (já convertendo para int), N
N = int(input())

# A saída será a variável fatorial, que deve conter o valor do fatorial de N, como estamos lidando com multiplicações, 'fatorial' é inicializada como 1.
fatorial = 1

# No cálculo do fatorial, temos nossa condição de parada quando N-? = 1, já que na multiplicação 1 é o elemento neutro
while(N != 1):

    # Efetuamos o cálculo de fatorial, reduzindo o N em 1 a cada iteração.
    fatorial = fatorial * N
    N = N-1

# Por fim, imprimimos o valor encontrado
print(fatorial)
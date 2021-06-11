# Problema 1149 - URI - Iniciante - Nível 1

# Inicializando as variáveis A, N, RESPOSTA
A, N, resposta = 0, 0, 0
# Recebemos todos os dados em uma única linha e o dividimos com SPLIT(),
# logo após, salvamos em um MAP e o convertemos para uma LIST. Assim, podendo
# trabalhar com iteradores e utilizar a função LEN()
numeros = list(map(int, input().split(' ')))

# X assume todos os valores de 0 até a quantidade de elementos da lista NUMEROS
for x in range(len(numeros)):
    # Se X for maior que zero e A for igual a 0, A recebe o valor da lista NUMEROS na posição X
    # Se A for diferente de 0, N recebe o valor da lista NUMEROS na posição X
    if(numeros[x] > 0):
        if(A == 0):
            A = numeros[x]
        else:
            N = numeros[x]

# Y assume todos os valores de 0 até o último valor assumido por N
# então, o valor da soma de A + Y é adicionado a RESPSOTA
for y in range(N):
    resposta += (A + y)

# Impressão da RESPOSTA usando f-string
print(f'{resposta}')
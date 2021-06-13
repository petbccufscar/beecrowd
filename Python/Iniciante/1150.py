# Problema 1150 - URI - Iniciante - Nível 1

# Começamos recebendo os dois inputs necessários (já convertendo para int), X e Z
X = int(input())
Z = int(input())

# Como há a condição de Z ser maior que X, enquanto Z for menor ou igual a X,
# refazemos a leitura
while(Z <= X):
    Z = int(input())

# Com a condição satisfeita, começamos a soma, que começa com o valor de X como descrito no problema.
soma = X

# Também iniciaremos um contador de iterações (i) e também será uma variável para somar os sucessores de X.
# 'i' começa em 1, por X ser sempre menor que Z.

i = 1
# Equanto a soma for menor que X.
while(soma <= Z):

    soma += X+i
    # Entrou no loop, incrementamos o contador 
    i += 1

# Por fim, imprimimos a variável i (número de iterações de soma)
print(i)

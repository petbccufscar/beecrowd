# Problema 1067 - Beecrowd - Iniciante - Nível 2

# Recebe o valor que será considerado para imprimir os ímpares.
valor = int(input())

# A expressão int((valor - 1)/2) indica quantos ímpares existem até valor n,
# dado que um k-ésimo número ímpar pode ser expresso por 2k + 1 = n, logo,
# o k máximo pode ser expresso por k == int((n - 1)/2).
# Considerando que range(n) irá iterar n - 1 vezes, adicionamos mais um.
for i in range(int((valor - 1)/2) + 1):
    print(2*i + 1)

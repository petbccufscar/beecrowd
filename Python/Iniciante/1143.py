# Problema 1143 - Beecrowd - Iniciante - Nível 1

# Lê o valor fornecido pela entrada padrão
valor = int(input())

# X assumirá todos os valores de 0 até o VALOR - 1
# em seguida, imprime o valor de X, seguido por X ao quadrado e X ao cubo
for x in range(valor):
    print(f'{x+1} {(x+1)**2} {(x+1)**3}')
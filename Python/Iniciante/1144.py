# Problema 1144 - URI - Iniciante - Nível 1

# Lê o valor fornecido pela entrada padrão
valor = int(input())

# X assumirá todos os valores de 0 até o VALOR - 1
# Imprime o valor de (X+1), (X+1)^2  e (X+1)^2, seguido pelo
# valor de (X+1), ((X + 1)^2)+1 e ((X + 1)^3)+1
for x in range(valor):
    print(f'{x+1} {(x+1)**2} {(x+1)**3}')
    print(f'{x+1} {((x+1)**2)+1} {((x+1)**3)+1}')
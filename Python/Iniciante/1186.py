# Problema 1186 - Beecrowd - Iniciante - Nível 3

# Iniciamos a matriz, que será uma lista de listas, a soma 
# se iniciará com 0 e recebemos a operação a ser realizada

operacao = input()

# Criando e preenchendo a matriz utilizando List Comprehension (Compreensão de Listas)
matriz = [[float(input()) for _ in range(12)] for _ in range(12)]
soma = 0

# Percorremos somente os elementos da matriz que estão abaixo da 
# diagonal secundária e então, adicionamos o valor correspondente
# matriz[i][j] à variável SOMA
for i in range(1, 12):
    for j in range(11, 11 - i, -1):
        soma += matriz[i][j]

# De acordo com a operação, o resultado é exibido com apenas uma
# casa decimal
if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/66:.1f}')